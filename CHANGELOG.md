# Changelog — Bjerknes-Diagnostic-Lab

All notable changes to the Bjerknes-Diagnostic-Lab repository are documented here.

## [2026-07-10] — NB3 promoted to deliverable; IRI data access resolved; two gates discovered

**Session type:** Engineering/prep (Task B3 pre-staging — tracker items D.2 + D.3).
Article-side edits (sections A, C of the tracker) logged in the tracker itself.

### Added
- - `revision_notes/task_B3_tracker.md` — working tracker for the 2026–27 probabilistic
  outlook task (sections 0/A–F/Q: article edits, footnote blockers, NB3 prep, run-day
  plan, standing decisions, queued items).
- Section-G code cells (B3 config, download/inspect, box-stats function) pasted into
  the NB3 notebook (tracker item D.3).
- `data/` workflow for Task B3: verified IRIDL download URL (NMME Precipitation_ELR
  `prob`, subset X 92–155 / Y −20–25, F-sliced), harvested and confirmed against the
  dataset page via Expert Mode.
- Tracker sections: "Data access — resolved" and "Risks & run-day checks (15 Jul)"
  in `revision_notes/task_B3_tracker.md`.

### Changed
- Added`03_SEAsia_Drought_Data_Processing.ipynb` — NB3 is the deliverable, not a template. 
  NB3, Section 2 data processing (drafted 9–10 Jul under a template name; renamed to the deliverable 
  convention before first commit).
- B3 config consolidated to a single cell: verified DATASET_URL; SEASONS re-scoped to
  ASO/SON/OND/NDJ 2026–27 (L axis caps at 4 months — DJF/JFM unreachable from the
  July issuance; dropped to preserve predictive timing); subset-window comment added.
- Download cell rewritten: browser-download workflow + magic-byte validation
  (programmatic download returns the dlauth login page as HTML).
- Task 2B code cell relocated out of the B3 block; duplicate Task 2A cell deleted
  (Steps 4–6 duplicated Steps 3–5 of the consolidated cell); 2A steps renumbered 1–9.

### Discovered (dry run — the reason dry runs exist)
- IRIDL downloads require an authenticated session (dlauth); urllib/curl receive HTML.
- IRI forecast data sits behind a license-approval gate
  (iri.columbia.edu/terms/forecast/1); access requested 10 Jul,
  ref f8725d9d51b4a11d4db44451b739208a30bd7a76, worst-case approval 17 Jul.
  Contingency recorded: run slips rather than substituting an unverified source.
- Data Library shutdown notice (CCSR migration) logged as run-day risk.

## [2026-07-07] — NB2 Phase A (Session 3, CONTENT): trim thesis repetition, anomaly reminder

**Session type:** Content (small, scoped from Session 2's deferred list). **Closes NB2 Phase A.**

### Changed (content)
- **Thesis de-duplicated (P3-a, P3-b):** "gradient beats magnitude" was stated ~6×; removed the two intro pre-announcements (cell 1's closing line; the slogan in cell 0's Scenario-B blockquote), so the claim is now *earned* at Scenario B (§7) and *landed* at the synthesis (§10) — two homes, not six. The intro poses the puzzle without spoiling it.
- **Anomaly-vs-total reminder at Scenario B (P3-c):** added a point-of-use line — these are anomaly fields; B removes only the *anomalous* meridional gradient, so what collapses is the ENSO-driven *change*, not the atmosphere's background Hadley cell. (Addresses the confusion the Phase-5 exam surfaced.)

### Not done (by design)
- Numbering the two unnumbered interludes ("Why this framing" preamble, "A note on scope" aside): left as intentional interludes — structural and unnecessary here.

### Verified
- Markdown-only edits; Restart & Run All clean; 23/23 tests green (no module/code change).

**NB2 Phase A (Deep Read & Comprehension) complete** — Sessions 1 (content) · 2 (structural) · 3 (content).

---

## [2026-07-06] — NB2 Phase A (Session 2, STRUCTURAL): caveats moved after their figures

**Session type:** Structural (whole-cell moves only — no prose changed; verified by source diff).

### Changed (structural)
- Moved **"Why this framing is worth foregrounding"** to directly after the title (was an unnumbered §2/§3 interlude), co-locating the motivation with the intro.
- Moved the **"off-equator ascent"** and **"jet-pinned"** caveats out of §5 (they preceded any figure) to just after Scenario A's figure — each caveat now follows the figure it explains.

### Verified
- Pure reorder: cell count unchanged (27), no cell source altered; Restart & Run All clean; 23/23 tests green (no module change).

### Deferred (Session 3, CONTENT)
- Trim the "gradient > magnitude" restatements to ≤2; add an anomaly-vs-total line at Scenario B; number the two remaining unnumbered sections.

---

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
- **`requirements.txt`** — pinned runtime dependencies (`numpy==2.5.0`, `matplotlib==3.11.0`), verified to execute both notebooks end-to-end in a fresh Python 3.12 virtual environment.
- **`.gitattributes` + nbstripout filter** — notebook outputs stripped from git while kept in the working copy; ~95% drop in committed notebook size, readable diffs.
- **README "Figures" section** — embeds the four-scenario meridional atlas + Bjerknes Fig 8, restoring on-page figures after output-stripping.
- **`test_bjerknes_physics.py`** — 13 physics-claim tests for the zonal module (regime taxonomy, node/gradient coincidence, structure-beats-magnitude width discrimination, oceanic memory); numpy-only, pytest or standalone.
- **`teleconnection_physics.py`** — meridional Hadley/jet field generators (`gen_sst`, `gen_pressure`, `gen_hadley`, `gen_zonal_wind`, `gen_momentum_flux`) extracted from NB2 as pure functions (output shape from the passed grid; no hidden globals).
- **`test_teleconnection_physics.py`** — 10 physics-claim tests for the meridional module, including the Scenario-B keystone (uniform SST → zero meridional pressure gradient) as an executable assertion.

### Changed
- **NB2 imports its generators** from `teleconnection_physics.py` instead of defining them inline, and reuses `gen_pressure` in the A-vs-B force panel (removing the duplicated `_sst_profile` / `_p_anom` helpers). Runs top-to-bottom unchanged.
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

## [2026-07-03] — NB1 Structural + Content Overhaul, Phase 5 exam

**Session type:** Mixed (structural + content) — *last mixed session before adopting
the strict one-type-per-session rule.* Full session report:
`revision_notes/2026-07-03_nb1_exam_session.md`.

### Changed (structural)
- Title/intro rewritten: new title "The Walker Circulation as a Zonal Thermal–Rotational
  Cell", explicit zonal/meridional axis boundary, "Four traps" framing.
- Section numbering repaired (duplicate §3s, "3.5"→5.1) and §3↔§4 reordered
  (model-then-anchor); all sections now sequential §1–15 + References + Info.

### Added (content)
- §13.2 "Where This Sits in Modern ENSO Research" (~800 words): EP/CP diversity,
  contested Walker trend (Vecchi 2006 vs L'Heureux 2013 — unresolved, not corrected),
  recharge-discharge ocean memory. 7 citations, all Phase-3.5 verified with DOIs.
- §15 "Conclusion": closes the Bjerknes arc, names the three-face principle, formalizes
  the NB1/NB2 boundary via the AAM hand-off.

### Removed / corrected
- References trimmed 20→13: 1 fabricated citation caught and cut (Sriver & Huber 2007,
  wrong title/journal), 12 decorative/unverifiable citations removed rather than edited
  from memory.
- Overclaimed empirical statements softened (ERA5/"reanalysis" → "observational studies";
  §13 now states the synthetic-data + digitized-maps evidentiary base explicitly).
- Duplicate "contribution" passages de-duped; §15 is now the sole home.

### Verified
- Restart & Run All clean; 51 cells, headings sequential.
- Phase 5 exam + fault map: Q1 6/10 (EP/CP→C/D assembly gap), Q2 epistemics full credit
  (refused unread papers), Q3 2/10 (AAM role-vs-parts). Re-test items logged in the
  revision note.