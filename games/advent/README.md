# ADVENT — source intake

**Status:** unchanged source candidate, not a playable BetterCP/M Games release.

Edition: Gillogly / Berkeley 350-point Adventure C lineage in BSDGames.

## Source and license

Retain every per-file notice and the distribution COPYING. Most files use BSD three-clause terms; extern.h retains Christos Zoulas's four-clause notice, including its acknowledgment requirement. This snapshot is not exclusively BSD-3-Clause. It is separate from the unresolved Goetz A02 implementation.

Pinned repository: https://github.com/vattam/BSDGames/commit/56b8944332186891cd5c0094bd3991e3c5f5a799

[SOURCE.json](SOURCE.json) identifies every imported path, Git blob, byte count, and SHA-256. All imported bytes are unchanged. The top-level MIT license does not relicense upstream/.

## Findings

The complete adventure source directory, database glorkz, generator setup.c, and upstream build descriptions are retained. This is the classic 350-point lineage, not Open Adventure's 430-point edition. Full location/puzzle/scoring fidelity has not been play-tested here.

## Work before release

Unix C source, not a CP/M implementation. The 56375-byte text database is compiled into generated data.c upstream; a direct memory-resident build is unsuitable for a small TPA. Investigate external database records, compact structures, and replacing Unix save/signal/file services. A host build may establish behavior before porting. Source eliminates the need to reconstruct this edition from a binary.

No compilation, execution, memory measurement, or terminal qualification is claimed. Availability of source does not by itself select the final implementation or release order.
