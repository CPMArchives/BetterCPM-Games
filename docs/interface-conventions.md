# Interface conventions

Every game provides case-insensitive, exact-token /HELP and /VER queries.
Process informational queries before loading game data or modifying saves,
scores, configuration, or other game state. Report unsupported combinations
clearly. Keep individual game options documented rather than prescribing a
large universal parser in advance.

Example identification:

```text
A0>WUMPUS /VER
WUMPUS 1.0 (001)
  - - -
 | BetterCP/M Games
 | Hunt the Wumpus
```

The example does not assign an actual version to an unimplemented game.
/HELP includes the same identification, a short description, usage, available
options, and where appropriate the terminal and external-file requirements.

Prefer memorable help and quit commands. Preserve established movement keys
where worthwhile and supply convenient alternatives. Do not impose identical
keys on command-driven adventures, board games, and action games. Explain
save, load, restart, and quit controls in the game itself.

Ask before discarding meaningful unsaved progress when the interaction permits
it. A cancelled command should leave play state intact. Restarting, abandoning
a game, and exiting to CP/M must be distinguishable where relevant.

Save/resume should be available for substantial games. Undo is appropriate
for puzzles and casual board play; it is not automatically appropriate for
every game or scored mode. High scores and statistics are optional.

Keep game rules separate from terminal operations. Start with small source-level
helpers for character output, input, cursor operations, and cleanup. Share
behavioral conventions across languages without forcing a single runtime.
