# tiny-chess-01

4 KB Python chess engine for [make.fun tiny-chess-01](https://make.fun/bounty/tiny-chess-01).

Negamax αβ, iterative deepening (node budget), quiescence (captures+promos), MVV-LVA + TT-move/killers/history, TT, tuned PST with endgame king centralization and passed-pawn bonuses, check extension, repetition. Stdlib only; lzma+base85 `main.py` ≤4096 bytes. MIT.

Local practice (kit trials 0–2, prior build): Elo 1451 / 1545 / 1451 (mean ~1482). Eval tune A/B vs that build: 7.0/12.
