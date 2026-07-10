# Task B3 Tracker — 2026–27 Probabilistic Outlook
**Repo location:** `revision_notes/task_B3_tracker.md`
**Created:** 2026-07-09 · **Updated:** 2026-07-10 · **Owner:** Shun-Chan
**Rule:** work top to bottom. One checkbox at a time. Nothing here needs to be held in your head.

---

## 0 · Sync protocol (fixes "we see different things")

- [ ] **0.1** Fresh PDF export attached for review sessions. *(working — keep doing it)*
- [x] **0.2** After today's C.2 edits: export fresh PDF and **replace the stale project-folder copy**
      (delete old `Github_5__El_Nino.pdf` in project knowledge, upload new).

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

- [ ] **B.1** Footnote re-verification sitting — **date: [13 July]**.
      Remaining after incidental verification: fn 1 (Moore/Abrams), fn 4 (IRI plume 97–98% —
      also re-check value against July IRI Quick Look), fn 6 (**ECB placeholder — literally says
      "replace with specific ECB publication URL"; publication blocker**), fn 7 (Gaupp et al.).
- [ ] **B.2** Read Saji et al. 1999 before citing 1997–98 positive-IOD co-occurrence.
      [VERIFY] bracket stays in doc until done.

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
- [ ] **D.3** Section-G cells pasted into NB3. Remaining hygiene (do with D.2):
      - [x] B3 stays after 2A (decided 10 Jul: adjacency to Figure 2A context).
      - [ ] Add comment to B3 config: `# NOTE: order (W, S, E, N) — different from set_extent's [W, E, S, N]`.
      - [ ] Four-panel figure cell: **use cartopy coastlines** (matches Figure 2A style;
            cartopy already imported/used in this notebook — prior "no cartopy" decision reversed).
            - cell written 10 Jul (session notes); insert after dry run confirms dim order; gated on 
            license approval (H.8).

## E · 15 July or after — NB3 run (one session, one commit)

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

- Four-panel seasons: ASO/SON/OND/NDJ 2026, single 15-Jul issuance.
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
- [ ] **Q.3** OPTIONAL, low priority: re-pull GLDAS subset to 10°S and regenerate Figure 2A so
      Java/Bali/Timor appear in the article's own soil-moisture map (requires re-download;
      separate session, separate commit).
- [ ] **Q.4** OPTIONAL: verify or compute the −1 to −3 mm/day SE Asia precipitation anomaly
      figure (from the brief) before ever using it; candidates: NCEP-NCAR composites in NB2,
      or literature read at source.
- [ ] **Q.5** Publication-day freshness pass: latest weekly indices for the wedge sentence
      (labeled traditional AND relative), latest discussion issuance, all access dates.

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

## G · Data access — resolved (10 Jul 2026)

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

## H · Risks & run-day checks (15 Jul)

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
6. DRY RUN (before 15 Jul): full Cells 3-6 execution on the Jun 2026 issuance.
   Purpose: validate download, C-axis name selection, dim order, figure cell.
   Dry-run outputs are THROWAWAY — no June-issuance number enters the article.
7. RUN-DAY CHECK 3: be logged in to iridl.ldeo.columbia.edu BEFORE downloading;
   verify file starts with CDF/HDF magic bytes, not <!DOCTYPE (login page).
8. LICENSE GATE (discovered 10 Jul dry run): IRI forecast datasets require
   approved access to protected domain iri.columbia.edu/terms/forecast/1.
   Request submitted 10 Jul, ref f8725d9d51b4a11d4db44451b739208a30bd7a76, 
   review window "5 business days" = worst case 17 Jul, i.e. POSSIBLY AFTER RUN DAY. 
   Follow-up email sent to help@iri.columbia.edu 10 Jul. On approval: read and 
   archive the license terms; record whether publication of derived 
   figures/statistics is permitted (closes the "verify before publication" flag).
9. IF NOT APPROVED BY 15 JUL: run slips to approval day. Do NOT substitute an
   unverified data source to hit the date — the computed sentence is the
   quantification of record and its provenance is the point. Article's other
   sections are unaffected; 13 Jul footnote sitting proceeds as planned.
