# BetterCP/M Games

**Historically inspired, not historically constrained.**

A curated, open-source collection of classic games for CP/M-compatible
computers. The aim is enjoyable gameplay, thoughtful presentation, and a
coherent collection, drawing on mainframe, minicomputer, Unix, and early
microcomputer traditions as well as traditional and original games.

BetterCP/M is the principal development and testing environment. Ordinary
gameplay should generally work on standard CP/M 2.2 without BetterCP/M
extensions. This project is independent of the
[BetterCP/M operating system](https://github.com/CPMArchives/BetterCPM).

## Project status

Source investigation and intake. Unmodified source for Robots, Snake,
Hangman, Ladder, Cpmtris, Find That Mine, ADVENT 350, Hammurabi, Mastermind,
and Super Star Trek is included with upstream notices and pinned provenance.
The latter four require source porting or translation for standalone CP/M.
See the [preferred-game assessment](docs/priority-source-assessment.md),
[source intake](docs/source-intake.md) and
[game sources](games/README.md). No playable BetterCP/M Games releases have
been built yet. ADVENT's original 350-point edition is approved; other
editions and the release lineup remain provisional.

## Start here

- [Project principles](docs/overview.md)
- [Game catalog and preliminary source findings](docs/game-catalog.md)
- [Compatibility requirements](docs/compatibility.md)
- [Interface conventions](docs/interface-conventions.md)
- [Version and revision tracking](docs/versioning.md)
- [Source provenance and licensing](docs/source-provenance.md)
- [Source intake findings](docs/source-intake.md)
- [Preferred games and reverse-engineering options](docs/priority-source-assessment.md)
- [Development roadmap](docs/roadmap.md)
- [Build conventions](tools/README.md)
- [Contributing](CONTRIBUTING.md)

Game selection comes before source selection. Existing CP/M implementations
are the first engineering candidates, but available source determines how we
build a game, not whether it deserves inclusion.

## Licensing

Original material in this initial repository is available under the
[MIT license](LICENSE). Imported third-party components retain their own
licenses and notices, detailed in [LICENSES.md](LICENSES.md); MIT does not relicense historical games,
text, level sets, dictionaries, or compiler runtimes.
