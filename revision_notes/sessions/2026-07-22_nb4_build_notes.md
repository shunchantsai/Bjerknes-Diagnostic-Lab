# NB4 Build — `04_Ropelewski_Halpert_Atlas_Method.ipynb` (tracker Q.6)

**Arc:** synthetic-first replication of the RH87 pipeline, built to make the
**coherence ≠ hit rate** distinction executable rather than merely understood.
**Arc START:** 2026-07-22 (spec relocated here from the RH87 reading notes, where it
did not belong).
**Session TYPE:** BUILD.
**Timebox:** 2–4 sessions. **A wanted 5th session = STOP** and ship what runs.
**Preemption:** the NB3 production run preempts this the moment the IRI licence approves.

**Status:** NOT STARTED. `04_*.ipynb` exists locally, **title-only, intentionally untracked**
(commit-or-hold decided 22 Jul: HOLD until build session 1 produces content).

**Why this notebook exists:** the coherence/hit-rate collapse recurred twice (RH87 notes,
F.11 → now `lessons.md`). A concept that collapses twice will collapse a third time, because
the screening statistic and the verification statistic sit at the same level of abstraction
**until you build them.** Building them separates them permanently. The S1 Phase-5 exam is
gated on this notebook running end-to-end.

---

## Sitting log
- **2026-07-22** — Arc opened. Spec relocated from `sessions/2026-07-12_lit_session1_RH87_notes.md`
  (Outputs Queue → "NB4 spec inputs"), verbatim, no changes. No build work yet.

---

## Spec inputs — from RH87, verified against the page during Lit Session 1

### Pipeline facts the replication must honour
- **Table 2 columns:** Region | "Season" | Coherence | episodes total/wet/dry. **No source column.** Sense **derived**.
- **Two-way split at the 50th percentile**, exhaustive.
- **TWO transforms:** ranks (global screen) → gamma percentiles (regional analysis), **both per calendar month.**
- **Coherence** = |Σv| / Σ|v|, **summed over STATIONS**. **NO HARDCODED THRESHOLD.**
- **Minimum five stations per region** (§4a) → episode totals differ across regions. *Build this into the generator.*
- **Phase-inversion trap:** harmonics point to the positive (wet) side; dry regions read 180° opposite.
- **Season identification is SUBJECTIVE in the paper** (step ii). NB4 must automate it **and flag the deviation**, or replicate the subjectivity honestly. **Do not silently invent an objective rule the paper doesn't have.**
- **Vector clock** (Fig. 5): Jul(0) top, Jan(+1) right, Jul(−1) bottom, Jan(0) left; solid = dry, dashed = wet.
- **⭐ PRINT COHERENCE AND HIT RATE SIDE BY SIDE for every cluster, denominators labelled (n_stations vs. n_episodes).** *(the notebook's pedagogical core — see `lessons.md`, 22/07/26)*
- **⭐ PRINT `n_total, n_wet, n_dry`, don't just balance them.** *(RH87's own table balanced and was still wrong — see `lessons.md`, 22/07/26)*
- **⭐ Optional closing note:** RH87's summary table disagrees with its own prose and figure for SSA — **a real-world demonstration of why this notebook prints its intermediate counts.** *One line.*

#### ⭐ FOUR PLANTED FAILURE MODES — one per pipeline stage
1. **Zero-inflated arid** *([C9], MME/NAS)* → dies at **ranking**. Never reaches a harmonic.
2. **Noise** → passes ranking, **dies at coherence**. No phase agreement among stations.
3. **SWA-type bimodal** *(V.5, [G7])* → passes coherence, **dies at season identification**. No contiguous season; the index is never built.
4. **Monster-episode pathology** → passes ranking, coherence **and** season identification with a beautiful arrow — **dies at the consistency count.** *The payload.*

### Scope decision — [G3], digitising Fig. 21
> **Log it; decide at Block B; default to a SEPARATE deliverable.** Would roughly double NB4. **NB4's justification is that it fits inside the license dead window. A doubled NB4 does not.**
---

## Build order (Block C)
1. **Generator module** `atlas_statistics.py` + `test_atlas_statistics.py` — tests green before any notebook cell.
2. **Stage 1:** rank → percentile → 24-month composite.
3. **Stage 2:** first-harmonic fit → vector clock → coherence (over STATIONS).
4. **Stage 3:** season identification (honest about the paper's subjectivity).
5. **Stage 4:** regional seasonal index → per-episode two-way split → consistency count (over EPISODES).
6. **The payload:** run the four planted failure modes; show each dying at its own stage.
7. **Then:** S1 Phase-5 exam (closed-book, against the paper — questions are in the RH87 notes).

## Open questions carried in from RH87 (do not block the build)
- **V.12** — identify ING's panel in Fig. 4 *by its printed label*, then straightedge-count. Expect 25 marked, 20 below.
- **V.14** — §2 says the longest series span 25 episodes; NAU's row is 26. What accounts for the extra one?
