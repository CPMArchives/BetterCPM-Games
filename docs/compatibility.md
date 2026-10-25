# Compatibility

## Target

Standard CP/M 2.2-compatible BDOS interface and conventional .COM programs.
BetterCP/M is the principal development environment, not a required runtime.
Prefer 8080-compatible code when practical; label Z80 requirements explicitly.
Do not sacrifice a good existing implementation merely to remove every Z80
instruction without a worthwhile portability benefit.

Use portable console and file services. Keep machine-specific ports and
display hardware out of portable game logic. Optional BetterCP/M features
must have an ordinary CP/M fallback unless separately justified and approved.

## Display and input

Separate character repertoire from terminal control: ASCII output can still
require cursor addressing. Declare supported dimensions, terminal profile,
color assumptions, and keyboard requirements for each game.

Offer a scrolling text mode where useful. Screen-oriented games may require
VT100/ANSI or another documented profile. They need not offer an unplayable
plain-console imitation. Support monochrome and ordinary ASCII glyphs where
practical; do not require CP437 characters accidentally.

Terminal configuration should be selectable without patching machine code.
Provide movement alternatives for keyboards without a numeric keypad or
working arrow-key escape sequences. Restore terminal state on normal exit
and handled failures.

## Memory and storage

Do not assume a fixed TPA or infer free memory from a nominal 64K machine.
Record executable size, static data, heap, stack allowance, buffers, external
files, overlays, and minimum demonstrated TPA for each supported build.
Keep upper-memory assumptions explicit and report insufficient memory cleanly.

Use CP/M-compatible 8.3 filenames for shipped and saved files. Handle missing
data, write protection, full disks, malformed saves, and failed writes without
claiming success. Preserve the previous valid save when practical; describe
the actual replacement/recovery procedure rather than promising atomicity.

## Timing and randomness

Real-time games must document calibration and connection-speed requirements.
No universal real-time clock is assumed. Avoid making delay-loop behavior an
unexamined consequence of CPU frequency or emulator speed.

Randomness must not silently require the Z80 refresh register in an otherwise
8080 build. Support repeatable seeds during investigation where useful.

## Qualification record

For each released game record the CPU, OS, emulator or machine, terminal,
geometry, TPA, compiler/options, required data, and directly exercised behavior.
Initially verify BetterCP/M and a standard CP/M 2.2 environment. Broaden the
matrix when actual target differences warrant it.
