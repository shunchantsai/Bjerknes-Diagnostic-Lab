**CLOSED 2026-07-03** — §13.2 Walker-trend clarity flag (raised in the exam session)
resolved: rewritten with explicit "unresolved, not corrected" framing, Phase-3.5
verified with DOIs. See CHANGELOG. Do not edit further; open a new arc file for
any subsequent NB1 work.

# Phase A: NB1 Deep Read & Comprehension

**Session Anchor:**
This session is about: Understanding NB1's content deeply.
Session TYPE: CONTENT (reading + comprehension, no editing yet)

**Date:** 2026-07-03 (continuing from git commit)

---

## Phase 1: Deep Read — Questions Inventory

Read through 01_Bjerknes_Zonal_Diagnostic.ipynb cold. Mark questions as you go.

### [C] Clarifying Questions
(Questions where I don't understand a mechanism)

1. "$M = \Omega a^2\cos^2\varphi + u\,a\cos\varphi$" I should further my understanding and application of this equation. Give me 3 practice Q&As.

2. "Once the equatorial air is no longer sealed in its own plane, it **leaks absolute angular momentum (AAM) poleward**, and steady winds require that leak to be refilled. The only refill is surface friction — which adds *eastward* AAM only when it drags the air eastward, i.e. only when the surface wind blows *westward*. So easterly trades are a **rotational necessity**, independent of the pressure gradient." I am having trouble visualising and conceptualising this clearly. Explain this to me with an annotated figure.

3. "### The Diagnostic Problem

This notebook investigates the nature of this alignment. Is this coincidence a structural feature of the Pacific system, or an empirical accident of those specific low-index regimes?

**Answer (Preview):** Neither. The coincidence is a structural feature of Scenario A (pure see-saw, no basin offset), but empirically rare because natural transitions involve basin-wide pressure changes. The notebook shows this explicitly: the four regimes (A–D) arise from a single closed decomposition, and only Scenario A exhibits coincidence." I just want to double check on this again. To make sure the answer I have is correct, and also true that the coincidence is a structural feature of Scenario A (pure see-saw, no basin offset) is empirically rare due to natural transitions involve basin-wide pressure changes. Has any other studies confirmed this? This feels like an important research question on ENSO. 

4. 


### [G] Generative Questions  
(Questions where the passage implies something I haven't thought through)

1. "A misplaced zero isallobar is not just a geometric error — it propagates through the climate system:

1. **Equatorial pressure anomaly** → misclassified *node* (zero isallobar) vs *peak* (gradient maximum)
2. **Hadley circulation intensity** → the magnitude of the pressure gradient drives Hadley overturning; 
   if the node and gradient-max don't coincide, a diagnostician using the node location 
   may sample the gradient at the wrong longitude, reading a weaker value than the true peak
3. **Angular-momentum flux** → the Hadley cell's intensity modulates the poleward eddy flux of AAM — 
   *the same conserved quantity from Trap 2, and the literal hand-off to NB2*
4. **Midlatitude jet position and strength** → sets whether ridges/troughs are displaced poleward or equatorward
5. **Downstream weather & extremes** → the shifted jet alters TC tracks, rainfall, and cold-air-outbreak frequency" & "**Scenarios C & D** (offset ≠ 0, small): Node displaced east or west of gradient-max → 
  a diagnostician reading the gradient at the node's location instead of the true peak 
  will sample a *weaker* gradient magnitude, thus **underestimate** Hadley intensity in both cases" I think I need a few illustrative examples with calculations and visuals to really understand this part. Also, could the diagnostician also sample a stronger gradient magnitude instead, thus overestimating Hadley intensity in both cases? An interesting thought experiment that perhaps I can write about and post on threads too.

2. The code cell "# ── Setup: import physics module and plotting functions ──
import numpy as np
import matplotlib.pyplot as plt
from bjerknes_physics import (
    pressure, gradient, find_zero_crossings, get_regime,
    plot_scenario, plot_width_diagnostic,
    tongue_width_history, plot_width_history,
    total_pressure_drop, integrated_cold_content,
    lon_fmt, DEFAULT_X, X0_COLD,
)
%matplotlib inline
print(f"X0_COLD = {X0_COLD:.0f} = {lon_fmt(X0_COLD)}  (canonical cold-year node / gradient-max longitude)")" prints "X0_COLD = 178 = 178°E  (canonical cold-year node / gradient-max longitude)". But so far in the notebook, there has been no explanation of why X0_COLD = 178°E  (canonical cold-year node / gradient-max longitude. I know we decided on this number because we read it from the figure in the paper roughly. This 178°E figure appears once in the paper "The zero isallobar intersects the Equator at 175°E in figure 3, 170°W in figure 4, 168°E in figure 5, and 178°E in figure 6, in other words a little west of the dateline on the average." Was this why we used this figure? If yes or no, then we should still explain why this code cell prints "0_COLD = 178 = 178°E  (canonical cold-year node / gradient-max longitude)" right?

3. "We can reliably infer the location and shape of pressure anomalies from the gradient structure (node, peaks, etc.), because these are geometric features. But the mapping from gradient magnitude to absolute wind speed is approximate — it requires knowledge of the boundary layer and the angular-momentum budget, not just the pressure field. Fortunately, the regime diagnostics (§4–7) depend only on locations, not magnitudes, so this limitation does not affect the notebook's conclusions." This is interesting. Show me 3 illustrative calculation examples.

### [S] Structural Questions
(Questions about whether something belongs in NB1, or if the framing is right)

1. "> Two questions that sound identical are not: *"Where did the pressure stop changing?"*
> (the temporal **node**, the zero isallobar) and *"Where is the pressure field steepest
> right now?"* (the spatial **gradient maximum**). In a pure cold-regime see-saw they
> coincide; add a basin-wide offset and they part. This notebook lives on the **zonal**
> axis of the Walker circulation — itself a superposition of a thermally driven loop and
> a rotational easterly overlay — and its whole task is to keep that pair, and several
> like it, apart." -> "sound identical but are not", "and its whole task is to keep that pair, and several like it, apart." Is this a bit meta? Or weird style of communication for this notebook?

2. "The Walker circulation is not one east–west loop but two circulations in one: a
**thermal cell** driven by the equatorial SST contrast, plus an **easterly overlay**
demanded by Earth's rotation. Both are zonal — both live on the $\partial p/\partial x$
axis — yet they have different origins, different vertical structures, and different
implications for what a surface pressure diagnostic can and cannot see. The four traps
below show where they enter, and where conflating them costs something." Okey it sounds a bit redundant to S1. Perhaps we merge them together and get rid of the repetitive parts.

3. So after the section on "## The stage: an actively maintained cold tongue", we move to "## Four traps that frame this notebook ... ### Trap 1 — Which axis drives the cell? ... ### Trap 2 — Why must there be trade winds? ... ### Trap 3 — What happens when the gradient dies? ... ### Trap 4 — Where does the pressure see-saw pivot?" And then "## Why the diagnostic matters: the downstream chain", followed by "**How the error manifests across regimes:**". Are the above writing flowing smoothly and logically? I have a feeling that the 4 trap section could be in a separate document. But this is just a question on the aesthetics. So not that important, right? What do you think? I do think they help frame the introduction and this notebook though. So maybe leave it as it is?

4. "(That overlay is why upper-tropospheric westerlies appear only east of ~150°E, where the loop's eastward return finally overpowers it — Sadler's observation.) " I think this part could include a quick link or reference to the figure on this below. What do you think? How should I implement this, if you think this is a good idea?

5. "Surface *westerlies* were then measured at 145°W, where trades should blow. This is the **Bjerknes feedback** run to a stall: weaker gradient → weaker trades → less upwelling → warmer east → weaker gradient still, a self-amplifying loop." I think the 145°W needs a precise reference to where this information is found within the Bjerknes 1969 paper. 

6. "### Why This Matters for Risk Modeling

In catastrophe (CAT) modeling, the hazard, exposure, and loss layers are all conditioned on correctly identifying the ENSO state. If a diagnostic conflates two quantities — isallobaric change and pressure gradient — that only coincide under specific regimes, errors propagate silently through the entire risk model. By disentangling the Southern Oscillation (the zonal see-saw) from basin-wide mass exchange, this notebook provides a rigorous, regime-aware framework for classifying equatorial Pacific dynamics." Yes I agree with it. But is it not slightly repetitive of the previous cell where it says "Why the diagnostic matters: the downstream chain
A misplaced zero isallobar is not just a geometric error — it propagates through the climate system:

Equatorial pressure anomaly → misclassified node (zero isallobar) vs peak (gradient maximum)
Hadley circulation intensity → the magnitude of the pressure gradient drives Hadley overturning; if the node and gradient-max don't coincide, a diagnostician using the node location may sample the gradient at the wrong longitude, reading a weaker value than the true peak
Angular-momentum flux → the Hadley cell's intensity modulates the poleward eddy flux of AAM — the same conserved quantity from Trap 2, and the literal hand-off to NB2
Midlatitude jet position and strength → sets whether ridges/troughs are displaced poleward or equatorward
Downstream weather & extremes → the shifted jet alters TC tracks, rainfall, and cold-air-outbreak frequency
How the error manifests across regimes:

Scenario A (offset = 0): Node and gradient-max coincide → no separation, no error
Scenario B (|offset| large): No zero isallobar exists → no node to misplace, no error
Scenarios C & D (offset ≠ 0, small): Node displaced east or west of gradient-max → a diagnostician reading the gradient at the node's location instead of the true peak will sample a weaker gradient magnitude, thus underestimate Hadley intensity in both cases
The single parameter controlling this separation is global_offset — the basin-wide pressure change that tilts the pressure field uniformly. The notebook's job is to show that this separation is systematic and parameter-controlled, so that when reading operational indices (which often assume node = gradient-max), you can correct for it or at least acknowledge the bias."?

7. The cell for "2. The Diagnostic Duality: Temporal vs. Spatial Dynamics". Yes very well written. I just wonder if it is repetitive of what's already before it or perhaps this is fine as this is a section that properly layout the fundamentals and the equations?

8. In "## 3. Setup: The Idealised Surface Pressure Model", the equation and table now introduces "| **`w`** | **Oceanic memory:** cold-tongue width. | Duration/history of equatorial upwelling — the *oceanic* width, distinct from the *atmospheric* branch width in §3.6. |" as a parameter that affects the p(x). Should this be introduced in earlier sections or here is fine?

9. "Two diagnostic results follow directly from this form:

1. **Spatial gradient.** $|\partial p/\partial x|$ is steepest exactly at $x = x_0$, anchored by the antisymmetric SO term *regardless of* `global_offset`. This is the **gradient maximum** — the "where is the field steepest right now?" location. (Its sign convention is treated in §3.5; only the location matters for §4–7.)
2. **Isallobaric change.** $\Delta p(x)$ is the difference of two such profiles over time. Where it vanishes defines the **node** of the see-saw — the "where did pressure stop changing?" location.

Keeping these two locations apart — and knowing that `global_offset` alone controls their separation — is the notebook's central task (§4 onward)." This part feels a bit repetitive again. What do I do?

---

## Phase 2–3: Claude Assessment & Answers

> Session 1 of Phase A. Scope covered: the three [C] Clarifying questions
> (Cell 0 / §1–§3 material). [G] and [S] questions deferred to a later session.

### [C1] — The angular-momentum equation

**Equation:** `M = Ω a² cos²φ + u a cosφ`  = absolute angular momentum (AAM) per unit
mass about Earth's rotation axis.

- `Ω` = Earth's rotation rate (7.292×10⁻⁵ s⁻¹)
- `a` = Earth radius (6.371×10⁶ m)
- `φ` = latitude
- `u` = zonal (eastward) wind relative to the surface

**One-line derivation.** A parcel at latitude φ sits a distance `r = a cosφ` from the
axis. Its total eastward velocity in inertial space is (Earth's ground speed) + (its wind)
= `Ω a cosφ + u`. AAM per unit mass = velocity × lever arm:
`(Ω a cosφ + u)(a cosφ) = Ω a² cos²φ + u a cosφ`.

- 1st term = **planetary** AAM (what it would have riding motionless with the solid Earth).
- 2nd term = **relative** AAM (the wind's contribution).
- Both carry cosφ, so **M is maximal at the equator, zero at the poles.** AAM decreasing
  poleward is the engine behind the whole trade-wind-necessity argument (see [C2]).

Handy constants: `Ω a ≈ 465 m/s` (equatorial surface speed), `Ω a² ≈ 2.96×10⁹ m²/s`.

**Practice Q1 — planetary AAM drops poleward.**
Compute planetary AAM at equator vs 30°N; fractional drop?
→ Equator: `Ω a² cos²0 = 2.96×10⁹`. 30°: `cos²30 = 0.75 → 2.22×10⁹`.
→ **25% drop over 30° of latitude.** Poleward-moving air enters a low-AAM world.

**Practice Q2 — why an AM-conserving Hadley cell is unphysical.**
Parcel leaves equator at rest (u=0), moves to 30°N conserving M. Arrival wind?
→ `Ω a² = Ω a² cos²30 + u a cos30` ⇒ `u = Ω a (sin²30 / cos30) = 465 × (0.25/0.866)`
→ **u ≈ 134 m/s** — ~3× any observed subtropical jet (~40–50 m/s). Lesson: the real
Hadley cell CANNOT conserve AAM; friction + eddies must bleed it out. This is the "leak"
of [C2], quantified.

**Practice Q3 — the wind term is small, but its sign runs everything.**
At 10°N a trade wind blows u = −7 m/s (easterly). Relative vs planetary AAM?
→ Lever arm `a cos10 = 6.27×10⁶`. Relative AAM `= −7 × 6.27×10⁶ = −4.4×10⁷`.
→ Planetary AAM `= 2.96×10⁹ × cos²10 = 2.87×10⁹`. Ratio ≈ **1.5%.**
→ The trade wind is ~1% of total AAM — but its *sign* is exactly what surface friction
exchanges with the Earth, and exactly what the easterly-necessity argument hinges on.

### [C2] — AAM leak & trade-wind necessity (the passage in §1/§2)

The passage is a **budget (torque-balance) argument, not a force balance.** It does NOT
say the pressure gradient drives the trades. It tracks the *stock* of AAM in the
equatorial belt and asks what keeps it steady. Four steps:

1. **The leak.** While air is "sealed in its own plane" (purely zonal, no N–S motion),
   AAM stays put. The Hadley cell breaks that seal: rising equatorial air moves poleward
   aloft and carries its AAM out of the belt. The belt continuously bleeds AAM poleward.
2. **Steady state demands a refill.** The trades don't accelerate or decay year over year,
   so the belt is ~steady. If AAM leaves poleward and the total doesn't drop, something
   must replace it. The only candidate is the surface torque via friction. (A pressure
   gradient pushes air around but cannot be a NET source of AAM about the axis — only a
   surface torque can.)
3. **Friction's sign rule.** Friction opposes the *relative* wind, so the AAM it delivers
   depends on wind direction:
   - surface wind blows **west** (easterly trade) → friction drags air **east** → *adds*
     eastward AAM ✓
   - surface wind blows **east** (westerly) → friction drags air **west** → *removes* it ✗
4. **Therefore easterlies.** Only a westward (easterly) surface wind gives a friction
   torque of the right sign to refill the poleward leak. So the tropics MUST have surface
   easterlies to stay in balance — from the AAM budget alone, no pressure gradient needed.
   That is what "rotational necessity, independent of the pressure gradient" means.

**Payoff for the notebook:** this is exactly why NB1 keeps the *thermal cell* (driven by
∂p/∂x) conceptually separate from the *easterly overlay* (demanded by the AAM budget). A
surface-pressure diagnostic sees the first cleanly but can be blind to the second — the
conflation the four traps warn against.

*(Claude produced an annotated 2-panel figure for this — budget on top, friction sign
rule on bottom. Not embeddable here; regenerate on request.)*

### [C3] — Is the "Scenario A coincidence" claim confirmed in the literature?

The claim splits into parts sitting on very different footing. VERIFICATION VERDICT:

- **"Coincidence is a structural feature of Scenario A"** → TRUE **by construction** of the
  tanh model (gradient max anchored at x₀ by the antisymmetric SO term; node sits at x₀
  only when global_offset = 0). Not an empirical finding — definitional. Frame it that way;
  cite no one.

- **"Coincidence is observed in cold-regime transitions"** → **cite Bjerknes (1969)
  directly.** In his four-map passage he notes the zero isallobar near the dateline AND
  states that at that same longitude the maximum westward pressure gradient (and,
  "presumably," the maximum easterlies) were observed in Jan 1963/65/67. That IS Scenario A,
  observed. His hedge word "presumably" ties neatly to the §3 caveat about *inferring*
  winds from gradients rather than measuring them.

- **"Coincidence is empirically rare because natural transitions involve basin-wide
  offsets that displace the node"** → **could NOT be traced to an external study.** The
  ingredients are established (SO as a mass see-saw; basin-wide pressure shifts), but the
  specific framing — a global_offset parameter sliding the node off the gradient max,
  giving a closed 4-regime taxonomy — appears to be **the notebook's own synthesis.**
  ACTION: mark as the notebook's hypothesis, not an established finding; soften any wording
  implying otherwise, unless a source is later found.

**Generative note:** the node-vs-gradient-max separation as a *diagnosable regime* isn't
something found in the literature search. Closest established work is ENSO diversity/flavors
(CP vs EP El Niño — Kao & Yu 2009, Kug et al. 2009, Capotondi et al. 2015), which partitions
events by *where the SST anomaly sits*, not by node/gradient coincidence. If the
decomposition maps onto that literature → that's the bridge. If not → that's the gap worth
writing about.

---

### [G] Generative Questions — Session 2

**[G1] — Node-error thought experiment + the "could it overestimate?" flip.**

Model: `p(x) = C − A·tanh((x−x₀)/w)` ⇒ `|∂p/∂x| = (A/w)·sech²((x−x₀)/w)`.
`sech²` = 1 at x₀, strictly decreasing away from it in BOTH directions. The gradient max
is a single symmetric peak at x₀.

- **Within the model, underestimate-only is a THEOREM.** Sampling |∂p/∂x| at any x ≠ x₀
  (which a displaced node forces) returns a value below the peak. C (east) and D (west)
  both land on the falling flank. You cannot overestimate the peak by sampling off it —
  tautological (the peak is the max).
- **Worked number.** Peak 0.45 hPa/°lon at 178°E; 12° displacement (C: 170°W, D: 166°E);
  width w ≈ 36°: `sech²(12/36) = sech²(0.333) ≈ 0.90` → 0.45 × 0.90 ≈ 0.40 hPa/°lon =
  ~10% underestimate. Lands inside the notebook's stated "5–15%".
- **Coupling caught (for Phase 3.5):** the "5–15%" figure IMPLIES a broad front (w≈36°).
  A narrower tongue → much larger underestimate. The error-budget % and the width
  assumption are not independent and shouldn't be tuned separately.

**The flip answer (the important part):** "always underestimate, symmetric in C and D" is
NOT a general truth — it's an artifact of two assumptions:
  1. *Single symmetric peak* (one antisymmetric tanh) → C and D err by EQUAL amounts. Real
     cold-tongue fronts are asymmetric (steeper east flank), so real C vs D would bias by
     DIFFERENT magnitudes — directional in size, not just sign. (Postable nuance.)
  2. *Location error alone* → overestimation BECOMES possible once you compound the node
     error with a WIDTH error (the §8.5 compounding). If the diagnostician also assumes a
     narrower w' < w, their modeled (A/w')·sech²(·) can EXCEED the true peak (A/w).
→ Threads-worthy framing: the DIRECTION of the diagnostic bias is a modeling artifact,
  not a law. It holds only under a symmetric-front, location-only assumption — and real
  fronts satisfy neither.

*(Claude produced a sech² curve figure marking peak 178°E and nodes C/D both at ~0.90×peak.
Not embeddable in markdown; regenerate on request.)*

**[G2] — Provenance of `X0_COLD = 178°E`.**

NOT because 178°E is the Figure 6 value (coincidence). It is ≈ the MEAN of Bjerknes's four
observed zero-isallobar crossings:
  175°E → 175 · 170°W → 190 · 168°E → 168 · 178°E → 178
  mean = 711 / 4 = **177.75°E ≈ 178°E** = Bjerknes's "a little west of the dateline on the
  average."
→ Defensible as the average of his four maps (stronger than picking one figure). The
  notebook currently prints `canonical cold-year node / gradient-max longitude` with NO
  explanation → see Pending Edit #3.

**[G3] — Why gradient MAGNITUDE → wind speed is only approximate (3 examples).**

Anchor: |∂p/∂x| = 0.45 hPa/°lon = 4.04×10⁻⁴ Pa/m, ρ ≈ 1.2 kg/m³.

- **Ex1 — geostrophic map diverges at the equator.** U ~ |∂p/∂x|/(ρf), f = 2Ω sinφ.
  10°→13 m/s, 5°→27, 2°→66, 1°→132, 0°→∞. One fixed gradient implies wildly different
  winds as f→0; on the equator geostrophy gives no usable number. Need a different balance.
- **Ex2 — friction balance introduces a free parameter (boundary layer).**
  r·u = −(1/ρ)∂p/∂x ⇒ u = −(1/ρr)∂p/∂x, r = drag rate (a BL property, not in the pressure
  field). τ=1 day → u≈29 m/s; τ=2 days → u≈58 m/s. Same gradient, ×2 spread. Both far above
  observed trades (~5–8 m/s); matching 7 m/s needs τ≈6 h. → local pressure+drag can't pin
  the wind without independent BL/drag knowledge.
- **Ex3 — absolute wind needs the AAM budget.** u_obs = u_thermal (from ∂p/∂x) + u_overlay
  (from AAM budget). Illustratively −7 = −4 (thermal) + −3 (overlay). Gradient constrains
  only u_thermal; the split is set by the global AAM balance ([C2]), absent from the local
  field. So even a perfect gradient underdetermines the wind.

**Payoff:** all three failures are about MAGNITUDE. §4–7 diagnose regimes from LOCATIONS
(node position, gradient-peak position) — geometric, invariant to f, r, BL, AAM split. So
the magnitude ambiguity does NOT touch the notebook's conclusions. Caveat correctly scoped.
**Phase 3.5: this VALIDATES the existing §3 caveat — no new pending edit. Queue stays at 3.**

**[G] TIER COMPLETE.** Remaining for NB1 Phase A: [S] structural questions (S1–S9, edit-
adjacent → pair with the Phase 4 session), then Phase 5–6 exam + fault map.

---

## Pending Edits — Phase 4 queue
> Identified during Phase A comprehension. NOT YET APPLIED. Notebook untouched until an
> edit-scoped (Phase 4) session. One change per cell.

1. **Soften "empirically rare" claim** (from [C3]). The framing that natural transitions
   displace the node via a basin-wide offset is the notebook's OWN hypothesis, not an
   established finding. Reword so it doesn't read as cited/confirmed.
2. **Add Bjerknes (1969) citation** at the cold-year node/gradient-max coincidence claim
   (from [C3]). His four-map dateline passage is the direct source for "coincidence
   observed in cold regimes."
3. **Add provenance note for `X0_COLD = 178°E`** (from [G2]). One line: four crossings
   (175°E, 170°W, 168°E, 178°E) → mean 177.75°E ≈ 178°E → Bjerknes "a little west of the
   dateline on the average." Attach near the code cell that prints the label.

---

## Phase 5–6: Exam & Fault Map

**Status:** Exam taken closed-book. Three bolts flagged for re-exposure. Re-check pending
(next session, before moving to [S]/Phase 4).

### Questions
- Q1 (conceptual): Why are equatorial easterlies a *rotational necessity* — name what leaks,
  what refills, the sign rule; and what breaks if surface winds were westerly.
- Q2 (trap): Is the node-sampling gradient bias direction-dependent? Under what condition
  could a diagnostician *overestimate* the peak — location error or something else?
- Q3 (structural): Why does the trade-wind-necessity argument belong in NB1 (zonal), not
  NB2 (meridional), given the AAM export is the hand-off to NB2?

### Self-assessment (closed-book result)
- Q1: recalled the skeleton (leak → friction refill; rotation + equatorial geometry as
  source). Lost the sign rule ("is that to do with perspectives?" — no). Felt un-internalised.
- Q2: correctly said bias is NOT direction-dependent. Forgot the overestimate condition.
- Q3: blank ("so confused").

### Fault map
- **Q1 — PARTIAL.** LANDED: leak/refill scaffold + rotational/geometric origin. NEEDS
  RE-EXPOSURE: the friction SIGN rule. AXIS/LABEL ERROR: fused two separate C2 ideas —
  the *frame story* (inertial-vs-Earth; explains the LEAK) vs the *sign rule* (friction
  opposes relative wind; explains the REFILL). The "perspectives" instinct belongs to the
  leak, NOT the refill.
- **Q2 — CORE LANDED.** "Not direction-dependent → always underestimate" is correct. NEEDS
  RE-EXPOSURE: overestimate = a WIDTH error (assume w' < w), NOT a location error. Pure
  location error can never beat the max.
- **Q3 — NOT LANDED.** Axis-ownership framing absent. Priority re-exposure (axis discipline
  is a core principle elsewhere).

### Re-exposure notes (the three bolts)
1. **Friction sign rule.** Friction drags air toward the ground's motion (ground moves
   east). Air blowing WEST (easterly) → dragged EAST → ADDS eastward AAM ✓. Air blowing
   EAST (westerly) → dragged WEST → REMOVES it ✗. Belt bleeds eastward AAM poleward, so it
   must gain from below → only an easterly opens the valve. Hook: "the refill valve only
   opens when the wind blows west." If westerly: friction drains, no steady state
   (mid-latitudes have westerlies precisely because eddies IMPORT momentum there — mirror
   image).
2. **Overestimate condition.** Can't sample above the peak (tautology). To overestimate,
   MISCOMPUTE with a narrower front w' < w so (A/w')·sech² > true (A/w). Hook: "can't
   sample above the peak, but can miscompute above it." → width error, not location.
3. **Axis ownership (NB1 vs NB2).** Trade wind = a ZONAL surface wind → "why easterly?" is
   a ∂p/∂x question → NB1 owns it. The momentum it supplies travels POLEWARD → ∂p/∂φ → NB2
   owns that. AAM budget spans both but SPLITS at the axis: origin zonal (NB1), destination
   meridional (NB2). Hook: "born zonal (NB1); momentum dies poleward (NB2)." This is why
   C2 called the AAM export "the literal hand-off to NB2" — the hand-off IS the axis boundary.

### Re-check plan
Next session: re-attempt Q1 (sign rule in one sentence) + Q3 (axis ownership) closed-book.
If both land → comprehension locked → proceed to [S] structural decisions + Phase 4 edits.

---

## Re-check (Session 2b) — outcome
- **Q2 axis ownership: LOCKED.** Went from blank to correct + confident; hook applied
  ("born zonal NB1, momentum dies poleward NB2").
- **Q1 sign rule: NOT locked (standing re-exposure).** The *leak* is now solid (momentum
  leaks poleward as the lever arm a·cosφ shrinks). But the *easterly* is still reached by
  the wrong route — "air is sucked in / conservation of momentum." That's a MERIDIONAL
  (continuity/return-flow) explanation for a ZONAL question. Suction explains the
  *equatorward* surface flow; it does NOT explain *easterly*. The easterly needs the
  friction sign rule. Residual gap is now narrow + named (suction ≠ friction; meridional ≠
  zonal). Re-surface once, cold, in a later session. NOT a blocker for [S].

---

## Phase A [S] — Structural Decisions (verified against uploaded NB1, 53 cells)
Meta-point: most "is this repetitive?" worries are SPIRAL (same idea at rising rigor =
good), not FLAT (same level, nothing new = cut). Only cut flat.

- **S1** (cell 0, "several like it" vague) → optional minor tighten. Low priority.
- **S2** (cell 0, thermal-cell vs easterly-overlay) → NOT redundant with S1's node/gradient
  pair; it's a DIFFERENT duality. Déjà-vu is rhythm, not content. Fix = add a one-line
  signpost. Do NOT merge. [Pass 2]
- **S3** (four-traps flow / separate doc?) → LEAVE AS IS. Logical arc; traps are load-
  bearing onboarding. Your instinct was right.
- **S4** (cell 0 bare "Sadler's observation") → structural: drop the dangling attribution
  (full cited version already in §7). [Pass 2]  +  content/verify: the Sadler citation
  itself is BLOCKED (see Verification).
- **S5** (145°W) → content/verify, BLOCKED (see Verification).
- **S6** (cell 1 CAT vs cell 0 downstream chain) → mild real overlap. Fix = back-reference
  the chain, don't restate it. [Pass 2]
- **S7** (cell 2 Diagnostic Duality) → LEAVE AS IS. Formal delivery of cell 0's narrative =
  spiral. Your guess was right.
- **S8** (`w` introduced §3) → LEAVE AS IS. §3 (at the model equation) is the correct home.
- **S9** (cell 4 "Two diagnostic results") → **REVERSED after seeing exact text: KEEP.**
  Item 1 carries the linchpin fact (gradient max at x₀ *regardless of* global_offset),
  stated here first in model-specific terms. Not flat redundancy.

---

## Phase 3.5 Verification — findings
- **Bjerknes 1969 PDF = scanned image, no text layer** (9 chars extractable). Machine
  verification impossible. Four zero-isallobar crossings grounded in the RESEARCHER'S OWN
  transcription: 175°E (Fig 3), 170°W (Fig 4), 168°E (Fig 5), 178°E (Fig 6), "a little west
  of the dateline on the average." Mean (170°W→190°E): (175+190+168+178)/4 = 177.75°E ≈
  178°E. → X0_COLD provenance: **GO** (text-sourced).
- **Sadler (1959): BLOCKED — citation integrity issue.** Web search finds Sadler's relevant
  equatorial upper-trop westerlies work in the 1960s–70s (e.g. "westerly flow east of 170°W
  in the absence of a ridge"), NOT a 1959 paper. "1959" may be a date error. ALSO: "Sadler"
  is absent from the References cell (51) despite 3 in-body cites. ALSO: notebook says "east
  of ~150°E"; sources say "east of ~170°W" — check that discrepancy. ACTION: trace to the
  actual Sadler paper before trusting; do NOT add a References entry until confirmed.
- **145°W / 1957–58 westerlies: BLOCKED.** Cannot verify from scanned PDF. ACTION: locate
  the exact Bjerknes figure/page, or soften.
- **Bjerknes coincidence citation: CLOSED (no edit).** Cell 1 already opens "In his landmark
  1969 paper..." — pending-edit #2 already satisfied.

---

## Phase 4 Edit Guide (old→new)   ◆ supersedes the earlier 3-item queue ◆
Discipline: PASS 1 (content) and PASS 2 (structural) are SEPARATE sessions. One change per
cell at a time; Restart & Run All at the end of each pass. Cell 0 gets two structural edits
— apply sequentially.

### PASS 1 — CONTENT
**[P1-a] Cell 1 — soften "empirically rare" to hypothesis.**
OLD: `but empirically rare because natural transitions involve basin-wide pressure changes.`
NEW: `This notebook further *hypothesises* that the coincidence is empirically uncommon — on the grounds that natural transitions typically involve basin-wide pressure changes — but that rarity is the notebook's own working conjecture, not an established observational result.`

**[P1-b] Cell 5 — correct X0_COLD provenance (text-sourced, not "needs digitizing"). TWO spots in the same cell = one coherent edit.**
Spot 1 — the "Source" subsection:
OLD (heading + last paragraph):
`### The Source (Stated, Not Yet Verified)`
… through …
`The text suggests these four change maps have zero isallobars that cluster near the dateline. The notebook currently assumes their mean sits at approximately **178°E**, but this value has **not been digitized or independently verified** from the figures.`
NEW:
`### The Source (Stated in Bjerknes's Text)`
… (keep the Fig 2 / Figs 3–6 bullet list unchanged) …
`Crucially, Bjerknes's **prose reports the equatorial zero-isallobar crossing for each map directly** — 175°E (Fig. 3), 170°W (Fig. 4), 168°E (Fig. 5), 178°E (Fig. 6) — summarised as *"a little west of the dateline on the average."* Taking 170°W as 190°E, the four average to **177.75°E ≈ 178°E**, which is the basis for X0_COLD. The anchor therefore rests on Bjerknes's *reported values*, not on figure digitization.`
Spot 2 — soften the two later lines that still say "unverified / must digitize":
OLD: `- The value is approximately correct based on Bjerknes's discussion of the dateline clustering, but not precisely verified`
NEW: `- The central value is text-sourced (mean of Bjerknes's four reported crossings, 177.75°E); digitizing the figures would refine per-year spread but is not needed for the central value`
OLD: `**Next step for readers who want to harden this work:** Digitize Bjerknes Figures 3–6 and report back the four isallobar longitudes and their mean. This is a concrete, finite task that will ground the entire notebook on verified data.`
NEW: `**Next step for readers who want to harden this work:** Digitize Bjerknes Figures 3–6 to quantify the per-year spread around the text-reported mean (177.75°E) and attach an uncertainty band to X0_COLD.`

**[P1-c] Bjerknes coincidence citation — NO EDIT (already satisfied, cell 1).**
**[P1-d] Sadler (1959) reference — BLOCKED. Verify first (see Verification). Do not draft.**
**[P1-e] 145°W (cell 0 Trap 3) — BLOCKED. Verify or soften (see Verification).**

### PASS 2 — STRUCTURAL
**[P2-a] Cell 0 (edit 1/2) — S2 signpost.**
OLD: `The Walker circulation is not one east–west loop but two circulations in one:`
NEW: `A second, physically distinct pairing sits beneath that diagnostic one. The Walker circulation is not one east–west loop but two circulations in one:`

**[P2-b] Cell 0 (edit 2/2) — S4 drop dangling attribution.**
OLD: `where the loop's eastward return finally overpowers it — Sadler's observation.)`
NEW: `where the loop's eastward return finally overpowers it.)`

**[P2-c] Cell 1 — S6 back-reference.**
OLD: `errors propagate silently through the entire risk model.`
NEW: `errors propagate silently through the entire risk model (the physical cascade is the downstream chain traced above).`

**[S9] — REVERSED: keep, no edit.**  **[S1] — optional minor, defer.**

### Leave-as-is: S3, S7, S8.

---

## Phase 3.5 Verification — UPDATE (OCR of Bjerknes 1969)
The scanned Bjerknes PDF was OCR'd (tesseract, ~38k chars). All three items resolved:

- **Four isallobar crossings — MACHINE-CONFIRMED.** Bjerknes (p.164) states verbatim: the
  zero isallobar crosses at 175°E (Fig 3), 170°W (Fig 4), 168°E (Fig 5), 178°E (Fig 6),
  "a little west of the dateline on the average," and *at that longitude the maximum westward
  pressure gradient* was also observed. → X0_COLD provenance verified; node–gradient
  COINCIDENCE is Bjerknes's own stated observation (pending-edit #2 fully satisfied).
- **Sadler (1959) — CONFIRMED REAL (earlier "fabrication" suspicion was wrong).** Found in
  Bjerknes's own reference list AND quoted by him: upper-tropospheric flow reverses near 150°,
  westerly band ~150°E to beyond 160°W. So the notebook's "~150°E" is CORRECT; the earlier
  "150°E vs 170°W mismatch" was a false alarm (170°W came from a *different*, 1975 Sadler
  report). Full ref: Sadler, J.C. (1959), Proc. 9th Pacific Science Congress (Bangkok 1957),
  Vol. 13, pp. 6–11.
- **145°W — CONFIRMED, with precise facts.** Bjerknes (~p.170): westerly surface winds
  *occasionally* observed at 145°W on the Equator in *November 1957*, attributed to *Austin
  (1960)* — used to argue the Walker circulation had "stopped." Notebook wording should add
  "occasionally / November 1957 / (Bjerknes 1969, citing Austin 1960)."

## Phase 4 Edit Guide — UNBLOCKED ITEMS (revised)
**[P1-d → READY] Add Sadler reference to cell 51.** Insert new subsection:
`### Observational Basis (Equatorial Winds)`
`- Sadler, J. C. (1959). Wind Regimes of the Troposphere and Low Stratosphere over the Equatorial and Sub-Equatorial Central Pacific. *Proceedings of the 9th Pacific Science Congress* (Bangkok, 1957), Vol. 13, pp. 6–11. *(Upper-tropospheric equatorial wind reversal near 150°E; quoted in Bjerknes 1969, used in §7.)*`
In-body Sadler cites (cells 13, 15): KEEP as-is. "~150°E": KEEP (verified correct).

**[P1-e → READY] Cell 0 Trap 3 — precise wording + attribution.**
OLD: `Surface *westerlies* were then measured at 145°W, where trades should blow.`
NEW: `Westerly surface winds were *occasionally* observed at 145°W on the Equator in November 1957 (Bjerknes 1969, citing Austin 1960) — where trades should blow.`

**[P1-b → READY, strengthened] Cell 5 X0_COLD — now text-verified.**
OLD heading: `### The Source (Stated, Not Yet Verified)`
NEW heading: `### The Source (Stated in Bjerknes's Text — verified)`
OLD: `The text suggests these four change maps have zero isallobars that cluster near the dateline. The notebook currently assumes their mean sits at approximately **178°E**, but this value has **not been digitized or independently verified** from the figures.`
NEW: `Bjerknes's prose reports each map's equatorial zero-isallobar crossing directly — 175°E (Fig. 3), 170°W (Fig. 4), 168°E (Fig. 5), 178°E (Fig. 6), "a little west of the dateline on the average." Taking 170°W as 190°E, the four average to **177.75°E ≈ 178°E** — the basis for X0_COLD. Bjerknes further notes that at that longitude the maximum westward pressure gradient (and, he presumes, the maximum easterlies) were observed, so the node–gradient coincidence is his own stated observation, not our inference.`
Also soften later in cell 5:
OLD: `- The value is approximately correct based on Bjerknes's discussion of the dateline clustering, but not precisely verified`
NEW: `- The central value is text-verified (mean of Bjerknes's four reported crossings, 177.75°E); digitizing the figures would only refine the per-year spread`
OLD: `**Next step for readers who want to harden this work:** Digitize Bjerknes Figures 3–6 and report back the four isallobar longitudes and their mean. This is a concrete, finite task that will ground the entire notebook on verified data.`
NEW: `**Next step for readers who want to harden this work:** Digitize Bjerknes Figures 3–6 to attach a per-year uncertainty band to the text-reported mean (177.75°E).`

## EDIT STATUS (as of this session)
Applied by user: P1-a ✅, P2-a ✅, P2-b ✅, P2-c ✅.
Still to apply: P1-b (cell 5, strengthened), P1-d (Sadler ref, cell 51), P1-e (145°W, cell 0).
No blocked items remain. Then Restart & Run All.
