# Revision Note — NB1 Comprehension Exam (Session: §13.2 Discussion, §15 Conclusion, X0_COLD/AAM foundations)

## Purpose
Self-assessment record of the Phase 5 exam on this session's content. Captures what I answered, what landed, what didn't, and the correct full answers — so the gaps are traceable and re-testable next session.

---

## Overarching pattern (read this first)
Across Q1 and Q3, the same failure shape appeared: **I produced the correct ingredients, then stalled at the assembly step and declared myself lost.** This is not a knowledge gap — it's an *assembly/confidence* gap. The fix is one move each time: "west is the mirror of east" (Q1), "role is what the parts do together" (Q3). Re-drill assembly, not content.

Also confirmed: **refusing to answer on papers I haven't read (Q2) is correct discipline, not failure.** Keep that instinct — it's the same one that caught a fabricated reference earlier in the project.

---

## Q1 — Conceptual: EP/CP flavors = the node-displacement problem

**What I got right (~6/10):**
- EP = cold tongue pinned east, at the South American coast ✓
- Node = the pivot of the see-saw ✓
- Node = where gradient-max sits *and* where pressure stops changing along the equator ✓ (the hard identity, produced from memory)

**Where I stalled:**
- Didn't complete the mirror: CP anomaly sits near the dateline = displaced **west**.
- Never mapped EP/CP → Scenario C/D.
- First instinct reached for "teleconnections / worldwide impact" — that's NB2 (meridional) territory; the question was strictly zonal. **Axis slip.**

**Full correct answer:**
El Niño has two spatial flavors — EP (warm anomaly east, near the South American coast) and CP (warm anomaly near the dateline, i.e. west of EP). The equatorial pressure field is a zonal see-saw whose **node** is simultaneously (a) where pressure stops changing along the equator and (b) where the gradient is steepest. Because the pressure structure tracks the SST anomaly, moving the anomaly east/west moves the whole pattern, node included:
- **EP** → anomaly east → node east → **Scenario C**
- **CP** → anomaly west → node west → **Scenario D**

The idealized decomposition dials this displacement in by hand (`global_offset`); the observational community found the same degree of freedom in the real ocean and called it "ENSO diversity." Scenarios C/D are the skeleton; EP/CP are the flesh. Both make one point: a scalar index reporting only *how strong* El Niño is stays blind to *where* it is — and where it sits changes everything downstream. ("A scalar is not a state," modern-observing-era version.)

**Caveat for posting:** EP↔C / CP↔D is an analogy of *structure*, not a claim that real events differ *only* in east-west position — nature also varies amplitude, duration, coupling. The idealized regimes isolate the displacement degree of freedom; reality varies several at once.

---

## Q2 — Trap: "Walker strengthening corrects Vecchi weakening"

**What I answered:** Couldn't — hadn't read either paper.
**Assessment:** Full credit on epistemics (honest refusal), incomplete on content. Note: this was a *reasoning* question answerable from the §13.2 text, and partly a test of my writing's clarity — so the miss is shared.

**The false reading:** *"Walker is strengthening — L'Heureux (2013) showed it across ten datasets, correcting the older Vecchi (2006) weakening result."*

**Three errors:**
1. **Timescale conflation (main error):** Vecchi (2006) = century-scale, greenhouse-forced weakening (model + long SLP reconstruction). L'Heureux (2013) = recent multidecadal *observed* strengthening. Different windows — a short-term strengthening can ride on a long-term weakening. Both true at once.
2. **"Corrects" is wrong:** L'Heureux doesn't overturn Vecchi. They sit in a recognized, unresolved tension (there's literature on *reconciling* the opposing trends). Open problem, not settled correction.
3. **"It's settled" is wrong:** The *sign* of the Walker trend is not agreed across observations vs. models (obs show strengthening; models predict weakening). That disagreement is the point — a real-world instance of "the diagnostic choice *is* the science."

**Caveat for posting:** If citing the "reconciling opposing trends" literature, verify the specific reference first (Chung et al. 2019 surfaced but was not fully verified). Same rule that caught the earlier bad citation.

---

## Q3 — Structural: why AAM (not SST) is the NB1→NB2 boundary

**What I answered (~2/10 on the answer):** "Angular momentum budget covers the Coriolis force, movement of trade winds, friction from Earth's rotation." Then conflated X0_COLD (178°E) with the AAM hand-off.

**Why it missed:** I described what AAM *is* (its components) instead of what *job* it does at the boundary (its role). Also merged two unrelated things — 178°E is a *longitude on the zonal axis*; the AAM hand-off is a *quantity crossing to the meridional axis*. They were sitting in the same fuzzy mental bin.

**Full correct answer:**
Each notebook owns one gradient axis:
- **NB1 (Walker):** zonal axis — every gradient is **∂p/∂x** (east–west).
- **NB2 (Hadley):** meridional axis — every gradient is **∂p/∂φ** (north–south).

Draw the boundary at the quantity that **crosses between axes** — that's **AAM**. The equatorial zonal cell **cannot close its own angular-momentum budget**: equatorial air is AAM-rich, so AAM must be exported poleward. It's generated/consumed in the zonal (∂p/∂x) system but **discharged along the meridional (∂p/∂φ) system** — it literally travels from NB1's world to NB2's. That crossing *is* the hand-off.

Why "SST drives both, so it's one story" is the wrong boundary: SST is a **shared cause**, not a hand-off. It sits *underneath* both circulations and forces both, but doesn't *cross* from zonal to meridional. It marks a common origin, not a seam.

**One-liner:** *SST is the shared root; AAM is the bridge. Draw the boundary at the bridge, not the root.*

---

## Fault map (for next session's re-test)

| Concept | Status | Action |
|---|---|---|
| Node = pivot = gradient-max = zero-change identity | **landed** (unprompted) | none |
| EP/CP geography (EP=east/coast) | **landed** | none |
| EP/CP → Scenario C/D mapping | **one step short** (missed CP=west=D) | re-test |
| Walker trend: timescales + unresolved | **supplied, not self-produced** | re-test cold |
| AAM's *role* (hand-off) vs *parts* (Coriolis/friction) | **needs re-exposure** | re-drill, framed as role |
| X0_COLD (178°E) vs AAM hand-off — keep distinct | **conflated once** | watch |
| Epistemic honesty (won't answer on unread papers) | **strong** | keep |

## Flag for a future *content* session (logged, not fixed — one-thing-per-session rule)
- §13.2's Walker-trend sentence may not make the "unresolved, not corrected" point clearly enough. Re-read for clarity when a content session is scoped. (Do not fix mid-structural or mid-exam.)

---

## Phase 7 Insight — captured

**The Walker-trend timescale lesson:** When two scientific results seem to contradict (Walker weakening vs. strengthening), check the timescale — Vecchi (2006) describes a century-scale greenhouse-forced weakening from models and long reconstructions, while L'Heureux (2013) observes a recent multidecadal strengthening across datasets. Both are true because they're measured over different windows, and the observation-model disagreement is the real science, not a settled correction.

---

*End of revision note — 2026-07-03*
