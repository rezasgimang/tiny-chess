# tiny-chess-01

A compact chess engine in 4,096 bytes of readable Python 3.13 (stdlib only).

## Design

- 0x88 board, alpha-beta search with iterative deepening to depth 12
- Fixed node budget (100,000 nodes/move) — fully deterministic, no clock
- Quiescence search (captures, plus all evasions when in check)
- MVV-LVA move ordering
- Hand-written piece-square tables (pawn advance, knight centrality,
  king middlegame safety) and standard piece values
- Castling, promotion, check evasion and mate detection

`main.py` is the whole engine. It talks to the make.fun env at
`MAKEFUN_ENV_URL`, reads `/game`, and posts moves in UCI to `/move`.

## Size

- `main.py`: 4,096 bytes (the cap)
- Whole repo: under 8,192 bytes, no file over 4,096
- MIT license
