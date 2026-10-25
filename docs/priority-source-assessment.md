# Preferred games: sources and reconstruction options

Assessment: 2026-10-25. Release order is flexible. ADVENT, Reversi, Yahtzee,
Sokoban, Snake, Mastermind, Hammurabi and Star Trek remain a useful editorial
priority group, not a fixed release sequence. Source availability determines
implementation route and timing, not editorial merit.

## Findings

| Game | Verified finding | Recommended route | Work remaining |
| --- | --- | --- | --- |
| ADVENT 350 | Gillogly/Berkeley C source, database, generator and BSD notices imported. Goetz A02 remains a separate unresolved CP/M candidate. | Keep the approved edition. Compare A02 if permissions/build become clear; otherwise port the licensed C baseline. | Large relative to small games: memory/data layout, Unix services, saves and exact fidelity. No disassembly needed. |
| Reversi | CP/M OTHELLO binary and BASIC catalog leads; no adoption-ready CP/M source established. Compact historical non-CP/M C player also located. | A new standard-rules implementation with bounded-search opponent is credible. Study a specific binary if its playing style matters. | Rules/UI small; opponent strength and CP/M response time moderate. No firm disassembly estimate without inspecting a selected binary. |
| Yahtzee | Actual 9728-byte YAHTZE.BAS obtained: 398 coherent tokenized BASIC line records. | Recover an ASCII listing using the matching dialect before considering disassembly. Alternatively implement selected rules directly. | Listing recovery likely small; standalone game small-to-medium. Source permissions unresolved, so file not imported. |
| Sokoban | CP/M port has unclear code rights and copied PC screens. Additional 3S/T3X and Sokoban RK/C source leads found. | Seek engine and level permissions separately; a new move/push/undo engine is a reasonable fallback. | Core small-to-medium; good levels, undo storage and saves are separate work. Whole-binary reconstruction not presently justified. |
| Snake | CP/M Turbo Pascal source already imported. | Build and evaluate existing implementation. | Terminal geometry, controls and timing; no reconstruction needed. |
| Mastermind | Ward/Zolman CP/M-era C source obtained for inspection, permissions unresolved. Mastermind II BASIC source imported separately. | Evaluate rules/solver; translate the licensed BASIC candidate or implement selected rules directly. | Small for human guessing; moderate with computer code-breaking, hints and configurable sizes. |
| Hammurabi | Readable BASIC listing imported: 119 lines, 4055 bytes. | Establish behavior and translate for standalone COM. | Small-to-medium, with careful numeric and assessment behavior. No reconstruction needed. |
| Star Trek | Super Star Trek BASIC imported: main listing 425 lines, 20467 bytes. VTREKSRC.ARC remains an unexamined archive lead. | Compare this baseline with Visual Star Trek and period refinements. Prefer source translation to disassembly. | Moderate-to-large: navigation/combat arithmetic, maps, interface and saves. |

These are comparative engineering judgments, not measured delivery estimates.
No imported candidate has been compiled, played, timed or TPA-qualified here.

## Additional source imports

[ADVENT](../games/advent/README.md) now has the BSDGames adventure directory,
database, generator, build descriptions and notices. Most source uses
three-clause BSD terms; extern.h retains Christos Zoulas's four-clause notice
and acknowledgment requirement. This is the classic 350-point lineage,
not the 430-point Open Adventure edition. Full puzzle fidelity remains to test.

[Hammurabi](../games/hammurabi/README.md),
[Mastermind](../games/mastermind/README.md), and
[Star Trek](../games/startrek/README.md) include the BASIC listings and relevant
instructions from coding-horror/basic-computer-games, with its Unlicense and
provenance documents. They were normalized for Vintage BASIC; they are not
already qualified CP/M builds. The required standalone COM releases will
need translation/compilation rather than distributing an interpreter alone.

Each SOURCE.json pins the commit and exact bytes. No game revision is assigned.
David Ahl's June 2022 public-domain declaration is reproduced by TRS-80 Revived;
older noncommercial-permission pages describe an earlier state. Preserve
credited authors and actual repository terms rather than extending one
archive's permission to unrelated contributions.

## ADVENT feasibility

Its raw database is 56375 bytes. Upstream generates an in-memory C array and
builds linked travel structures, so recompiling it unchanged is not a small-TPA
plan. Investigate external text/travel records, compact runtime structures,
and replacement of Unix save, signal, random and file services. This is a
substantial source port rather than an adoption-and-polish estimate. The score
routine and database were inspected; no end-to-end solution was run.

## Yahtzee recovery evidence

URL: https://electrickery.hosting.philpem.me.uk/comp/px8/oldcomputersTools/yahtze.bas

- Download: 9728 bytes.
- SHA-256: `24ad6fb6b78e124cd83f6e8f21c9eb73a243b0cda38acff33f9f5b096f95bd73`.
- Header: FF 25 FB; first linked line record begins at file offset 3.
- Pointer-to-file offset 8B2Bh follows all 398 records, line numbers 10 through
  3910, to the zero-pointer terminator at file offset 9724. Records end in
  zero and line numbers increase monotonically.
- Strings include the game name, scoring labels and instructions, but no
  established author or reuse grant was found in inspected strings.

This is structural recovery evidence, not a complete detokenization or working
game. Match the Epson/Microsoft BASIC dialect; do not blindly substitute
GW-BASIC tokens. LOAD/LIST with the matching interpreter and save an ASCII
listing where supported. Recovery and permission to publish are distinct.

## Reverse engineering choices

1. Recover source representation: expand tokenized BASIC or extract a listing.
   Yahtzee is a concrete candidate; its interpreter need not be disassembled.
2. Study behavior: run a historical binary and identify rules, scoring, options
   and interface. This may suffice for a new implementation.
3. Reconstruct code: disassemble to recover algorithms/data structures when
   a specific engine, opponent or undocumented behavior merits the effort.

Mastermind, Yahtzee and Sokoban's basic engine are credible fresh-implementation
candidates. Reversi's old opponent may merit observation, although a clean
bounded-search engine may be easier to maintain. ADVENT and Star Trek now
have substantial source baselines. Reconstructing code does not establish
redistribution rights to that code, game text or levels.

## Release planning

Keep the balanced preferred group without forcing replacements now. Five of
its eight games now have imported source candidates. Ship worthwhile games
as their builds and polish become ready; the other initial imports remain
candidates without silently replacing preferred games.

## Sources and remaining leads

- https://github.com/vattam/BSDGames/tree/master/adventure
- https://github.com/coding-horror/basic-computer-games
- https://www.trs-80.com/sub-old-news-site-news-2021-2023.htm (June 15, 2022)
- https://www.sydneysmith.com/wordpress/cpm-mm/ and
  https://www.sydneysmith.com/products/cpm-mm/mm1.c (Ward/Zolman C obtained)
- https://sourceforge.net/projects/mastermindrk/files/ (single-file z88dk C
  source lead; archive not obtained, so license not audited)
- https://www.seasip.info/Unix/Joyce/pcwpd_catalogue.html (OTHELLO.BAS,
  YAT.BAS/YATSCORE.BAS, MASTMIND.COM leads)
- https://www.gaby.de/ftp/pub/cpm/znode51/fog/ (YAHTZEE.BAS, MASTERMD.BAS leads)
- https://www.ioccc.org/1987/lievaart/index.html (compact 1987 Reversi player;
  source availability alone does not make obfuscated code a good starting point)
- https://t3x.org/DOS/index.html and https://t3x.org/DOS/3s20xe.zip (archive
  inspected: T3X R7, 38909-byte main source, undo/saves; custom short license
  notice and Sasquatch levels marked used with permission. Not T3X/0 CP/M code.)
- https://sourceforge.net/projects/sokobanrk/ (C/z88dk lead; original level
  set included, requiring asset review independently of engine permissions)
- https://oldcomputers.dyndns.org/public/pub/cdrom/walnut_creek_cdrom/beehive/games/index.html
  (VTREKSRC.ARC listed as C source; download returned an access error here)

Unobtained archives do not establish source unavailability. This is not an
exhaustive search or a completed reconstruction/runtime qualification.
