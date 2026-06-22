# Bjerknes Diagnostic Lab: ENSO Dynamics and Feedback Physics

## Overview

This repository provides a computational exploration of the **Bjerknes Mechanism**, the fundamental feedback loop driving the El Niño-Southern Oscillation (ENSO). The project implements diagnostic tools to identify and classify shifts in equatorial Pacific dynamics, directly connecting atmospheric feedback physics to observable ocean-atmosphere interactions.

Designed as both a technical tutorial and a research-grade diagnostic framework, this work bridges climate dynamics theory and practical applications in climate risk modeling and catastrophe insurance assessment.

## Scientific Foundation

The Bjerknes mechanism, articulated in foundational work by Jacob Bjerknes (1969), describes how anomalous sea surface temperature (SST) in the equatorial Pacific triggers atmospheric pressure response, which in turn modifies trade wind patterns and surface currents—completing a feedback loop that either amplifies or dampens the initial anomaly. This positive feedback is the engine of ENSO variability.

This repository operationalizes Bjerknes's diagnostic framework by:
- Computing equatorial pressure gradients and their atmospheric tendencies
- Implementing zero isallobars and gradient maxima diagnostics to detect shifts in Walker Circulation intensity
- Classifying the state of the system into discrete ENSO regimes based on feedback strength and sign

## Key Objectives

- **Diagnostic Clarity:** Separate the *temporal* zero isallobar (where pressure stopped changing) from the *spatial* gradient maximum (where the pressure field is steepest right now). These are mathematically independent; conflating them induces regime-dependent errors in ENSO phase classification.
- **Mathematical Framework:** Implement a four-regime taxonomy (Scenarios A–D) based on the relationship between the temporal node and spatial peak, controlled by two parameters: the see-saw amplitude and a basin-wide pressure offset.
- **Oceanic Memory:** Model how the equatorial cold tongue width encodes upwelling history via a leaky integrator (τ≈18 months). Show that two states with identical *present* forcing can differ by 1.80× in integrated cold content if they followed different *past* forcing histories.
- **Pedagogical Metrics:** Compare two competing diagnostics—one that cannot see width (total pressure drop, flat) and one that can (integrated cold content, rising)—to demonstrate why point-value indices (peak SST, gradient maxima) miss spatial extent and historical depth.

## Contents

- **`Bjerknes-Diagnostic-Lab.ipynb`**: Primary interactive notebook containing narrative, mathematical foundations, visualizations, and regime classification logic.
- **`bjerknes_physics.py`**: Modular Python implementation of Bjerknes feedback diagnostics, isallobar detection, and regime classification functions.

## Four Mathematical Regimes: The Temporal Node vs. Spatial Peak

The diagnostic framework separates two independent questions about equatorial pressure:

1. **Where did pressure stop changing?** (the zero isallobar — temporal)
2. **Where is the pressure field steepest right now?** (the gradient maximum — spatial)

Under Option 2 (two active see-saw states), these coincide only under special conditions. The four regimes are:

- **Scenario A (Coincident):** No basin-wide offset (global_offset = 0). The zero isallobar sits exactly on the gradient maximum at 178°E. This is Bjerknes's cold-year observation: study only cold years and the two quantities appear identical.
  
- **Scenario B (No crossing):** Basin-wide pressure rise exceeds the see-saw amplitude. The zero isallobar vanishes entirely—no equatorial crossing. The gradient maximum still exists, but the temporal node is gone. A diagnostic that *requires* a zero isallobar fails silently here.
  
- **Scenario C (Node displaced east):** Modest basin-wide rise slides the node ~12° east of the gradient maximum (to ~170°W). The gradient maximum has not moved; only the temporal node has.
  
- **Scenario D (Node displaced west):** Mirror image of C: a basin-wide fall slides the node ~12° west (to ~166°E).

**Key insight:** These regimes show that a *single number* (the zero-isallobar longitude) is regime-dependent. Cold years (A) use one diagnostic; warm years (B) have no diagnostic; neutral years (C/D) use a displaced one. A catalogue phase-labelled on this single diagnostic is contaminated with systematic bias, not random error.

## Getting Started

### Requirements

- Python 3.7+
- `numpy`, `matplotlib`

### Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/shunchantsai/Bjerknes-Diagnostic-Lab.git
cd Bjerknes-Diagnostic-Lab
pip install numpy matplotlib
```

### Running the Notebook

Open the Jupyter notebook in your preferred environment:

```bash
jupyter notebook Bjerknes-Diagnostic-Lab.ipynb
```

The notebook is fully self-contained and includes inline documentation, mathematical derivations, and interactive visualizations of feedback dynamics across all four regimes.

## Discussion Topics and Research Extensions

This diagnostic framework raises several important questions for further investigation:

1. **Historical Classification:** How have equatorial Pacific states (1950–present, via ERA5 SLP and OISST) mapped onto the four regimes A–D? Do observed transitions follow the theoretical taxonomy? Are there states with multiple zero crossings or non-monotonic gradients that the tanh model cannot represent?

2. **Oceanic Memory Timescale:** The leaky integrator uses τ≈18 months, derived from Bjerknes's observation of the 1963–65 transition. Does this timescale hold across different epochs? Does it vary with background climate state? Real ocean data (subsurface temperature, reanalysis upwelling indices) could constrain τ empirically.

3. **Metric Validation Against Hazard:** The notebook shows that integrated cold content sees width while pressure-drop diagnostics do not. Do observed tropical cyclone genesis rates, track density, and rainfall patterns actually correlate better with cold content than with standard ENSO indices (SOI, ONI, etc.)? That is the step from "conceptual clarity" to "empirical superiority."

4. **Catastrophe Risk Implications:** ENSO regime misclassification propagates through every layer of a CAT model (hazard parameterization, exposure weighting, loss estimation). A systematic phase-classification error is non-random and cannot be corrected with a scalar loading. Quantifying the downstream loss impact of node–gradient confusion would clarify the value of this diagnostic framework for insurance and risk management.

## Applications and Audience

This work is designed to be actionable across multiple audiences:

- **Climate Scientists:** A reproducible toolkit for understanding the mathematical structure of equatorial pressure diagnostics. Shows how temporal (node) and spatial (peak) features are independent, and why this matters for ENSO phase classification.
  
- **ENSO Researchers & Modelers:** A clear pedagogical framework for separating the zero isallobar from the gradient maximum. Useful for diagnosing model biases and for understanding historical observational records where these quantities have been conflated.
  
- **Insurance and CAT Modeling:** Demonstrates how a regime-dependent classification error propagates through hazard models, exposure, vulnerability, and loss. Provides a concrete example of why the choice of ENSO diagnostic (node vs. peak vs. index) matters for portfolio stress testing and climate-adjusted risk assessment.
  
- **Risk Analysis & Think Tanks:** Observable diagnostics (zero isallobar, gradient maximum) that can be computed from reanalysis data (ERA5, MERRA-2) to assess equatorial Pacific state in near-real time. Useful for scenario analysis and climate-informed decision support.
  
- **Policy & Resilience Planning:** The framework clarifies why a "single ENSO phase label" can mask different forcing histories and different circulation intensities. This supports arguments for ensemble-based or history-aware climate scenario analysis in adaptation planning.

## Scope and Limitations

This notebook uses an **idealised tanh pressure profile** with a single control parameter (`global_offset`). Real equatorial pressure fields are shaped by multiple processes simultaneously—trade-wind variability, off-equatorial (10–15°S) forcing, MJO modulation, and seasonal mean biases. A real pressure field could exhibit:

- Multiple zero crossings (not captured by the idealised model)
- Non-monotonic gradients
- Asymmetry between cold and warm seasons

The notebook demonstrates the *principle* — that temporal (zero isallobar) and spatial (gradient maximum) features are mathematically independent — using a simplified framework. **This is a clarity exercise, not a reanalysis-ready diagnostic.**

Extending this to observational data (ERA5 equatorial SLP profiles and OISST, 1950–present) is the natural next step. That would test whether the four regimes (A–D) map cleanly onto observed ENSO states and whether the crossing–gradient separation correlates with downstream TC statistics and precipitation anomalies.

## References

Bjerknes, J. (1969). Atmospheric teleconnections from the equatorial Pacific. *Monthly Weather Review*, 97(3), 163–172.

## License

This project is made available for educational and research use. Please cite appropriately in derivative work.

## Author

Shun-Chan Tsai  
Geography & Climate Risk Analysis  
[GitHub: shunchantsai](https://github.com/shunchantsai)
