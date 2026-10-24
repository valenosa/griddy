#!/usr/bin/env python3
"""Verify the form of Griddy's documentation.

Checks that the documents stay consistent with each other. It only reads files.

    python tools/verify_docs.py

Checks:
  - identifiers (S, R, P, F, T, INV, PR) are defined once, in the right document,
    without numbering gaps, and every citation points to a definition;
  - ADR files: name, title, required fields and sections, valid status and type,
    numbering without gaps, and an index (docs/adr/README.md) that matches them;
  - every ADR-NNNN cited anywhere exists;
  - versioned documents declare a version, and the SDD "Based on" line matches them;
  - every accepted ADR, rule and feature appears in the SDD traceability matrix;
  - every parameter name cited in backticks is defined in the model's Parameters table;
  - relative links resolve, tables have consistent columns, code blocks are closed.

Output: one line per finding, [ERROR] or [WARNING], then a summary.
Exit code 1 if there are errors, 0 otherwise. Python 3.9+, standard library only.

Adapted from the verification script of the sdd-gobernanza process. Project-specific
settings live in CONFIG below: adding a phase spec or an identifier kind is a
one-line change.
"""

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent

CONFIG = {
    # Markdown files to scan, as glob patterns relative to the repository root.
    "scan": ["*.md", "docs/**/*.md"],
    # Files excluded from identifier checks (they contain placeholders).
    "exclude_ids": ["docs/adr/template.md"],
    # Identifier prefix -> files where it may be defined.
    "id_homes": {
        "S": ["docs/model.md"],
        "R": ["docs/model.md"],
        "P": ["docs/model.md"],
        "F": ["docs/poc-spec.md"],
        "T": ["docs/sdd.md"],
        "INV": ["docs/sdd.md"],
        "PR": ["docs/sdd.md"],
    },
    "model": "docs/model.md",
    "sdd": "docs/sdd.md",
    # Documents that must declare "Version: X.Y".
    "versioned": ["docs/model.md", "docs/poc-spec.md", "docs/sdd.md"],
    # Identifier prefixes that must appear in the SDD traceability matrix.
    "traced_prefixes": ["R", "F"],
    "adr_dir": "docs/adr",
    "adr_index": "docs/adr/README.md",
    "adr_required_fields": ["Status", "Date", "Type"],
    "adr_required_sections": ["Context", "Alternatives considered", "Decision", "Consequences"],
    "adr_types": ["Product", "Technical"],
    "adr_statuses": ["Proposed", "Accepted", "Deprecated"],  # plus "Superseded by ADR-NNNN"
}

RE_FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
RE_HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
RE_INLINE_CODE = re.compile(r"`[^`]*`")
RE_TABLE_SEP = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?\s*$")
RE_ADR = re.compile(r"(?<![\w-])ADR-(\d{4})(?!\w)")
RE_VERSION = re.compile(r"\*\*Version:\*\*\s*v?(\d+(?:\.\d+)+)")
RE_BASED_ON_LINE = re.compile(r"\*\*Based on:\*\*(.*)")
RE_BASED_ON_ITEM = re.compile(r"v(\d+(?:\.\d+)+)\s*\(`([^`]+)`\)")
RE_PARAM = re.compile(r"`([A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+)`")


# --------------------------------------------------------------------------- docs

class Doc:
    def __init__(self, path):
        self.path = path
        self.rel = path.relative_to(ROOT).as_posix()
        raw = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").split("\n")
        self.raw = raw
        self.lines, self.unclosed_fence = self._blank_code_blocks(raw)
        self.headings = [(i, len(m.group(1)), m.group(2))
                         for i, l in enumerate(self.lines, 1) if (m := RE_HEADING.match(l))]

    @staticmethod
    def _blank_code_blocks(raw):
        out, open_fence = [], None
        for i, line in enumerate(raw, 1):
            m = RE_FENCE.match(line)
            if open_fence is None:
                if m:
                    open_fence = (m.group(1)[0], len(m.group(1)), i)
                    out.append("")
                else:
                    out.append(line)
            else:
                if m and m.group(1)[0] == open_fence[0] and len(m.group(1)) >= open_fence[1] \
                        and line.strip() == m.group(1):
                    open_fence = None
                out.append("")
        return out, (open_fence[2] if open_fence else None)

    def section(self, predicate):
        """(start, end) line range of the first heading matching predicate."""
        for idx, (line, level, text) in enumerate(self.headings):
            if predicate(text):
                end = len(self.lines)
                for (l2, lv2, _) in self.headings[idx + 1:]:
                    if lv2 <= level:
                        end = l2 - 1
                        break
                return line, end
        return None

    def text(self, start, end):
        return "\n".join(self.lines[start - 1:end])

    def version(self):
        for line in self.lines[:40]:
            if m := RE_VERSION.search(line):
                return m.group(1)
        return None


class Report:
    def __init__(self):
        self.items = []

    def error(self, where, msg):
        self.items.append(("ERROR", where, msg))

    def warn(self, where, msg):
        self.items.append(("WARNING", where, msg))

    def count(self, level):
        return sum(1 for i in self.items if i[0] == level)


def norm(version):
    parts = [int(p) for p in version.split(".")]
    while len(parts) > 1 and parts[-1] == 0:
        parts.pop()
    return tuple(parts)


def table_cells(line):
    s = RE_INLINE_CODE.sub("", line).replace("\\|", "").strip()
    s = s[1:] if s.startswith("|") else s
    s = s[:-1] if s.endswith("|") else s
    return [c.strip() for c in s.split("|")]


# --------------------------------------------------------------------- identifiers

def id_pattern(prefixes):
    alt = "|".join(sorted(map(re.escape, prefixes), key=len, reverse=True))
    return re.compile(r"(?<![\w-])(" + alt + r")-(\d+)(?!\w)")


def check_identifiers(docs, report):
    homes = CONFIG["id_homes"]
    pattern = id_pattern(homes)
    alt = "|".join(sorted(map(re.escape, homes), key=len, reverse=True))
    defs, refs = {}, {}
    for doc in docs:
        if doc.rel in CONFIG["exclude_ids"]:
            continue
        for n, line in enumerate(doc.lines, 1):
            defined = None
            stripped = line.lstrip()
            m = None
            if stripped.startswith("#"):
                m = re.match(r"^#{1,6}\s+[*_`]*(" + alt + r")-(\d+)(?!\w)", stripped)
            elif stripped.startswith("|") and not RE_TABLE_SEP.match(line):
                first = table_cells(line)[0] if table_cells(line) else ""
                m = re.fullmatch(r"[*_`]*(" + alt + r")-(\d+)[*_`]*", first)
            if m:
                key = (m.group(1), int(m.group(2)))
                if doc.rel in homes[key[0]]:
                    defined = key
                    defs.setdefault(key, []).append((doc.rel, n))
                elif stripped.startswith("#"):
                    report.error(f"{doc.rel}:{n}", f"{fmt(key)} is defined here, but {key[0]}-xx "
                                 f"belongs in {', '.join(homes[key[0]])}.")
            skipped_def = False
            for mm in pattern.finditer(line):
                key = (mm.group(1), int(mm.group(2)))
                if key == defined and not skipped_def:
                    skipped_def = True
                    continue
                refs.setdefault(key, []).append((doc.rel, n))

    for key, places in defs.items():
        if len(places) > 1:
            where = ", ".join(f"{d}:{l}" for d, l in places)
            report.error(f"{places[1][0]}:{places[1][1]}", f"{fmt(key)} is defined more than once ({where}).")
    for prefix in homes:
        nums = sorted(n for (p, n) in defs if p == prefix)
        if nums:
            missing = [n for n in range(1, nums[-1] + 1) if n not in nums]
            if missing:
                report.warn(", ".join(homes[prefix]), "Numbering gap: "
                            + ", ".join(f"{prefix}-{n:02d}" for n in missing)
                            + ". Numbers are never reused; restore it marked as superseded or resolved.")
    for key, places in refs.items():
        if key not in defs:
            d, l = places[0]
            report.error(f"{d}:{l}", f"{fmt(key)} is cited but not defined in "
                         f"{', '.join(homes[key[0]])}.")
    return defs


def fmt(key):
    return f"{key[0]}-{key[1]:02d}"


# ----------------------------------------------------------------------------- ADRs

def check_adrs(docs, report):
    adr_dir = ROOT / CONFIG["adr_dir"]
    adrs = {}
    for path in sorted(adr_dir.glob("*.md")):
        if path.name in ("README.md", "template.md"):
            continue
        rel = path.relative_to(ROOT).as_posix()
        m = re.fullmatch(r"(\d{4})-[a-z0-9-]+\.md", path.name)
        if not m:
            report.error(rel, "ADR file name must be NNNN-lowercase-slug.md.")
            continue
        num = int(m.group(1))
        lines = path.read_text(encoding="utf-8").split("\n")
        title = re.match(r"^# ADR-(\d{4}): (.+)$", lines[0]) if lines else None
        if not title:
            report.error(f"{rel}:1", "First line must be '# ADR-NNNN: Title'.")
            continue
        if int(title.group(1)) != num:
            report.error(f"{rel}:1", f"Title number ADR-{title.group(1)} does not match the file name.")
        fields = {}
        for line in lines[:15]:
            if fm := re.match(r"^- \*\*(\w[\w ]*):\*\*\s*(.+)$", line):
                fields[fm.group(1)] = fm.group(2).strip()
        for field in CONFIG["adr_required_fields"]:
            if field not in fields:
                report.error(rel, f"Missing field '**{field}:**'.")
        status = fields.get("Status", "")
        superseded = re.fullmatch(r"Superseded by ADR-(\d{4})", status)
        if status and status not in CONFIG["adr_statuses"] and not superseded:
            report.error(rel, f"Invalid status '{status}'.")
        if fields.get("Type") and fields["Type"] not in CONFIG["adr_types"]:
            report.error(rel, f"Invalid type '{fields['Type']}'.")
        if fields.get("Date") and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", fields["Date"]):
            report.error(rel, "Date must be YYYY-MM-DD.")
        sections = {l[3:].strip() for l in lines if l.startswith("## ")}
        for s in CONFIG["adr_required_sections"]:
            if s not in sections:
                report.error(rel, f"Missing section '## {s}'.")
        adrs[num] = {"rel": rel, "title": title.group(2).strip(), "status": status,
                     "type": fields.get("Type", ""), "superseded_by": superseded}

    for num, a in adrs.items():
        if a["superseded_by"] and int(a["superseded_by"].group(1)) not in adrs:
            report.error(a["rel"], f"Superseded by ADR-{a['superseded_by'].group(1)}, which does not exist.")
    if adrs:
        missing = [n for n in range(1, max(adrs) + 1) if n not in adrs]
        if missing:
            report.warn(CONFIG["adr_dir"], "ADR numbering gap: "
                        + ", ".join(f"ADR-{n:04d}" for n in missing) + ".")

    # Citations
    for doc in docs:
        if doc.rel in CONFIG["exclude_ids"]:
            continue
        for n, line in enumerate(doc.lines, 1):
            for m in RE_ADR.finditer(line):
                if int(m.group(1)) not in adrs:
                    report.error(f"{doc.rel}:{n}", f"ADR-{m.group(1)} is cited but does not exist.")

    # Index
    index = next((d for d in docs if d.rel == CONFIG["adr_index"]), None)
    if index is None:
        report.error(CONFIG["adr_index"], "ADR index not found.")
        return adrs
    rows = {}
    for n, line in enumerate(index.lines, 1):
        if line.lstrip().startswith("|") and not RE_TABLE_SEP.match(line):
            cells = table_cells(line)
            if cells and (m := RE_ADR.search(cells[0])) and len(cells) >= 4:
                rows[int(m.group(1))] = (n, cells)
    for num, a in adrs.items():
        if num not in rows:
            report.error(index.rel, f"ADR-{num:04d} is missing from the index.")
            continue
        n, cells = rows[num]
        for label, value, cell in (("title", a["title"], cells[1]), ("type", a["type"], cells[2]),
                                   ("status", a["status"], cells[3])):
            if value != cell:
                report.error(f"{index.rel}:{n}", f"ADR-{num:04d} {label} is '{cell}' in the index "
                             f"but '{value}' in the file.")
    for num, (n, _) in rows.items():
        if num not in adrs:
            report.error(f"{index.rel}:{n}", f"Index lists ADR-{num:04d}, which has no file.")
    return adrs


# ---------------------------------------------------------------- versions, matrix

def check_versions(docs_by_rel, report):
    for rel in CONFIG["versioned"]:
        doc = docs_by_rel.get(rel)
        if doc is None:
            report.error(rel, "Versioned document not found.")
        elif doc.version() is None:
            report.error(rel, "No '**Version:** X.Y' line in the header.")
    sdd = docs_by_rel.get(CONFIG["sdd"])
    if sdd is None:
        return
    line = next((l for l in sdd.lines[:40] if RE_BASED_ON_LINE.search(l)), None)
    if line is None:
        report.error(sdd.rel, "No '**Based on:**' line in the header.")
        return
    items = RE_BASED_ON_ITEM.findall(line)
    if not items:
        report.error(sdd.rel, "The 'Based on' line must list 'name vX.Y (`file`)' entries.")
    for version, file in items:
        target = (sdd.path.parent / file).resolve()
        rel = target.relative_to(ROOT).as_posix() if target.is_relative_to(ROOT) else file
        doc = docs_by_rel.get(rel)
        if doc is None:
            report.error(sdd.rel, f"'Based on' cites {file}, which does not exist.")
        elif doc.version() and norm(doc.version()) != norm(version):
            report.error(sdd.rel, f"Based on {rel} v{version}, but it is at v{doc.version()}: "
                         f"the SDD is out of date or its header was not updated.")


def check_traceability(docs_by_rel, defs, adrs, report):
    sdd = docs_by_rel.get(CONFIG["sdd"])
    if sdd is None:
        return
    rng = sdd.section(lambda t: "traceability" in t.lower())
    if rng is None:
        report.error(sdd.rel, "No section with 'traceability' in its title.")
        return
    text = sdd.text(*rng)
    missing = [f"ADR-{n:04d}" for n, a in sorted(adrs.items())
               if a["status"] == "Accepted" and f"ADR-{n:04d}" not in text]
    pattern = id_pattern(CONFIG["traced_prefixes"])
    cited = {(m.group(1), int(m.group(2))) for m in pattern.finditer(text)}
    for key, places in sorted(defs.items()):
        if key[0] not in CONFIG["traced_prefixes"]:
            continue
        rel, line = places[0]
        row = docs_by_rel[rel].lines[line - 1].lower()
        if "superseded" in row or "resolved" in row:
            continue
        if key not in cited:
            missing.append(fmt(key))
    if missing:
        report.error(f"{sdd.rel}:{rng[0]}", "Missing from the traceability matrix: "
                     + ", ".join(missing) + ".")


# ------------------------------------------------------------------- parameters

def check_parameters(docs, docs_by_rel, report):
    model = docs_by_rel.get(CONFIG["model"])
    if model is None:
        return
    rng = model.section(lambda t: "parameters" in t.lower())
    if rng is None:
        report.error(model.rel, "No 'Parameters' section.")
        return
    defined = set()
    for line in model.lines[rng[0] - 1:rng[1]]:
        if line.lstrip().startswith("|"):
            cells = [c for c in line.strip().strip("|").split("|")]
            if cells and (m := RE_PARAM.fullmatch(cells[0].strip())):
                defined.add(m.group(1))
    for doc in docs:
        if doc.rel in CONFIG["exclude_ids"]:
            continue
        for n, line in enumerate(doc.lines, 1):
            for m in RE_PARAM.finditer(line):
                if m.group(1) not in defined:
                    report.error(f"{doc.rel}:{n}", f"Parameter `{m.group(1)}` is not defined in "
                                 f"{model.rel} (Parameters).")


# ------------------------------------------------------------ links, tables, code

def check_markdown(doc, report):
    if doc.unclosed_fence:
        report.error(f"{doc.rel}:{doc.unclosed_fence}", "Unclosed code block.")
    link = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
    for n, line in enumerate(doc.lines, 1):
        for m in link.finditer(RE_INLINE_CODE.sub("", line)):
            target = m.group(1)
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            path = unquote(target.split("#")[0].split("?")[0])
            if path and not (doc.path.parent / path).exists():
                report.error(f"{doc.rel}:{n}", f"Broken link: {target}")
        if "[[" in RE_INLINE_CODE.sub("", line):
            report.warn(f"{doc.rel}:{n}", "Wiki-style link ([[...]]); GitHub does not render it.")
    i, lines = 0, doc.lines
    while i < len(lines) - 1:
        if lines[i].lstrip().startswith("|") and RE_TABLE_SEP.match(lines[i + 1]):
            cols = len(table_cells(lines[i]))
            j = i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                if len(table_cells(lines[j])) != cols:
                    report.error(f"{doc.rel}:{j + 1}", f"Row has {len(table_cells(lines[j]))} "
                                 f"columns; the table header (line {i + 1}) has {cols}.")
                j += 1
            i = j
        else:
            i += 1


# ----------------------------------------------------------------------------- main

def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    paths = sorted({p for pattern in CONFIG["scan"] for p in ROOT.glob(pattern) if p.is_file()})
    paths = [p for p in paths if "node_modules" not in p.parts]
    docs = [Doc(p) for p in paths]
    docs_by_rel = {d.rel: d for d in docs}
    report = Report()

    defs = check_identifiers(docs, report)
    adrs = check_adrs(docs, report)
    check_versions(docs_by_rel, report)
    check_traceability(docs_by_rel, defs, adrs, report)
    check_parameters(docs, docs_by_rel, report)
    for doc in docs:
        check_markdown(doc, report)

    counts = {}
    for (p, _) in defs:
        counts[p] = counts.get(p, 0) + 1
    summary = ", ".join(f"{counts[p]} {p}" for p in CONFIG["id_homes"] if p in counts)
    print(f"Griddy docs verification: {len(docs)} files, {len(adrs)} ADRs, {summary or 'no identifiers'}")
    order = {"ERROR": 0, "WARNING": 1}
    for level, where, msg in sorted(report.items, key=lambda i: (order[i[0]], i[1])):
        print(f"[{level}] {where}  {msg}")
    e, w = report.count("ERROR"), report.count("WARNING")
    print(f"Result: {e} error{'s' if e != 1 else ''}, {w} warning{'s' if w != 1 else ''}.")
    return 1 if e else 0


if __name__ == "__main__":
    sys.exit(main())
