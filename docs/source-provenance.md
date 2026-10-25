# Source provenance and licensing

Investigate existing CP/M implementations first. Evaluate source completeness,
gameplay, dependencies, portability, and rights independently. An archived
binary, a published listing, or a public GitHub repository is not by itself
permission to redistribute and modify the work.

Before importing a game, place a provenance record beside its source covering:

- Game and selected historical edition; upstream authors and implementation.
- Exact archive/repository URL, version or commit, retrieval date, and checksum.
- Source completeness and any generated, missing, or reconstructed portions.
- Language, CPU, toolchain, libraries, runtime, data files, and overlays.
- Actual license notices and the files to which they apply.
- Separate provenance and permissions for text, puzzles, levels, dictionaries,
  graphics, configuration tools, and other included assets.
- Local changes, intentional rule differences, build reproduction, and checks.

Retain all upstream notices. Original project material uses the top-level MIT
license; imported components retain their applicable terms. Review compatibility
of linked components for each executable. Do not apply one repository license
to unrelated historical material or infer a game's license from a utility
bundled in the same archive.

Mark unresolved permissions explicitly and keep such code outside the tracked
project until the implementation is approved. A new implementation may be an
option, but writing new code does not establish rights to copied text, levels,
or other content. Document the intended sources and boundaries before work.

Source discovery and inspection are authorized. Third-party imports and
substantial implementation await maintainer review of the selected approach.
