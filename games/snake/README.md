# Snake — source intake

**Status:** unmodified upstream source, not a BetterCP/M Games release.
No compilation, gameplay, memory measurement, or CP/M runtime qualification has been performed for this intake.

Edition: 1.2acn Turbo Pascal conversion.

## Source and license

Original Karl A. Brokstad; Turbo Pascal conversion by linker3000 with permission; acn key/terminal changes. The source contains an explicit GPL v2-or-later grant.

License summary: GPL-2.0-or-later. The top-level MIT license does not apply to upstream/.

Pinned source repositories:

- https://git.imzadi.de/acn/vt100-games/commit/12e2e2c26351022b3aea03c1fc4184398e7770e3

[SOURCE.json](SOURCE.json) records every imported file, original path, upstream Git blob, size, and SHA-256. All imported file bytes, including line endings and CP/M EOF markers, are unchanged. Prebuilt executables, disk images, compiler binaries, and unrelated assets are excluded.

## Build dependencies

Turbo Pascal 3.0A for CP/M-80, compile SNAKE.PAS to a COM file. Compiler and runtime tools are external, not bundled. Upstream instructions assume an ANSI-configured 8 MHz system.

## Display and CPU

80x25 VT100/ANSI; upstream -m option suppresses color. Numeric and H/J/K/L movement.

## Work before adaptation or release

Check terminal geometry, CPU-speed calibration, and end-of-game cleanup. Do not assume an 80x24 target has an extra usable row.
