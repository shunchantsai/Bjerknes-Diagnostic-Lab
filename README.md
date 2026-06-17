# Bjerknes Diagnostic Lab: Numerical Frameworks for ENSO Dynamics

## Overview
The El Niño-Southern Oscillation (ENSO) is the planet's primary driver of interannual climate variability, altering global atmospheric circulation, dictating agricultural yields, and modulating wildfire and catastrophe risks worldwide. At its core lies the **Bjerknes Mechanism**: a powerful coupled feedback loop where equatorial Pacific sea surface temperature gradients and trade wind strengths mutually reinforce one another.

This repository provides a computational sandbox that formalizes Jacob Bjerknes’s foundational 1969 theory into an explicit numerical diagnostic tool. By tracking mathematical boundary shifts, this lab demonstrates how large-scale pressure anomalies break down stable atmospheric states, providing a mechanistic look at the triggers behind El Niño and La Niña events. It serves as both an interactive educational tutorial for advanced students and a structural framework for climate risk diagnostics.

## Key Objectives
- **Dynamical Visualization:** Model the non-linear transition between equatorial pressure gradients and transient atmospheric responses.
- **Diagnostic Engineering:** Implement numerical root-finding and spatial differentiation to isolate the precise coordinates of **zero isallobars** and **gradient maxima**.
- **Regime Shift Simulation:** Examine the sensitivity of the Walker Circulation by treating basin-wide pressure offsets ($\Delta\bar{p}$) as a control parameter ("the knob") to trigger systemic decoupled climate states.

## Repository Architecture
To maintain professional software standards and separate scientific exposition from production code, the project is split into two main layers:
1. **`bjerknes_physics.py` (The Physics Engine):** A modular Python script containing the raw mathematical formulations, underlying data arrays, numerical root-finding algorithms, and dynamic gradient calculators. 
2. **`Bjerknes-Diagnostic-Lab.ipynb` (The Narrative Dashboard):** An interactive Jupyter Notebook serving as the public-facing interface. It imports the engine, provides exhaustive scientific and mathematical context using LaTeX formatting, executes the climate experiments, and renders the diagnostic visualizations.

## Getting Started & Reproducibility

### Prerequisites
Ensure you have Python 3.8+ installed along with the core scientific computing stack:
```bash
pip install numpy matplotlib pandas
