# Cpmtris — source intake

**Status:** unmodified upstream source, not a BetterCP/M Games release.
No compilation, gameplay, memory measurement, or CP/M runtime qualification has been performed for this intake.

Edition: Russell Marks v1.1 distribution.

## Source and license

Russell Marks, 1996/1999. The game README grants GPL v2 or later; COPYING is retained from the same repository. The README says v1.1 while the main source header still says v1.0; that upstream discrepancy is preserved. Use the original distribution rather than the later VT100/8 MHz default patch as the initial reference.

License summary: GPL-2.0-or-later. The top-level MIT license does not apply to upstream/.

Pinned source repositories:

- https://github.com/jamesots/zcn/commit/db3544f1363e209d40da24a838eb28b66319edc8

[SOURCE.json](SOURCE.json) records every imported file, original path, upstream Git blob, size, and SHA-256. All imported file bytes, including line endings and CP/M EOF markers, are unchanged. Prebuilt executables, disk images, compiler binaries, and unrelated assets are excluded.

## Build dependencies

External ZMAC assembler. Original Makefile concatenates cpmtris.z, rand.z, and conio.z, assembles out.z, and installs ../bin/cpmtris.com. Its ../bin destination belongs to the upstream tree and must be adapted later to this repository build/ convention. Required multiply/divide routines are present in cpmtris.z despite a generic maths.z comment in rand.z.

## Display and CPU

Z80; default 80x24 VT52 at 3.5 MHz, with VT100, ZCN and VC404 selection/calibration. rand.z uses the Z80 R register.

## Work before adaptation or release

Review shape selection, rotation, constant-speed gameplay, terminal profiles, and delay loops before choosing the final historical rules. Do not label this source 8080-compatible.
