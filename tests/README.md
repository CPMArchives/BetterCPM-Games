# Verification

Use checks proportional to each change. No game tests exist yet.

For an adopted game, establish that it builds, starts, supports /HELP and /VER,
plays its fundamental rules, and returns cleanly to CP/M. Exercise saves,
terminal modes, memory limits, and critical failures when applicable.

Use focused deterministic tests for nontrivial rules or demonstrated bugs.
Do not build a large testing framework or rerun unrelated suites for small
identification/documentation changes. Record the actual tested environments
and distinguish successful builds from runtime qualification.
