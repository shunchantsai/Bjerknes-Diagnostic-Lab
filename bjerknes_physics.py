"""
bjerknes_physics.py — Idealised equatorial pressure diagnostics
================================================================

This module implements the idealised Walker-circulation pressure model
used in the Bjerknes Diagnostic Lab notebook. It provides:

  1. Physics: pressure(x), gradient(x), and isallobaric change Δp(x)
  2. Diagnostics: zero-crossing finder and regime classifier
  3. Plotting: the four-panel diagnostic engine with full annotations
  4. Formatting: longitude tick labels and sanity-check printer

All functions operate on a continuous longitude axis where
120 = 120°E, 180 = dateline, 270 = 90°W.

Reference
---------
Bjerknes, J. (1969). "Atmospheric Teleconnections from the
Equatorial Pacific." Monthly Weather Review, 97(3), 163–172.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


# ══════════════════════════════════════════════════
#  1. DOMAIN AND FORMATTING
# ══════════════════════════════════════════════════

DEFAULT_X = np.linspace(120, 270, 1200)
"""Default longitude axis: 120°E to 90°W."""

LON_TICKS  = [120, 150, 180, 210, 240, 270]
LON_LABELS = ["120°E", "150°E", "180°", "150°W", "120°W", "90°W"]

def lon_fmt(v):
    """Convert continuous coordinate to human-readable longitude string."""
    if abs(v - 180) < 0.01:
        return "180°"
    return f"{v:.0f}°E" if v < 180 else f"{360 - v:.0f}°W"


# ══════════════════════════════════════════════════
#  2. CORE PHYSICS
# ══════════════════════════════════════════════════

def pressure(x, A, x0, w, base):
    """
    Idealised equatorial sea-level pressure (Walker pattern).

    p(x) = base - A · tanh((x - x0) / w)

    Parameters
    ----------
    x    : array-like, longitude in continuous coordinates
    A    : float, amplitude (half the east–west pressure difference)
    x0   : float, inflection longitude (where the slope is steepest)
    w    : float, width parameter (controls how sharp the gradient is)
    base : float, basin-wide mean pressure level (hPa)
    """
    return base - A * np.tanh((x - x0) / w)


def gradient(x, A, x0, w):
    """
    Analytic spatial gradient ∂p/∂x.

    Most negative (strongest westward drive) at x = x0.
    """
    return -(A / w) * (1.0 / np.cosh((x - x0) / w)) ** 2


# ══════════════════════════════════════════════════
#  3. DIAGNOSTICS
# ══════════════════════════════════════════════════

#def find_zero_crossings(xv, yv):
#    """
#    Return longitudes where yv changes sign (linear interpolation).
#
#    These are the points where the zero isallobar crosses the equator
#    in the 1-D profile.
#    """
#    s = np.sign(yv)
#    out = []
#    for i in np.where(np.diff(s) != 0)[0]:   # [0] unpacks the tuple
#        x_zero = xv[i] - yv[i] * (xv[i + 1] - xv[i]) / (yv[i + 1] - yv[i])
#        out.append(x_zero)
#    return out

def find_zero_crossings(xv, yv):
    """
    Return longitudes where yv changes sign (linear interpolation).
    
    Handles edge cases where data points land exactly on zero.
    """
    s = np.sign(yv)
    out = []
    for i in np.where(np.diff(s) != 0)[0]:   # [0] unpacks the tuple
        dy = yv[i + 1] - yv[i]
        if abs(dy) < 1e-15:                   # both points effectively zero
            x_zero = 0.5 * (xv[i] + xv[i + 1])
        else:
            x_zero = xv[i] - yv[i] * (xv[i + 1] - xv[i]) / dy
        # filter near-duplicate crossings (within 0.1° of previous)
        if not out or abs(x_zero - out[-1]) > 0.1:
            out.append(x_zero)
    return out

def get_regime(dpbar, A1, A2):
    """
    Classify the ENSO regime from the basin-wide offset Δp̄.

    Returns one of:
      A (Coincident)   — crossing sits on the gradient maximum
      B (No crossing)  — |Δp̄| > |A2 − A1|, no equatorial crossing
      C (East of max)  — crossing east of the gradient maximum
      D (West of max)  — crossing west of the gradient maximum
    """
    dA = A2 - A1
    if abs(dpbar) > abs(dA):
        return "B (No crossing)"
    if abs(dpbar) < 1e-5:
        return "A (Coincident)"
    return "C (East of max)" if dpbar > 0 else "D (West of max)"


# ══════════════════════════════════════════════════
#  4. PLOTTING ENGINE
# ══════════════════════════════════════════════════

# Colour palette
C_PT   = "#1f77b4"    # p(t)
C_PTD  = "#e8593c"    # p(t+Δt)
C_DP   = "teal"       # Δp
C_GRAD = "purple"     # ∂p/∂x


    if X is None:
        X = DEFAULT_X

def plot_scenario(dpbar, scenario_title="", subtitle="",
                  A1=3.5, A2=4.2, x0=185.0, w=22.0, base=1010.0,
                  X=None, savepath=None):
    """
    Produce the four-panel Bjerknes diagnostic figure for one scenario.

    Parameters
    ----------
    dpbar           : basin-wide uniform pressure offset (the single knob)
    scenario_title  : bold title above the figure
    subtitle        : italic explanatory line below the title
    savepath        : if given, save figure to this path

    Returns
    -------
    crossings : list of zero-crossing longitudes
    x0        : gradient-maximum longitude
    """
    p1 = pressure(X, A1, x0, w, base)
    p2 = pressure(X, A2, x0, w, base + dpbar)
    dp = p2 - p1
    g  = gradient(X, A2, x0, w)
    crossings = find_zero_crossings(X, dp)

    fig, axes = plt.subplots(2, 2, figsize=(13, 9))
    ax1, ax2, ax3, ax4 = axes.ravel()

    # Title + subtitle
    fig.suptitle(scenario_title, fontsize=15, fontweight="bold", y=0.99)
    fig.text(0.5, 0.955, subtitle, fontsize=9, ha="center", va="top",
             color="grey", style="italic", wrap=True)

    # Overall legend
    legend_handles = [
        Line2D([0], [0], color=C_PT,   lw=2, ls="-",
               label=r"$p(t)$ — pressure at time $t$"),
        Line2D([0], [0], color=C_PTD,  lw=2, ls="--",
               label=r"$p(t{+}\Delta t)$ — pressure after interval"),
        Line2D([0], [0], color=C_DP,   lw=2, ls="-",
               label=r"$\Delta p$ — isallobaric change"),
        Line2D([0], [0], color=C_GRAD, lw=2, ls="-",
               label=r"$\partial p / \partial x$ — spatial gradient"),
        Line2D([0], [0], color="grey",  lw=1, ls="--",
               label="zero line"),
    ]
    fig.legend(handles=legend_handles, loc="upper center",
               bbox_to_anchor=(0.5, 0.935), ncol=3, fontsize=8,
               frameon=True, edgecolor="#cccccc")

    # ① Raw pressure field
    ax1.set_title(
        r"① Raw pressure field — $p(x,\, t)$ and $p(x,\, t{+}\Delta t)$",
        fontsize=10, loc="left", pad=10)
    ax1.plot(X, p1, color=C_PT, lw=2)
    ax1.plot(X, p2, color=C_PTD, lw=2, ls="--")
    ax1.set_ylabel("hPa")

    # ② Isallobaric change
    ax2.set_title(
        r"② Isallobaric change — $\Delta p(x) = p(t{+}\Delta t) - p(t)$",
        fontsize=10, loc="left", pad=10)
    ax2.axhline(0, color="grey", lw=1, ls="--")
    ax2.plot(X, dp, color=C_DP, lw=2)
    ax2.fill_between(X, dp, 0, where=dp >= 0, color=C_DP, alpha=0.12)
    ax2.fill_between(X, dp, 0, where=dp < 0,  color=C_PTD, alpha=0.08)
    ax2.set_ylabel("hPa change")

    # ③ Zero isallobar crossing
    ax3.set_title(
        r"③ Zero isallobar crossing — where $\Delta p = 0$",
        fontsize=10, loc="left", pad=10)
    ax3.axhline(0, color="grey", lw=1, ls="--")
    ax3.plot(X, dp, color=C_DP, lw=2)
    for c in crossings:
        ax3.plot(c, 0, "o", color="orange", ms=12,
                 markeredgecolor="white", markeredgewidth=1.5)
    ax3.set_ylabel(r"$\Delta p$ (hPa)")

    # ④ Spatial gradient
    ax4.set_title(
        r"④ Spatial gradient — $\partial p / \partial x$ and its maximum",
        fontsize=10, loc="left", pad=10)
    ax4.axhline(0, color="grey", lw=1, ls="--")
    ax4.plot(X, g, color=C_GRAD, lw=2)
    ax4.plot(x0, gradient(x0, A2, x0, w), "o", color="violet", ms=14,
             markeredgecolor="white", markeredgewidth=1.5)
    ax4.set_ylabel("hPa/°lon")

    # Common formatting
    for a in (ax1, ax2, ax3, ax4):
        a.set_xticks(LON_TICKS)
        a.set_xticklabels(LON_LABELS, fontsize=8)
        a.set_xlim(120, 270)
        a.grid(alpha=0.15)

    plt.tight_layout(rect=[0, 0, 1, 0.90])

    if savepath:
        fig.savefig(savepath, dpi=150, bbox_inches="tight")
    plt.show()

    # Sanity-check print
    if crossings:
        for c in crossings:
            rel = ("ON" if abs(c - x0) < 0.5
                   else "EAST of" if c > x0
                   else "WEST of")
            print(f"  crossing at {lon_fmt(c)}  |  "
                  f"gradient max at {lon_fmt(x0)}  |  {rel} the max")
    else:
        print(f"  NO crossing  |  gradient max at {lon_fmt(x0)}")

    return crossings, x0
