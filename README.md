# tiny-chess-01

4 KB Python chess engine for [make.fun tiny-chess-01](https://make.fun/bounty/tiny-chess-01).

Negamax αβ, iterative deepening (node budget), quiescence (captures+promos), MVV-LVA + TT-move/killers/history, TT, tuned PST with endgame king centralization and passed-pawn bonuses, check extension, repetition. Stdlib only; lzma+base85 `main.py` ≤4096 bytes. MIT.

Local practice (kit trials 0–2, HEAD 10f4c3a, verified 17 Nov 2026): Elo 1464 / 1326 / 1464 (mean 1418). Mean per-move time ~2.3s, no timeouts. Eval tune A/B vs prior build: 7.0/12.
