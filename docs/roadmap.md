# Roadmap

## Current foundation

- Separate repository and project documentation.
- Original 24-entry catalog and preliminary implementation leads.
- Compatibility, interface, provenance, build, and versioning conventions.

There are no game binaries, imported third-party sources, assigned game
revisions, or completed compatibility qualifications yet.

## Complete the assessment

1. Compare the proposed first-release games on actual gameplay merits.
2. Select precise rules and editions, especially Star Trek, Solitaire, Poker,
   Lunar Lander, the dungeon crawler, and the trading game.
3. Inspect promising CP/M source packages and their notices. Resolve runtime
   and content rights separately. Establish reproducible baseline builds.
4. Measure memory, terminal assumptions, dependencies, and CPU requirements.
5. Recommend implementation approaches and concrete initial scopes for review.

Effort estimates remain coarse until a baseline exists: small for local polish
on reproducible source, medium for substantial interface/save/terminal work,
and large or uncertain for compiler reconstruction, major translation, new
opponent logic, or reimplementation. These are planning categories, not
measured estimates or delivery promises.

## Proposed first implementation batch

Robots, Reversi, and ADVENT are proposed pilots. Investigate ADVENT early even
if another pilot becomes playable first. Obtain maintainer agreement before
imports or substantial implementation. Preserve approved edition choices
when selecting a later or different implementation.

Add only the helpers demonstrated necessary by these games. Keep existing
implementation languages where they remain maintainable; do not mandate a
rewrite into assembly or a single compiler for collection uniformity.

## First release proposal

ADVENT, Reversi, Yahtzee, Sokoban, Snake, Mastermind, Hammurabi, and Star Trek.
Confirm this lineup after gameplay and source assessment. Release individual
games as they reach the quality bar; a collection milestone need not delay
every useful program until all candidates are ready.

For release, provide corresponding source, notices, per-game instructions,
exact artifact identities, required data, and verification records. Prepared
disk images follow demonstrated demand and working standalone packages.
