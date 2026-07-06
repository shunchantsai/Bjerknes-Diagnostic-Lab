# Changelog — Bjerknes-Diagnostic-Lab

All notable changes to the Bjerknes-Diagnostic-Lab repository are documented here.

## [2026-07-05] — NB2 Phase A (Session 1, CONTENT): full §1–§10 read, §6 re-scope + accuracy fixes

**Session type:** Content (Phase A deep-read → Phase 3.5 verify → Phase 4 edits → Phase 5 exam).
Structural findings deferred to a Session 2 (STRUCTURAL).

### Changed (content)
- **§6 "Why this framing is worth foregrounding" — rewritten (P1-a).** Removed an inaccurate claim
  (the operational standard ENSO index is the SST-based Niño 3.4 / ONI, *not* a single pressure-based
  index; SOI is secondary) and an internal contradiction with cell 0 (the node-vs-gradient question is
  NB1's). Re-scoped to NB2's actual question: does the jet respond to SST *magnitude* or *structure*?
- **§4 pressure equation — `c_p` → `SCALE_P` (P1-d).** The scaling constant was mislabeled as the
  thermodynamic specific heat $c_p$; it is the §2 tuning knob (0.6 hPa/°C·km). Renamed, defined, and
  now matches the code symbol.
- **§2 tuning-knob caveat de-duplicated (P1-b);** cell 5 owns the full caveat, cell 3 points forward.
- **Z_MID altitude mislabel corrected (P1-c):** 7 km is mid-troposphere (~500 hPa), not the
  boundary-layer / free-troposphere transition.
- **Axis precision (P1-e):** Scenario B's missing gradient named *meridional (north–south)* where
  previously "horizontal," removing a zonal-vs-meridional ambiguity.
- **Scope note de-staled (P1-f):** the ∂p/∂φ vector overlay was flagged as an "open" future refinement,
  but the A-vs-B force panel (§7) already delivers it; note rewritten to say so.
- **§5 "±5–15 hPa" corrected (P1-g):** real ENSO SLP anomalies are only a few hPa — the SCALE_P row now
  states the magnitudes are illustrative, not calibrated (former BLOCKED item).
- **§9 wording (P1-h):** split-D / wavy-jet refinements reframed from "deferred" to "left to the prose on
  principle," matching the note on scope (the axisymmetric model doesn't generate them).
- **§10 parallelism (P1-i):** Scenario D's one-liner now names it "sign-flipped," like C.
- **§10 closing (P1-j):** added a one-line takeaway returning to the thesis + the NB1↔NB2 angular-momentum hand-off.
- **§10 taxonomy note (P1-k):** flags the A/B/C/D set as a constructed diagnostic; B is an idealized control, not an observed state.

### Verified (Phase 3.5)
- Standard-ENSO-index claim checked against NOAA / IRI sources (→ P1-a).
- Held & Hou (1980) citation confirmed genuine.
- Test suite unchanged: 23/23 green (no module change).
- **Cell 14 Bjerknes quote verified verbatim** against the 1969 paper (MWR 97(3), §4 "The Walker Circulation").
- **"±5–15 hPa" refuted** (Bjerknes's own ±1.5 mb / ~5–6 mb; the SOI is a normalized index) → fixed in P1-g.
- **[G3] 4-scenario taxonomy** confirmed a *construct* (not Bjerknes's); observed ENSO diversity (EP/CP flavors) supports the pattern-over-magnitude framing; B is an idealized control.

### Deferred
- **Structural (Session 2):** relocate the anomaly / meridional-axis explanation adjacent to the
  Scenario-B figure and the A-vs-B force panel; consolidate the "structure beats magnitude" restatements
  (cells 0, 7, 14) to ≤2; reorder cell 14's off-equator subtitle out of §5. *Content is present; the
  problem is placement.*
- **Both former BLOCKED items cleared** in Phase 3.5 (Bjerknes quote verified verbatim; ±5–15 hPa fixed → P1-g).

---

## [2026-07-04] — Repo engineering (Steps 1–3): reproducibility, output hygiene, NB2 modularization

**Session type:** Engineering (repo-level: environment, git hygiene, module extraction, tests).
No notebook *science* changed — NB2's physics is unchanged (keystone check: peak |−∂p/∂φ| A = 0.327, B = 0.000 hPa/°lat).

### Added
- **`requirements.txt`** — pinned runtime dependencies (`numpy==2.5.0`, `matplotlib==3.11.0`), verified to execute both notebooks end-to-end in a fresh Python 3.12 virtual environment (`e3ebf03`).
- **`.gitattributes` + nbstripout filter** — notebook outputs stripped from git while kept in the working copy; ~95% drop in committed notebook size, readable diffs (`698c288`).
- **README "Figures" section** — embeds the four-scenario meridional atlas + Bjerknes Fig 8, restoring on-page figures after output-stripping (`1621c20`).
- **`test_bjerknes_physics.py`** — 13 physics-claim tests for the zonal module (regime taxonomy, node/gradient coincidence, structure-beats-magnitude width discrimination, oceanic memory); numpy-only, pytest or standalone (`db0c6e2`).
- **`teleconnection_physics.py`** — meridional Hadley/jet field generators (`gen_sst`, `gen_pressure`, `gen_hadley`, `gen_zonal_wind`, `gen_momentum_flux`) extracted from NB2 as pure functions (output shape from the passed grid; no hidden globals) (`4dc628b`).
- **`test_teleconnection_physics.py`** — 10 physics-claim tests for the meridional module, including the Scenario-B keystone (uniform SST → zero meridional pressure gradient) as an executable assertion (`4dc628b`).

### Changed
- **NB2 imports its generators** from `teleconnection_physics.py` instead of defining them inline, and reuses `gen_pressure` in the A-vs-B force panel (removing the duplicated `_sst_profile` / `_p_anom` helpers). Runs top-to-bottom unchanged (`4dc628b`).
- **README** — corrected the dependency list (pandas was never imported); rewrote Getting Started as a pinned-venv setup; updated Contents for the new module and both test suites.
- **CHANGELOG scope** — this log now tracks the whole repository, not just NB1.

### Verified
- Both notebooks execute clean (`Restart & Run All`) in a fresh environment from `requirements.txt`.
- Full test suite: **23 passed** (13 zonal + 10 meridional); Scenario-B keystone green.

---

## [2026-07-03] — NB1 Phase A: Bjerknes verification + content edits

**Session type:** Content (Phase A deep-read → Phase 3.5 verification → Phase 4 edits).
Structural edits identified in the same pass are listed separately below.

### Changed (content)
- **§4 X0_COLD provenance — now text-verified against Bjerknes (1969).** OCR of the
  scanned source confirms the four equatorial zero-isallobar crossings stated in Bjerknes's
  prose (175°E, 170°W, 168°E, 178°E; mean 177.75°E ≈ 178°E). Removed the "not yet verified /
  digitize the figures" framing; noted that the node–gradient coincidence is Bjerknes's own
  stated observation.
- **§Trap 3 (145°W) — precision + attribution.** Now "westerly surface winds occasionally
  observed at 145°W on the Equator in November 1957 (Bjerknes 1969, citing Austin 1960)."
- **§1 coincidence claim — softened to hypothesis.** The "empirically rare" statement now
  reads as the notebook's own working conjecture, not an established observational result.

### Added
- **Sadler (1959) reference** (Proc. 9th Pacific Science Congress, Vol. 13, 6–11) to the
  References cell — closes a source cited in §7 but previously missing from the list.

### Changed (structural)
- Intro: signpost distinguishing the two dualities (node/gradient vs thermal/rotational);
  removed a dangling "Sadler's observation" attribution (full cited version kept in §7);
  CAT paragraph now back-references the downstream chain instead of restating it.

---

## [2026-07-03] — NB1 Structural Content Overhaul + Phase 5 Exam

**Session Scope:** Deep structural and content revision of NB1 following multi-session assessment (Phases 0–7 of deep-read workflow). Focus: heading renumbering, section reordering, Discussion modernization, Conclusion addition, reference verification.

**Session TYPE:** Mixed (structural + content) — *last mixed session before adopting strict one-thing-per-session rule.*

### Major Changes

#### 1. Notebook Title & Introduction (Cell [0]) — REWRITTEN
**What changed:**
- **Old title:** "# Bjerknes Diagnostic Lab: Probing ENSO Dynamics"
- **New title:** "# The Walker Circulation as a Zonal Thermal–Rotational Cell" + tagline "*Notebook 1 — the zonal (∂p/∂x) axis*"
- **Old intro:** 2 paragraphs, abstract framing
- **New intro:** Extended (~8 paragraphs) with explicit "Four traps" subsections (Trap 1–4), each with Question → Trap → Fix structure

**Why:** The original intro was vague about the notebook's scope. The new intro explicitly draws the axis boundary (zonal vs. meridional, ∂p/∂x vs ∂p/∂φ) and introduces NB2 by name and link. It also frames Trap 4 as "the notebook's own question" and clarifies that Traps 1–3 are settled by physics, but Trap 4 motivates the entire decomposition in §§4–7.

**Consequence:** The intro is now ~3× longer, but the pedagogical structure is clear: readers know what axis they're on, why the four traps frame the problem, and where the answer (regimes A–D) will come from.

#### 2. Heading Renumbering & Section Reordering (Cells [4]–[14])

**Old structure (broken):**
```
[4]  ## 3. The X0_COLD Anchor...
[7]  ## 3. The Idealised Surface Pressure Model...  [duplicate 3!]
[8]  ## 3.5 The Vertical Dimension...
[9]  ## (no heading, just code)
[11] ### Comparing the model...
[12] ## 3.6 Ascent/Descent...
[13] ## 3.7 Rotational Correction...
[14] ## (no heading, loose code)
[16] ## 4. The Taxonomy...  [skipped to 4]
```

**New structure (clean):**
```
[4]  ## 3. The X0_COLD Anchor...
[7]  ## 4. Setup: The Idealised Surface Pressure Model...
[8]  ## 5. The Vertical Dimension...
[9]  ## 5.1 Vertical Structure...  [fixed: was "# 5.1", now proper "##"]
[11] ### Comparing the model...
[12] ## 6. Ascent/Descent Widths...
[13] ## 7. Rotational Correction (AAM)...
[14] ### Decomposition...  [now proper subsection]
[16] ## 8. The Taxonomy of Regimes...
[17] ## 9. The Four Regimes, Made Concrete...
...
[47] ## 13. Discussion...
[48] ## 14. Quantitative Implications...
[49] ## 15. Conclusion  [NEW]
[50] ## References...
[51] ## Notebook Information...
```

**Critical logical fix:** §3 (X0_COLD anchor) and §4 (Setup: idealized model) were originally ordered as "anchor-then-model," which put the cart before the horse. Readers met "X0_COLD = 178°E (a parameter of the tanh model)" before seeing the tanh model itself. Reordering to "model-then-anchor" is pedagogically correct: introduce the model, *then* discuss the provenance and uncertainty of one of its parameters.

**Consequence:** Every section from §4 onward is now incremented by 1 (old §4→new §5, old §5→new §6, etc.), but the logical flow is fixed.

#### 3. New Section §13.2: "Where This Sits in Modern ENSO Research" (Cell [48]) — ADDED

**Content:** ~800 words connecting NB1's node-vs-gradient decomposition to three modern ENSO threads:

1. **ENSO diversity (EP/CP flavors):** Cold-tongue vs. warm-pool El Niño types → zonal displacement of the whole pattern → Scenarios C/D in idealized language.
2. **Contested Walker trend:** Vecchi (2006) century-scale weakening + L'Heureux (2013) recent multidecadal strengthening = unresolved tension (not a "correction"), demonstrating why the diagnostic choice *is* the science.
3. **Ocean memory:** Recharge-discharge paradigm (Jin 1997) quantifies what §12's leaky-integrator captures qualitatively; Ren & Jin (2013) extends to both ENSO types.

**Citations added (all verified):**
- Kao & Yu (2009), *J. Climate* 22(3)
- Kug, Jin & An (2009), *J. Climate* 22(6)
- Vecchi et al. (2006), *Nature* 441(7089)
- L'Heureux, Lee & Lyon (2013), *Nature Climate Change* 3(6)
- Ren & Jin (2013), *J. Climate* 26(17)
- Capotondi et al. (2015), *BAMS* 96(6)
- Timmermann et al. (2018), *Nature* 559(7715)

**Boundary discipline:** Every reference is framed on the **zonal/diagnostic** angle only. Capotondi and Timmermann both touch teleconnections (meridional/NB2 territory); framing keeps them strictly on diversity/complexity/zonal-regime structure.

#### 4. New Section §15: "Conclusion" (Cell [49]) — ADDED

**Content:** ~300 words that:
1. Close the Bjerknes arc (open on his 1969 cold-January observation, close on "that coincidence was Scenario A only").
2. Name the three-face principle ("a scalar is not a state").
3. Draw the NB1/NB2 boundary explicitly via angular-momentum flux: "the equatorial cell cannot close its own AAM budget; the leak to the meridional (poleward) direction *is* the hand-off to NB2."
4. Formalize the axis boundary: NB1 owns ∂p/∂x, NB2 owns ∂p/∂φ.

**Why it's needed:** §13 (Discussion) talks about the error's nature; §14 (Quantitative Implications) talks about downstream impacts and how-to corrective steps; the payoff cell (§12.1) talks about three faces. But nothing *closed the loop*: returned to Bjerknes's opening observation and stated its frame (Scenario A = special case). The Conclusion does that, plus it formalizes the NB1/NB2 seam for readers of both notebooks.

**Consequence:** This prevents the notebook from just trailing off ("§14 ends on a hypothetical, then References").

#### 5. Reference Section Overhaul (Cell [50]) — TRIMMED & VERIFIED

**Removed (13 references):**
- **Sriver & Huber (2007)** — discovered fabricated: wrong title, journal ("vol. 0"). Searched and found actual 2007 paper (different title, *Nature*). Decided to cut entirely rather than edit from memory — safer epistemic stance.
- **ERA5 (Hersbach 2020), MERRA-2 (Gelaro 2017)** — inconsistent with notebook's stated use of synthetic data + Bjerknes's digitized maps. Removed; "reanalysis" language softened elsewhere (see below).
- **Cai et al. (2018), Timmermann et al. (1999), Hurley & Garner (2013), Adames & Wallace (2014), Barnes & Hartmann (2010), Gray (1979), Camargo & Sobel (2005), Katz et al. (2002), Vitart & Robertson (2018), Bretherton & Caldwell (2020), Peixoto & Oort (1992)** — decorative (not cited in text); no confidence in accuracy from memory; cut rather than risk repeating the Sriver error.

**Added (7 references, all verified against primary sources):**
- See §13.2 citations above (Kao & Yu, Kug et al., Vecchi, L'Heureux, Ren & Jin, Capotondi, Timmermann).

**Verification process (Phase 3.5):**
- Every citation searched for title, authors, journal, volume, year, DOI.
- Titles and journals double-checked against abstracts / journal websites.
- DOIs tested as links.
- One citation (Chung et al. 2019, "Reconciling opposing Walker circulation trends") surfaced during Vecchi/L'Heureux search but not yet fully verified — flagged in notes for future sessions.

**Consequence:** NB1's reference list is now shorter (~6 primary + 7 modern ENSO context = 13 total) but *all load-bearing*. Each reference has a one-line note saying where it's used in the text.

#### 6. Softened Empirical Claims (Cells [12], [46])

**Cell [12] (§3.7 "Without Zonal Walls..."):**
- **Old:** "…robust in modern reanalysis (e.g., ERA5)."
- **New:** "…robust, well-documented feature in later observational studies."
- **Why:** NB1 uses synthetic data and Bjerknes's 1969 digitized maps, not reanalysis. Claiming "robust in ERA5" overstates the notebook's evidentiary base. Softening removes the overclaim while keeping the substantive point (it's a real observed feature).

**Cell [46] (§13 Discussion):**
- **Old:** § could have read "modern reanalysis shows…"
- **New:** Explicit disclaimer in the opening: "This notebook uses synthetic data and Bjerknes's (1969) digitized maps, not reanalysis. The quantitative cascade in §10 uses order-of-magnitude sensitivities representative of the literature; it is illustrative, not calibrated."
- **Why:** Prevents overstatement of authority; sets epistemic frame for CAT users reading the risk cascade.

#### 7. Trimmed Duplicate Concluding Passages

**§13.2 closing sentence (removed):**
- **Old ending:** "This notebook's contribution is narrower and older-fashioned: it shows, in Bjerknes's own diagnostic and with a minimal model, *why* discarding that structure produces patterned, directional error rather than harmless noise."
- **Removed:** Because the new §15 Conclusion now owns the "what does this notebook contribute" statement.
- **Why:** De-duplication — avoid the same idea (contribution/epistemic frame) stated in three places (payoff cell + §13.2 + §15). The Conclusion should be the sole place for that statement, making it the tightest.

**Consequence:** §13.2 now ends on Timmermann et al., cleanly handing off to §14 without the meta-commentary.

### Quality Checks (Post-Editing)

#### Execution
- ✅ Restart & Run All: clean, no errors
- ✅ Verified cell count: 51 cells (38 markdown, 13 code)
- ✅ No new duplicate headings
- ✅ Section numbers §1–15 + References + Notebook Info (all sequential)

#### Phase 3.5 Verification
- ✅ All 7 citations verified against primary sources with DOIs
- ✅ Fabricated reference (Sriver) caught and removed
- ✅ Overclaimed empirical statements (ERA5, reanalysis) softened
- ✅ Non-computed numbers (0.45, 12°, 1.6 offset, etc.) traced to source cells or marked as illustrative

#### Phase 5–6 Exam & Fault Map
- ✅ Q1 (EP/CP ↔ Scenario C/D): landed 6/10; assembly gap at "CP=west" identified for re-drill
- ✅ Q2 (Walker timescale trap): epistemics full credit (refused to answer on unread papers); content supplied for re-test
- ✅ Q3 (AAM boundary): landed 2/10 on answer; role-vs-parts framing needs re-exposure
- ✅ Fault map generated; gaps flagged for next session's re-tests

### Known Issues Logged (Not Fixed — One-Thing-Per-Session Rule)

These are deferred to future *content* sessions. Logging here prevents loss:

1. **§13.2 Walker-trend sentence clarity:** The "Vecchi + L'Heureux = unresolved, not corrected" point may not land clearly enough on first read. Candidate for re-wording in a dedicated content session.
2. **EP/CP ↔ C/D mapping:** Assembly gap (one step short: "CP=west=Scenario D") — ready for re-drill with exam.
3. **AAM role (vs. parts):** Conceptual grasp present; framing as role/boundary-function needs work. Re-test in next session's Phase 5 exam.

### Workflow Updates Applied

- **Phase 3.5 (Verify) added:** Every citation, empirical claim, and non-computed number now verified against primary sources before entering the notebook.
- **Stricter one-thing-per-session rule adopted:** Future sessions will enforce separation of structural and content edits. This session violated the rule (mixed both); it's explicitly the last time.
- **Phase 5–6 Exam + Fault Map:** Exam questions calibrated to session scope, answered, graded, and fault map generated — ready for re-tests next session.

---

## Session Statistics

| Metric | Value |
|--------|-------|
| Cells changed | ~12 (structural) + 4 (content added) |
| Sections reordered | 2 (§3 ↔ §4) |
| Section headings corrected | 5 (duplicate 3s, 3.5→5.1, etc.) |
| New content cells | 2 (§13.2, §15) |
| References verified | 7 |
| References removed (unverified) | 13 |
| Net reference count | 13 (old: ~20) |
| Exam questions | 3 (calibrated, graded) |
| Fault map entries | 7 (7/7 concepts tracked) |

---

## Execution Checklist (Phase 4–8)

- [x] Cell renumbering complete; no duplicates
- [x] §3 ↔ §4 reordered; logical flow fixed
- [x] §13.2 added (modern ENSO context, 7 verified citations)
- [x] §15 added (Conclusion, closes arc, draws NB1/NB2 boundary)
- [x] References trimmed (13 removed, 7 verified added)
- [x] Empirical claims softened (ERA5→observational, etc.)
- [x] Duplicate concluding passages de-duped
- [x] Restart & Run All: clean, no errors
- [x] Phase 5 exam completed; fault map generated
- [x] Revision note saved to `revision_notes/2026-07-03_nb1_exam_session.md`

---

## Next Session Protocol

**Session Type:** Will be declared explicitly in Phase 0 (STRUCTURAL OR CONTENT, not both).

**Gaps to re-test (if in scope):**
- EP/CP ↔ Scenario C/D assembly (Q1 re-drill)
- Walker timescale lesson (Q2 re-test from cold)
- AAM role framing (Q3 re-exposure)

**Known issues to address (when content session is scoped):**
- §13.2 Walker-trend sentence clarity

---

*End of changelog entry — 2026-07-03*