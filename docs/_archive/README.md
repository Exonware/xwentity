# Archive (xwentity)

**Purpose:** Staging for deprecated or legacy docs before you delete or merge them elsewhere. Not long-term storage.

---

## Process

1. **Move** obsolete content here only when you are about to retire it.
2. **Review** each file: keep anything worth keeping (requirements, architecture, decisions, evidence).
3. **Extract** into the right place:
   - Requirements / vision / milestones → REF_22_PROJECT, REF_12_IDEA, or `docs/logs/project/`
   - Architecture / layout → REF_13_ARCH
   - Reviews / compliance → `docs/logs/reviews/` (REVIEW_*.md)
   - Change history / migration → `docs/changes/` or `docs/logs/SUMMARY_CHANGE.md`
   - Plans → `docs/logs/plans/` or SUMMARY_PLAN
   - Test or bench evidence → `docs/logs/tests/`, `docs/logs/benchmarks/`
4. **Delete** from `_archive` after value is captured. Do not leave substantive content here indefinitely.

When empty, this folder should hold only `.gitkeep` and this README.

---

Disposition review: [logs/reviews/REVIEW_20260208_ARCHIVE_DISPOSITION.md](../logs/reviews/REVIEW_20260208_ARCHIVE_DISPOSITION.md).
