# Mastermind — source intake

**Status:** unchanged source candidate, not a playable BetterCP/M Games release.

Edition: Steve North / Creative Computing Mastermind II BASIC listing, normalized transcription.

## Source and license

Upstream repository Unlicense retained. The listing credits Steve North and Creative Computing. The upstream README documents Vintage BASIC normalization; preserve this provenance instead of calling it an original CP/M source.

Pinned repository: https://github.com/coding-horror/basic-computer-games/commit/5301155192d91d74d337899cecc59dbda59c4c17

[SOURCE.json](SOURCE.json) identifies every imported path, Git blob, byte count, and SHA-256. All imported bytes are unchanged. The top-level MIT license does not relicense upstream/.

## Findings

232 BASIC lines, 5203 bytes. This version supports both human and computer code-breaking, configurable colors and positions, and a history display. Its I(P) candidate array grows as colors^positions: bounds must be selected for a CP/M TPA.

## Work before release

A compatible BASIC can provide a behavioral baseline. A standalone COM implementation may translate the rules and candidate filtering into C or assembly. Test duplicate-color feedback, impossible clues, candidate storage, and input bounds. Source already exists; binary disassembly is unnecessary.

No compilation, execution, memory measurement, or terminal qualification is claimed. Availability of source does not by itself select the final implementation or release order.
