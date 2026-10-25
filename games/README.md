# Games

Candidate sources live in individual subdirectories. Each upstream/ tree
is an unchanged reference import with its own notices. Local README and
SOURCE.json files describe provenance, dependencies, and outstanding work.

| Game | Imported source |
| --- | --- |
| [Robots](robots/README.md) | C and matching MESCC runtime headers |
| [Snake](snake/README.md) | Turbo Pascal |
| [Hangman](hangman/README.md) | C, XTerm routines, sample words |
| [Ladder](ladder/README.md) | Turbo Pascal reconstruction and all includes |
| [Cpmtris](cpmtris/README.md) | Z80 assembly |
| [Minesweeper](minesweeper/README.md) | Find That Mine C, KS and MESCC headers |

These are source candidates, not qualified binaries or a final release lineup.
See the [catalog](../docs/game-catalog.md) for all editorial candidates and
[intake findings](../docs/source-intake.md) for this batch.

Each game should keep its source, instructions, provenance/license notices,
data requirements, build entry point, and relevant verification together.
Choose detailed per-game organization when selecting the implementation.
