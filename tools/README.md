# Build tools

Build scripts belong here; generated artifacts belong in the ignored root
`build/` directory. Imported games retain their upstream compiler/assembler
requirements; project build commands have not yet been established.

Run `python3 tools/verify_sources.py` from the repository root to verify the
unchanged upstream source inventory and checksums. This does not build games.

Give every adopted game a documented, reproducible individual build command.
Record exact compiler/assembler/linker versions, options, library dependencies,
and generated data steps. Preserve upstream tool identities. Avoid bundling
compiler binaries without established redistribution rights.

Host cross builds are welcome. Native CP/M builds may also be supported when
useful; they are not a reason to complicate every small game's initial build.
A collection build should call the individual builders rather than duplicate
their logic. Add it when there are working games to collect.
