# Documentation

Griddy follows Spec-Driven Development: decide and document first, specify next, code last. Changes always flow **model → SDD → code**. If a problem shows up lower down, it is fixed upstream first and then propagated down. Chat conversations are not a source: anything decided in one is written here before it is used.

## Map

| Role | File | For |
|---|---|---|
| Overview and status | [README.md](../README.md) | Everyone |
| Glossary | [CONTEXT.md](../CONTEXT.md) | Everyone |
| **Model document:** what Griddy does and why | [model.md](model.md) | Everyone |
| Decision register | [adr/](adr/README.md) | Everyone |
| Phase plan | [ROADMAP.md](../ROADMAP.md) | Everyone |
| Phase 1 spec: features and acceptance criteria | [poc-spec.md](poc-spec.md) | Everyone |
| **SDD:** how Griddy is built | [sdd.md](sdd.md) | Whoever implements, person or agent |
| Design principles | [design-principles.md](design-principles.md) | Design and UI work |
| Testing strategy | [testing-strategy.md](testing-strategy.md) | Implementation |
| Contribution rules and commit format | [CONTRIBUTING.md](../CONTRIBUTING.md) | Contributors |

A new session or contributor should read, in order: this file, the glossary, the model document, the current phase spec, then the SDD.

## Levels

| Level | Answers | Files |
|---|---|---|
| Model | What and why | `model.md`, phase specs, ADRs of type Product, glossary, roadmap |
| SDD | How | `sdd.md`, ADRs of type Technical |
| Code | The implementation | `src/`, tests |

## Where does something go?

Ask: **would two implementations that differ in this give the user a different result?**

- **Yes:** it belongs to the model. A significant decision is a Product ADR; a behavior rule is an `R-xx`; a fixed value is a parameter.
- **No:** it belongs to the SDD. A significant decision is a Technical ADR; a small choice is a `T-xx`.
- **A model decision forces something concrete in the code:** both. The model states it; the SDD translates and cites it.
- **Unsure:** ask before choosing.

## Identifiers

| ID | Meaning | Defined in |
|---|---|---|
| `ADR-NNNN` | Decision | One file per decision in `adr/` |
| `S-xx` | Assumption | `model.md` section 3 |
| `R-xx` | Behavior rule | `model.md` section 6 |
| `P-xx` | Pending item | `model.md` section 10 |
| `F-xx` | Feature | Phase specs (`poc-spec.md`) |
| `T-xx` | Minor technical decision | `sdd.md` section 11 |
| `INV-xx` | Invariant | `sdd.md` section 6 |
| `PR-xx` | Test | `sdd.md` section 9 |

Rules:

- **Cite, don't copy.** Write "R-09" or "ADR-0010" instead of repeating the content; copies go stale.
- **Numbers are never reused or deleted.** Retired items are marked as superseded or resolved.
- **Values are fixed once,** in the model's Parameters table, and referred to by name elsewhere.
- **Every accepted ADR, rule and feature appears in the SDD traceability matrix,** even if only as "no implementation impact".

## Versions

- `model.md`, each phase spec and `sdd.md` carry a version in their header and a Changes table at the end.
- The SDD header declares the versions it is based on. If they do not match the current ones, the SDD is out of date.
- **Major** bump when a change invalidates something already approved; **minor** when it adds or clarifies.

## Changing something already documented

1. Classify the change (model, SDD or both) and check for conflicts with accepted decisions. If it conflicts, stop and decide explicitly.
2. Update the model first: the ADR (a new one if an accepted decision changes), rules, parameters and every section that mentions it. Bump the version and add a Changes row.
3. Update the SDD: traceability matrix, affected sections, the "Based on" line, version and Changes.
4. Update code and tests, using the traceability matrix to find them.
5. Run the verification below.
6. Commit everything in **one commit** so the history shows why it changed together.

## Verification

```
python tools/verify_docs.py
```

Checks form, not content: identifiers defined and cited correctly, numbering without gaps, ADR fields and index, SDD "Based on" versions, traceability coverage, links, tables and code blocks. It exits with code 1 on errors and runs in CI on every push. Content checks (does the SDD implement exactly what the model says?) are done by review.
