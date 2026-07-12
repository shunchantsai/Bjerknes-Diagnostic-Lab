# Literature Course — Session 1: Ropelewski & Halpert 1987

**Session Anchor:**
This session is about: Comprehending RH87's two-stage method (composite/harmonic → consistency count) and Table 2 / Fig. 5 / Fig. 21, for the article's ING/NAU/southern-US claims.
**Session TYPE:** CONTENT (reading + comprehension; no notebook or article editing)
**Started:** 2026-07-12
**File renamed** from `2026-07-12_phase_a_nb4_revision_notes.md` — this arc is literature-course Session 1 on the RH87 *paper*, not NB4 Phase A. NB4 does not exist yet; it is a proposal (see Outputs Queue, item c).

## Sitting log
> One line per sitting. Filename date = arc start; this log + `git log` are the timeline. Filename never changes.

- **2026-07-12** — Template adapted from NB1 skeleton; [C]/[G] pre-seeded; Outputs Queue drafted. No reading done. *(Closing reconcile missed — caught up 07-13.)*
- **2026-07-13** — Catch-up close: file renamed, queue items annotated with provenance/destination/status, stale NB1 block removed. No reading done yet.
- **YYYY-MM-DD** — …

**Phase 1 status: NOT STARTED** — next action: §1–2 method pass.

---

## Phase 1: Deep Read — Questions Inventory

Read RH87 non-linearly: §1–2 once for method; then Table 2, Fig. 21, and regional prose §4a/§4b/§4d/§4f. Mark questions as you go.

### [C] Clarifying Questions
(Questions where I don't understand a mechanism)

1. The (0)/(+) notation: what do year (0) and year (+) mean, and which calendar months does ING's Jun(0)–Nov(0) "season" span for a 2026 episode?

2. How are the 20/25 (ING) and 22/26 (NAU) hit rates derived from Table 2's episode columns (total, wet, dry)? What does the minority column (e.g. wet count in a dry-sense region) represent?

3.

### [G] Generative Questions
(Questions where the passage implies something I haven't thought through)

1. Why are harmonic vectors alone "not sufficient," and what does the per-episode consistency count add that the composite cannot?

2. The abstract counts **four** Australia regions; Fig. 5 outlines **five** candidates (NAU, EAU, SAT, CAU, SWA). Which one failed, and at which stage — the coherence screen or the consistency count?

3.

### [S] Structural Questions
(Questions about where a claim belongs: article vs. NB4 spec; which evidence type it is — composite/harmonic screen vs. per-episode count; and citation provenance, e.g. RH87 vs. RH86)

1. Which Table 2 rows originate in Ropelewski & Halpert **1986** (MWR 114) rather than this paper? (Known case: Gulf of Mexico–N. Mexico. Check the source attribution for every row the article touches.)

2.

3.

---

## Phase 2–3: Claude Assessment & Answers

> Lit Session 1. Scope: full [C]/[G] inventory for RH87; [S] items route to tracker (article connections, NB4 spec inputs) rather than an edit queue.

### [C1] —

### [C2] —

### [C3] —

### [G1] —

### [G2] —

### [G3] —

---

## Outputs Queue — NOT YET APPLIED
> Cross-scope outputs of this session. Route each at a sitting close; act on nothing mid-session.
> Format per item: WHAT · WHERE FROM · ROUTES TO · STATUS.
> **Verification rule (Phase 3.5):** numbers below entered via the session brief and Claude's walkthrough. Neither is a source. Nothing marked PENDING VERIFICATION enters the tracker or article as fact until I have read the row/passage on the physical page myself. (Context: Claude's screen-reads of this scan failed twice on 07-12 — see item d.)

### Tracker items → `revision_notes/task_B3_tracker.md`
- **(a) NAU dry signal.** Northern Australia, Sep(0)–Mar(+), 22 of 26 episodes dry (RH87 Table 2, p. 1625). *From:* session brief 07-12. *Routes to:* tracker, as independent literature support for task **E.5** (testing the brief's northern-Australia claim against NB3's NDJ panel). **STATUS: PENDING VERIFICATION** — read the NAU row on p. 1625 myself (total / wet / dry values).
- **(b) RH86 provenance footnote rule.** The Gulf of Mexico–N. Mexico wet signal (Oct(0)–Mar(+), 18/22) appears in RH87 Table 2 but is sourced from **Ropelewski & Halpert 1986, Mon. Wea. Rev. 114** — a different paper. The article's southern-US flood footnote must cite 1986, not 1987. *From:* session brief 07-12. *Routes to:* tracker footnote rule. **STATUS: PENDING VERIFICATION** — confirm the row's source attribution on the page.
- **(c) NB4 proposal.** `04_RH87_Teleconnection_Atlas_Method.ipynb` — synthetic-first replication of the RH87 pipeline (rank → percentile → 24-month composite → harmonic fit → coherence → consistency count). Generator: 80–100 gamma-rainfall stations, ~25 planted episodes, four clusters (ING analog dry Jun(0)–Nov(0) with planted 20/25; NAU analog dry Sep(0)–Mar(+) with planted 22/26; noise-only; monster-episode pathology). Deliverables: Fig. 5-analog vector map, Fig. 3/4-analog pair, Table 2 analog (exact columns), pathology demonstration (passes amplitude screen, fails count). Companion module `atlas_statistics.py` + tests. GHCN-M real-data stretch: optional, post-article. *Routes to:* one-line tracker entry now; STRUCTURAL design session later (schedule Block B). **Hard rule: NB3 preempts NB4 the day IRI license `f8725d…` approves.** **STATUS: ripe** (no verification dependency).
- **(d) Lessons entry** → `git_and_data_ops_lessons.md` / fault map. Two Claude verification failures, 07-12: (i) Table 2 columns misdescribed and framed as image-confirmed — the crops actually showed Fig. 19 + prose; true columns (my read of the page): Region | "Season" | Coherence | No. of episodes: total, wet, dry. (ii) Coherence called "not a computed statistic" — p. 1608 defines it as the **ratio of mean vector magnitude to mean scalar magnitude** ("directional steadiness"). Lesson reinforced: secondary screen-reads are not verification; table pages get read from the page. **STATUS: ripe.**

### Article connection → article Sources Ledger (route in a future VERIFY session)
- **ING mechanism citation.** ING dry "season" Jun(0)–Nov(0) (20/25 episodes dry) = canonical citation for the SE Asia drought paragraph's mechanism claim; maps onto NB3's rescoped ASO/SON/OND panels. For a 2026 episode: Jun–Nov 2026. **STATUS: PENDING VERIFICATION** (same Table 2 read as item a).

### NB4 spec inputs → Block B design doc
- Table 2 exact columns: Region | "Season" | Coherence | No. of episodes: total, wet, dry — sense *derived* from counts, not hardcoded. *(Columns verified by my own read of the physical table, 07-12; row values still pending.)*
- Coherence definition: |mean vector| / mean |vector| over a region's harmonic vectors (p. 1608).
- Vector-clock convention (Fig. 5): 24-month clock — Jul(0) top, Jan(+1) right, Jul(−1) bottom, Jan(0) left — with concentric amplitude rings; solid vs. dashed region outlines = dry vs. wet.

---

## Phase 5–6: Exam & Fault Map

**Status: DEFERRED** — Phase 5 exam for this paper runs only after NB4's pipeline executes end-to-end (schedule Block C, item 16). Questions may be drafted now; sitting the exam before implementation is out of scope.

### Questions
- Q1 (conceptual):
- Q2 (trap):
- Q3 (structural):

### Self-assessment (closed-book result)
- Q1:
- Q2:
- Q3:

### Fault map
- Q1 —
- Q2 —
- Q3 —

### Re-exposure notes

### Re-check plan

---

## Per-sitting closing protocol (2 min)
1. Update the Sitting log line + Phase 1 status above (honest state; "read" never precedes reading).
2. Route only **ripe** queue items; PENDING VERIFICATION items stay here or enter the tracker flagged as pending.
3. `git add` this file (+ CHANGELOG line if written) → `git commit -m "lit s1 (RH87): <one-line actual state>"` → `git push`.
4. Reconcile: `git status` clean; tracker matches reality; CHANGELOG matches reality.
