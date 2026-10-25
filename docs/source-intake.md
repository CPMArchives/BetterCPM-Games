# First source intake — 2026-10-25

This records the first six imports. See the
[preferred-game follow-up](priority-source-assessment.md) for four further
source imports and the current flexible-release planning decision.

The maintainer has authorized source discovery and import. This batch
preserves candidates for examination and adaptation; it does not finalize
game editions, release membership, or BetterCP/M game revisions.

| Candidate | Source imported | Next engineering question |
| --- | --- | --- |
| [Robots](../games/robots/README.md) | C game, matching MESCC runtime headers, docs and license texts | Establish build; compare rules and terminal behavior. |
| [Snake](../games/snake/README.md) | Turbo Pascal source, docs and GPL notice | Calibrate timing and screen dimensions. |
| [Hangman](../games/hangman/README.md) | C game, XTerm source/header, upstream sample words and license | Establish build; curate suitable words. |
| [Ladder](../games/ladder/README.md) | Main Turbo Pascal source and all nine include modules, docs and license | Remove original LADCONF.COM dependency. |
| [Cpmtris](../games/cpmtris/README.md) | Original Z80 source trio, Makefile, game README and GPL text | Establish assembler build and terminal/speed settings. |
| [Minesweeper](../games/minesweeper/README.md) | Find That Mine 2.1, KS and matching MESCC headers, docs and GPL text | Establish build; inspect ASCII/color/profile handling. |

Every imported file has an original path, pinned repository commit, Git blob
ID, byte count, and SHA-256 in its game's SOURCE.json. Imported bytes are
unchanged. Upstream binaries, compiler executables, disk images, screenshots,
and unrelated assets are excluded. Per-game READMEs describe dependencies.

Robots and Find That Mine use the VT100 collection's matching headers, rather
than an unverified mixture with current compiler-library versions. Cpmtris
uses the original ZCN distribution source before the VT100/8 MHz default patch.
These choices identify starting points without binding final game editions.

## Findings

- Robots grants GPL v2 or later, but its bundled MESCC headers use GPL v3.
  Both license texts and the distinction are retained.
- Ladder's source grants GPL v2 or later; its repository supplies GPL v3.
  Both notices are retained. The source election permits v3.
- Ladder expects original LADCONF.COM when configuration is missing. No
  separate redistribution grant for that binary was established, so it is
  excluded. The reconstruction is not yet a self-contained playable package.
- Hangman's supplied words are Italian place names, not a curated English
  vocabulary. They identify the upstream sample, not the final word list.
- Cpmtris's README says v1.1, while its main source header says v1.0. The
  reference import preserves that upstream discrepancy.
- Sokoban's readme.v2 says the PC screens were copied; the inspected package
  also lacks a sufficiently clear game-code grant. Its code and levels are
  not imported. Seek a licensed implementation and cleared level set.
- Sargon's inspected source retains a reproduction restriction and is not
  imported. Chess remains an editorial candidate.
- ADVENT A02 has identifiable 350-point FORTRAN source, but game/text
  permissions and a reproducible build remain unresolved. A GPL text for
  extraction tools does not license the adventure. ADVENT stays approved;
  no expanded edition is substituted.

## Verification and limits

Run `python3 tools/verify_sources.py` to check the inventory, Git blob IDs,
SHA-256 values, and sizes of imported files. During intake the bytes were
also compared directly with the selected upstream Git commits. Pascal include
modules and MESCC header dependencies were inspected for completeness.

No compilation, game execution, TPA measurement, terminal qualification, or
gameplay testing is claimed. Establish those baselines before modifying the
implementations or publishing runnable releases.
