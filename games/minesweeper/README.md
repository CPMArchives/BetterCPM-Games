# Find That Mine — source intake

**Status:** unmodified upstream source, not a BetterCP/M Games release.
No compilation, gameplay, memory measurement, or CP/M runtime qualification has been performed for this intake.

Edition: 2.1 color CP/M adaptation.

## Source and license

Miguel Garcia / FloppySoftware, with color changes by Anna Christina Nass. ftm.c and ks.h explicitly grant GPL v3 or later; MESCC headers specify GPL v3. The matching headers from this adapted package are retained, avoiding an unverified mix with newer libraries.

License summary: GPL-3.0-or-later game and KS library; MESCC runtime headers GPL-3.0. The top-level MIT license does not apply to upstream/.

Pinned source repositories:

- https://git.imzadi.de/acn/vt100-games/commit/12e2e2c26351022b3aea03c1fc4184398e7770e3

[SOURCE.json](SOURCE.json) records every imported file, original path, upstream Git blob, size, and SHA-256. All imported file bytes, including line endings and CP/M EOF markers, are unchanged. Prebuilt executables, disk images, compiler binaries, and unrelated assets are excluded.

## Build dependencies

MESCC: put upstream/mescc/*.h on the include path beside ftm.c and ks.h; CC FTM, CCOPT FTM, ZSM FTM, HEXTOCOM FTM. Compiler/tool executables are external, not imported. This 2.1 source includes ks.h but not ks_cent.h; do not confuse it with the original 2.0 source dependencies.

## Display and CPU

Upstream 2.1 defaults to VT100COL, has coordinate-based commands and CP437 border characters enabled by default. KS also contains named terminal profiles. Validate the actual game/profile combinations before claiming support.

## Work before adaptation or release

Make ASCII/monochrome presentation selectable, review first-move and random placement rules, and verify each advertised terminal. Keep FTM as the upstream name until a BetterCP/M identity is assigned.
