# Contributing

## Commit messages

Griddy follows [Conventional Commits](https://www.conventionalcommits.org/).

```
<type>(<optional scope>): <short summary in imperative mood>
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

Examples:

```
feat(grid): reorder posts with long-press drag
fix(crop): keep zoom when switching aspect ratio
docs(adr): record storage decision
```

Work in progress is kept on a branch and squashed before merging, instead of using a `wip` type.

No AI co-author trailers are added to commits.
