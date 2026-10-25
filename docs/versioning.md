# Version and revision tracking

Each game has its own implementation version and revision identity:
`GAME 1.0 (001)`. The revision is not a count of compiler invocations. Rebuilding
the same accepted inputs does not advance it. An unrelated game's changes
do not advance it.

Keep these separate:

| Identity | Purpose |
| --- | --- |
| Game version | Maintainer-assigned user-facing development milestone |
| Game revision | Independent accepted executable revision |
| Repository commit | Repository-wide source provenance |
| Collection release | Distribution milestone containing specific game revisions |

Use a small authoritative metadata registry when the first game is implemented.
Do not assign fictional versions or revisions to catalog candidates. Build
scripts consume identities; ordinary builds do not increment counters.

Follow BetterCP/M's current acceptance principle: compare candidate artifacts
under the same assigned identity and display state. Input changes trigger
review, not automatic increments. If an executable remains unchanged, retain
its revision. A changed linked shared routine can affect several games;
review those consumers rather than every game in the repository.

Track externally loaded game data by version/checksum in the game package
record. A level or text change may change the package even when its executable
does not. Save formats need their own compatibility marker; a game revision
is not a substitute for a file-format version.

Build records should identify the game, version/revision, target/profile,
source commit when known, toolchain and options, artifact sizes/checksums,
and required data files. Do not embed the current repository commit into every
game on every build solely to make unchanged executables different.

The collection release manifest selects exact executable and data artifacts.
No metadata generator or release automation is needed until real artifacts
exist. Preserve the conventions without copying the operating system's full
tracking infrastructure prematurely.
