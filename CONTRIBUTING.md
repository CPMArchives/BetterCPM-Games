# Contributing

Choose games on gameplay quality, variety, historical character, and fitness
for CP/M-class machines. Source availability affects engineering and schedule,
not editorial merit. Avoid adding games merely because code is convenient.

Before implementing a game:

1. Propose the game and exact rules or historical edition.
2. Investigate existing CP/M implementations before starting a Unix port or
   new implementation.
3. Record provenance, source completeness, permissions, language, CPU,
   terminal requirements, data files, and build dependencies.
4. Recommend adopt and polish, adapt and modernize, port, or reimplement.
5. Obtain maintainer agreement on the implementation and scope before
   importing third-party code or beginning substantial implementation.

Preserve recognizable gameplay. Explain intentional rule changes and offer
them as separate options when practical. Do not introduce rule changes as
unnoticed consequences of translation or interface work.

Follow the interface, compatibility, and versioning documents. Retain
third-party notices and review the licenses of linked libraries and data.
Keep compiler installation separate from the shipped games.

Verification should be proportional: build, start, play the affected paths,
exit cleanly, and check relevant saves, terminal behavior, memory limits,
and failures. Add focused rule tests where they prevent real regressions.
An elaborate shared testing framework is not a prerequisite.

Document what was actually verified. Archive descriptions, inspected source,
successful compilation, and runtime results are different kinds of evidence.
