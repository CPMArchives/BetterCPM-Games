# Star Trek — source intake

**Status:** unchanged source candidate, not a playable BetterCP/M Games release.

Edition: 1978 Super Star Trek BASIC lineage, normalized transcription.

## Source and license

Upstream repository Unlicense retained. Preserve source credits to Mike Mayfield, David Ahl, Bob Leedom, and John Gorders. The source records a 1978 Microsoft 8K BASIC conversion; the present transcription was normalized for Vintage BASIC.

Pinned repository: https://github.com/coding-horror/basic-computer-games/commit/5301155192d91d74d337899cecc59dbda59c4c17

[SOURCE.json](SOURCE.json) identifies every imported path, Git blob, byte count, and SHA-256. All imported bytes are unchanged. The top-level MIT license does not relicense upstream/.

## Findings

The main listing is 425 lines, 20467 bytes, and states a historical 24K memory requirement. That is an upstream requirement, not a measured COM/TPA footprint. It includes navigation, scans, phasers, torpedoes, shields, damage, and library-computer functions.

## Work before release

Interpret with a compatible BASIC for baseline comparison, or translate for a standalone CP/M COM. Numeric navigation and combat, string-based maps, and save-state design need work. This is a concrete candidate, not an editorial decision against Visual Star Trek or later refinements.

No compilation, execution, memory measurement, or terminal qualification is claimed. Availability of source does not by itself select the final implementation or release order.
