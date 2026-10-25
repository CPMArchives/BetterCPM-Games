# Hangman — source intake

**Status:** unmodified upstream source, not a BetterCP/M Games release.
No compilation, gameplay, memory measurement, or CP/M runtime qualification has been performed for this intake.

Edition: sblendorio CP/M C implementation.

## Source and license

Stefano Blendorio. Repository LICENSE supplies GPL v2; source and XTerm files are imported from the same published repository. The supplied words.txt is a small Italian place-name sample, not an English game dictionary. It is retained as the upstream sample under the repository license, not presented as a final word set.

License summary: GPL v2 repository license; original LICENSE retained. The top-level MIT license does not apply to upstream/.

Pinned source repositories:

- https://github.com/sblendorio/hangman-cpm/commit/cdc50ae43b0116ab29550cd511ad46f246dc4ea9

[SOURCE.json](SOURCE.json) records every imported file, original path, upstream Git blob, size, and SHA-256. All imported file bytes, including line endings and CP/M EOF markers, are unchanged. Prebuilt executables, disk images, compiler binaries, and unrelated assets are excluded.

## Build dependencies

HI-TECH C 3.09 CP/M command documented upstream: c -lf hangman.c xterm.c. Standard compiler headers/libraries remain external. Upstream also documents POSIX GCC and Amiga builds; none has been run here.

## Display and CPU

XTerm source supports VT52, VT100, ANSI, Kaypro, ADM31, C128, Memotech, and CPC/Z19; source layout includes 80-column coordinates.

## Work before adaptation or release

Curate a suitable word list and document its provenance. Inspect word selection and file access before adapting. Upstream README links to omitted screenshots and binary distributions.
