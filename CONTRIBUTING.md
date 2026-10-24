# Contributing

## Documentation first

Griddy follows Spec-Driven Development. Read [docs/README.md](docs/README.md) before changing behavior: changes flow model → SDD → code, and a behavior change without its documentation change is incomplete.

- New or changed decision: write an ADR from [the template](docs/adr/template.md) and add it to the [index](docs/adr/README.md).
- Before committing documentation changes, run `python tools/verify_docs.py`.

## Commit messages

Griddy follows [Conventional Commits](https://www.conventionalcommits.org/).

```
<type>(<optional scope>): <short summary in imperative mood> [<optional references>]
```

| Type | Use for |
|---|---|
| `feat` | A new user-facing feature |
| `fix` | A bug fix |
| `docs` | Documentation only |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `test` | Adding or fixing tests |
| `style` | Formatting, no logic change |
| `perf` | Performance improvement |
| `build` | Build system or dependencies |
| `ci` | CI configuration |
| `chore` | Maintenance that fits nothing above |

References point to what the commit implements or changes: features, rules, ADRs, invariants. Documentation commits state the new document versions.

```
feat(grid): reorder posts with long-press drag [F-05, R-05]
fix(crop): keep zoom when switching aspect ratio [R-03, INV-02]
docs: record storage decision (model v0.2, SDD v0.2) [ADR-0014]
```

Work in progress stays on a branch and is squashed before merging; there is no `wip` type.

No AI co-author trailers are added to commits.
