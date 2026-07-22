# Article Artifacts — Sources Ledger · Hold List · Revision Log

**Canonical home of the three living artifacts** (moved out of Article_Writing_Workflow.md,
which is protocol-only and changes only when a protocol changes). The copy in the Doc's
appendix is a *mirror for travel* — regenerate it after edits here, never edit it first.

Rules:
- Rows are keyed by **claim content**, never by footnote number (fn numbers rot — drift rule).
- Every load-bearing claim gets a Ledger row when its `[verify]` tag is resolved.
- Dated facts ("as of <date>") get re-verified in the pre-submission VERIFY-all pass;
  none may be older than the latest monthly update at submission.
- Status vocabulary: CONFIRMED / HELD (→ Hold List) / RETIRED (claim removed from text).

---

## A. Sources Ledger — every load-bearing claim maps to a source

| Claim (content-keyed) | Value in text | Source | Status | Last verified |
|---|---|---|---|---|
| Latest Niño 3.4 (traditional) | +1.7 °C (wk of 17 Jun) | IRI Quick Look, Jun 2026 | CONFIRMED | 2026-07-07 |
| Relative vs traditional wedge | +1.1 °C rel. vs +1.7 °C trad., same week | CPC weekly indices (rel_wksst9120.txt / wksst9120.for) + 11 Jun DD Fig. 2 caption | CONFIRMED (tracker B.1.n+4: decimal-precision basis labeled) | 2026-07-17 |
| Monthly May value | +0.94 °C (monthly, ERSSTv5-style) | CPC monthly index | CONFIRMED, labeled monthly vs weekly (B.1.n+4) | 2026-07-17 |
| Tropical SST warming + attribution | tropical ocean warming faster since 1950; human influence | IPCC AR6 WG1 Ch.9 §9.2.1.1 p.1221 + SPM A.1/A.1.6 | CONFIRMED (read off page; negative Ch.2 walk documented) | 2026-07-17 |
| WMO ensemble: Niño 3.4 ≈ +2.0 °C JAS, narrow spread; IOD +0.6 °C JAS | as stated | WMO Global Seasonal Climate Update JAS 2026 (archived PDF) | CONFIRMED (tracker B.1.n+2) | 2026-07-17 |
| June convection coupling over Indonesia | near- to below-average convection | CPC ENSO Diagnostic Discussion, 11 Jun 2026 (archived PDF) | CONFIRMED (B.1.n+3); July-language recheck lives with Q.1 | 2026-07-17 |
| SE Asia OND soil-moisture anomaly: stable in sign, not size | −0.07 ± 0.03 (1997–98) vs −0.17 ± 0.03 (2015–16), Cluster 2 | Solander et al. 2020, HESS 24, 2303–2322, Table 3 | CONFIRMED (values verbatim; units m³/m³ established — tracker B.3 closed facts) | 2026-07-18 |
| ING dry / SSA wet: sense + season only | ING dry Jun(0)–Nov(0); SSA wet Nov(0)–Feb(+); episode counts NOT relied on (SSA table row anomalous) | Ropelewski & Halpert 1987, MWR 115(8), 1606–1626 | CONFIRMED — Table 2 row + Fig. 21 + Fig. 4/17 captions. ⚠ **Re-dated 22 Jul:** the earlier "three-witness" justification included a Fig. 4c count that has since been VOIDED (wrong panel; see lit_session1 notes V.12, reopened). **The sense + season claim is unaffected** — it never rested on that count — but the row's evidence basis is restated here honestly. ING's episode count (20/25) is currently SINGLE-witnessed and is not cited. | 2026-07-22 |
| Gulf/N-Mexico wet signal (southern-US case, NOT YET DRAFTED) | 18/22 wet | **Ropelewski & Halpert 1986, MWR 114 — never 1987** (Table 2 asterisk + §5 + §4g) | PRE-STAGED provenance rule | 2026-07-16 |
| SE Asia OND 1997 soil-moisture anomaly (Fig 2A) | box mean −0.020, min −0.105, max +0.008 m³/m³ vs 1979–2014 OND climatology | Computed for this article: GLDAS Noah V2.0 0–10 cm, 108 OND files 1979–2014, box 95/−10/150/7.5; NB3 Task 2A, commit c275cd5 | CONFIRMED (own computation; assertions on n, months, years, extent, units all passed) | 2026-07-20 |

<!-- Add rows as [verify] tags resolve: Saji 1999 (Session 2), Cai 2021 (Session 4),
     Singh 2022 / Sarhadi 2018 / Abrams / ASEANCOF (B.1 sweep), CPC 9 Jul DD (Q.1). -->

---

## B. Hold List — facts pending, with a trigger

| Item | Current placeholder in text | Source to check | Trigger | Note (19 Jul review) |
|---|---|---|---|---|
| Very-strong probability | none — text now states 75% NDJ / 81% OND | CPC ENSO Strength Probabilities | — | Appears RESOLVED in text; confirm the fn during B.1 sweep, then delete row |
| NDJ persistence % | none — text states 99% OND–DJF, 98/97% JFM/FMA | IRI Jun 2026 update | — | Appears RESOLVED in text; confirm fn, delete row |
| 1997/2015 analog magnitude at equivalent date | "onset anomalies of similar magnitude preceded seasonal peaks well above 2.0 °C" — **no citation on sentence** | CPC ONI history | before VERIFY-all | STILL HELD — sentence currently uncited; cite off ONI table or soften |
| "~1 °C warmer than 1997" | not found in current text | ERSST/OISST | — | Possibly RETIRED — confirm removed, then delete row |
| IRI ELR below-normal probabilities (boxes) | [COMPUTED FIGURE SLOT] + [PLACEHOLDER] | IRI 15 Jul issuance | licence clearance (f8725d…); IRIDL sunset ~end Oct | Production run inserts computed sentence |
| Compound-event antecedent soil-moisture deficit | [PLACEHOLDER] | current drought monitor data | post-recompute drafting | Every number computed (NB3) or read at source |
| Sections 3–6 brief numbers | rice tonnages; 20–30 % rice price rise; World Bank GDP drag 0.5–2.0 % | FAO/IRRI/national stats; the actual World Bank document (unidentified) | B.1.n acquisition, gates Sections 3–6 | Cite off the page or DELETE the number |

---

## C. Revision Log — the article's CHANGELOG

| Date | Session type | Section | What changed |
|---|---|---|---|
| 2026-07-07 | VERIFY | Intro | updated Niño 3.4 to +1.7 °C; added TONI/RONI hook; moved 4 items to Hold List |
| 2026-07-17 | VERIFY | Intro fn 1 | [VERIFY] retired: tropical-SST citation built from AR6 Ch.9 §9.2.1.1 + SPM A.1/A.1.6, read off the page |
| 2026-07-17 | VERIFY | §2 GSCU/convection/index fns | GSCU figures, 11 Jun convection wording, +0.94/+1.7 verified vs archived sources; fn dates/URLs corrected; monthly/weekly bases labeled |
| 2026-07-20 | DRAFT | §2 Fig 2A | replaced absolute-values figure with computed OND 1997 anomaly map (to 10°S); rewrote surrounding paragraph and caption with three-leg comparability guard; added New Guinea divergence sentence; deleted pending-recompute hedge |
| 2026-07-20 | VERIFY | Intro | "from from" typo fixed; fns 14/19 opening quotes and fn 18 tail confirmed clean |
| 2026-07-22 | VERIFY | §2 sources | ING ledger row re-dated and re-justified: the Fig. 4c second witness was voided (wrong panel, V.12 reopened). Sense + season unaffected; episode count now single-witnessed and not cited. |
