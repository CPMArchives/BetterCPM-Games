# Game catalog

Assessment date: 2026-10-25. This is the original 24-entry editorial shortlist.
Only ADVENT's edition is approved. All other selections and approaches below
remain proposals. No candidate has been built or play-tested for this project.
Minimum TPA, peak runtime memory, stack use, executable size, and final CPU
compatibility are unmeasured for every entry.

| Category | Candidate | Edition or rules to investigate | Source finding / next step |
| --- | --- | --- | --- |
| Strategy and board | Chess | Compare worthwhile historical engines | CP/M Sargon assembly inspected; restrictive notice remains. Resolve permissions and compare alternatives. |
| Strategy and board | Checkers | Select rules and opponent strength | No adoption-ready source verified. |
| Strategy and board | Reversi | Standard 8x8 game with computer opponent | Historical Othello binary listed; reusable source unresolved. |
| Strategy and board | Gomoku | Decide board size and overline rules | No adoption-ready source verified. |
| Cards and dice | Solitaire | Select a specific patience game | No adoption-ready source verified; generic title is insufficient. |
| Cards and dice | Blackjack | Specify dealer, split, double, and payout rules | BLACKJAC.ARC listed in Walnut Creek; contents and permissions unverified. |
| Cards and dice | Poker | Select variant and meaningful computer opposition | No adoption-ready source verified. |
| Cards and dice | Yahtzee | Verify scoring and bonus rules | YAHTZE.ARC listed; source and permissions unverified. |
| Adventure and exploration | ADVENT | Original 350-point edition, approved | Goetz A02 has FORTRAN source and external data; compare other faithful implementations. |
| Adventure and exploration | Wumpus | Compare classic 20-room game with later variants | Historical BASIC leads; select precise behavior and permitted source. |
| Adventure and exploration | Star Trek | Compare Super Star Trek and Visual Star Trek | VTREKSRC.ARC explicitly listed as CP/M C source; contents and rights unverified. |
| Adventure and exploration | Dungeon crawler | Compare Rogue and other worthwhile crawlers | Goodenough CP/M Rogue 1.7 located; source and rights unresolved. |
| Arcade and action | Tetris | Select rotation, randomization, scoring, and speed behavior | Russell Marks's cpmtris: Z80 source, stated GPL v2, configurable terminal/speed. |
| Arcade and action | Snake | Select movement, growth, collision, and speed rules | Brokstad/linker3000 CP/M Turbo Pascal lineage: source, stated GPL v2. |
| Arcade and action | Robots | Compare classic BSD rules with CP/M variations | Garcia's C/MESCC implementation: source, stated GPL v2; limited teleport tickets. |
| Arcade and action | Sokoban | Select good levels and undo policy | Marks's CP/M C port: source, data file, undo and temporary save. Code and level rights unresolved. |
| Arcade and action | Ladder | Compare reconstruction with historical game | mecparts Turbo Pascal rewrite: GPL v3 repository; original LADCONF dependency and endgame fidelity need review. |
| Word and logic | Hangman | Curate words and difficulty | sblendorio C implementation: repository GPL v2, XTerm routines, external word file. |
| Word and logic | Mastermind | Specify code length, alphabet, repeats, and feedback | No adoption-ready source verified. |
| Word and logic | Boggle | Specify grid, dictionary, scoring, and timing | No adoption-ready source verified; dictionary licensing and storage need attention. |
| Word and logic | Minesweeper | Select board presets and first-move policy | Find That Mine: C/MESCC, Z80, GPL notice; coordinate commands, terminal/character-set assumptions. |
| Simulation and management | Hammurabi | Compare Ahl's game with richer historical management games | Historical BASIC and licensed-port leads; no chosen source. |
| Simulation and management | Lunar Lander | Choose numerical simulation or real-time action | LANDER.ARC listed; Storer's original numerical game documented separately. |
| Simulation and management | Trading game | Compare compelling trading and progression systems | STARSHIP.ARC listed as space trading with source; hardware assumptions and rights unverified. |

Sokoban is retained in the handoff's original category for traceability; it
is a turn-based spatial puzzle, not a real-time action game. Category labels
must not determine implementation assumptions.

## Provisional first release

ADVENT, Reversi, Yahtzee, Sokoban, Snake, Mastermind, Hammurabi, and Star Trek.
This proposed eight-game selection covers all six categories. It is based on
gameplay variety, not the relative convenience of available source. No game
is excluded from the broader collection by this proposal.

## Suggested opening work

Investigate ADVENT's exact edition, source permissions, and reproducible build
early. Proposed first implementation batch: Robots, Reversi, and ADVENT,
subject to maintainer review. Robots is an additional early pilot and does not
silently replace a game in the proposed release lineup.

## Evidence and limits

- [CP/M VT100 collection](https://git.imzadi.de/acn/vt100-games): source-bearing
  game directories and build notes for several candidates.
- [IF Archive CP/M catalog](https://www.ifarchive.org/indexes/if-archive/games/cpm/):
  distinguishes Goetz A02 (350), expanded editions, and other CP/M releases.
- [A02 archive contents](https://unbox.ifarchive.org/?url=/if-archive/games/cpm/cpm-advent.zip):
  FORTRAN source and game/data files are visible. A GPL file under advdis
  does not establish the license of the game.
- [Modern 350-point adaptation](https://microheaven.com/advent/): PunyInform
  implementation with CP/M support; assess fidelity and interpreter costs.
- [Ladder reconstruction](https://github.com/mecparts/Ladder): repository
  GPL v3; build notes describe Turbo Pascal, configuration dependencies,
  timing limits, and uncertainty about the original endgame.
- [Hangman](https://github.com/sblendorio/hangman-cpm): source, sample words,
  XTerm routines, and HI-TECH C build command.
- [Sargon CP/M source](https://github.com/z80playground/sargon-cpm/blob/main/sargon78.asm):
  original restrictive copyright notice remains in the inspected source.
- [Walnut Creek Beehive games listing](https://oldcomputers.dyndns.org/public/pub/cdrom/walnut_creek_cdrom/beehive/games/index.html):
  archive-level leads for Trek, Yahtzee, Blackjack, trading, and other games.
- [Storer's Lunar Landing archive](https://www.cs.brandeis.edu/~storer/LunarLander/LunarLander.html):
  primary historical material for the numerical landing game.

A stated repository license is a lead, not a completed audit of every file,
linked runtime, text, or data set. Archive descriptions are not source audits.
