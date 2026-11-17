# tiny-chess-01

4 KB Python chess engine for [make.fun tiny-chess-01](https://make.fun/bounty/tiny-chess-01).

Negamax αβ, iterative deepening (node budget), quiescence (captures+promos), MVV-LVA + TT-move/killers/history ordering, TT, PST, check extension, repetition, LMR. Stdlib only; lzma+base85 `main.py` ≤4096 bytes. MIT.

Local practice (kit trials 0–2): Elo 1451 / 1545 / 1451 (mean ~1482).
