# Literature Course — Session 1: Ropelewski & Halpert 1987

**Session Anchor:** Comprehending RH87's two-stage method (composite/harmonic → consistency count) and Table 2 / Fig. 5 / Fig. 21, for the article's ING/NAU/southern-US claims.
**Session TYPE:** CONTENT (reading + comprehension; no notebook or article editing)
**Started:** 2026-07-12

## Sitting log
- **2026-07-12** — Template adapted from NB1 skeleton. No reading. *(Reconcile missed — caught up 07-13.)*
- **2026-07-13** — Catch-up close: file renamed, queue annotated.
- **2026-07-13 (2)** — Paper read. Inventory populated, then **deduplicated**. Batch 1 (method spine) answered.
- **2026-07-13 (3)** — Verification pass. V.2–V.5 resolved; **V.1 failed (false positive — F.6)**; V.6–V.8 opened.
- **2026-07-13 (4)** — §4, §5, Table 2 read. **V.1, V.6, V.7, V.8 RESOLVED.** Table 2 audited: **the abstract's 80% claim fails for 5 of 19 rows.**
- **2026-07-13 (5)** — Table 2 rows read by eye. **F.11: the coherence/hit-rate collapse recurred.**
- **2026-07-13 (6)** — §4f prose was eye-read too → **Claude's "OCR" hypothesis FALSIFIED (F.12).** SSA discrepancy is real. **V.11 opened.**
- **2026-07-13 (7)** — **V.11 RESOLVED. NAU CONFIRMED by two witnesses (§4b prose states "22 out of 26" verbatim).** **ING has NO prose count — residual exposure → V.12.** **Fig. 17b counted: 16 marked episodes → prose + figure agree; Table 2's SSA row is the outlier.** **⭐ THE THREE-WITNESS STRUCTURE DISCOVERED: every region has a Table 2 row + a §4 prose paragraph + a figure pair. Every number in this paper can be triangulated.** **V.13 opened (the SSA row is internally consistent — 18+1=19 — which is a strange typo; test row-alignment misread vs. genuine erratum).**

**Phase 1: COMPLETE. Phase 2–3: Batches 1–2 COMPLETE. Batch 3 pending.**
**Next action: (1) V.12 — count Fig. 4c, close ING's exposure [HIGHEST VALUE]. (2) V.13 — straightedge the SSA row [cheap, timeboxed]. (3) Route ripe items. (4) Batch 3.**

---

## ⭐⭐⭐ THE THREE-WITNESS STRUCTURE — the most useful thing learned this session
> *Every region in RH87 is described in **three independent places**. Any number can be triangulated.*

| witness | what it gives | example (SSA) |
|---|---|---|
| **1. Table 2 row** | season, coherence, total/wet/dry | 0.82 · 19 / 18 / 1 |
| **2. §4 prose paragraph** | the count in words, *plus* the coherence value, *plus* a pointer to the figure | 0.81 · "14 wet episodes out of 16 ENSOs" |
| **3. Figure pair** (Fig. 3-type composite + Fig. 4-type time series) | **the marked ENSO episodes are COUNTABLE** as dark bars | Fig. 17b → **16 bars counted** |

**The prose explicitly cites the figure** — *"the time series (**Fig. 17b**) indicates…"*. **The paper hands you the triangulation.**

> **⭐ RULE — every number entering the article gets TWO witnesses minimum, and the second one is preferably the figure, because a bar chart cannot be mis-typeset.**
> *This is F.10 (internal consistency as verification) turned into a standing procedure.*

**Where the article's three numbers stand:**

| claim | witness 1 (Table 2) | witness 2 (prose) | witness 3 (figure) | status |
|---|---|---|---|---|
| **NAU 22/26** | ✅ | ✅ *"22 out of 26"* (§4b, verbatim) | Fig. 7a *(available)* | **✅ SOLID — two witnesses agree** |
| **ING 20/25** | ✅ | ❌ **§4a states NO count** | **Fig. 4c — NOT YET COUNTED** | ⚠ **→ V.12** |
| **Gulf/N. Mex 18/22** | ✅ | ❌ **no RH87 prose — imported from RH86** | ❌ not in RH87 | ⚠ **→ verify in RH86 itself** |

---

## ⚠️ HOW TO WEIGHT CLAUDE IN THIS FILE
> *Calibration data, gathered the hard way. Read before accepting any `[CLAUDE]` tag.*

**Claude's claims about WHAT THE SOURCE SAYS: 0 for 4.**

| Claude's confident claim | outcome, on my reading of the page |
|---|---|
| "Gemini fabricated 'fit to the entire data record'" | **WRONG** — it is the paper's verbatim wording (F.2) |
| "The western US is invisible by construction" | **WRONG** — mis-scoped; Great Basin is in Table 2 (F.7) |
| "SWA failed on aridity / zero-inflation" | **WRONG** — it failed on season ambiguity (F.8) |
| "The prose/table mismatch is OCR" | **WRONG** — I typed the prose by eye (F.12) |

**Claude's DERIVATIONS from stated premises have held up every time I checked them.**
The coherence formula's behaviour · the gamma-pooling arithmetic · the binomial figures · the two-way-split mechanics · the four-failure-mode structure · the three-witness triangulation.

> **⭐ RULE: Claude's reasoning is a tool. Claude's claims about what a source says are HYPOTHESES TO TEST, never findings. The page is the only witness.**

---

## ⭐⭐ THE ONE THING THAT KEEPS FAILING: COHERENCE ≠ HIT RATE
> *Collapsed twice (F.6, F.11). The load-bearing distinction of the entire paper.*

**Coherence never touches an episode. Not once.**

Worked example — one region, five stations:

| station | amplitude A | phase φ |
|---|---|---|
| S1 | 15 | 200° |
| S2 | 22 | 210° |
| S3 | 18 | 195° |
| S4 | 25 | 220° |
| S5 | 12 | 190° |

- |Σv| = **90.33** · Σ|v| = **92.00** · **coherence = 0.982**
- Scatter the phases (20°, 150°, 280°, 95°, 340°), same amplitudes → **coherence = 0.223**
- **No episode was counted anywhere.** The inputs were five *station harmonics*.

| | **COHERENCE** | **HIT RATE** |
|---|---|---|
| summed / counted over | **STATIONS** in a region | **EPISODES** in the record |
| inputs | harmonic vectors (A, φ) | the regional seasonal index — one value per episode |
| denominator for CEN | however many stations CEN contains | **19** |
| pipeline stage | **screening** — *does the region exist?* | **verification** — *should I believe it?* |
| CEN's value | **0.77** | **14/19 = 0.737** |
| cannot tell you | whether episodes agree **across time** | whether stations agree **with each other** |

**⚠ For CEN the two land within 0.03 by coincidence.** The paper's near-collisions manufacture this error.
**§5, verbatim:** *"The harmonic analysis is **not sufficient, in itself**, to establish the consistency of an implied ENSO-precipitation relationship."* **Collapsing the screen into the verification destroys the thesis.**

---

## ⭐ HEADLINE FINDINGS

1. **The 0.80 coherence criterion exists, is inherited from RH86 — and is NOT enforced in RH87.** §4: regions are selected "on a **subjective basis**"; the rule applied is "**relatively high** coherence." **Proof: CEN sits in Table 2 at 0.77**, admitted (§4g) only for adjacency. → **NB4 must not hardcode a threshold.**
2. **The abstract's "at least 80% … in almost every region" fails for 5 of 19 rows** — EAU 76.9%, SAT 75.0%, CAU 73.1%, SEA 77.3%, CEN 73.7%. §4a's version is scoped to the **Pacific Basin**, where it is exactly true — **and ING at 80.0% is the binding minimum.**
   → **ARTICLE RULE: never cite "R&H87: 80%" for a region. Cite the row.**
3. **The provenance trap is CONFIRMED.** Table 2's North America header carries an asterisk: *"From Ropelewski and Halpert, 1986."* Also §5; cross-referenced §4g. **Gulf and N. Mexico = 22 / 18 wet → 18/22. Footnote cites RH86.**
4. **FIVE numbers near 0.8, all different quantities:**

| number | what it actually is | enforced? |
|---|---|---|
| **0.80** | RH86's *coherence* criterion, quoted in §4 | **No** — RH87 uses "relatively high" |
| **0.80** | Great Basin's *coherence value* | (a value) |
| **≥80%** | *episode hit-rate* finding, §4a | **Pacific Basin only** |
| **80.0%** | ING's *hit rate* | (a value — and the binding minimum for #2) |
| **0.77 vs 0.737** | CEN's *coherence* vs CEN's *hit rate* | (coincidence — F.11) |

> **Grep for "0.8" and you will find the wrong one. Verify the QUANTITY, not the digits.**

5. **⚠️ TABLE 2's SSA ROW DISAGREES WITH ITS OWN PROSE AND FIGURE.** Prose (0.81; 14 wet of 16) and **Fig. 17b (16 bars counted)** agree with each other; Table 2's row (0.82; 19/18/1) does not. **Two witnesses beat one.** → **But V.13 must first rule out a row-alignment misread**, because 18 + 1 = 19 is *internally consistent*, which is a strange thing for a typo to be.

6. **⭐ THE THREE-WITNESS STRUCTURE** (see the standing section). **Every number in this paper can be triangulated. Use it.**

---

## Phase 1: Questions Inventory (deduplicated)

### [C] Clarifying
- **[C1]** (0)/(+)/(−) notation; ING's Jun(0)–Nov(0) for a 2026 episode. — **ANSWERED**
- **[C2]** Deriving 20/25 and 22/26 from Table 2's columns; the minority column. — **ANSWERED · NAU double-witnessed**
- **[C3] [MINE]** §1: are the two clauses the same point twice? — **ANSWERED**
- **[C4] [MINE]** Table 2's anatomy; **and I could not find the US flood signal in it.** — **RESOLVED (V.2/V.6).**
- **[C5]** Coherence: how |Σv|/Σ|v| works. — **ANSWERED — see standing section. Has failed twice.**
- **[C6]** Gamma percentiles. — **ANSWERED · conditioning RESOLVED (V.8)**
- **[C7]** Phase vs. composite. — **ANSWERED**
- **[C8]** Convergence-zone displacement (SPCZ/ITCZ). — **Batch 3**
- **[C9]** Zero-inflation (MME/NAS). — **Batch 3 · NB4 failure mode #1**

### [G] Generative
- **[G1]** Why harmonic vectors are "not sufficient." — **ANSWERED**
- **[G2]** Four Australian regions vs. five in Fig. 5. — **RESOLVED (V.5): SWA, at season identification.**
- **[G3] [MINE]** Reproduce Fig. 21; digitise to shapefiles; re-run on modern data. — **Scope proposal → Block B.**
- **[G4]** Subjective boundaries; overlapping stations. — **Batch 3**
- **[G5]** Exclusions & non-stationarity. **How to *parameterise* rather than exclude?** — **Batch 3 · own sitting · PhD-signal**
- **[G6]** The 1932 "atypical" episode. — **Batch 3. *(Note: §4a says 1932 is the ONLY ENSO year atypical in EVERY Pacific region — which is why the paper doubts it was a true episode. Good [G6] material.)***
- **[G7]** Bimodal responses. — **RESOLVED with [G2].**

### [S] Structural
- **[S1]** Which Table 2 rows originate in RH86? — **RESOLVED (V.6): both North America rows.**
- **[S2]** Numeric coherence threshold. — **RESOLVED (V.1): 0.80, from RH86, NOT enforced.**
- **[S3]** Evidence hierarchy. — **ANSWERED: the tally.**
- **[S4]** Mechanism vs. observation: proves or cites? — **Batch 3. *(Provisional: cites.)***
- **[S5]** Scope of absence: Fig. 21's white space. — **Batch 3 · §5's two limitations.**
- **[S6]** **Table 2's reliability, given the SSA anomaly.** — **RESOLVED (V.11): the anomaly is isolated; NAU is double-witnessed; ING needs Fig. 4c (V.12).**

### Parked (→ Sessions 2–4)
- **[P1]** How has the literature updated RH87 since 1987? · **[P2]** Have the coherent regions shifted?

---

## Verification queue (Phase 3.5)

### ✅ RESOLVED

- **V.1 — coherence threshold. EXISTS, INHERITED, NOT APPLIED.** §4: *"…only in regions for which the 'coherence' equaled or exceeded 0.80 (Ropelewski and Halpert, 1986). **Thus, in this study, only those areas of relatively high coherence are subjected to the following further analyses.**"* **Proof it isn't a gate: CEN sits at 0.77.** → **Gemini's premise was accurate; Claude's fabrication suspicion was wrong (F.2).** → **F.6 stands anyway: right conclusion, wrong passage.**

- **V.2 — the southern-US row. RESOLVED.** Both US rows present. Fig. 21: dashed (= wet) **Oct(0)–Mar(+)** over the southern US/Gulf. → [C4]'s alarm was a **miss**, not a hole.

- **V.3 — row values. RESOLVED.** **wet + dry = total in all 19 rows** → binary classification, no neutral category.

- **V.4 — one transform or two? TWO.** Ranks for the global screen; gamma percentiles for the regional analysis.

- **V.5 — the missing Australian region. SWA.** §4b: *"…does not show as clearly defined an ENSO-related precipitation season… the tendency for drier than normal conditions for the Jul(0) to Sep(0) season is not significantly different than a similar dry period later in the composite. Thus, SWA is excluded."*
  - **Fails at SEASON IDENTIFICATION** — before the count is ever reached. **[G2] and [G7] are the same finding.** → **NB4 failure mode #3.**

- **V.6 — RH86 attribution. Stated in THREE places.** (1) Table 2's North America header asterisk → *"From Ropelewski and Halpert, 1986."* (2) §5: *"Two other regions… the Gulf and Mexican and the Great Basin of the United States, were discussed in an earlier paper (Ropelewski and Halpert, 1986)."* (3) §4g cross-reference. **No source *column*.**
  - **→ FOOTNOTE RULE CONFIRMED: the southern-US flood case cites Ropelewski & Halpert 1986 (MWR 114).**

- **V.7 — Great Basin vs. the western US. Claude's claim was MIS-SCOPED.** §5: the method *"does not identify regions… over which the magnitude of ENSO-related precipitation anomalies may be large but **vary in sign from episode to episode**. The western United States may be an example."* Great Basin is nonetheless in Table 2 — an **Apr(0)–Oct(0) wet** signal (9/11), **from RH86**. **Both are true.**
  - **§5's TWO limitations:** (i) sign-flipping regions are invisible **by construction**; (ii) *"very much at the mercy of available station data"* — omissions: **the west coast of South America and the eastern Pacific.**

- **V.8 — gamma fit conditioning. RESOLVED BY INTERNAL CONSISTENCY: per calendar month.** Step (i) says *"fit to the entire data record"*; the next paragraph says the method *"effectively removes the annual cycle."* **A pooled fit would MAXIMALLY ENCODE the annual cycle** → **the pooled reading makes the paper's own sentence false.** → **"Entire data record" = all YEARS, not all months pooled.** → **F.10.**

- **V.11 — ⭐ IS TABLE 2 RELIABLE WHERE THE ARTICLE TOUCHES IT? RESOLVED — mostly yes, with one gap.**
  - **✅ NAU — CONFIRMED, two witnesses.** §4b, verbatim: *"The precipitation percentile time series for NAU for the Sep(0) to Mar(+) season (Fig. 7a) confirms that the overwhelming majority of ENSO episodes, **22 out of 26**, are associated with dry conditions in this region."* **Matches Table 2 exactly. Tracker item (a) is fully verified.**
  - **⚠ ING — NO PROSE COUNT EXISTS.** §4a describes ING qualitatively (*"highly consistent occurrences of negative precipitation departures"*) and never states 20/25. **The article's most important citation currently rests on Table 2 alone — the same artifact that failed for SSA.**
    - **Partial internal corroboration (F.10):** §4a's closing sentence — *"the precipitation departures are in the direction indicated by the ENSO composites for **at least 80% of the ENSO episodes for each of the core areas**"* — is a constraint on **all six** Pacific rows. **ING is exactly 80.0% — the binding minimum, the row that makes that sentence just barely true.** If ING were really 18/25 (72%), §4a would be false. **So Table 2's ING row and §4a's prose are jointly consistent.** Real evidence — not conclusive.
    - **→ V.12: count Fig. 4c. This closes it.**
  - **⚠ Gulf/N. Mexico — no RH87 prose count at all.** Imported wholesale from RH86. **Checkable only against RH86 itself** — which the footnote already points to. **→ verify there when writing the flood case.**

### ⚠️ OPEN

- **V.12 — ⭐ COUNT FIG. 4c (ING's time series). [HIGHEST VALUE — do this first]**
  Figure 4 is the Pacific Basin's time-series set (same figure type as Figs. 7, 17, 20): century-long percentile bars with **ENSO episodes marked as dark bars**. **ING is panel (c).**
  - **Expect: 25 marked episodes, of which 20 fall below the median line.**
  - **This gives ING its second witness and closes the article's largest residual exposure.**
  - *(You have already done exactly this for Fig. 17b. Same procedure.)*

- **V.13 — the SSA row: erratum, or row-alignment misread? [cheap, timeboxed]**

  | witness | coherence | episodes |
  |---|---|---|
  | **Table 2 (eye-read)** | 0.82 | 19 total, 18 wet, 1 dry (94.7%) |
  | **§4f prose (eye-read)** | **0.81** | **"14 wet episodes out of 16 ENSOs"** (87.5%) |
  | **Fig. 17b (bars counted)** | — | **16 marked episodes** ✅ |

  - **Prose + figure agree. Two witnesses beat one.**
  - **⚠ BUT THE PUZZLE: 18 + 1 = 19.** Table 2's SSA row is **internally consistent**. *A typesetter garbling three numbers such that they still sum correctly is a strange failure.* **The competing hypothesis is a row-alignment misread on a dense 19-row table.**
  - **THE CHEAP TEST:** put a **straightedge** under the SSA row and read it again. **Then scan the whole table for `16 | 14 | 2`** (14 + 2 = 16, consistent with prose + figure).
    - If `16 | 14 | 2` **is** SSA's row → it was a misread; the paper is clean; delete Headline Finding #5.
    - If the row really reads `19 | 18 | 1` and `16 | 14 | 2` appears nowhere → **a genuine erratum in a citation-of-record paper, propagated for four decades.** Worth **one footnote** in the article's notes. Nothing more.
  - **SCOPE: SSA is not one of the article's regions. Timebox this. V.12 comes first.**

---

## IMPACT ASSESSMENT — what the SSA anomaly actually touches

**For the paper (if the erratum is real):** a **data-entry error in one row of a summary table**, in a hand-typeset 1987 journal. It touches **nothing** — not the method, not the other 18 rows, not a single conclusion. And note what the triangulation tells us: **the prose and the figure agree with each other**, which means the *analysis* was right and only the *transcription into Table 2* slipped. **A clerical fault, not a scientific one.**

**NB3 (`03_SEAsia_Drought_Data_Processing.ipynb`) — ZERO IMPACT.** NB3 computes IRI tercile probabilities from NMME forecast data. **RH87 supplies no input to it.** RH87 is the article's *mechanism citation*; NB3 is its *quantification*. Independent artifacts. **No change required.**

**NB4 (`04_Ropelewski_Halpert_Atlas_Method.ipynb`) — NO IMPACT ON CORRECTNESS; a small gift for framing.** NB4 replicates the **method** on **synthetic** data. A wrong row in RH87's Table 2 cannot propagate into it. But it **sharpens two spec decisions already made**:
- **Derive sense and hit rate from counts. Never hardcode.** *(RH87's table would have caught its own error had it been generated rather than transcribed.)*
- **Print `n_total, n_wet, n_dry` for every cluster.** *A pipeline that prints its counts makes an inconsistency visible. RH87's table did not.*
- **Optional, and rather good:** a closing note in NB4 observing that the paper's own summary table disagrees with its prose and figure for one region — **a real-world demonstration of exactly why the notebook prints its intermediate counts.** *(One line. Not a feature.)*

**The article — bounded, and mostly reassuring.**
- **NAU 22/26 — solid.** Two witnesses agree.
- **ING 20/25 — one bounded action (V.12: count Fig. 4c).**
- **Gulf/N. Mexico 18/22 — one bounded action (verify in RH86 itself).** The footnote already points there.
- **The SSA finding earns at most ONE footnote** in the article's notes, if you want to show the working. **Do not make it a feature.** *(It is a nice signal of rigor to a CAT-modelling or admissions reader — and an obvious over-reach if you lean on it.)*

---

## TABLE 2 — read, audited, EYE-VERIFIED
> `wet + dry = total` in **all 19 rows** ✓ → binary classification, no neutral category.
> **17 core regions + 2 from RH86 = 19** ✓ matches §5.
> Hit rate = majority ÷ total. **Sense is DERIVED from the counts.**
> **Coherence is NOT in this arithmetic** — it comes from the station harmonics.

| Region | "Season" | Coher. | Total | Wet | Dry | Sense | **Hit %** |
|---|---|---|---|---|---|---|---|
| **Pacific Basin** | | | | | | | |
| Central Pacific (CP) | May(0)–Apr(+) | 0.98 | 8 | 7 | 1 | wet | 87.5 |
| S. Central Pacific (SCP) | Jul(0)–Jun(+) | 0.88 | 8 | 8 | 0 | wet | 100.0 |
| **Indonesia–New Guinea (ING)** ✅ | **Jun(0)–Nov(0)** | 0.82 | **25** | 5 | **20** | **dry** | **80.0** ← *binding minimum for §4a's claim; **needs Fig. 4c (V.12)*** |
| Fiji–New Caledonia (FNC) | Oct(0)–Mar(+) | 0.95 | 11 | 2 | 9 | dry | 81.8 |
| Micronesia–W. Pacific (MWP) | Oct(0)–May(+) | 0.91 | 13 | 1 | 12 | dry | 92.3 |
| Hawaiian (HAW) | Nov(0)–May(+) | 0.88 | 11 | 2 | 9 | dry | 81.8 |
| **Australia** | | | | | | | |
| **Northern Australia (NAU)** ✅✅ | **Sep(0)–Mar(+)** | 0.95 | **26** | 4 | **22** | **dry** | **84.6** ← ***double-witnessed (§4b verbatim)*** |
| Eastern Australia (EAU) | Sep(0)–Feb(+) | 0.89 | 26 | 6 | 20 | dry | ⚠ 76.9 |
| S. Australia–Tasmania (SAT) | May(0)–Oct(0) | 0.94 | 24 | 6 | 18 | dry | ⚠ 75.0 |
| Central Australia (CAU) | Mar(0)–Feb(+) | 0.86 | 26 | 7 | 19 | dry | ⚠ 73.1 |
| *(Southwestern Australia — SWA)* | — | — | — | — | — | **EXCLUDED (V.5)** | — |
| **Indian Subcontinent** | | | | | | | |
| India (IND) | Jun(0)–Sep(0) | 0.86 | 26 | 5 | 21 | dry | 80.8 |
| Minicoy–Sri Lanka (MSL) | Oct(0)–Dec(0) | 0.92 | 26 | 21 | 5 | wet | 80.8 |
| **Tropical & southern Africa** | | | | | | | |
| East Equatorial Africa (EEQ) | Oct(0)–Apr(+) | 0.93 | 13 | 11 | 2 | wet | 84.6 |
| Southeast Africa (SEA) | Nov(0)–May(+) | 0.90 | 22 | 5 | 17 | dry | ⚠ 77.3 |
| **South America** | | | | | | | |
| Northeastern SA (NSA) | Jul(0)–Mar(+) | 0.91 | 17 | 1 | 16 | dry | 94.1 |
| **Southeastern SA (SSA)** ❗ | Nov(0)–Feb(+) | **0.82** | **19** | **18** | **1** | wet | **94.7** ← ***prose says 0.81 and 14/16; Fig. 17b shows 16 bars — V.13*** |
| **Central America** | | | | | | | |
| Central America–Caribbean (CEN) | Jul(0)–Oct(0) | **0.77** | 19 | 5 | 14 | dry | ⚠ 73.7 |
| **North America \*** | | | | | | | |
| Great Basin | Apr(0)–Oct(0) | **0.80** | 11 | 9 | 2 | wet | 81.8 |
| **Gulf and N. Mexico** ✅ | **Oct(0)–Mar(+)** | 0.93 | **22** | **18** | 4 | **wet** | **81.8** ← *no RH87 prose; **verify in RH86*** |

**\* From Ropelewski and Halpert, 1986.** ← *the provenance trap, living in a footnote marker*

**⚠ = below the abstract's 80%.** Five rows: EAU, SAT, CAU, SEA, CEN — **including three of the four Australian regions.**
**Pacific Basin minimum = 80.0% (ING, exactly on the line)** → §4a's claim, scoped to §4a, is **true**, and ING is what makes it so.

---

## Phase 2–3: Answers

> **Tagging:** `[VERIFIED]` = read on the page by me. `[CLAUDE]` = Claude's reasoning — **not a source.**
> **See "HOW TO WEIGHT CLAUDE": Claude's source-content claims are 0 for 4.**
> The Phase 5 exam is closed-book **against the paper**, not against these answers.

### Batch 1 — the method spine

**[C1] — (0)/(+)/(−).** Year **(0)** = development year; **(+)** = following; **(−)** = preceding. Composite window = **Jul(−1) → Jun(+1)** = 6 + 12 + 6 = **24 months**, centred on (0). `[VERIFIED: Fig. 19 x-axis]`
- 2026 episode: **ING Jun(0)–Nov(0) = June–November 2026** → maps onto NB3's ASO/SON/OND panels.
- **NAU Sep(0)–Mar(+) = Sep 2026 – Mar 2027** → NDJ 2026–27 sits *inside* it. This licenses the E.5 test.

**[C2] — hit rates.** Majority count ÷ total. ING 20/25; NAU 22/26. **The minority column is the counterexample ledger** — the episodes that betrayed the signal, which a composite mean hides. `[VERIFIED: wet + dry = total in all 19 rows; NAU double-witnessed]`

**[C3] — §1's two clauses are NOT the same.** `[CLAUDE]`
- Clause 1 = prior work computing a **correlation**: one scalar, forcing a choice of index *and* lag, presuming linearity and simultaneity.
- Clause 2 = prior work **inspecting time series** at hand-picked stations: descriptive, no statistic.
- Grouped because they share one flaw: **the investigator chose the regions and the timing in advance.** §5 verbatim: *"The key to the success of the empirical methods described in this paper is that the 'core' regions and 'seasons' … are **themselves determined by the analysis**."*
- **The redundancy I sensed is real — but it is in the *criticism*, not the *methods*. And the criticism is the point.**

**[C5] — coherence.** → **See the standing section.** `[VERIFIED: §4]`
> **coherence = |Σ v| ÷ Σ|v|**, summed **over the stations in a region**.
- Denominator **strips out amplitude** — weak-but-agreeing scores as high as strong-but-agreeing.
- Measures **phase agreement only**: do the stations' anomalies peak at the same *stage of the episode*?
- **⭐ It says NOTHING about whether episodes agree across time.** *(F.6, F.11.)*

**[C6] — gamma percentiles.** `[CLAUDE; conditioning VERIFIED via V.8]`
- **Why gamma:** precipitation is non-negative and right-skewed; a z-score is a poor summary (+2σ in the dry season may be trivial; the same z in the wet season is a flood).
- **Why percentiles:** after the transform, **50 = "median for this month at this station" everywhere on Earth** — the precondition for averaging across episodes *and* across stations.
- **Why gamma over ranks (paper's words):** gamma percentiles *"represent quantities that are easier to interpret and relate to physical processes while maintaining some of the more desirable features of the percentile ranks."* → **invertible to millimetres; ranks are purely ordinal.**
- **The annual cycle dies by construction — because the fit is per calendar month (V.8).**

**[C7] — phase vs. composite: different jobs.** `[CLAUDE]`
- Composite = **24 numbers**; harmonic = **two**. **That compression is the only reason a global screening map exists.**
- The composite retains what the harmonic discards: **the shape of the curve** — asymmetry, duration, **bimodality**. *Hence [G7]. Hence SWA.*
- **Phase → delineate regions. Composite → identify the "season"** (step ii: *"used to identify **subjectively** the 'season'… with the largest apparent signal and the sign of that signal"*).
- **Trap (§4):** harmonics are constrained toward the **positive (wet)** side; for a dry region like ING the meaningful phase is **180° opposite the plotted arrow.**

**[G1] / [S3] — why "not sufficient," and where the burden of proof sits.** `[VERIFIED: §5, verbatim]`
> *"The harmonic analysis is not sufficient, in itself, to establish the consistency of an implied ENSO-precipitation relationship and thus further analyses are required."*
- **The failure mode:** a composite mean can be dragged to a convincing value by two or three extreme episodes while the *majority* sit on the wrong side of the median. **Coherence can look excellent too** — it only checks stations against each other.
- **Worked pathology:** episode percentiles = 55, 52, 58, **5**, **8** → composite mean **35.6**, healthy amplitude, beautiful arrow. But **3 of 5 episodes were above median.** Sold as "ENSO → dry," this is wrong 60% of the time.
- **The fix: count episodes.** ING 20/25. NAU 22/26. Coin-flip null: P(≥20 of 25) ≈ 0.002; P(≥22 of 26) ≈ 0.0003.
- **⚠ §5 explicitly DECLINES significance testing:** *"such tests are not appropriate to the a posteriori results presented here."* **The article must not attach p-values or significance language to RH87's hit rates.**
- **[S3]: the count carries the burden of proof.** The vector map *discovers and delineates*; **the count is the claim.** *"Given an El Niño, ~4-in-5 odds of a dry Jun–Nov in ING"* is priceable. An amplitude is not.

### Batch 2 — Table 2 and the article's claims (COMPLETE)

**The two-way split, in full.** `[CLAUDE mechanics; binary nature VERIFIED]`
- **What is split:** the **regional seasonal index** — *one scalar per episode*: average the gamma percentiles over every station in the region and every month in the season.
- **Where the split falls: the 50th percentile.** Because each month is scored against *its own* climatology, the seasonal average has median ≈ 50 **by construction.** "Below 50" = *drier than the median year for this region in this season.* No arbitrary threshold, no units, comparable across regions and hemispheres.
- **What is produced:** n_total, n_wet, n_dry (exhaustive).
- **What is done with them:** (1) **sense is DERIVED**; (2) **hit rate** = majority ÷ total; (3) **the minority column is the counterexample ledger**; (4) **⭐ the hit rate IS a base rate** — *"given an El Niño, ~4-in-5 odds of a dry Jun–Nov in ING."* **Priceable. An amplitude is not.**

**The two transforms.** `[VERIFIED: V.4 + §4 step (i)]`
- **Stage 1 — global screen: RANKED percentiles.** Distribution-free, cheap, robust. Resolution capped by record length.
- **Stage 2 — regional analysis: GAMMA percentiles.** Continuous, and **invertible to physical units** — the paper's own stated reason.
- **Both remove the annual cycle — because both are conditioned per calendar month (V.8).**

**[C4]/[S5] — Table 2 is NOT exhaustive.** `[VERIFIED: §5]` **Two limitations:** (i) regions whose anomalies are large but **flip sign between episodes** are invisible **by construction**; (ii) *"very much at the mercy of available station data"* — omissions: **the west coast of South America and the eastern Pacific.**
→ **ARTICLE RULE: absence from Table 2 is not evidence of absence of teleconnection.**

**Station-count constraint** `[VERIFIED: §4a]`: *"Because a minimum of **five stations** is required to represent a region, the length of the time series depicted in each of Figs. 4a–f varies from region to region."* **→ This is why episode totals differ across rows (8 for CP, 25 for ING, 26 for NAU). NB4 spec input.**

### Batch 3 — the method's limits *(next content sitting)*
**[C8], [C9], [G4], [G5], [G6], [S4], [S5]**
- **[S4] provisional:** the paper **cites** mechanism, never proves it — Kousky et al. (1984); Arkin (1982); Quiroz (1983b); Lau & Chan (1983). **Its own data are statistical throughout.**
- **[G5]'s second half** (parameterising non-stationarity rather than excluding the region) is **the PhD-signal question.** Own sitting.
- **[G6] enriched:** §4a — *"1932 is the only ENSO year to show an atypical precipitation anomaly in **each** of the Pacific Basin regions. This casts some doubt as to whether the 1932 ENSO was a typical episode."* **The paper is willing to question the EPISODE LIST when the precipitation disagrees with it. That is a circularity worth interrogating.**

---

## Fault map (route to `git_and_data_ops_lessons.md`)

- **F.1 — Claude's screen-reads are not verification.** *(Superseded in scope by F.12.)*
- **F.2 — ✏️ CLAUDE'S ERROR, not Gemini's.** *"Fit to the entire data record"* is the paper's **verbatim wording**; Claude called it a fabricated premise. **Real lesson: source wording can be ambiguous, and the resolution tool is INTERNAL CONSISTENCY (F.10).** *The pooled-vs-per-month arithmetic still stands: under a pooled fit a drought July of 200 mm reads at the ~85th percentile — i.e. WET — while a drought January of 10 mm reads at the 3rd. And the annual cycle is the **second** harmonic of a 24-month window, so stage 1 would look fine; **stages 2–4 fail quietly.***
- **F.3 — ✅ RESOLVED. The 0.80 exists but is not enforced** — CEN sits at 0.77.
- **F.4 — Two scoped commits require two edit sessions.** **The tell is a diffstat larger than the intended scope.** Tool: `git add -p`.
- **F.5 — Repo file operations go through git** (`git mv`, `git rm`), not Finder.
- **F.6 — ⭐ MATCHING DIGITS ARE NOT A MATCHING CLAIM. [Keystone.]** Searching for "0.80", I found *"at least 80% of the ENSO episodes"* and marked V.1 VERIFIED. **That 80% is the HIT RATE — a *verification* statistic. The claim under test was a *coherence* threshold — a *screening* statistic.** **The premise turned out TRUE anyway — which makes it worse:** *a correct conclusion from wrong evidence is still a verification failure*, and it would have carried a VERIFIED tag into the article. **Rule: state what the number should MEAN — formula, units, pipeline stage — BEFORE looking for it.**
- **F.7 — Claude's western-US claim was MIS-SCOPED.** *"The western US is invisible" and "sign-flipping precipitation is invisible" have different consequences.*
- **F.8 — Claude's SWA hypothesis was wrong.** Predicted aridity; **it failed at season identification.** *A wrong prediction, honestly logged, is how the fourth failure mode got found.*
- **F.9 — ⭐ THE SHORTCUT MIGRATES.** Having stopped generating *questions* with an LLM, I transcribed **Table 2** with one. **The rule was never "don't use LLMs." It was: OWN THE PREMISE.** *(The §4/§5 prose was in fact eye-typed — the migration was real for the table only.)* **Rule: numbers that enter an artifact are read by ME, off the page.**
- **F.10 — ⭐ INTERNAL CONSISTENCY IS A FORM OF VERIFICATION.** Used three times now: V.8 (gamma conditioning) · V.11 (§4a's ≥80% constrains ING's row) · V.13 (Fig. 17b as third witness). **→ Now formalised as the THREE-WITNESS STRUCTURE at the top of this file.**
- **F.11 — ⭐ THE COHERENCE/HIT-RATE COLLAPSE RECURRED.** **Coherence is summed over STATIONS and never touches an episode.** It recurred because CEN's two numbers nearly collide (0.77 vs 0.737). **Credit: I noticed 14/19 ≠ 0.77 and ASKED rather than papering over it.** *Noticing a number that doesn't add up is worth more than a confident wrong answer.* **A concept that collapses twice will collapse a third time — because the screen and the verification sit at the same level of abstraction UNTIL YOU BUILD THEM. → NB4 is the fix. The exam is non-negotiable.**
- **F.12 — ⭐⭐ CLAUDE'S CLAIMS ABOUT SOURCE CONTENT ARE 0 FOR 4.** *(fabricated-premise · western-US · SWA-aridity · OCR — all wrong.)* **Meanwhile Claude's DERIVATIONS have held every time.** **Rule: Claude's reasoning is a tool; Claude's claims about what a source says are HYPOTHESES TO TEST, never findings.**
- **F.13 — ⭐ NEW: A TABLE CAN BE INTERNALLY CONSISTENT AND STILL WRONG.** Table 2's SSA row satisfies `wet + dry = total` (18 + 1 = 19) **and still disagrees with the paper's own prose and figure.** **An internal-consistency check is necessary, not sufficient.** *(This is precisely why NB4 must print its counts rather than merely balance them — and precisely why the three-witness rule exists.)*

---

## Outputs Queue

### Tracker → `revision_notes/task_B3_tracker.md`
- **(a) NAU.** Sep(0)–Mar(+), **22 of 26 dry (84.6%)**, coherence 0.95. **DOUBLE-WITNESSED: Table 2 + §4b prose verbatim.** Independent literature support for **E.5**; NDJ 2026–27 falls inside the NAU season. **STATUS: ✅✅ FULLY VERIFIED — RIPE.**
- **(b) Southern-US provenance.** Gulf and N. Mexico: Oct(0)–Mar(+), **22 / 18 wet (81.8%)**, coherence 0.93. **Footnoted *"From Ropelewski and Halpert, 1986"*** (also §5). **→ Footnote cites RH 1986, MWR 114.** **STATUS: ✅ provenance VERIFIED — RIPE.** ⚠ *The 18/22 figure itself has no RH87 prose witness; verify in RH86 when writing the flood case.*
- **(c) NB4 proposal.** Tracker **Q.6**; preemption rule in **F**. **STATUS: routed ✓**
- **(d) Lessons** → `git_and_data_ops_lessons.md`: **F.2, F.4, F.5, F.6, F.7, F.9, F.10, F.11, F.12, F.13.** **STATUS: RIPE — route this sitting.**
- **(e) ARTICLE RULE — cite the row, not the abstract.** Five of 19 rows fall below 80%. **STATUS: ✅ RIPE.**
- **(f) ARTICLE RULE — no significance language.** §5: *"such tests are not appropriate to the a posteriori results presented here."* **STATUS: ✅ RIPE.**
- **(g) ⭐ NEW RULE — TWO WITNESSES MINIMUM.** Every number entering the article needs a second, independent witness in the source — **preferably the figure, because a bar chart cannot be mis-typeset.** **STATUS: ✅ RIPE.**
- **(h) SSA anomaly.** **STATUS: OPEN — pending V.13.** *Not article-blocking. Worth at most one footnote.*

### Article Sources Ledger
- **ING mechanism citation.** Jun(0)–Nov(0), **20/25 dry (80.0%)**, coherence 0.82. Canonical citation for the SE Asia drought mechanism claim; maps to NB3's ASO/SON/OND panels; for 2026 = **Jun–Nov 2026**. **STATUS: ⚠ ONE WITNESS ONLY — pending V.12 (count Fig. 4c).** *(It sits exactly ON the 80% line. Do not round up.)*
- **"Not exhaustive" caveat.** §5's two limitations. **STATUS: ✅ RIPE.**

### NB4 spec inputs → Block B
- **Table 2 columns:** Region | "Season" | Coherence | episodes total/wet/dry. **No source column.** Sense **derived**.
- **Two-way split at the 50th percentile**, exhaustive.
- **TWO transforms:** ranks (global screen) → gamma percentiles (regional analysis), **both per calendar month.**
- **Coherence** = |Σv| / Σ|v|, **summed over STATIONS**. **NO HARDCODED THRESHOLD.**
- **Minimum five stations per region** (§4a) → episode totals differ across regions. *Build this into the generator.*
- **Phase-inversion trap:** harmonics point to the positive (wet) side; dry regions read 180° opposite.
- **Season identification is SUBJECTIVE in the paper** (step ii). NB4 must automate it **and flag the deviation**, or replicate the subjectivity honestly. **Do not silently invent an objective rule the paper doesn't have.**
- **Vector clock** (Fig. 5): Jul(0) top, Jan(+1) right, Jul(−1) bottom, Jan(0) left; solid = dry, dashed = wet.
- **⭐ PRINT COHERENCE AND HIT RATE SIDE BY SIDE for every cluster, denominators labelled (n_stations vs. n_episodes).** *(F.11 — the notebook's pedagogical core.)*
- **⭐ PRINT `n_total, n_wet, n_dry`, don't just balance them.** *(F.13 — RH87's own table balanced and was still wrong.)*
- **⭐ Optional closing note:** RH87's summary table disagrees with its own prose and figure for SSA — **a real-world demonstration of why this notebook prints its intermediate counts.** *One line.*

#### ⭐ FOUR PLANTED FAILURE MODES — one per pipeline stage
1. **Zero-inflated arid** *([C9], MME/NAS)* → dies at **ranking**. Never reaches a harmonic.
2. **Noise** → passes ranking, **dies at coherence**. No phase agreement among stations.
3. **SWA-type bimodal** *(V.5, [G7])* → passes coherence, **dies at season identification**. No contiguous season; the index is never built.
4. **Monster-episode pathology** → passes ranking, coherence **and** season identification with a beautiful arrow — **dies at the consistency count.** *The payload.*

### Scope decision — [G3], digitising Fig. 21
> **Log it; decide at Block B; default to a SEPARATE deliverable.** Would roughly double NB4. **NB4's justification is that it fits inside the license dead window. A doubled NB4 does not.**

---

## Phase 5–6: Exam

**Status: DEFERRED** until NB4's pipeline runs end-to-end (Block C, item 16).
**Closed-book against the PAPER, not against Claude's answers.** *(See "HOW TO WEIGHT CLAUDE": 0 for 4.)*
**⚠ F.11 makes this exam non-optional.**

### Candidate questions
- **Q1 (conceptual):** State the coherence formula. **What is its denominator summed over?** Say what it does **not** measure, and name the statistic that does.
- **Q2 (trap):** RH87 contains **five** numbers near 0.8. Name each, give its formula and pipeline stage, and say which — if any — is enforced as a selection rule.
- **Q3 (structural):** Name the four stages of the pipeline. For each, give a region *or* a synthetic cluster that fails **at that stage**.
- **Q4 (article-facing):** ING's hit rate is 80.0%; EAU's is 76.9%. Explain why the abstract can say "at least 80% in almost every region" and why **you** may not.
- **Q5 (provenance):** Where in RH87 is the Gulf/N. Mexico signal attributed to RH86 — and why can't that attribution be read off Table 2's columns?
- **Q6 (method):** Name the three independent witnesses RH87 provides for every region, and explain why the figure is the strongest of them.

---

## Documentation hygiene — this file is a FUNNEL
> Once Batch 3 is answered and V.12/V.13 are closed:
> 1. Collapse the verification queue into resolved facts.
> 2. **Ship the fault map to `git_and_data_ops_lessons.md` and DELETE it from here.**
> 3. **Keep permanently: THE THREE-WITNESS STRUCTURE · HOW TO WEIGHT CLAUDE · COHERENCE ≠ HIT RATE · the Table 2 audit · headline findings · the exam.**
> **Documentation that only grows is documentation nobody re-reads.**

## Per-sitting closing protocol (2 min)
1. Update the Sitting log + phase statuses (honest state).
2. Route only **ripe** items; PENDING items stay flagged.
3. `git add` → `git commit -m "lit s1 (RH87): <one-line actual state>"` → `git push`.
4. Reconcile: `git status` clean; **read the diffstat** (F.4); tracker and CHANGELOG match reality.
