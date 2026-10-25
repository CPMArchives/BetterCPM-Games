# Ladder — source intake

**Status:** unmodified upstream source, not a BetterCP/M Games release.
No compilation, gameplay, memory measurement, or CP/M runtime qualification has been performed for this intake.

Edition: mecparts Turbo Pascal reconstruction 1.33TP.

## Source and license

Turbo Pascal reconstruction by mecparts, drawing on the Java implementation by Stephen Ostermiller and Go implementation by Mats Engstrom. Retain the source grant (GPL v2 or later) and upstream LICENSE (GPL v3); the source election permits using v3. This is not the original Yahoo Software source.

License summary: GPL-2.0-or-later source grant; upstream repository supplies GPL v3 LICENSE. The top-level MIT license does not apply to upstream/.

Pinned source repositories:

- https://github.com/mecparts/Ladder/commit/d85f99c4f1d7ef6851431284f2497cb9b2e077af

[SOURCE.json](SOURCE.json) records every imported file, original path, upstream Git blob, size, and SHA-256. All imported file bytes, including line endings and CP/M EOF markers, are unchanged. Prebuilt executables, disk images, compiler binaries, and unrelated assets are excluded.

## Build dependencies

Turbo Pascal for CP/M; upstream entry point src/ladder.pas and all nine included Pascal modules are present. Configure terminal cursor sequences in ladconst.pas before a later build. Compiler not imported.

## Display and CPU

Screen-oriented ASCII platform game; configured cursor visibility sequences and Turbo Pascal terminal installation.

## Work before adaptation or release

Original LADCONF.COM is deliberately excluded: no separate redistribution grant for that historical binary was established. The source tries to chain to it when LADDER.DAT is missing. Replace or remove that dependency before a self-contained release. No LADDER.DAT is imported. Review seven-level endgame fidelity and delay calibration. Upstream README screenshot is omitted.
