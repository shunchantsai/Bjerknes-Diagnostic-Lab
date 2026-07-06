# Phase A: NB2 Deep Read & Comprehension

**Session Anchor:**
This session is about: Understanding NB2's content deeply — the meridional ENSO → Hadley → jet teleconnection.
Session TYPE: **CONTENT** (reading + comprehension, no editing yet)

**Date:** 2026-07-05

**Scope lock (from the NB2 workflow, Phase 0):** CONTENT only. Structural problems are logged to
DEFERRED, not fixed. Physics fixes are `teleconnection_physics.py` edits (+ test), logged for an EDIT session.

### Taxonomy & heading grammar  *(so any future session doc is self-explaining)*

This project nests on **four levels**. The word "Phase" is used on two of them — the **letter** is the
*campaign*, the **number** is the *step* — so this key disambiguates:

| Level | What it is | This doc |
|---|---|---|
| **Campaign** (letter) | the arc across a notebook | **Phase A** |
| **Notebook** | which notebook | **NB2** |
| **Session** | one scoped sitting (CONTENT *or* STRUCTURAL, never both) | **Session 1** |
| **Workflow Phase** (number) | the step within a session (0–8) | currently **Phase 1** |
| **Tags** (within a Phase) | the item labels | `[C]` `[G]` `[S]` → `[G1]`, `[S2]`, … |

**Campaigns (the letters):**
- **Phase A — Deep Read & Comprehension** *(you are here)*: read cold, inventory questions, verify, edit for understanding, exam.
- **Phase B — Revision & Hardening**: apply outstanding edits, clear every BLOCKED item, tighten prose/structure, re-verify.
- **Phase C — Publication & Portfolio**: final polish, README / figures / citations, outreach.

**Heading grammar (within a session doc):**
- `## Phase 0 — Anchor` · `## Phase 1: Deep Read` → inventory as `### [C] Clarifying`, `### [G] Generative`, `### [S] Structural`
- `## Phase 2–3: Claude Assessment & Answers` → per-item verdicts `### [G1] …`, `### [G2] …`, `### [S1] …`, `### [S2] …`, plus `### Additional Phase 3 findings`
- `## Phase 3.5 Verification — Sources checked`
- `## Phase 4 Edit Guide — PASS 1 (CONTENT only)` → edits as `**[P1-a] …**` with OLD/NEW blocks
- `## Structural findings — DEFERRED` · `## Physics/module findings — DEFERRED` · `## EDIT STATUS`

**You are here: Phase A · NB2 · Session 1 — COMPLETE.**

**Session tracker:**
- [x] Phase 0 Anchor · Phase 1 Deep Read + full inventory
- [x] Phase 2–3 Assessment — [G1][G2][S1][S2] + [C] comprehension (via tutoring)
- [x] Phase 3.5 Verify — [G1] confirmed; BLOCKED logged (±5–15 hPa, Bjerknes quote)
- [x] Phase 4 CONTENT — P1-a/b/c/d/e applied + committed
- [x] Phase 5 Exam → Phase 6 Fault map (ψ≠pressure, meridional axis — corrected, re-tested, landed)
- [x] Phase 7 Capture (see below)
- [x] Phase 8 — commit this doc to `revision_notes/`

**→ NEXT SESSION: Phase A · NB2 · Session 2 (STRUCTURAL)** — relocate the anomaly / meridional-axis explanation to the Scenario-B figure + force panel; consolidate "structure beats magnitude" (cells 0, 7, 14) to ≤2; reorder cell 14's off-equator subtitle out of §5. *Content is present; the problem is placement.*

---

## Phase 1: Deep Read — Questions Inventory  *(reading in progress — §1–§5 done; §6–§10 pending)*

### [C] Clarifying Questions
*(Questions where I don't understand a mechanism — fill in as you read §6–§10)*

1.
2.
3.

### [G] Generative Questions

1. **[G1]** Cell 6: *"Standard ENSO diagnostics track a single pressure-based index and rarely separate the temporal node … from the spatial peak."* Is this true? My instinct says the literature would discuss it if so, but I haven't seen it made clear. Assess.
2. **[G2]** Cell 6: *"…asks a question the index-based framing tends to collapse: is the coincidence of node and gradient maximum structural, or regime-dependent? Is it a thermodynamic inevitability…?"* Am I reading this right (that the index framing is too limiting)? It feels sophisticated but dense — what do I do with it?

### [S] Structural Questions  *(→ route to DEFERRED this session)*

1. **[S1]** Many sections (§2 domain, Z_MID/H_CELL/SCALE_P, "Why this framing is worth foregrounding", §3 scenarios, §4 generators…) keep re-making similar points. I want it clear and succinct — Nature-like, but pedagogical.
2. **[S2]** §5's subtitle *"Why the equatorial ascent sits off the equator…"* presupposes figures the reader hasn't seen yet. Needs re-ordering later.

---

## Phase 2–3: Claude Assessment & Answers

> **Session scope:** CONTENT pass on §1–§6 (as far as read). Covered: [G1], [G2], and the CONTENT core of
> [S1]. [S2] and the *section-merge* half of [S1] are STRUCTURAL → DEFERRED. Two accuracy issues surfaced
> beyond the inventory (cell 5) — flagged.

### [G1] — "standard ENSO diagnostics track a single pressure-based index / rarely separate node from gradient"

Your instinct is right; the claim is inaccurate on two counts (see Phase 3.5 for sources):

1. The **standard operational ENSO index is SST-based** — Niño 3.4 / the Oceanic Niño Index — *not* pressure-based. The pressure-based Southern Oscillation Index (Tahiti−Darwin MSLP) exists and is widely used, but it is one atmospheric index among several, not "the" standard. "A single pressure-based index" mischaracterises the field.
2. The **node-vs-gradient-maximum (zero-isallobar) distinction is NB1's own diagnostic lens**, from Bjerknes's 1969 isallobaric maps. Mainstream ENSO indices don't operate in that framework at all, so it's misleading to say they "rarely separate" the two — there's no separation for them to collapse; they summarise the event as a scalar magnitude.

→ **VERDICT: rewrite.** Reframe honestly: operational indices reduce ENSO to a scalar *magnitude*; this atlas asks whether the downstream jet responds to *magnitude or structure*. (Folded into [P1-a].)

### [G2] — the dense "structural, or regime-dependent / thermodynamic inevitability" sentence

Your reading (that it argues the index framing is too limiting) is a fair reconstruction of dense prose — but the sentence's real problem is deeper than density: **it is NB1's question wearing NB2's clothes, and it contradicts your own cell 0.**

- **Internal contradiction.** Cell 0 states: *"Rather than tracking the equatorial node position, we instead ask: how much does this ENSO state strengthen or weaken the meridional overturning?"* Cell 6 then re-opens *"is the coincidence of node and gradient maximum structural, or regime-dependent?"* — the very node/gradient question cell 0 said NB2 sets aside.
- **Wrong mechanism label.** Per NB1, the node–gradient coincidence is *geometric/parametric* (it follows from the tanh profile's algebra and the `global_offset` parameter), **not** thermodynamic. Offering "thermodynamic inevitability" as one horn imports the wrong physics.

→ **VERDICT: don't just rephrase for density — re-scope cell 6 to NB2's actual question** (magnitude vs structure driving the meridional teleconnection). Removes both the contradiction and the mislabel. (Same [P1-a] rewrite — so [G1] and [G2] resolve together.)

### [S1] — sections re-make the same points (CONTENT core only; merges → DEFERRED)

Two genuinely CONTENT de-duplications (fixable in place, no cell moves):

1. The **"tuning knobs, not physical constants" caveat is stated twice** — cell 3 ("not physical constants… pedagogically clear") and cell 5 ("Key caveat upfront: tuning knobs…"). Cell 5 owns it in full (with the table); cell 3 should just point forward. → [P1-b].
2. The **"structure beats magnitude / B is the keystone" thesis is pre-stated three times** before §7 develops it — cell 0 (Scenario-B blockquote), cell 6 ("the central finding…"), cell 7 ("the takeaway lives in B"). The [P1-a] rewrite removes the cell-6 instance, leaving cell 0 (intro hook) + cell 7 (at the table) = your "at most twice." **No edit needed to cells 0/7** — fixing cell 6 resolves the thesis-repetition automatically.

The rest of [S1] — whether these sections should be *merged/consolidated* — is STRUCTURAL → DEFERRED with a map.

### [S2] — §5 subtitle presupposes figures; reorder later → STRUCTURAL, DEFERRED

Correct catch. Cell 14 ("Why the equatorial ascent sits *off* the equator…") is good physics but sits under §5 (the plotting function) *before any figure is drawn*, so it front-loads an interpretation of figures the reader hasn't met. The fix is a *reorder* (ordering = structural) → DEFERRED with a target. Interim CONTENT-only option offered in DEFERRED if you want something before the reorder.

### Additional Phase 3 findings (beyond your inventory — your call)

- **Cell 5 accuracy:** Z_MID = 7 km is described as "matching the real boundary-layer / free-troposphere transition." That transition is ~1–2 km; **7 km is mid-troposphere** (which the same table says). Mislabel → ready CONTENT fix [P1-c].
- **Cell 5 unverified number:** "Real ENSO anomalies are ±5–15 hPa; this scaling matches observations." Not sourced → BLOCKED pending verification.

**Phase 3 checklist result (§1–§6):** axis discipline ✓ · causal chain ✓ · prescribed-vs-derived ✓ (cell 13 is admirably explicit the jet is pinned by construction) · sign conventions ✓ · idealisation-knobs ✓ (well hedged) · keystone ✓ · **cross-NB coherence ✗ (cell 6 vs cell 0 — the main finding).**

---

## Phase 3.5 Verification — Sources checked

- [x] **[G1] "single pressure-based index" — REFUTED.** Operational standard is the SST-based Niño 3.4 / Oceanic Niño Index (adopted as the primary ENSO monitoring index); the pressure-based SOI (Tahiti−Darwin MSLP) is a secondary atmospheric index among several. Sources: NOAA Climate Data Guide, IRI, World Climate Service. → cell 6 claim inaccurate; rewrite (P1-a).
- [ ] **Cell 5 "ENSO anomalies ±5–15 hPa" — UNVERIFIED / BLOCKED.** Individual-station MSLP anomalies during strong ENSO are typically a few hPa; ±15 hPa looks high. Verify against a source, or soften / label illustrative, before it stays. Do NOT draft a replacement number until checked.
- [ ] **Cell 14 Bjerknes quote — VERIFY VERBATIM.** *"When the cold water belt along the Equator is well developed, the air above it will be too cold and heavy to join the ascending motion in the Hadley circulations."* Load-bearing quote — check word-for-word against the Bjerknes 1969 OCR you produced for NB1 before it stays.
- [x] **Cell 13 "Held–Hou" — REAL.** Held, I. M. & Hou, A. Y. (1980), *Nonlinear axially symmetric circulations in a nearly inviscid atmosphere*, J. Atmos. Sci., 37, 515–533. Genuine and correctly invoked. Consider adding the full ref to the notebook's reference list.
- [x] **Regression tripwire:** `python test_teleconnection_physics.py` → 10/10 (keystone B ≈ 0 green). No physics touched this session.

---

## Phase 4 Edit Guide — PASS 1 (CONTENT only)

**[P1-a] Cell 6 — rewrite (fixes [G1] inaccuracy + [G2] contradiction/mislabel; removes one redundant thesis restatement).**
OLD (heading + opening paragraph, through the A/B/C/D bullets and "central finding" line):
`## Why this framing is worth foregrounding`
`Standard ENSO diagnostics track a single pressure-based index and rarely separate the *temporal* node … from the *spatial* peak …. This notebook makes that separation explicit and asks a question the index-based framing tends to collapse: **is the coincidence of node and gradient maximum structural, or regime-dependent?** Is it a thermodynamic inevitability, or does it depend on the regime …?`
… (A/B/C/D bullets, where the A bullet reads "zero isallobar and gradient maximum align") …
NEW:
`## Why this framing is worth foregrounding`
`Operational ENSO indices reduce each event to a single scalar — the SST-based Niño 3.4 / Oceanic Niño Index, or the pressure-based Southern Oscillation Index. A scalar answers *how strong* an event is, not *how structured*: two states with the same peak anomaly can have very different meridional shapes. This atlas asks the question the scalar hides — **does the downstream winter jet respond to the magnitude of the SST anomaly, or to its meridional structure?**`
`The A/B/C/D design isolates exactly that:`
`- **A (Strong El Niño):** sharp meridional gradient → vigorous Hadley overturning → strong jet.`
`- **B (Basin-wide warm):** the warmest state (+2.5 °C) but *uniform* — no gradient, no driver, the teleconnection collapses.`
`- **C & D (La Niña):** sign-reversed, spatially displaced forcing → tests whether the response survives disrupted structure.`
`**The central finding: it is the gradient, not the magnitude, that drives the teleconnection.** The visualization is the proof.`

**[P1-b] Cell 3 — drop the duplicated tuning-knobs caveat (cell 5 owns it).**
OLD: `The following section defines three **tuning parameters** (Z_MID, H_CELL, SCALE_P) that shape the idealized pressure and Hadley fields. These are **not** physical constants — they are chosen to make the figures look pedagogically clear and roughly realistic. The display scales are frozen so the four scenarios can be compared by eye.`
NEW: `The next subsection defines the three shaping parameters (Z_MID, H_CELL, SCALE_P) and explains why they are held fixed. The display scales are frozen so the four scenarios can be compared by eye.`

**[P1-c] Cell 5 — correct the Z_MID altitude mislabel (accuracy). OPTIONAL (beyond your inventory).**
OLD: `Places inversion in mid-troposphere, matching the real boundary-layer / free-troposphere transition.`
NEW: `Places the pressure-anomaly sign-reversal in the mid-troposphere (~500 hPa), where a warm column's low-below / high-above structure changes over.`

**[P1-d] Cell 9 — rename mislabeled `c_p` → `SCALE_P` and define it (accuracy; from [C2]).** Replace all `c_p` with `\text{SCALE\_P}` (4×) and add a sentence: SCALE_P is the §2 pressure-scaling knob, **not** the specific heat $c_p$.

**[P1-e] Cell 0 — axis precision.** OLD: `*no* horizontal pressure-anomaly gradient` → NEW: `*no* meridional (north–south) pressure-anomaly gradient`. (Targets the zonal-vs-meridional slip the exam exposed.)

**[BLOCKED — verify first, do not draft]**
- Cell 5 "±5–15 hPa" — verify or soften (Phase 3.5).
- Cell 14 Bjerknes quote — verify verbatim against your OCR (Phase 3.5).

---

## Structural findings — DEFERRED (log only, do NOT fix this session)

- **[S2] Reorder cell 14** out of §5 (before any figure) to where it pays off — either §4 (field generators, where `center_lat ≈ 5–6°` is set and the off-equator ascent is motivated) or immediately after the first figure (§6, Scenario A). *Interim CONTENT-only option if wanted before then:* reword the subtitle so it doesn't presuppose the figure, e.g. `### Why the scenarios set center_lat ≈ 5–6°: the cold tongue pushes ascent off the equator`.
- **[S1-structural] Consolidation pass.** After [P1-a]/[P1-b], the thesis and the tuning-caveat each appear ≤ twice. Remaining structural question: should cell 6 exist as its own section, or **merge into cell 0's "The one question this notebook answers"** (they now frame the same question)? Recommend merging in a STRUCTURAL session; also review whether §2's cell 3 and cell 5 want to be one cell.

## Physics/module findings — DEFERRED (log only)

- None this session. Cell 13's prescribed-jet caveat is exemplary as-is; no module change indicated.

---

## Phase 7 — Capture

**Insight (trap fired → misconception):** The warmest El Niño state produces the *weakest* mid-latitude jet. A teleconnection is driven by the SST *gradient*, not its magnitude; a uniformly warm Pacific has no north–south gradient, so nothing drives the Hadley overturning that builds the jet. **Structure beats magnitude.**

**Process note (internal):** even after a careful read, comprehension slid to the zonal axis and needed anomaly-vs-total spelled out — the explanation exists but sits in the intro, far from the figure. **Fix = proximity, not more words** → the Session-2 (STRUCTURAL) spec.

**Optional (batch later):** Traditional-Chinese translation + ≤500-char Threads split.

---

## EDIT STATUS (as of this session)

**CONTENT PASS COMPLETE.** Applied ✅: **P1-a** (cell 6 rewrite), **P1-b** (cell 3 dedup), **P1-c** (cell 5 Z_MID), **P1-d** (cell 9 c_p→SCALE_P), **P1-e** (cell 0 axis precision). Restart & Run All: clean; 23/23 tests green.
No further CONTENT edits — the remaining findings are STRUCTURAL (proximity / consolidation), not content gaps.
Blocked (pending verification): cell 5 "±5–15 hPa"; cell 14 Bjerknes quote.
Deferred (STRUCTURAL, next session): S2 (reorder cell 14); S1-structural (merge cell 6 → cell 0; consider merging cells 3/5).
After applying: **Restart & Run All** (markdown-only edits — confirm clean). Tests unaffected (no module change).
Next: **Phase 5 exam** on this session's scope once edits are applied.
