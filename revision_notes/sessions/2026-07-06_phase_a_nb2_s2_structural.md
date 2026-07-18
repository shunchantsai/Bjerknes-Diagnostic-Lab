# Phase A: NB2 — Session 2 (STRUCTURAL)

**Session Anchor:**
This session is about: relocating existing cells so explanations sit next to the figures they explain — **whole-cell moves only, no prose rewriting.**
Session TYPE: **STRUCTURAL** (ordering / moving / headings). Any edit that needs *rewriting* a sentence is logged as CONTENT for a later session.

**Date:** 2026-07-06

### Taxonomy & heading grammar
| Level | What it is | This doc |
|---|---|---|
| **Campaign** (letter) | the arc across a notebook | **Phase A** |
| **Notebook** | which notebook | **NB2** |
| **Session** | one scoped sitting | **Session 2 (STRUCTURAL)** |
| **Workflow Phase** (number) | the step within a session (0–8) | starting **Phase 1** |

**You are here: Phase A · NB2 · Session 2 — moves applied + verified; ready to commit.**

**Session tracker:**
- [x] Phase 0 Anchor (STRUCTURAL)
- [x] Phase 1 Structure map (below)
- [x] Phase 2–3 Assessment — spec split into structural (this session) vs content (deferred)
- [x] Phase 4 Moves — M1/M2/M3 applied; verified pure reorder (27 cells, no source changed), Restart & Run All clean
- [x] Phase 7 Capture — "a caveat belongs after the figure it explains; motivation belongs before the setup"
- [ ] Phase 8 — commit reordered notebook + this doc + CHANGELOG line

---

## Phase 1: Structure map (current, post P1-a…k)

```
 0 [md] # Title: ENSO -> Hadley -> Jet Atlas
 1 [md] ## 1 - Setup
 2 [co] imports
 3 [md] ## 2 - Domain, constants, display scales
 4 [co] domain arrays
 5 [md] ### Understanding Z_MID, H_CELL, SCALE_P
 6 [md] ## Why this framing is worth foregrounding      ← UNNUMBERED interlude (§2/§3)
 7 [md] ## 3 - The four scenarios
 8 [co] scenarios dict
 9 [md] ## 4 - Field generators
10 [co] import teleconnection_physics
11 [md] ## 5 - The plotting function
12 [co] plot_scenario def
13 [md] **A second honest caveat — jet location pinned…**  ← in §5, before any figure
14 [md] ### Why the equatorial ascent sits off the equator ← in §5, before any figure  [S2]
15 [md] ## 6 - Scenario A
16 [co] plot_scenario("A")                                 ← FIRST figure appears here
17 [md] ## 7 - Scenario B (the key insight)
18 [co] plot_scenario("B")
19 [co] A-vs-B force panel
20 [md] ## 8 - Scenario C
21 [co] plot_scenario("C")
22 [md] ## 9 - Scenario D
23 [co] plot_scenario("D")
24 [md] ## A note on scope                                 ← UNNUMBERED interlude (§9/§10)
25 [md] ## 10 - Reading the four together
```

**Duplication map (for the deferred content pass):**
- thesis "gradient > magnitude": cells 0, 6, 7, 17, 25 (+ code comment 19)
- anomaly-vs-total: cells 0, 5, 17, 25
- meridional-axis callouts: many (fine — that's the subject)

---

## Phase 2–3: Structural assessment

**Do now (whole-cell moves, no rewriting):**
1. **[M1] Move cell 6** ("Why this framing") → immediately after cell 0 (title). Removes the unnumbered §2/§3 interlude; co-locates motivation with the intro.
2. **[M2] Move cell 14** ("off-equator ascent") → to just after cell 16 (Scenario A's figure). Fixes [S2]: it no longer presupposes an unseen figure.
3. **[M3] Move cell 13** ("jet pinned" caveat) → with M2, to just after Scenario A. *(Optional companion; user's call.)*

**Deferred to Session 3 (CONTENT) — needs rewriting, not moving:**
- Trim the "gradient > magnitude" thesis to ≤2 statements (delete/reword in cells 6, 7).
- Put an anomaly-vs-total line at Scenario B (cell 17) without duplicating cell 0 (rewrite).
- Optional: number the two unnumbered sections consistently.

---

## Phase 4: Move guide  *(execute after target order is confirmed)*

- **M1** applied: "Why this framing" → cell 1 (after title).
- **M2** applied: "off-equator ascent" → after Scenario A's figure (now cell 15).
- **M3** applied: "jet-pinned caveat" → after the ascent (now cell 16).
Verified: pure reorder (no cell source altered), executes clean, 23/23 tests green.

---

## Deferred — CONTENT (Session 3)
- thesis trim to ≤2 · anomaly line at Scenario B · section numbering

## EDIT STATUS
Moves applied ✅: M1, M2, M3 (verified pure reorder). Restart & Run All clean; 23/23 tests green.
Deferred → Session 3 (CONTENT): thesis trim to ≤2; anomaly line at Scenario B; section numbering.
Next: Phase 8 commit.
