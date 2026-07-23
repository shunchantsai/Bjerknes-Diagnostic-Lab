# Revision Note — ENSO Comprehension Exam (Source: ASMC Seasonal Outlook, JJA 2026)

**Session Anchor:**
This session is about: testing ENSO comprehension against an operational forecast
product rather than a paper — mechanism, probabilistic interpretation, skill
structure, and the hazard→loss chain. **Closed-book attempt first, assessment after.**
Session TYPE: **EXAM.**

**Date:** 2026-07-24
**Source:** https://asmc.asean.org/asmc-seasonal-outlook — Seasonal Forecast for
June–August 2026, page updated 3 June 2026 (i.e. the outlook was issued *before*
the season it forecasts; usable later as a verification target).

### Taxonomy
| Level | This doc |
|---|---|
| Campaign | **Operational-product literacy** (outside the NB1–NB4 arc) |
| Source | **ASMC JJA 2026 Seasonal Outlook** |
| Session | **Exam Session 1 (5 questions, 5 marks each)** |

## Purpose
Self-assessment record of a five-question exam on ENSO as it appears in an
operational seasonal forecast. Captures what I answered, what landed, what didn't,
and the correct full answers — so the gaps are traceable and re-testable. Marking
points in the model answers are **bolded**, one mark each.

---

## Overarching pattern (read this first)

Two distinct failure shapes appeared, and they are not the same kind of error.

1. **Axis slip, again (Q1).** Named the *Hadley* cell for a zonal-mode
   teleconnection. This is the mirror image of the Q3 slip logged on 2026-07-03,
   where meridional material was reached for on a strictly zonal question. Same
   fuzzy bin, opposite direction. **The axis discipline is not yet automatic.**
   NB1 owns ∂p/∂x, NB2 owns ∂p/∂φ — ENSO's *own* mode is NB1's axis.

2. **Product-layer conflation (Q2).** Merged the tercile probability with the
   inter-model agreement count. These are two separate fields printed on the same
   page. This is not a physics gap — it is a **forecast-epistemics** gap, and it
   is the one with the most carry into CAT work, where the same
   consensus-mistaken-for-validity error recurs in multi-model hazard ensembles.

Q3–Q5 were substantially unattempted (correctly flagged as unknown rather than
guessed). **Honest "I don't know" preserved — same discipline logged on 2026-07-03,
Q2. Keep it.** Q5 in particular was a genuine content gap: the ENSO→peat-fire→haze
chain was not previously known at all, so it is new material rather than a decayed
memory.

---

## Q1 — Mechanism

**Question.** The outlook says El Niño conditions tend to raise the chance of
below-normal rainfall over much of the southern ASEAN region (the Maritime
Continent). Walk through the physical chain that produces that — from equatorial
Pacific SST anomalies to suppressed convection over Indonesia/Borneo. Name the
circulation involved and say what happens to it.

**What I answered.** "Pacific SST anomalies suppress convection over
Indonesia/Borneo because the Hadley circulation is weakened during El Niño and
less moist air rises to form clouds and then rain."

**What landed (~2/5).**
- Direction of the effect correct: suppressed convection → less rainfall ✓
- Correctly identified that a large-scale overturning cell is weakened ✓

**Where it missed.**
- **Named the wrong cell.** Hadley is meridional (equator→subtropics), driven by
  the latitudinal insolation gradient. ENSO is a **zonal** mode; the circulation
  is **Walker**. Not a pedantic distinction — it is the geometry of the whole
  teleconnection.
- **No relocation of ascent.** Said the cell "weakens" but not that the ascending
  branch *migrates east*, leaving the Maritime Continent under subsidence. The
  migration is what does the drying.
- **No Bjerknes feedback**, despite the repo being named after it. The feedback
  was available but not applied to the ASEAN teleconnection — known in the Pacific
  basin frame, not yet transferred.

**Full correct answer (5 marks).**

Under El Niño, positive SST anomalies develop in the central and eastern
equatorial Pacific, so **the zonal SST gradient between the western Pacific warm
pool and the eastern cold tongue weakens**. Because the easterly trades are driven
by that gradient, they slacken; slackened trades reduce equatorial upwelling and
deepen the eastern thermocline, warming the east further — **the Bjerknes
feedback, a positive coupled ocean–atmosphere loop that amplifies the initial
anomaly**. The circulation being modified is **the Walker circulation, a zonal
(east–west) equatorial overturning cell — not the meridional Hadley cell, since
ENSO is fundamentally a zonal mode**. As it weakens, its ascending branch does not
merely slow but migrates: **deep convection relocates eastward toward the central
Pacific, leaving the Maritime Continent beneath the anomalous descending branch**.
Over Indonesia and Borneo this produces **large-scale subsidence, low-level
divergence and a drier free troposphere, suppressing deep convection and
delivering below-normal rainfall** — the teleconnection ASMC refers to for the
southern ASEAN region.

**One-liner:** *ENSO is zonal. If the answer names Hadley, the axis has slipped.*

---

## Q2 — Reading a probabilistic product

**Question.** ASMC gives tercile forecasts and shows a "number of models in
agreement" map. The FAQ example describes a 50–70% probability of the below-normal
tercile near Peninsular Malaysia. Two parts: (a) what does that number actually
mean, given climatology assigns 33% to each tercile; and (b) what does high
inter-model agreement tell you, and what does it *not* tell you?

**What I answered.** "Number means the percentage of the models that agree the
simulated precipitation will be below / normal / above, split 33% roughly."
(b) not attempted.

**What landed (~1/5).**
- Correctly recognised that terciles are three categories and that 33% is the
  reference split ✓

**Where it missed.**
- **Conflated two separate products.** The tercile probability is *not* a count of
  models agreeing — that is the separate Figure 2 agreement map. The probability
  comes from the distribution of ensemble *members*.
- **Misread the 33%.** It is definitional, not an output: terciles are equal-
  frequency bins of the observed climatology, so 33% is the **no-skill baseline**.
  The forecast's entire information content is the *departure* from it.
- (b) unattempted — and (b) is the half that matters.

**Full correct answer (5 marks).**

**(a)** The tercile framework rests on a definitional point: **terciles are
constructed by dividing the observed 1991–2020 climatological distribution into
three equal-frequency bins, so 33% per category is the no-skill, no-information
baseline rather than any model output**. The forecast value itself is derived from
the ensemble: **the probability is the calibrated fraction of multi-model ensemble
members whose seasonal rainfall total falls below the 33rd-percentile threshold of
that climatology**. Its informational content lies entirely in **the departure from
33% — a 50–70% below-normal forecast roughly doubles the climatological odds, while
still leaving around one chance in three that the season verifies near- or
above-normal**.

**(b)** The agreement map is a separate diagnostic: **it counts how many individual
models select the same dominant tercile, which measures consensus among models, not
the probability of the outcome**. Crucially, **agreement is not skill: models share
convective parameterisations, initialisation datasets and dynamical lineages, so
they are not independent and can be confidently wrong together — only hindcast
verification such as the ROC score establishes whether that agreement has
historically verified**.

**One-liner:** *Agreement is not skill. Shared bias produces consensus without
validity — which is exactly why ASMC prints agreement and ROC as separate fields.*

---

## Q3 — Skill structure

**Question.** The page reports moderate-to-good rainfall skill over the
eastern/central southern ASEAN region but low skill over Mainland Southeast Asia,
and the ROC maps show skill shifting between DJF and MJJ. Explain why seasonal
rainfall predictability is so unevenly distributed in space and season here.
Include the spring predictability barrier in your answer and say whether a forecast
issued in early June is on the favourable or unfavourable side of it.

**What I answered.** "ENSO and IOD both affect rainfall in Mainland Southeast Asia
— the battleground of regimes, many mechanisms acting on the resultant rainfall."
Then: did not know what the spring predictability barrier is, or how to tell which
side of it a June forecast sits on.

**What landed (~2/5).**
- **Correct instinct, correctly stated:** competing drivers → degraded
  predictability. "Battleground of regimes" is the right idea in the right words ✓
- Correctly identified IOD as a co-driver over Mainland SE Asia ✓

**Where it missed.**
- Did not generalise to the underlying principle: predictability comes from *slow
  boundary forcing* dominating variance over *fast internal chaos*.
- Spring predictability barrier: **not known.** New material.
- Did not connect ENSO's seasonal phase-locking to the DJF-vs-MJJ ROC contrast.

**Full correct answer (5 marks).**

Seasonal predictability exists only where **slowly varying boundary forcing
(principally SST) explains a large share of rainfall variance, as opposed to fast
internal atmospheric chaos, which is unpredictable beyond a fortnight**. Over the
equatorial Maritime Continent, convection is directly coupled to local and Pacific
SSTs, giving moderate-to-good skill; over Mainland Southeast Asia in JJA, by
contrast, **rainfall is governed by monsoon onset timing, intraseasonal variability
(MJO/BSISO) and tropical-cyclone landfalls, with ENSO and the IOD competing as
drivers — a battleground of mechanisms rather than a single dominant one**. The
seasonal contrast in the ROC maps follows from **ENSO's phase-locking to the annual
cycle: the teleconnection is strongest and most spatially coherent in SON–DJF, and
comparatively weak and diffuse in JJA**. The spring predictability barrier is the
sharp loss of ENSO forecast skill for predictions initialised in or spanning
roughly March–May, arising because **ENSO amplitude reaches its annual minimum
while the Bjerknes feedback is at its weakest — the ITCZ sits near the equator,
trades and the zonal SST gradient are slack, coupled growth rates are low, so
stochastic forcing such as westerly wind bursts can redirect the system, and the
Niño3.4 autocorrelation collapses across April–May, destroying persistence-based
skill**. A forecast issued on 3 June therefore sits **on the favourable side of the
barrier, since the coupled system has usually committed by early boreal summer —
though a newly emerging, immature El Niño still exerts a weak teleconnection, so
confidence in the ENSO state does not transfer to confidence in the JJA rainfall
response**.

**How to check this independently:** plot Niño3.4 anomaly correlation as a function
of initialisation month × lead time from a hindcast archive. The spring-start curves
fall off a cliff; the June-start curves do not. *(Candidate diagnostic — see fault map.)*

**One-liner:** *Past the ENSO barrier ≠ the teleconnection is reliable. Confidence in
the state does not transfer to confidence in the response.*

---

## Q4 — The asymmetry

**Question.** Temperature is forecast above-normal with good skill almost
everywhere, while rainfall skill is patchy and the signal is weaker. Why? And a
follow-up that matters for how you'd use this: how much of that confident warm
signal is ENSO doing work, versus something else?

**What I answered.** "Rainfall is not just thermodynamics but also to do with
circulation — something dynamic that the Clausius–Clapeyron relationship doesn't
cover."

**What landed (~2/5).**
- **The core physical distinction, produced unprompted and correctly:**
  thermodynamic constraint vs dynamical placement, with Clausius–Clapeyron named as
  the thing that bounds moisture but not location ✓ This is a genuinely good answer
  to the first half.

**Where it missed.**
- No statistical-character argument (Gaussian vs heavy-tailed/intermittent).
- No Maritime Continent model-bias point (resolution, diurnal cycle).
- **The follow-up was not attempted — and it is the operationally decisive half.**
  Most of the warm signal is the **trend against an ageing 1991–2020 baseline**,
  not ENSO.

**Full correct answer (5 marks).**

Temperature and rainfall differ first in their statistical character:
**near-surface temperature is a smooth, spatially coherent, approximately Gaussian
field, whereas rainfall is intermittent, heavy-tailed and highly localised, making
tercile classification intrinsically harder and noisier**. They differ second in
what governs them: **temperature is largely thermodynamically constrained, while
rainfall requires the model to place convection and moisture convergence correctly
— Clausius–Clapeyron specifies how much water vapour the atmosphere can hold, but
not where it will precipitate**. Third, **the Maritime Continent is a known locus of
systematic model error: coarse resolution smears the land–sea mask of the
archipelago and the diurnal cycle of convection is poorly represented, degrading
rainfall skill specifically in this region**. The decisive point for interpretation,
however, is attribution of the warm signal: **much of the confident above-normal
temperature forecast reflects the anthropogenic warming trend measured against a
1991–2020 baseline whose midpoint is now over two decades old — "above normal" is
the odds-on tropical outcome in most months irrespective of ENSO phase, and models
score well because detecting a monotonic trend is easy**. El Niño adds a genuine
increment through reduced cloud cover, subsidence warming and lagged tropical
tropospheric warming, but **the practical consequence is that high skill on the
temperature panel is no evidence of skill on rainfall — the two must not be allowed
to lend each other credibility**.

**One-liner:** *A high ROC score can mean the model detected the trend, not the mode.
Ask which signal the skill is scoring before you spend the credibility elsewhere.*

---

## Q5 — From outlook to loss

**Question.** The page links El Niño-driven dry conditions to hotspots and
transboundary haze. Sketch the hazard chain and then identify where it breaks down
as a predictor — i.e. what non-climatic factors determine whether a dry season in
Sumatra or Kalimantan actually becomes a severe haze year. Then name at least one
ENSO-related risk in the region that this rainfall-and-haze framing misses entirely.

**What I answered.** Did not know the hazard. Guessed antecedent soil moisture as a
control, with the sign inverted ("more moisture, less haze, but more hotspots").
Could not name a missing risk.

**What landed (~1/5).**
- **Reached for antecedent soil moisture** — the right *variable*, and the correct
  instinct that a pre-conditioning state matters ✓

**Where it missed.**
- **Sign inverted.** Less antecedent moisture → lower water table → more fire. The
  drying *is* the causal link.
- Hazard mechanism (peat combustion) not known at all — **new material, not decay.**
- The anthropogenic controls (drainage, clearing incentives, tenure conflict,
  governance, ignition) not identified.
- No missing-risk named. The TC and Atlantic-shear channels in particular are
  directly relevant to both a Taiwan-facing and a portfolio-facing frame.

**Full correct answer (5 marks).**

The hazard is peat fire. **Drought lowers the water table in the drained tropical
peat domes of Riau, Jambi, South Sumatra and Central Kalimantan; once it falls below
roughly 40 cm the peat becomes combustible and fires burn belowground, smouldering
for weeks, largely immune to conventional suppression and emitting extreme PM2.5,
which the prevailing southwesterly/southeasterly monsoon flow transports to
Singapore, Peninsular Malaysia and southern Thailand — hence "transboundary"**. The
canonical analogues are **the strong El Niño years of 1997/98 and 2015, the latter
causing regional excess mortality estimated in the tens of thousands and Indonesian
economic losses in the tens of billions of dollars**. The chain breaks down as a
predictor because the controlling variables are largely anthropogenic: **whether the
peat has been drained and canalised at all (intact peat swamp resists burning even in
drought), palm-oil and pulpwood price incentives to clear by fire in a given year,
land-tenure conflict in which fire is used as a tool, and ignition itself, which is
almost entirely human — climate sets susceptibility, people set the fires**.
Governance is the fourth and most underrated term: **Indonesia's post-2015 response
(peat restoration agency, canal blocking, moratoria, concession-level enforcement)
has measurably decoupled recent dry years from 2015-scale haze, so a modern El Niño
does not mechanically reproduce 2015 — ENSO conditions the hazard, while exposure,
vulnerability and policy determine the loss**. Finally, the rainfall-and-haze framing
omits most of the ENSO risk surface: **El Niño shifts western North Pacific
tropical-cyclone genesis eastward and southward (redistributing rather than simply
reducing landfall risk for the Philippines, Vietnam, Japan and Taiwan), suppresses
Atlantic hurricane activity via increased vertical wind shear over the main
development region — the largest ENSO–catastrophe linkage in dollar terms and
directly priced in reinsurance and cat-bond markets — and additionally drives
Mekong-basin drought and hydropower deficits, rice and palm-oil yield anomalies,
Coral Triangle bleaching, and a temporary fall in western Pacific sea level as warm
water shifts east**.

**Caveat for posting:** the 2015 mortality and loss figures are widely cited but
range widely across studies. **Verify the specific reference before publishing a
number** — same rule that caught the earlier bad citation.

**One-liner:** *ENSO conditions the hazard; drainage, incentives and governance
determine the loss. This is the hazard/exposure/vulnerability split stated in
someone else's vocabulary.*

---

## Fault map (for next session's re-test)

| Concept | Status | Action |
|---|---|---|
| ENSO = zonal mode → Walker, not Hadley | **slipped** (2nd axis error, mirror of 03/07 Q3) | re-drill cold; axis check before answering |
| Eastward relocation of ascending branch | **missing** | re-test |
| Bjerknes feedback applied to ASEAN teleconnection | **known in basin frame, not transferred** | re-test in teleconnection framing |
| Tercile probability vs model-agreement count | **conflated** | re-test cold |
| 33% as no-skill baseline (definitional) | **misread as output** | re-test |
| Agreement ≠ skill; ROC as the arbiter | **not produced** | re-drill — highest CAT carry |
| Slow boundary forcing vs internal chaos | **implicit, not stated** | re-test |
| Competing drivers degrade skill ("battleground") | **landed** (unprompted) | none |
| Spring predictability barrier — mechanism | **new material** | learn, then re-test cold |
| Barrier — which side a June forecast sits on | **new material** | re-test |
| CC bounds moisture, not placement | **landed** (unprompted, clean) | none |
| Warm signal = trend, not ENSO | **not produced** | re-drill — highest product-literacy carry |
| Peat-fire hazard chain | **new material** | learn, then re-test |
| Antecedent moisture — sign | **inverted** | re-test |
| ENSO risks beyond rainfall (TC, Atlantic shear, hydro) | **not produced** | build a risk-surface list |
| Honest refusal on unknown material | **strong** | keep |

---

## Phase 7 Insight — captured

**Agreement is not skill.** A multi-model ensemble can converge because its members
share convective parameterisations, initialisation datasets and dynamical lineages
— consensus without independence, and therefore without validity. Only hindcast
verification (ROC) establishes whether that consensus has historically been right.
The corollary is the one that generalises: **check which signal the skill is
scoring.** A seasonal outlook can be genuinely, verifiably skilful on temperature
because it is detecting a warming trend against an ageing baseline, while being
near-useless on the rainfall that actually drives the hazard. High skill on one
panel lends no credibility to the panel beside it.

Direct transfer to the Bjerknes-to-Risk pipeline: this is the same error as reading
multi-model hazard-ensemble convergence as confidence in a loss estimate. And Q5
supplies the vocabulary bridge — **ENSO conditions the hazard; exposure,
vulnerability and policy determine the loss.**

---

## Outputs queue
- **Threads post** — candidate spine: *a forecast can be confident, high-agreement
  and high-skill on the wrong variable.* Illustrated via the trend-vs-ENSO
  attribution and the agreement-vs-ROC distinction, landing on how CAT modellers
  and investors misread ensemble consensus. **Differentiated;** "El Niño means dry
  Indonesia" is not.
- **Candidate diagnostic** — Niño3.4 hindcast anomaly correlation, initialisation
  month × lead, to make the spring barrier visible rather than asserted. Small,
  self-contained, and it would sit naturally alongside the NB1 material. *Log it;
  do not let it preempt NB4.*
- **Verification target** — this outlook was issued 3 June 2026 for JJA 2026. Score
  it against observations after August for a forecast-verification piece.

---

*End of revision note — 2026-07-24*
