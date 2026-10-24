# Instructions for AI agents

Read this before doing anything in this repository. It applies to every session.

## Orientation

Read, in order: [docs/README.md](docs/README.md), [CONTEXT.md](CONTEXT.md), [docs/model.md](docs/model.md), the current phase spec ([docs/poc-spec.md](docs/poc-spec.md)), [docs/sdd.md](docs/sdd.md) and [docs/adr/README.md](docs/adr/README.md). The current status and next steps are in [README.md](README.md), section "Status".

Chat history is not a source. Anything decided in a conversation is written into the right document before it is used.

## Before every task, read the source

Never work from memory of the docs, even within the same session: they may have changed, and recollection drifts.

1. Identify what the task touches: features (`F-xx`), rules (`R-xx`), parameters, ADRs and SDD sections. Use the SDD traceability matrix and search (`grep`) to find them.
2. Re-read those passages in the files before planning or writing code.
3. State in the plan which identifiers the work implements, and cite them in commit messages and in the header comment of each module.
4. If the docs do not answer a question the task raises, do not fill the gap by guessing: ask, or propose a documented decision.

## Documentation is always kept in sync

Griddy follows Spec-Driven Development: changes flow **model → SDD → code**.

- **Every change or addition updates the documentation in the same commit**: a new feature, a changed behavior, a new library, a new decision, a fixed value, a changed folder structure. If code and docs disagree, the work is not done.
- Follow the process in [docs/README.md](docs/README.md), section "Changing something already documented": update the model first (ADR, rules, parameters), then the SDD (sections and traceability matrix), then code and tests. Bump versions and add a row to each document's Changes table.
- When the status or next steps change, update the "Status" section of [README.md](README.md).
- Run `python tools/verify_docs.py` before every commit that touches documentation. It must report 0 errors.
- If a request contradicts an accepted ADR, a rule (`R-xx`) or a parameter, do not apply it: show the conflict and ask the owner.
- If implementing something requires a product decision nobody made, propose it with alternatives and a recommendation, and wait for approval. Minor technical decisions may be taken and recorded as `T-xx` in the SDD.

## Definition of done

A change is done when the code, its tests, the documentation and the traceability matrix all agree, CI passes, and it is committed.

## Working rules

- No application code before the owner approves the current phase spec. Throwaway experiments that resolve a pending item (`P-xx`) are allowed when the owner asks for them, kept out of `src/`.
- Do not start a next step without the owner's confirmation.
- Code, docs and commits in English (ADR-0005). Talk to the owner in Spanish.
- Commits follow [CONTRIBUTING.md](CONTRIBUTING.md): Conventional Commits with references, author `Valentín Rodrigo Osa Pochelú <83839175+valenosa@users.noreply.github.com>`, and no AI co-author trailers.
- Never push to `main`: work on a branch and open a pull request for the owner to review and merge, as described in [CONTRIBUTING.md](CONTRIBUTING.md), section "Branches and pull requests".
