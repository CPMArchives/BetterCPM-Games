# Hammurabi — source intake

**Status:** unchanged source candidate, not a playable BetterCP/M Games release.

Edition: Ahl / Creative Computing BASIC listing, Vintage BASIC-normalized transcription.

## Source and license

Upstream repository publishes these files under the Unlicense; retain LICENSE. David Ahl also issued a public-domain declaration in June 2022. The repository README identifies Lyle Kopnicky's Vintage BASIC normalization, so this is not claimed to be an untouched 1978 typescript.

Pinned repository: https://github.com/coding-horror/basic-computer-games/commit/5301155192d91d74d337899cecc59dbda59c4c17

[SOURCE.json](SOURCE.json) identifies every imported path, Git blob, byte count, and SHA-256. All imported bytes are unchanged. The top-level MIT license does not relicense upstream/.

## Findings

119 BASIC lines, 4055 bytes. Source is readable; no binary reverse engineering is needed. The ten-year land/grain/population simulation and end-of-term assessment are present.

## Work before release

Interpret with a compatible BASIC for initial investigation, or translate into a suitable CP/M compiler language for the required standalone COM release. No interpreter/compiler is bundled. Verify numeric rounding, plague/starvation, and assessment behavior before adaptation.

No compilation, execution, memory measurement, or terminal qualification is claimed. Availability of source does not by itself select the final implementation or release order.
