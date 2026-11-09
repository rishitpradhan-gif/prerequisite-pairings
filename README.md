# Prerequisite Pairings

**[Download & run locally](LOCAL.md)** — a short guide and ready-to-run ZIP.

**When does a forced paired reply remain legal under arbitrary prerequisites?**

This project gives an exact answer for every finite prerequisite poset: the two endpoints of each pair must have the same set of external predecessor blocks. A global condition over every possible play reduces to a polynomial local test.

A second theorem compresses reachable completed rounds into ideals of a quotient poset and counts complete plays as `e(Q) × 2^t`.

- [Full proofs](PROOFS.md)
- [Exhaustive verification results](evidence/verification.json)
- [Related work](REFERENCES.md) · [Research provenance](PROVENANCE.md)

## Reproduce

Python 3.10+, standard library only:

```sh
python3 verify.py
```

The verifier compares the local theorem with an independent state-space oracle on **72,482 poset–matching instances**. It uses transitive predecessor relations and explores every legal initiating choice, including choices after hypothetical game termination.

## Why this is useful

Prerequisite-constrained claiming games appear to require reasoning over every move history. The characterization identifies exactly when a fixed matching policy can be certified without that search. Its quotient theorem explains the resulting state-space compression rather than merely observing a speedup.

Companion result: [Fourteen](https://github.com/rishitpradhan-gif/fourteen) applies fixed-response structure to a sharp Connect Four obstruction. Research direction by Rishit Pradhan; proof development and implementation were AI-assisted. These are new project results with self-contained proofs; worldwide priority is not asserted.
