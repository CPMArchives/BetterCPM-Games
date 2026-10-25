# Game catalog

Assessment date: 2026-10-25. This is the original 24-entry editorial shortlist.
Only ADVENT's edition is approved. All other selections and approaches below
remain proposals. No candidate has been built or play-tested for this project.
Minimum TPA, peak runtime memory, stack use, executable size, and final CPU
compatibility are unmeasured for every entry.

Source intake update: unchanged candidate source is now tracked for
[Robots](../games/robots/README.md), [Snake](../games/snake/README.md),
[Hangman](../games/hangman/README.md), [Ladder](../games/ladder/README.md),
[Cpmtris](../games/cpmtris/README.md), and
[Minesweeper](../games/minesweeper/README.md). See the
[intake report](source-intake.md) for pinned provenance, license distinctions,
and missing runtime dependencies. Import does not finalize the release lineup.

Follow-up: source is also imported for [ADVENT 350](../games/advent/README.md),
[Hammurabi](../games/hammurabi/README.md),
[Mastermind](../games/mastermind/README.md), and
[Super Star Trek](../games/startrek/README.md). These require porting or
translation, rather than being ready-made CP/M games. See the
[preferred-game assessment](priority-source-assessment.md) for all seven
remaining source searches and reverse-engineering options. Release order is
flexible; games may wait for suitable sources without losing editorial merit.

| Category | Candidate | Edition or rules to investigate | Source finding / next step |
| --- | --- | --- | --- |
| Strategy and board | Chess | Compare worthwhile historical engines | CP/M Sargon assembly inspected; restrictive notice remains. Resolve permissions and compare alternatives. |
| Strategy and board | Checkers | Select rules and opponent strength | No adoption-ready source verified. |
| Strategy and board | Reversi | Standard 8x8 game with computer opponent | CP/M binary/BASIC leads; no adoption-ready source. A fresh bounded-search opponent is a credible fallback. |
| Strategy and board | Gomoku | Decide board size and overline rules | No adoption-ready source verified. |
| Cards and dice | Solitaire | Select a specific patience game | No adoption-ready source verified; generic title is insufficient. |
| Cards and dice | Blackjack | Specify dealer, split, double, and payout rules | BLACKJAC.ARC listed in Walnut Creek; contents and permissions unverified. |
| Cards and dice | Poker | Select variant and meaningful computer opposition | No adoption-ready source verified. |
| Cards and dice | Yahtzee | Verify scoring and bonus rules | Actual tokenized YAHTZE.BAS obtained, 398 structurally verified line records; recover matching-dialect listing, establish permissions. |
| Adventure and exploration | ADVENT | Original 350-point edition, approved | Licensed Gillogly/Berkeley C baseline imported. CP/M A02 FORTRAN remains a separate source/permissions lead. |
| Adventure and exploration | Wumpus | Compare classic 20-room game with later variants | Historical BASIC leads; select precise behavior and permitted source. |
| Adventure and exploration | Star Trek | Compare Super Star Trek and Visual Star Trek | Super Star Trek BASIC source imported; CP/M Visual Star Trek archive still unexamined. |
| Adventure and exploration | Dungeon crawler | Compare Rogue and other worthwhile crawlers | Goodenough CP/M Rogue 1.7 located; source and rights unresolved. |
| Arcade and action | Tetris | Select rotation, randomization, scoring, and speed behavior | Cpmtris source imported: original Z80 distribution, GPL v2-or-later, configurable terminal/speed. |
| Arcade and action | Snake | Select movement, growth, collision, and speed rules | Turbo Pascal 1.2acn source imported, GPL v2-or-later. |
| Arcade and action | Robots | Compare classic BSD rules with CP/M variations | C source and matching headers imported; game GPL v2-or-later, MESCC runtime GPL v3. |
| Arcade and action | Sokoban | Select good levels and undo policy | Source inspected but not imported: readme.v2 reports copied PC screens; game-code grant unresolved. |
| Arcade and action | Ladder | Compare reconstruction with historical game | Pascal source imported: source grant GPL v2-or-later, repository GPL v3 text. LADCONF.COM excluded. |
| Word and logic | Hangman | Curate words and difficulty | C/XTerm source and sample words imported under repository GPL v2 license. |
| Word and logic | Mastermind | Specify code length, alphabet, repeats, and feedback | Mastermind II BASIC imported; Ward/Zolman CP/M C inspected with permissions unresolved. |
| Word and logic | Boggle | Specify grid, dictionary, scoring, and timing | No adoption-ready source verified; dictionary licensing and storage need attention. |
| Word and logic | Minesweeper | Select board presets and first-move policy | Find That Mine 2.1 C/KS/MESCC source imported; GPL v3 family, coordinate commands, CP437/color assumptions. |
| Simulation and management | Hammurabi | Compare Ahl's game with richer historical management games | Classic BASIC source imported; standalone COM translation required. |
| Simulation and management | Lunar Lander | Choose numerical simulation or real-time action | LANDER.ARC listed; Storer's original numerical game documented separately. |
| Simulation and management | Trading game | Compare compelling trading and progression systems | STARSHIP.ARC listed as space trading with source; hardware assumptions and rights unverified. |

Sokoban is retained in the handoff's original category for traceability; it
is a turn-based spatial puzzle, not a real-time action game. Category labels
must not determine implementation assumptions.

## Preferred editorial group; flexible release order

ADVENT, Reversi, Yahtzee, Sokoban, Snake, Mastermind, Hammurabi, and Star Trek.
This eight-game group covers all six categories and remains a useful
editorial preference, not a fixed first-release commitment. Release order
may follow source readiness and engineering progress. No game is removed
from consideration merely because it must wait for sources.

## Suggested opening work

Use the source candidates now available to choose a manageable opening batch.
Prioritize playable quality and variety, while continuing source recovery for
the preferred games. ADVENT has a licensed C baseline but substantial CP/M
porting work; Reversi and Yahtzee can use fresh implementations if appropriate.
The other imports remain candidates without silently replacing preferred games.

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
