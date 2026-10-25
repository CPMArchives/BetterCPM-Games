# Build tools

Build scripts belong here; generated artifacts belong in the ignored root
`build/` directory. No compiler or assembler has been selected for games yet.

Give every adopted game a documented, reproducible individual build command.
Record exact compiler/assembler/linker versions, options, library dependencies,
and generated data steps. Preserve upstream tool identities. Avoid bundling
compiler binaries without established redistribution rights.

Host cross builds are welcome. Native CP/M builds may also be supported when
useful; they are not a reason to complicate every small game's initial build.
A collection build should call the individual builders rather than duplicate
their logic. Add it when there are working games to collect.
