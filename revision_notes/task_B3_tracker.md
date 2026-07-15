# Task B3 Tracker — 2026–27 Probabilistic Outlook
**Repo location:** `revision_notes/task_B3_tracker.md`
**Created:** 2026-07-09 · **Updated:** 2026-07-14 · **Owner:** Shun-Chan
**Rule:** work top to bottom. One checkbox at a time. Nothing here needs to be held in your head.
**Rule:** every sitting ends with a two-minute reconcile pass — tick what's done, amend what changed, log the session.
---

## 0 · Sync protocol (fixes "we see different things")

- [ ] **0.1** Fresh PDF export attached for review sessions. *(working — keep doing it)*
- [x] **0.2** After today's C.2 edits: export fresh PDF and **replace the stale project-folder copy**
      (delete old `Github_5__El_Nino.pdf` in project knowledge, upload new).
- [x] **0.3** Repo is public: Claude can review pushed state directly via clone on request (scoped checks, not full-repo reads); uploads only needed for uncommitted WIP and article PDFs.

---

## A · Google Doc — CONTENT scope ✅ SECTION COMPLETE (9–10 Jul)

- [x] A.1 Wedge sentence revised (traditional +1.7 / relative +1.1 / 0.6 °C).
- [x] A.2 Follow-on "one-degree wedge" phrase fixed.
- [x] A.3 Replacement paragraph v2 pasted, footnotes converted.
- [x] A.4 Traditional table checked: 17JUN2026 Niño 3.4 = +1.7 ✓
- [x] A.5 Fig. 2 caption checked: "relative sea surface temperature anomalies" verbatim ✓
- [x] A.6 Provenance footnote (footnote 3) replaced with full version incl. Fig. 2 pointer.
- [x] A.7 Cleanup verified: v1 deleted, commentary removed, brief's numbers block deleted,
      fn 2 rebuilt, fn 11 dates fixed, Figure 2A caption added.

## B · Deferred but blocks publication

- [ ] **B.1** FOOTNOTE AUDIT — ESCALATED 14 Jul. Not a "re-verification sitting": an audit of four footnotes found FOUR DEFECTS. Assume nothing is verified until it is.
      - fn 1 (Abrams et al., "Recalibrating Climate Risk", Green Futures Solutions): source REAL, but concerns IAM damage functions / NGFS scenarios — NOT catastrophe models. CATEGORY SLIPPAGE. Sentence over-loaded: makes 3 claims (tropical SST rise / shifted extremes / CAT-model calibration) on one citation. SPLIT the sentence.
      - fn 4 (97–98%): number was READ OFF A PLOT. Phrasing traced to NOAA CRW text, not IRI.
        ⚠ PRODUCT TRAP: 97–98% is the CCSR/IRI **model-based plume** (mid-month), NOT the **CPC Official Probabilistic Forecast** (early-month, human consensus). Different products, different numbers. Numeric tables: cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/probabilities/ 
Cite the right product; take the number from a TABLE, never a figure. Attribution required: "ENSO Forecast Data © 2002–2026 by IRI, CC BY 4.0".
      - fn 6: FABRICATED TITLE on a real, unrelated URL (ECB Environmental Statement 2025 — a report on ECB carbon footprint). Worse than the placeholder it replaced: silently broken, looks finished. REPLACE with Sarhadi et al. 2018, Sci. Adv. 4, eaau3487, DOI 10.1126/sciadv.aau3487 (READ IT FIRST).
      - fn 7: FABRICATED TITLE AND DOI. Correct authors/journal/vol/pages/year — invented identifiers (LLM signature). Real: Gaupp et al., "Changing risks of simultaneous global breadbasket failure", Nat Clim Chang 10, 54–57 (2020), 10.1038/s41558-019-0600-z.
        ⚠ AND ON READING IT: Gaupp CONTRADICTS the sentence — dependence can raise OR LOWER aggregate risk, and MITIGATES it for wheat/maize/soybean; dependence structure shows no significant change. GAUPP IS DROPPED. Sentence rewritten around Singh et al. 2022 (Nat Clim Chang, 10.1038/s41558-021-01276-3 — the PUBLISHED version, not the preprint).
      - ⚠ SCOPE: 4/4 sampled footnotes were defective. AUDIT EVERY FOOTNOTE, not just these. Every DOI resolves. Every URL opens to the claimed title. Every title matches the page. Every number comes from a table. Every citation supports THAT sentence's claim.
      - fn 4 ACCESS DATE IS STALE: the article says "accessed June 17, 2026" on a page that updates monthly. Re-access and re-date.
- [ ] **B.2** Read Saji et al. 1999 before citing 1997–98 positive-IOD co-occurrence.
      [VERIFY] bracket stays in doc until done.
- [ ] **B.3** FIGURE 2A CONTRADICTS ITS OWN CITATION (Solander et al. 2020, HESS 24, 2303-2322)
      ✅ NUMBER VERIFIED 14 Jul against the actual Table 3: Cluster 2, OND, 1997-1998 = -0.07 ± 0.03. Cluster 2 = N/NE Amazon + maritime SE Asia. Attribution correct.
      ❌ INTERPRETATION CONTRADICTS THE SOURCE. NB3 cell 5 states maritime zones were "comparatively moist" while mainland SE Asia was dry. Solander concludes the OPPOSITE: the largest, most consistent soil-moisture reductions occurred over "the maritime regions of southeastern Asia, Indonesia and New Guinea" (up to 0.28). 
      CAUSE: Figure 2A plots RAW absolute soil moisture (cells 2-4), not an anomaly, so it renders CLIMATOLOGY (mainland is naturally drier than rainforest) and is being read as DROUGHT. Cell 5's prose must be struck.
      ⇒ ACTION: compute the TRUE anomaly vs a stated GLDAS climatology period, or relabel Figure 2A as an absolute-value map and delete every drought inference drawn from it.
      Option A (anomaly) is correct — it satisfies the notebook's own opening principle ("every number you cite should be one you've computed or verified yourself").
      ⇒ FOLDS IN Q.3: the GLDAS box clips at 5°S, excluding Java/Bali/Timor — exactly the maritime regions Solander names as driest. The re-pull to 10°S and the anomaly computation are ONE job.
      ⚠ GLDAS V2.0 MAY NOT REACH 2016. NB3 cell 1 asserts "1948-2015"; verify on the GES DISC product page. If V2.0 ends ~2014, Solander's 1979-2016 climatology CANNOT be rebuilt from V2.0 alone, and splicing V2.1 introduces a discontinuity at the join (which is why Solander bias-corrected). RESOLUTION: use whatever period V2.0 covers, STATE IT, and present the result as an INDEPENDENT estimate — not a replication.
      ⚠ BIAS CORRECTION: a raw-GLDAS anomaly is NOT the same quantity as Solander's -0.07. They report bias correction shifts values by ~±0.05 — on a -0.07 signal that is up to ±70%. Never claim the two numbers are directly comparable.
      ⚠ EARTHDATA re-activated 14 Jul (account appears to have lapsed). TEST the bearer-token flow on ONE file before queuing ~114 (38 yrs × OND months).
      ⚠ UNITS: NB3's /100 conversion (kg/m² → m³/m³ for a 10 cm layer) is arithmetically right, but Solander's Table 3 gives no units. Confirm volumetric in their methods.
      ⇒ DIFFERENT FAILURE CLASS from fn 1/4/6/7: the citation is correct and the FIGURE is wrong. A verified number can still sit under a false claim. Verifying the source is necessary and NOT sufficient — verify that the artifact computes what the prose says.

## C · CPC July discussion + perishable snapshots

- [x] **C.1** July 9 discussion posted and read. Weekly (relative) values: Niño 3.4 +1.2,
      Niño-4 +0.5, Niño-1+2 +2.7 — **exact match to rel_wksst 01JUL2026 row**; relative-index
      provenance finding replicated.
- [x] **C.2** Apply the three strength-update edits, then tick:
      1. Intro: "As of late June 2026" → "As of early July 2026".
      2. Intro strength sentence: 63% NDJ → **"75% probability that the NDJ seasonal average
         will reach or exceed +2.0°C ... rising to 81% for the October–December peak season."**
         Fn 5: access date → 10 July 2026.
      3. Paragraph v2 first sentence: "in its 9 July diagnostic discussion, assigns an **81%**
         probability that the **October–December** seasonal average will reach very strong El
         Niño thresholds — which would rank 2026–27 among the largest events since 1950".
         Fn 8: issued 9 July 2026, accessed 10 July 2026.
      NOT changed: fn 12 (Indonesia convection) stays cited to 11 June discussion — dated
      citation, still accurate. Wedge sentence stays on 17-June week pair (freshness pass later).
- [x] **C.3** ASMC outlook page + ASEANCOF-26 bulletin PDF saved locally.
- [x] **C.4** Swap footnotes 10 and 14 from the event webpage to the bulletin itself:
      > ASEAN Climate Outlook Forum, *Consensus Bulletin for June–July–August (JJA) 2026
      > Season*, Twenty-Sixth Session of the ASEAN Climate Outlook Forum (ASEANCOF-26),
      > 19–22 May 2026, online; ASEAN Specialised Meteorological Centre,
      > https://asmc.asean.org/events-twenty-sixth-session-of-the-asean-climate-outlook-forum-aseancof-26/
      > (accessed 10 July 2026; PDF archived locally).

## D · NB3 prep before 15 July

- [x] **D.1** Box bounds APPROVED: Maritime (95, −10, 150, 7.5) · Mainland (92, 8, 110, 25) ·
      N Australia (110, −20, 155, −10). Format (W, S, E, N). Deliberate deviation from Figure 2A
      domain [95–145°E, 5°S–20°N]: Maritime box extends to 10°S so Java/Bali/Timor are
      included (Figure 2A's GLDAS subset clips at 5°S and misses them).
- [x] **D.2** IRI maproom → "Access the dataset used to create this map" → paste URL into
      `DATASET_URL`. https://iridl.ldeo.columbia.edu/maproom/Global/Forecasts/.
      NMME_Seasonal_Forecasts/Precipitation_ELR.html
      (resolved via Expert Mode; see G)
- [x] **D.3** Section-G cells pasted into NB3. Remaining hygiene (do with D.2):
      - [x] B3 stays after 2A (decided 10 Jul: adjacency to Figure 2A context).
      - [x] Add comment to B3 config: `# NOTE: order (W, S, E, N) — different from set_extent's [W, 
         E, S, N]`.
      - [x] Four-panel figure cell: **use cartopy coastlines** (matches Figure 2A style; cartopy already imported/used in this notebook — prior "no cartopy" decision reversed).
            - cell written 10 Jul (session notes); insert after dry run confirms dim order; gated on license approval (H.8).

## E · 15 July or after — NB3 run (one session, one commit)

- [ ] E.0 DEAD-WINDOW: synthetic validation of NB3 Task 2F (notebook cells 15-20;
      "Cells 3-6" in old H.6 = Task-2F-local numbering — corrected).
      Run make_synthetic_elr.py -> data/data_SYNTHETIC.nc. SYNTHETIC=True in cell 15.
      Cells added 14 Jul: extraction (C-by-name, runtime dim-order discovery),
      GRID CHECK, stats loop, four-panel figure, sentence emitter.
      VALIDATES: C-by-name resolution, dim order, box coverage, tercile sum, NaN/mask
      decision (Section F), figure render, (W,S,E,N) -> [W,E,S,N] reorder.
      ⚠ EXIT before E.2: SYNTHETIC=False · delete data_SYNTHETIC.nc · .gitignore it ·
      commit the generator, never the output.
      LIMIT: structure taken from the IRIDL Description page, never verified against a
      real file. NECESSARY, NOT SUFFICIENT.
- [ ] E.1 Confirm dataset page (G, root URL) shows F axis extended to Jul 2026 (= run-day check H.4).
- [ ] E.2 Run top to bottom; read GRID CHECK and NaN CHECK PASS/FAIL lines.
- [ ] E.3 Four-panel figure renders (ASO/SON/OND/NDJ), cartopy coastlines,
      box outlines, dominant-tercile hatching.
- [ ] E.4 Paste computed sentence into Google Doc at [COMPUTED FIGURE SLOT] + footnote
      (IRI forecast, issued 15 July 2026, dataset URL, accessed run date).
- [ ] E.5 Test the brief's "northern Australia" claim against the NDJ 2026–27 panel (closest to the
      brief's original DJF target; see H.2)
- [ ] E.6 Commit (single scope: "NB3 Task B3: IRI tercile computation + figure"), CHANGELOG,
      tick tracker, replace project-folder PDF again if article text changed.

## F · Standing decisions (do not re-litigate)

- Four-panel seasons: ASO/SON/OND 2026 / NDJ 2026–27, single 15-Jul issuance.
- Land-masking: GLDAS validity mask if GRID CHECK passes; else all-cells-with-label.
- **Cartopy: YES** for the four-panel figure (reversed 10 Jul — already a notebook dependency,
  used by Figure 2A; visual consistency wins).
- ">50% below-normal across most of SE Asia" is never asserted; NB3 computation is the
  quantification of record. Corroborating context: ASEANCOF-26 consensus map legend assigns
  exactly 50% (20/30/50) to its Below-Normal category — even the regional consensus never
  exceeded 50%.
- Mainland SE Asia = "mix of below- to above-normal" (bulletin verbatim), not "no dominant tercile".
- CPC monthly discussions quote **relative** weekly indices (Fig. 2 caption, confirmed 11 Jun
  and replicated 9 Jul). IRI Quick Look quotes traditional. Never compare across without labeling.
- NB4 is dead-window work only: the NB3 production run preempts NB4 the moment the IRI licence approves (ref 6fbac555…, 14 Jul; f8725d… has no witness — see H.8)
- Dead-window priority: (1) NB3 synthetic validation [E.0], (2) footnote audit [B.1],
  (3) NB4 [Q.6]. NB4 is LAST, not first. All three preempted by NB3 production the moment
  the licence clears.
- CITATIONS (standing, adopted 14 Jul after a 4/4 defect rate): no footnote enters the
  article until (1) its DOI resolves, (2) its URL opens to the claimed title, (3) the title
  matches the page, (4) every number comes from a table, never read off a plot, and (5) the
  source supports THAT sentence's specific claim — not an adjacent one. Verifying the source
  is necessary and NOT sufficient: the artifact must also compute what the prose says it
  computes (see B.3, Figure 2A). Citation-verification protocol lives in
  Article_Writing_Workflow.md. Assume nothing is verified until it is.


## Q · Queued content & study items (not blocking Task B3)

- [ ] **Q.1** STUDY SESSION: full close-read of the 9 July ENSO Diagnostic Discussion, every
      figure — comprehend → note → test against article claims → decide framing implications.
      Schedule: after the 15 July NB3 run, before drafting the Southern US flood case (the
      winter-outlook figures are load-bearing there). Includes: check July convection language
      vs fn 12's June claim.
- [ ] **Q.2** CONTENT: incorporate ASEANCOF-26 **Annex C (ESCAP impact-based forecast)**
      exposure statistics into the rice/compound paragraphs — Indonesia ≈95.4% (50.8 M t) of
      rice production exposed to below-normal rainfall (90.2% of total production in moderate
      likelihood); hydropower exposure (97.2% of Indonesia's plants). This is the exposure
      layer between physical signal and CAT-modeling argument. Cite the bulletin, Annex C.
- [ ] **Q.3** ⚠ PROMOTED 14 Jul — NO LONGER OPTIONAL. Re-pull GLDAS to 10°S. This is now part of B.3: the box clips at 5°S, excluding Java/Bali/Timor — exactly the maritime regions Solander identifies as driest. The re-pull and the anomaly computation are ONE JOB.
- [ ] **Q.4** OPTIONAL: verify or compute the −1 to −3 mm/day SE Asia precipitation anomaly
      figure (from the brief) before ever using it; candidates: NCEP-NCAR composites in NB2,
      or literature read at source.
- [ ] **Q.5** Publication-day freshness pass: latest weekly indices for the wedge sentence
      (labeled traditional AND relative), latest discussion issuance, all access dates.
- [ ] **Q.6** PROPOSED BUILD: NB4 — `04_Ropelewski_Halpert_Atlas_Method.ipynb`, synthetic-first
      RH87 method replication (spec inputs + rationale: `revision_notes/2026-07-12_lit_session1_
      RH87_notes.md`, Outputs Queue item c). Skeleton file exists locally, UNCOMMITTED —
      intentional, awaiting design session. Tick when the Block B STRUCTURAL design session
      is held and NB4 gets its own notes file + CHANGELOG entry.

## G · Data access

- DATASET_URL (root): https://iridl.ldeo.columbia.edu/SOURCES/.IRI/.FD/.NMME_Seasonal_Forecast/.Precipitation_ELR/
- Download URL (dry run, Jun 2026 issuance): root + .prob/X/92/155/RANGE/Y/-20/25/RANGE/F/%28Jun%202026%29/VALUES/data.nc
  - On 15 Jul: change F clause to (Jul 2026). No other change.
  - Subset window (92, -20, 155, 25) = union of all four analysis boxes, NOT
    BOX_SEASIA_FULL — N_AUSTRALIA extends to 20S/155E.
- Variable: prob [X Y C | L F], percent. Tercile axis C is UNORDERED with ids
  (Below_Normal) (Normal) (Above_Normal) — select by name in code, never by position.
- Verified on dataset page 10 Jul 2026: F axis Feb 2017–Jun 2026 (113 pts),
  L axis 1.0–4.0 months, 1° global grid, page expires 14 Jul 2026.
- AUTH (discovered 10 Jul dry run): IRIDL downloads require a logged-in session
  (dlauth) — urllib/curl receive the login page as HTML. Workflow: download
  data.nc in a logged-in browser, move to data/. Notebook cell validates magic
  bytes and opens; it does not download.
- 11 Jul: Dry-run attempt surfaced that the rewritten download cell (designed in prior session) was never applied to the notebook — old urllib version ran, saved dlauth HTML as the .nc. Fixed; committed 11 Jul (evening commit, combined with 2F move). Lesson 1: designed edits are not done edits; verify the artifact matches the design record before running. Lesson 2 (caught same day): the tracker itself asserted "committed" before git log showed it — the reconcile pass must include git status; "done" means committed and pushed, not edited.
- 14 Jul: THE AUTH NOTE ABOVE IS INCOMPLETE. Login (dlauth) was necessary but NEVER
  SUFFICIENT; the LICENCE realm (iri.columbia.edu/terms/forecast/1) is the true gate.
  Confirmed by hitting the terms page while fully logged in (H.8).
  LESSON → lessons file: a diagnosis that explains the symptom is not necessarily the
  cause. "urllib got HTML" was fully explained by the login theory, so the login theory
  looked confirmed — and it was incomplete. The licence gate sat right behind it and was
  only seen when the download was tested END-TO-END rather than reasoned about.

## H · Risks & run-day checks (run day = LICENCE APPROVAL DAY, not 15 Jul — see H.9)

1. SCOPE CHANGE (decided 10 Jul): figure panels are ASO / SON / OND / NDJ from
   the single 15 Jul issuance. L axis caps at 4 months, so DJF 2026-27 and
   JFM 2027 are NOT reachable from the July issuance — they would require the
   September issuance and were dropped to preserve the article's predictive
   timing. SEASONS list in NB3 config updated accordingly.
2. N. AUSTRALIA CLAIM: brief's below-normal claim was queued against DJF, which
   we will not have. Test it against the NDJ panel instead; caption/article must
   say NDJ, not DJF.
3. IRIDL SHUTDOWN RISK: Data Library banner (10 Jul) says "will soon shut down —
   try new CCSR service 05/21/2026." If the download cell fails on 15 Jul, check
   the CCSR migration page for the new dataset path before debugging locally.
4. RUN-DAY CHECK 1: reload dataset page; confirm F axis now extends to Jul 2026.
   If it still ends Jun 2026, the issuance is not posted yet — wait, do not
   download.
5. RUN-DAY CHECK 2: in the downloaded file, print target_season for all L and
   confirm ASO/SON/OND/NDJ before running stats. Dry-run expectation (Jun
   issuance): Jul-Sep / Aug-Oct / Sep-Nov / Oct-Dec 2026.
6. DRY RUN — NEVER PERFORMED. Blocked by the LICENCE gate (H.8), not the login.
   ⚠ CELL NUMBERING: the old H.6 said "Cells 3-6". Those were Task-2F-LOCAL numbers.
   Notebook indices (03_SEAsia_Drought_Data_Processing.ipynb):
     15 — Task 2F config (SYNTHETIC toggle, boxes, SEASONS, axis contract)
     16 — synthetic-run banner
     17 — file validation (magic bytes); opens `ds`; does NOT extract
     18 — box_mask + below_normal_stats + SEASONS x BOXES loop
     19 — four-panel figure (ASO/SON/OND/NDJ)
     20 — article-sentence emitter
   ⚠ AS OF 14 JUL, HALF THE PIPELINE DID NOT EXIST:
     - cells 19 and 20 were PLACEHOLDER COMMENTS, despite D.3 being ticked [x]
       ("cell written 10 Jul in session notes") — written in the NOTES, never inserted.
       DESIGNED EDITS ARE NOT DONE EDITS — third occurrence. D.3 UNTICKED.
     - NO extraction cell existed between 17 and 18: cell 17 opened `ds`, cell 18
       expected prob_below/normal/above + lat/lon, and nothing produced them.
     - NO GRID CHECK cell existed, though Section F's land-masking decision depends on it.
     - cell 17's comment asserted prob(category, forecast_time, lat, lon) — WRONG.
       Real contract is prob[X Y C | L F]. A wrong dim-order comment above the extraction
       code is how the dim-order bug gets written. Corrected.
   ⇒ The dry run would have FAILED EVEN WITH VALID DATA. Validate via synthetic .nc (E.0).
7. RUN-DAY CHECK 3: be logged in to iridl.ldeo.columbia.edu BEFORE downloading;
   verify file starts with CDF/HDF magic bytes, not <!DOCTYPE (login page).
8. 14 JUL UPDATE — LICENCE NOT CLEARED. Confirmed BY TEST, not inference: pasted the
   Jun-2026 download URL into a logged-in browser and was redirected to
   /auth/credential?...&realm=iri.columbia.edu/terms/forecast/1. The terms gate, not
   the login. Re-registered → SECOND ref 6fbac555e6d443f7ca25ef719632ff1e24acc573
   (shunchantsai@gmail.com, 14 Jul).
   ⚠ NO WITNESS FOR THE 10 JUL REQUEST. Searched all inboxes for 'f8725d9d...',
   'Access Request Confirmation', 'protected domain' — NO RESULT. The ref f8725d…
   exists ONLY in this tracker. The 10 Jul submission may never have completed.
   By the two-witness rule it is a single-source claim and must be treated as unproven.
   ⇒ TREAT 14 JUL AS THE REAL SUBMISSION DATE. 5 business days → WORST CASE ~21 JUL,
     not 17 Jul. Plan the dead window accordingly.
   ACTION 14 Jul: emailed help@iri.columbia.edu quoting BOTH refs; asked (a) which is
   live, (b) whether the resubmission reset the clock, (c) which address the 10 Jul
   confirmation was sent to. Also asked for the publication/attribution terms in advance.
   ON APPROVAL: archive the licence terms; record whether publication of derived
   figures/statistics is permitted (closes the "verify before publication" flag).
9. RUN DAY 15 JUL IS DEAD. Licence not cleared as of 14 Jul (H.8); worst case now ~21 Jul.
   The run slips to APPROVAL DAY. RULE UNCHANGED AND STILL RIGHT: do NOT substitute an
   unverified data source to hit a date — the computed sentence is the quantification of
   record and its provenance is the point.
   Note the July issuance was not posted on 14 Jul either (F axis still ended Jun 2026,
   N=113; page "Last updated: 15 Jun 2026" → IRI posts ~the 15th). So even an approved
   licence would not have enabled a 14 Jul run.
   DEAD-WINDOW WORK, in priority order: E.0 (synthetic validation of NB3) → B.1 (footnote
   audit + Figure 2A) → Q.6 (NB4). NB4 IS LAST. See Section F.


## Reference URLs

| What | URL |
|---|---|
| CPC ENSO Diagnostic Discussion (html) | https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.shtml |
| CPC ENSO Diagnostic Discussion (pdf, Fig. 2 caption) | https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/enso_advisory/ensodisc.pdf |
| CPC ENSO strength probabilities (75% NDJ / 81% OND table) | https://cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/strengths/ |
| RONI observed history (NOT the forecast table) | https://cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/ |
| Weekly Niño — traditional table | https://www.cpc.ncep.noaa.gov/data/indices/wksst9120.for |
| Weekly Niño — relative table | https://www.cpc.ncep.noaa.gov/data/indices/rel_wksst9120.txt |
| WMO GSCU JAS 2026 | https://wmo.int/media/update/global-seasonal-climate-update-july-august-september-2026 |
| ASEANCOF-26 page + bulletin | https://asmc.asean.org/events-twenty-sixth-session-of-the-asean-climate-outlook-forum-aseancof-26/ |
| ASMC rolling seasonal outlook (perishable) | https://asmc.asean.org/asmc-seasonal-outlook/ |
| IRI Precipitation Terciles maproom | https://iridl.ldeo.columbia.edu/maproom/Global/Forecasts/NMME_Seasonal_Forecasts/Precipitation_ELR.html |
| IRI ENSO Quick Look | https://iri.columbia.edu/our-expertise/climate/forecasts/enso/current/ |
| Singh et al. 2022 (accepted manuscript, DOE) | https://www.osti.gov/servlets/purl/1881165 |
| CPC official ENSO probabilities (numeric table) | https://cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/probabilities/ |
| Sarhadi et al. 2018 | https://doi.org/10.1126/sciadv.aau3487 |