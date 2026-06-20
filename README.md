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

- **Scientific Foundation:** Visualize the interaction between equatorial SST anomalies, pressure gradients, and atmospheric tendencies within the Bjerknes feedback loop.
- **Diagnostic Tool:** Implement numerical diagnostics (zero isallobars and gradient maxima identification) to identify transitions in Walker Circulation regime.
- **Regime Classification:** Explicitly classify ENSO states into four discrete regimes—**Cold (La Niña)**, **Warm (El Niño)**, **Transition (Mixed/Neutral)**, and **Damping (Feedback Suppressed)**—based on basin-wide pressure anomalies and feedback strength.
- **Experimental Climate Scenarios:** Simulate how basin-wide pressure anomalies (Δp̄) and SST forcing trigger shifts between regimes under different atmospheric parameterizations.

## Contents

- **`Bjerknes-Diagnostic-Lab.ipynb`**: Primary interactive notebook containing narrative, mathematical foundations, visualizations, and regime classification logic.
- **`bjerknes_physics.py`**: Modular Python implementation of Bjerknes feedback diagnostics, isallobar detection, and regime classification functions.

## Four ENSO Regimes

The diagnostic framework classifies the equatorial Pacific into four operationally distinct regimes:

1. **Cold (La Niña):** Cooler-than-normal SSTs drive anomalous high pressure and strengthened trades; positive feedback amplifies the cold state.
2. **Warm (El Niño):** Warmer-than-normal SSTs drive anomalous low pressure and weakened trades; positive feedback amplifies the warm state.
3. **Transition (Neutral):** Weak SST forcing or contradictory pressure-wind feedbacks; system exhibits low regime coherence.
4. **Damping (Suppressed):** Negative feedback dominates; atmospheric response opposes SST forcing, acting to restore neutral conditions.

Each regime is identified through quantitative diagnostics: isallobar position, gradient magnitude, and feedback sign inference from pressure-wind covariance.

## Getting Started

### Requirements

- Python 3.7+
- `numpy`, `matplotlib`, `pandas`, `scipy`

### Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/shunchantsai/Bjerknes-Diagnostic-Lab.git
cd Bjerknes-Diagnostic-Lab
pip install numpy matplotlib pandas scipy
```

### Running the Notebook

Open the Jupyter notebook in your preferred environment:

```bash
jupyter notebook Bjerknes-Diagnostic-Lab.ipynb
```

The notebook is fully self-contained and includes inline documentation, mathematical derivations, and interactive visualizations of feedback dynamics across all four regimes.

## Discussion Topics and Research Extensions

This diagnostic framework raises several important questions for further investigation:

1. **Parameterization Sensitivity:** How do choices in atmospheric moisture and heating parameterizations affect the detection and classification of regime transitions? The current implementation uses a simplified tanh-based feedback function; comparison with full GCM output would clarify the degree of model dependence.

2. **Regime Transition Mechanisms:** What triggers transitions between Cold and Warm regimes? Is the transition always through Neutral/Damping states, or can the system exhibit bistability? Observable leading indicators (SSTA, SOI, thermocline depth) could be used to forecast regime shifts operationally.

3. **Temporal Stability and Predictability:** How persistent are the four regimes, and what is the timescale of regime switching? Integration with subsurface ocean dynamics (thermocline displacement, ocean heat content) may improve transition prediction.

4. **Catastrophe Risk Implications:** ENSO regimes have well-documented impacts on regional precipitation, tropical cyclone activity, and flood/drought hazard. This framework could enable rapid regime-aware risk assessment for insurance and disaster risk reduction applications.

## Applications

This work is designed to be actionable across multiple audiences:

- **Climate Scientists:** A reproducible, diagnostic toolkit for analyzing ENSO dynamics in observations and model output.
- **Insurance and CAT Modeling:** Rapid regime classification to inform climate-adjusted hazard models and portfolio stress testing.
- **Risk Analysis and Think Tanks:** Observable diagnostics for assessing equatorial Pacific state and associated global climate impacts.
- **Policy and Resilience Planning:** Regime-aware scenario analysis for climate adaptation and disaster risk reduction strategies.

## References

Bjerknes, J. (1969). Atmospheric teleconnections from the equatorial Pacific. *Monthly Weather Review*, 97(3), 163–172.

## License

This project is made available for educational and research use. Please cite appropriately in derivative work.

## Author

Shun-Chan Tsai  
Geography & Climate Risk Analysis  
[GitHub: shunchantsai](https://github.com/shunchantsai)
