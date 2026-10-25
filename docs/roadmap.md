# Roadmap

## Current foundation

- Separate repository and project documentation.
- Original 24-entry catalog and preliminary implementation leads.
- Compatibility, interface, provenance, build, and versioning conventions.
- First source intake: Robots, Snake, Hangman, Ladder, Cpmtris, and Find That
  Mine, preserved unchanged with file checksums and license notices.
- Preferred-game follow-up: ADVENT 350 C plus Hammurabi, Mastermind II and
  Super Star Trek BASIC sources imported with the same provenance records.

There are no game binaries, assigned BetterCP/M game revisions, or completed
compatibility qualifications yet. Source intake does not finalize the lineup.

## Complete the assessment

1. Compare the proposed first-release games on actual gameplay merits.
2. Select precise rules and editions, especially Star Trek, Solitaire, Poker,
   Lunar Lander, the dungeon crawler, and the trading game.
3. Inspect promising CP/M source packages and their notices. Resolve runtime
   and content rights separately. Ten source candidates are imported;
   establish their reproducible baseline builds next.
4. Measure memory, terminal assumptions, dependencies, and CPU requirements.
5. Recommend implementation approaches and concrete initial scopes for review.

Effort estimates remain coarse until a baseline exists: small for local polish
on reproducible source, medium for substantial interface/save/terminal work,
and large or uncertain for compiler reconstruction, major translation, new
opponent logic, or reimplementation. These are planning categories, not
measured estimates or delivery promises.

## Choose a manageable opening batch

Release order is flexible. Begin with worthwhile games whose builds and
adaptation scope can be made concrete; let other preferred games wait for
sources. Continue ADVENT investigation early because its source port is
substantial. Source imports are authorized; agree on adaptation scope before
substantial implementation. Preserve the approved 350-point edition.

Add only the helpers demonstrated necessary by these games. Keep existing
implementation languages where they remain maintainable; do not mandate a
rewrite into assembly or a single compiler for collection uniformity.

## Preferred group and release planning

ADVENT, Reversi, Yahtzee, Sokoban, Snake, Mastermind, Hammurabi, and Star Trek.
This is an editorial priority group, not a fixed first-release lineup or
sequence. Release individual games as they reach the quality bar; let other
preferred games wait for sources. See the
[source and reconstruction assessment](priority-source-assessment.md).

For release, provide corresponding source, notices, per-game instructions,
exact artifact identities, required data, and verification records. Prepared
disk images follow demonstrated demand and working standalone packages.
