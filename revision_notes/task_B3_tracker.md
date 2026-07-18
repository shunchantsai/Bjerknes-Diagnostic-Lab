# Task B3 Tracker — 2026–27 Probabilistic Outlook
**Repo location:** `revision_notes/task_B3_tracker.md`
**Created:** 2026-07-09 · **Updated:** 2026-07-18 · **Owner:** Shun-Chan
**Rule:** work top to bottom. One checkbox at a time. Nothing here needs to be held in your head.
**Rule:** every sitting ends with a two-minute reconcile pass — tick what's done, amend what changed, log the session.

NEXT SITTING — queue as of 18 Jul (post ba9e493, tree clean, all 17 Jul closures pushed)

STANDING RULE — PREEMPTION: if the IRI licence clears (no ETA; IRI short-staffed),
NB3's production run takes the sitting. Everything below is dead-window work.

1. B.3 step 1 — Earthdata bearer-token test, ONE file. (~5 min)
   WHY: everything downstream of Figure 2A depends on auth; the account lapsed once.
   Fail-fast beats failing 40 files into a ~114-file queue.
   HOW: curl -LJO -H "Authorization: Bearer <TOKEN>" <single-file URL> from notes;
   magic-byte check the file. AFTER: proven token flow, logged in tracker.

2. B.3 step 2 — GLDAS V2.0 coverage read off the GES DISC product page. (~10 min)
   WHY: NB3 cell 1 asserts 1948–2015 from memory; if V2.0 ends earlier, the
   climatology-period claim is wrong at source. Decision already locked: state what
   V2.0 actually covers; independent estimate, never a replication.
   HOW: product landing page → temporal extent → correct cell 1 if needed.

3. B.1 fast sweep — fns 2, 9/10, 12, 15, 17, 20. (one clerical sitting)
   WHY: audit's founding fact = 4/4 sampled fns defective; every apparatus entry gets
   walked. These six are the cheap remainder — all sources already archived.
   HOW: archived doc beside article sentence; tick with a tracker note quoting the
   supporting source line (n+2/3/4 pattern). Fn 2: Abrams post-split sentence vs
   report. Fns 15/17/20: ASEANCOF bulletin (claims near-verbatim). Fn 12: Annex C
   (95% / 50.8 Mt / 90% band). Fns 9/10: Singh/Sarhadi still match post-merge.

4. B.3 steps 3–4 — full pull to 10°S, anomaly, mask. (the big block)
   WHY: current figure clips at 5°S (excludes Java/Bali/Timor — the regions Solander
   names driest) and plots absolutes, which can't show drought. Recompute turns the
   article's weakest figure into its strongest.
   HOW: ~108 files, Maritime box 95/−10/150/7.5; OND 1997 anomaly vs stated
   climatology; GLDAS validity mask.

5. B.3 step 5 — Solander units check (Table 3 volumetric?).
   WHY: NB3's /100 conversion assumes volumetric; the table states no units; one wrong
   assumption propagates into every comparison sentence.
   HOW: read the methods section for the units statement. Claude can run this from
   the project PDF in parallel with steps 2–4 — say the word.

6. B.3 step 6 — re-plot, regenerate PNG, retire placeholders. Closes B.3 + Q.3.
   HOW: Figure 2A as anomaly map; caption = anomaly + climatology period + the
   comparability guard (raw-GLDAS anomaly never presented as directly comparable to
   Solander's bias-corrected −0.07); swap figure in Doc; delete "recompute pending."

7. Q.6 — NB4 build (synthetic R&H replication). Subordinate to the preemption rule.
   WHY: the portfolio piece showing why consistency counts catch monster-episode
   pathologies.

8. B.1.n — source acquisition for Sections 3–6 brief numbers (rice tonnages, 20–30%
   price rise, "World Bank" GDP drag — no document identified for the last).
   WHY: nothing crosses brief→prose unsourced. Long tail; gates Sections 3–6 drafting.
   HOW: per number, find + read the primary document, cite off the page — or delete.

9. Study track (non-blocking): RH87 Batch 3; Lit Session 2 — Saji 1999.
   WHY: Session 2 closes B.2 AND retires the article's last live [VERIFY] marker
   (the Saji tag in the IOD sentence). A full session, not a footnote errand.

10. Closing protocol every sitting: tick/amend tracker → log session → git add →
    single-line single-scope commits → push → git status clean → audit.sh.

OPENING MOVE: #1 then #2 (fifteen minutes combined, de-risks everything after),
then #3 or #4 by energy — clerical → sweep; data → start the pull.

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
⚠ FN NUMBERS DRIFT when footnotes are inserted/deleted. Rule: tracker records claim
      TEXT; numbers re-verified by content search after any fn insertion/deletion. Never
      renumber by arithmetic (disproven 17 Jul).
- [ ] B.1.n  Sections 3–6 are BRIEF, not prose. Brief embeds unsourced numbers that MUST
      be verified at primary source before promotion to prose: rice production (2 Mt gain
      1997–98 / 15 Mt loss 2015–16 / 400,000 ha Indonesia — candidate sources: FAO, IRRI,
      national stats; NOT yet located); 20–30% rice price rise 1997–98 (candidate: FAO/World
      Bank commodity data); 0.5–2.0% GDP drag "World Bank estimates" (no document identified
      — treat as UNSOURCED CLAIM until the actual World Bank report is found and read).
      Rule: no number crosses from brief to prose without a read source. NOTE: ASEANCOF-26
      Annex C (ESCAP IBF) provides CURRENT-cycle rice exposure numbers (e.g. Indonesia 95.4%
      / 50.8 Mt of production exposed to below-normal rainfall, JJA 2026) — citable for
      forward-looking exposure framing; NOT a substitute for the historical figures.
- [x] B.1.n+1  fn 17 ("more than six models agree on below-normal") VERIFIED 16 Jul against
      ASMC Seasonal Forecast Jul–Sep 2026 (updated 6 Jul) — states >6 models predict
      below-normal as dominant tercile over southern ASEAN region. Footnote label updated
      Jun–Aug → Jul–Sep 2026; archived PDF confirmed = this version.
- [x] B.1.n+2  CLOSED 17 Jul. All three claims verified against WMO GSCU JAS 2026 page:
      "~2.0 °C for the seasonal average" ✓; "Spread among the individual forecast systems
      is generally narrow during JAS 2026" ✓; IOD "JAS 2026 seasonal mean value of 0.6 °C" ✓.
      Page shows "19 June 2026, updated 3 July 2026" — fns 14/19 dated accordingly.
      PDF archived 17 Jul; archive note added to fns 14 and 19.
- [x] B.1.n+3  CLOSED 17 Jul. 11 Jun discussion text verified from archived PDF:
      "Convection ... was near or below average over Indonesia (Fig. 5)" — article's
      "near- to below-average" paraphrase FAITHFUL; fn 18 holds as written. fn 18 archive
      URL fixed .shtml→.php; 11 Jun + 9 Jul PDFs archived locally; archive note added to
      fn 18. NOTED for optional freshness pass: 9 Jul discussion upgrades wording to
      "suppressed over Indonesia" — article may cite the stronger July language later,
      but the dated June citation is accurate as-is.
- [x] B.1.n+4  CLOSED 17 Jul. Both values verified at source: +0.94 °C = MONTHLY May 2026
      anomaly, stated verbatim in fn 3 (IRI June 2026 Quick Look, pub. 22 Jun, PDF
      archived); +1.7 °C = weekly, wk centred 17 Jun, confirmed in BOTH the Quick Look
      and wksst9120.for (traditional; May weeks 0.8–1.0, one decimal — 0.94 is monthly,
      not weekly). Old tracker ref "fn 2" was stale; true home fn 3, CPC series fn 4.
      Doc tweak APPLIED: "from a monthly mean of +0.94 °C in May to approximately
      +1.7 °C in the week centred on 17 June" — bases now labeled.
- [x] B.1.n+5  fn 5 75% NDJ re-verified on live strengths page 16 Jul (user check) — update
      access date in fn 5 to 16 Jul; archive page PDF.
- [x] B.1.n+6  fn 11 (81% OND) provenance VERIFIED 16 Jul: figure appears in 9 Jul discussion
      text itself.
- [x] B.1.n+7  fn 6 Singh + fn 7 Sarhadi identities & numbers verified at source 16 Jul;
      fn 7 misattribution repaired by Section 1 paragraph merge (stationarity/22% → Singh,
      severity → Sarhadi).
      - fn 1 (Abrams et al., "Recalibrating Climate Risk", Green Futures Solutions): source REAL, but concerns IAM damage functions / NGFS scenarios — NOT catastrophe models. CATEGORY SLIPPAGE. Sentence over-loaded: makes 3 claims (tropical SST rise / shifted extremes / CAT-model calibration) on one citation. SPLIT the sentence.
      - fn 4 (97–98%): number was READ OFF A PLOT. Phrasing traced to NOAA CRW text, not IRI.
        ⚠ PRODUCT TRAP: 97–98% is the CCSR/IRI **model-based plume** (mid-month), NOT the **CPC Official Probabilistic Forecast** (early-month, human consensus). Different products, different numbers. Numeric tables: cpc.ncep.noaa.gov/products/analysis_monitoring/enso/roni/probabilities/ 
Cite the right product; take the number from a TABLE, never a figure. Attribution required: "ENSO Forecast Data © 2002–2026 by IRI, CC BY 4.0".
      - fn 6: FABRICATED TITLE on a real, unrelated URL (ECB Environmental Statement 2025 — a report on ECB carbon footprint). Worse than the placeholder it replaced: silently broken, looks finished. REPLACE with Sarhadi et al. 2018, Sci. Adv. 4, eaau3487, DOI 10.1126/sciadv.aau3487 (READ IT FIRST).
      - fn 7: FABRICATED TITLE AND DOI. Correct authors/journal/vol/pages/year — invented identifiers (LLM signature). Real: Gaupp et al., "Changing risks of simultaneous global breadbasket failure", Nat Clim Chang 10, 54–57 (2020), 10.1038/s41558-019-0600-z.
        ⚠ AND ON READING IT: Gaupp CONTRADICTS the sentence — dependence can raise OR LOWER aggregate risk, and MITIGATES it for wheat/maize/soybean; dependence structure shows no significant change. GAUPP IS DROPPED. Sentence rewritten around Singh et al. 2022 (Nat Clim Chang, 10.1038/s41558-021-01276-3 — the PUBLISHED version, not the preprint).
      - ⚠ SCOPE: 4/4 sampled footnotes were defective. AUDIT EVERY FOOTNOTE, not just these. Every DOI resolves. Every URL opens to the claimed title. Every title matches the page. Every number comes from a table. Every citation supports THAT sentence's claim.
      - fn 4 ACCESS DATE IS STALE: the article says "accessed June 17, 2026" on a page that updates monthly. Re-access and re-date.
      - RESOLUTIONS (verified 15 Jul, paste into Doc — confirm each DOI resolves first):
      - fn 6 → Sarhadi et al. 2018, Sci. Adv. 4, eaau3487, 10.1126/sciadv.aau3487.
      - fn 7 → Singh et al. 2022, Nat Clim Chang 12, 163-170, 10.1038/s41558-021-01276-3.
        Numbers (from OSTI accepted ms, NOT preprint): ~68% compound droughts under ENSO
        (El Niño alone ~46%); ~22% rise in ENSO frequency → ~70% rise in compound droughts
        (263→448). Teleconnections LARGELY STATIONARY — frame frequency/severity, not pattern.
      - fn 1 → Abrams et al., Recalibrating Climate Risk. Supports "models underestimate"
        ONLY. Split sentence: SST-rise clause needs IPCC AR6 WG1; CAT-model clause needs an
        industry source or gets narrowed.
      - fn 5 (was fn 4) → 97–98% RESOLVED 16 Jul: sourced to IRI EXPERT ASSESSMENT prose (June 2026 update, enso-iri_update tab), NOT the model plume. Season corrected: 99% through OND–DJF; 97–98% is JFM–FMA 2027, not NDJ. Product label fixed model-plume → expert-assessment. Number now from text, not a plot.
      - STILL TODO: audit every OTHER footnote; verify Singh numbers on OSTI page.
- [x] B.1.n+8  fn 3 duplicate sentence DELETED 16 Jul (confirmed in export). The fn-1 split
      stands (SST + loss sentences under fn 1 + fn 2); the old unsplit "...raised mean tropical
      SST, shifted loss distributions, amplified extremes... [3]" sentence is gone. Old fn 3
      renumbered — current fn 3 is the IRI Quick Look.
- [x] B.1.n+9  fn 1 IPCC AR6 — CLOSED 17 Jul, Doc edit applied. KEEP "tropical" upheld.
      Ch.2 walked: NEGATIVE (global-mean statements only, §2.3.1.1.3 p. 324; §2.3.3.1).
      Ch.9 walked: POSITIVE — §9.2.1.1 (p. 1221): "tropical ocean has been warming faster
      than other regions since 1950," fastest in tropical Indian and W Pacific; global mean
      SST +0.88 [0.68–1.01] °C 1850–1900→2011–2020 (very likely). Summary p. 1223: very
      high confidence Indian Ocean + W equatorial Pacific warmed faster than global avg;
      E equatorial Pacific slower or slightly cooled.
      ATTRIBUTION LEG: Ch.9 is observations — pair with SPM A.1 (p. 4: "unequivocal that
      human influence has warmed the atmosphere, ocean and land") and/or A.1.6 (p. 5:
      human influence extremely likely the main driver of upper-ocean 0–700 m warming
      since the 1970s). Wording verified against SPM copy 17 Jul.
      SCOPE GUARD: citation licenses MEAN tropical rise, NOT Niño-region absolute baselines
      (E eq. Pacific caveat, p. 1223).
      TICKED 17 Jul: footnote replaced in Doc, [VERIFY] marker confirmed gone by search.
- [ ] **B.2** Read Saji et al. 1999 before citing 1997–98 positive-IOD co-occurrence (gated on Lit Session 2). Clean PDF re-uploaded to project 16 Jul (parses; corrupted copy replaced). On read, confirm against the text (not Claude): (i) 1997 was a positive IOD, (ii) the independence-from-ENSO framing that licenses "independent" in the article. [VERIFY] bracket stays in Doc until done.

- [ ] **B.3** — Figure 2A: raw map read as drought (Solander et al. 2020, HESS 24, 2303–2322)

STATUS: open. Blocked only on the anomaly recompute + re-plot (see ACTIONS).
All verification sub-questions below are now CLOSED.

CORE DEFECT (diagnosed 14 Jul): Fig 2A plots raw absolute soil moisture (cells 2–4),
not an anomaly. A raw field renders CLIMATOLOGY (mainland naturally drier than
rainforest), which was being misread as DROUGHT. Cell-5 prose originally claimed
maritime zones were "comparatively moist / mainland dry" — the OPPOSITE of Solander,
who finds the largest, most consistent OND soil-moisture reductions over maritime
SE Asia, Indonesia, New Guinea (up to 0.28). Notebook cell-5 prose corrected 15 Jul;
article Doc paragraph corrected (old step 7, confirmed applied 18 Jul).
Failure class: citation correct, FIGURE wrong. Verifying a source is necessary,
not sufficient — verify the artifact computes what the prose says.

CLOSED verification facts:
- NUMBER (14 Jul): Table 3, Cluster 2, OND 1997–98 = −0.07 ± 0.03. Cluster 2 =
  N/NE Amazon + maritime SE Asia. Attribution correct.
- "STABLE ACROSS EVENTS" CLAIM: FALSE and removed. Cluster 2 OND is −0.07 (1997–98)
  vs −0.17 (2015–16) — differ >2×. Now stated as "stable in sign, not size" (fn 11).
- V2.0 COVERAGE (18 Jul, GES DISC product page): Jan 1948 – Dec 2014. OND 2015/2016
  do NOT exist in V2.0. Our climatology is therefore 1979–2014 (OURS), stated as an
  independent estimate, never a replication of Solander's 1979–2016.
- UNITS (18 Jul): Solander Table 3 is unit-silent; established m³/m³ via Figs. 2–4
  axis labels, Fig. 5 colorbar ±0.25 + Discussion "up to 0.28" (p.2315), 0–10 cm
  layer (p.2305) ⇒ kg/m² ÷ 100 exact. Eq. 1's "(%)" is a source-internal
  inconsistency, not a doubt about Table 3. Our /100 conversion stands.

COMPARABILITY GUARD (two legs, both mandatory, for the caption rewrite):
Our anomaly is (a) NOT bias-corrected — Solander regresses GLDAS against 16 in-situ
sites (Eq. 1); (b) Noah-only 1.0° — Solander uses the 4-LSM ensemble mean
(VIC, CLM, Noah, Mosaic). Never present the two numbers as directly comparable;
Solander is corroboration of sign/pattern only.

ACTIONS (the re-pull and anomaly are ONE job; folds in Q.3):
[x] Test Earthdata bearer token on ONE file — CLOSED 18 Jul 2026. Oct 1997 subset
    returned HDF5 (magic-byte check via `file`), 30K.
[x] Pull — CLOSED 18 Jul 2026. 108 files, OND 1979–2014, box 95/−10/150/7.5 verified
    on file (lat −9.5 to 7.5; 1° cells are half-degree-centred, so −9.5 is the
    southernmost centre inside a −10 boundary). units "kg m-2" read from
    SoilMoi0_10cm_inst attrs, confirming the /100 conversion premise off the data.
    (Old box clipped at 5°S, excluding Java/Bali/Timor — the maritime zones
    Solander names driest. New box reaches 10°S.)
[ ] Compute OND 1997 anomaly vs 1979–2014 climatology; apply GLDAS validity mask.
    NOTE: cell index 2 hardcodes three open_dataset calls — rewrite as a stack over
    all 108 (open_mfdataset or glob) before the anomaly can be computed.
[ ] Re-plot Fig 2A as anomaly; rewrite caption with the two-leg guard; swap into
    Doc; delete the "recompute pending" hedge. Closes B.3 + Q.3.
    STAGED CAPTION TEXT (do not apply until the anomaly figure exists):

    NB3 cell index 5 replacement:
    Figure 2A shows the OND 1997 soil-moisture **anomaly** over the Maritime Continent,
    computed here from GLDAS Noah V2.0 (0–10 cm) as the departure of OND 1997 from the
    1979–2014 OND climatology. Negative values (browns) mark drying relative to the
    region's own baseline; the maritime zone — Sumatra, Java, Borneo, and the islands
    east to New Guinea — shows the coherent negative signal expected during a strong
    El Niño.

    This is an **independent estimate, not a replication** of Solander et al. (2020).
    Two differences forbid a direct number-to-number comparison: our field is Noah-only,
    whereas Solander uses the four-model GLDAS ensemble mean (VIC, CLM, Noah, Mosaic);
    and ours is raw, whereas Solander bias-corrects GLDAS against 16 in-situ sites.
    Solander's Table 3 reports the OND 1997–98 anomaly for their maritime-inclusive
    Cluster 2 as −0.07 ± 0.03 m³/m³. We cite that as corroboration of the **sign and
    spatial pattern** of maritime drying — not as a value our map should reproduce.

    Doc Fig 2A caption:
    Figure 2A. OND 1997 soil-moisture anomaly over the Maritime Continent (GLDAS Noah
    V2.0, 0–10 cm, departure from the 1979–2014 OND climatology). Browns indicate drying
    relative to baseline. Computed independently for this article; not directly comparable
    to the bias-corrected four-model ensemble anomaly of Solander et al. (2020), whose
    Cluster 2 OND 1997–98 value (−0.07 ± 0.03 m³/m³) corroborates the sign and pattern of
    maritime drying shown here.

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

- [x] E.0 ✅ DONE 16 Jul (verified against committed artifact: exec [1..15], GRID CHECK
      PASS x3, tercile sum 100.0, dim order (F,L,C,Y,X) discovered at runtime, figure
      watermarked SYNTHETIC). RESIDUE → E.2 precondition: SYNTHETIC=False + delete
      data_SYNTHETIC.nc on run day. Original item follows for the record.
      DEAD-WINDOW: synthetic validation of NB3 Task 2F (notebook cells 15-20;
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
      brief's original DJF target; see H.2). Literature side: RH87 NAU Sep(0)–Mar(+), 22/26 dry,
      double-witnessed — NDJ sits inside the season (2026-07-12_lit_session1_RH87_notes.md).
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
      Schedule: after the NB3 production run (slips to licence approval day; H.9), before
      drafting the Southern US flood case (the winter-outlook figures are load-bearing there).
      Includes: check July convection language vs fn 12's June claim. Fn-12 references here and
      in the B.1 sweep are located by CLAIM CONTENT (drift rule): the sweep closes the Annex C
      numbers only; the convection-language check closes HERE — don't double-close.
      Provenance rule for the flood case: the Gulf/N-Mexico wet signal (18/22) cites
      Ropelewski & Halpert 1986 (MWR 114), never 1987 — see lit_session1 notes V.6.
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
  (Below_Normal) (Normal) (Above_Normal) — select by name in code, never by position. (description-page order; runtime differs, extraction resolves by name.)
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
10. LICENCE HAS NO ETA (IRI short-staffed, confirmed 14 Jul — prior estimates void).
    The article is now LICENCE-INDEPENDENT: its claims rest on RH87 base rates + mechanism
    (in hand), not the IRI forecast. NB3 production is an indefinite background wait, drop-in
    ready via the validated synthetic pipeline. All other work (B.1, B.3, NB4, non-forecast
    sections) resequenced ahead of it. The July ELR issuance fills ONE section; its FRAMING
    depends on timing — FORECAST if the licence clears soon, else RETROSPECTIVE VALIDATION of
    the prior forecast (a different epistemic object: state it validates a forecast, not
    describes a known outcome). Issuance is archived issuance-stamped, retrievable either way.
    Forecast section carries a marked placeholder until data arrives.

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