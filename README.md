# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/rezasgimang/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/rezasgimang/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Built for the [make.fun tiny-chess-01 bounty](https://make.fun/bounty/tiny-chess-01): the strongest chess engine in 4 KB of Python.

A compact chess engine in Python 3.13 (stdlib only). `src.py` is the
readable source; `main.py` is the same engine packed with the kit's
compressor (LZMA), so it fits the 4,096-byte entry cap.

## Design

- 0x88 board, alpha-beta search with iterative deepening to depth 12
- Fixed node budget (150,000 nodes/move) — fully deterministic, no clock
- Zobrist transposition table (exact/lower/upper bounds, mate scores excluded)
- Killer-move ordering, MVV-LVA capture ordering, TT-move first
- Quiescence search (captures and promotion pushes, plus all evasions when in check)
- Hand-written piece-square tables (pawn advance, knight centrality,
  king middlegame safety, rook 7th rank, queen centrality, endgame king
  centralization), passed-pawn bonuses, bishop-pair bonus, standard piece values
- Root repetition avoidance (never walks into a third occurrence of a position)
- Castling, promotion, check evasion and mate detection

`main.py` is the whole engine. It talks to the make.fun env at
`MAKEFUN_ENV_URL`, reads `/game`, and posts moves in UCI to `/move`.

## Size

- `main.py`: 2,633 bytes packed (the cap is 4,096)
- `src.py`: 5,377 bytes readable source (sent beside the sessions, not counted
  against the repo cap — see the kit's compress notes)
- Whole repo: under 8,192 bytes, no committed file over 4,096
- MIT license
