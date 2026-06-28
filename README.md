# Bjerknes Diagnostic Lab: ENSO Dynamics on Two Axes

A two-part computational study of the El Niño–Southern Oscillation, built around a single
idea from Bjerknes (1969): the equatorial Pacific pressure see-saw, and how its structure
propagates outward to shape mid-latitude weather. The two notebooks examine the *same*
ENSO regime taxonomy along the two perpendicular axes of the system — the **zonal**
(east–west, Walker) axis and the **meridional** (north–south, Hadley-to-jet) axis.

## The two parts

**Part 1 — `01_Bjerknes_Zonal_Diagnostic.ipynb` (the zonal axis).**
A diagnostic study of Bjerknes's equatorial see-saw along *longitude*. It separates two
quantities that standard ENSO indices tend to collapse: the **zero isallobar** (the *temporal*
node, where pressure has stopped changing) and the **gradient maximum** (the *spatial* peak,
where the east–west pressure gradient is steepest). It asks whether their coincidence — which
Bjerknes observed in the cold Januaries of the 1960s — is structural or regime-dependent,
classifies four regimes (A/B/C/D) by a basin-wide-offset parameter, and traces how a
node-classification error would propagate through an idealized catastrophe-risk chain.

**Part 2 — `02_Hadley_Jet_Meridional_Teleconnection.ipynb` (the meridional axis).**
A visual atlas of the *downstream* teleconnection along *latitude*: how each ENSO state drives
(or fails to drive) the Hadley overturning, the poleward transport of angular momentum, and
the subtropical jet. Its central finding is that it is the **meridional SST gradient, not the SST
magnitude, that drives the teleconnection** — the warmest uniform state produces the weakest
jet. A three-panel anatomy (SST forcing → pressure + Hadley circulation → jet) is built once
and reused across all four scenarios.

## How the two parts connect

Both notebooks share one **A/B/C/D regime taxonomy**, viewed on perpendicular axes:

| | Part 1 (zonal) | Part 2 (meridional) |
|---|---|---|
| **A** | Pure see-saw: node *on* the gradient maximum | Strong El Niño: sharp gradient, vigorous jet |
| **B** | Basin-wide offset erases the node entirely | Uniform warm: no gradient, teleconnection collapses |
| **C** | Node displaced east | Cold La Niña, weak gradient |
| **D** | Node displaced west | Cold La Niña, spatially disrupted |

The correspondence is **exact for A and B** — and **B is the shared keystone**: it is the case
where structure disappears on *both* axes (no node to misplace in Part 1; no gradient to drive
the jet in Part 2). For C and D, the label and the "node displaced east/west" framing carry
across, while Part 2 realizes them specifically as cold La Niña states, because tracing the
meridional teleconnection requires a warm-vs-cold contrast that the zonal node-geometry
framing does not supply. The two notebooks are perpendicular views of one taxonomy, not
identical scenarios — a point each notebook states explicitly.

## A note on scope

Both notebooks are **idealized diagnostics, not GCMs or calibrated models**. The fields are
prescribed analytic forms chosen for pedagogical clarity, not solved from primitive equations,
and where Part 1 estimates a downstream risk cascade, those figures are order-of-magnitude
illustrations of how an error *propagates and compounds*, not derived results. The aim is
mechanistic understanding and an honest, legible account of one causal chain.

## Contents

- `01_Bjerknes_Zonal_Diagnostic.ipynb` — Part 1: the zonal node-vs-gradient diagnostic.
- `02_Hadley_Jet_Meridional_Teleconnection.ipynb` — Part 2: the meridional jet teleconnection atlas (self-contained; defines its own field generators).
- `bjerknes_physics.py` — the physics and diagnostic functions imported by **Part 1**. (Part 2 is self-contained and does not use this module.)

## Getting Started

Requires Python 3.x with `numpy`, `matplotlib`, and `pandas`. Open either notebook in
Jupyter and run all cells; each is self-documenting and regenerates its figures from scratch.

## Reference

Bjerknes, J. (1969). Atmospheric teleconnections from the equatorial Pacific. *Monthly Weather Review*, 97(3), 163–172.
