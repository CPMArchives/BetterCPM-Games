# Robots — source intake

**Status:** unmodified upstream source, not a BetterCP/M Games release.
No compilation, gameplay, memory measurement, or CP/M runtime qualification has been performed for this intake.

Edition: Miguel Garcia 1.01, with acn VT100 clear-screen change.

## Source and license

Miguel I. Garcia Lopez / FloppySoftware; VT100 change by Anna Christina Nass. The game grants GPL v2 or later. Its bundled MESCC headers explicitly use GPL v3; any future executable using those headers must respect that combination. Both license texts are included.

License summary: GPL-2.0-or-later game; bundled MESCC runtime headers GPL-3.0. The top-level MIT license does not apply to upstream/.

Pinned source repositories:

- https://git.imzadi.de/acn/vt100-games/commit/12e2e2c26351022b3aea03c1fc4184398e7770e3
- https://github.com/MiguelVis/ftm/commit/9971bb8b0ce16c7ffe581579dc69702a068e4261

[SOURCE.json](SOURCE.json) records every imported file, original path, upstream Git blob, size, and SHA-256. All imported file bytes, including line endings and CP/M EOF markers, are unchanged. Prebuilt executables, disk images, compiler binaries, and unrelated assets are excluded.

## Build dependencies

MESCC for CP/M-80: place upstream/mescc/*.h on the include path; CC ROBOTS, CCOPT ROBOTS, ZSM ROBOTS, HEXTOCOM ROBOTS. Compiler, assembler, and conversion executables are external and not imported. The game also contains CP/M-86 and SamaruX branches, not selected for this project.

## Display and CPU

VT100 clear-screen sequence; turn-based numeric movement and limited teleport tickets.

## Work before adaptation or release

Review rules against BSD Robots, terminal redraw behavior, input handling, and random seeding before adaptation. No BetterCP/M identity assigned.
