# Instructions for AI agents

Read this before doing anything in this repository. It applies to every session.

## Orientation

Read, in order: [docs/README.md](docs/README.md), [CONTEXT.md](CONTEXT.md), [docs/model.md](docs/model.md), the current phase spec ([docs/poc-spec.md](docs/poc-spec.md)), [docs/sdd.md](docs/sdd.md) and [docs/adr/README.md](docs/adr/README.md). The current status and next steps are in [README.md](README.md), section "Status".

Chat history is not a source. Anything decided in a conversation is written into the right document before it is used.

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
