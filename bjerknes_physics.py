"""
bjerknes_physics.py — Idealised equatorial pressure diagnostics
Reference: Bjerknes, J. (1969). Monthly Weather Review, 97(3), 163-172.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

DEFAULT_X = np.linspace(120, 270, 1200)
LON_TICKS  = [120, 150, 180, 210, 240, 270]
LON_LABELS = ["120°E", "150°E", "180°", "150°W", "120°W", "90°W"]

def lon_fmt(v):
    if abs(v - 180) < 0.01: return "180°"
    return f"{v:.0f}°E" if v < 180 else f"{360 - v:.0f}°W"

#def pressure(x, A, x0, w, base):
#    return base - A * np.tanh((x - x0) / w)

def pressure(x, A, x0, w, base, shift=0.0):
    """
    x: longitude
    A: amplitude of the see-saw
    x0: center point (anchor)
    w: width
    base: mean pressure
    shift: antisymmetric see-saw term (the SO component)
    """
    # The 'shift' term creates the see-saw (high in west, low in east)
    # The tanh function naturally anchors around x0
    return base - (A + shift) * np.tanh((x - x0) / w)
    
def gradient(x, A, x0, w):
    return -(A / w) * (1.0 / np.cosh((x - x0) / w)) ** 2

def find_zero_crossings(xv, yv):
    s = np.sign(yv)
    out = []
    for i in np.where(np.diff(s) != 0)[0]:
        dy = yv[i + 1] - yv[i]
        if abs(dy) < 1e-15:
            x_zero = 0.5 * (xv[i] + xv[i + 1])
        else:
            x_zero = xv[i] - yv[i] * (xv[i + 1] - xv[i]) / dy
        if not out or abs(x_zero - out[-1]) > 0.1:
            out.append(x_zero)
    return out

def get_regime(dpbar, A1, A2):
    dA = A2 - A1
    if abs(dpbar) > abs(dA): return "B (No crossing)"
    if abs(dpbar) < 1e-5:    return "A (Coincident)"
    return "C (East of max)" if dpbar > 0 else "D (West of max)"

def integrated_forcing(A, x0, w, x_start=120, x_end=270):
    """
    Computes the total integrated easterly forcing by integrating 
    the absolute pressure gradient over the Pacific basin.
    """
    x = np.linspace(x_start, x_end, 1000)
    g = gradient(x, A, x0, w)
    # The absolute value ensures we capture the magnitude of forcing 
    # regardless of sign, representing the total atmospheric energy input
    return np.trapz(np.abs(g), x)

C_PT, C_PTD, C_DP, C_GRAD = "#1f77b4", "#e8593c", "teal", "purple"

def plot_scenario(dpbar, scenario_title="", subtitle="",
                  A1=3.5, A2=4.2, x0=185.0, w=22.0, base=1010.0,
                  X=None, savepath=None):
    if X is None:
        X = DEFAULT_X
    p1 = pressure(X, A1, x0, w, base)
    p2 = pressure(X, A2, x0, w, base + dpbar)
    dp = p2 - p1
    g  = gradient(X, A2, x0, w)
    crossings = find_zero_crossings(X, dp)
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))
    ax1, ax2, ax3, ax4 = axes.ravel()
    fig.suptitle(scenario_title, fontsize=15, fontweight="bold", y=0.99)
    fig.text(0.5, 0.955, subtitle, fontsize=9, ha="center", va="top",
             color="grey", style="italic", wrap=True)
    legend_handles = [
        Line2D([0],[0], color=C_PT,  lw=2, ls="-",  label=r"$p(t)$ — pressure at time $t$"),
        Line2D([0],[0], color=C_PTD, lw=2, ls="--", label=r"$p(t{+}\Delta t)$ — pressure after interval"),
        Line2D([0],[0], color=C_DP,  lw=2, ls="-",  label=r"$\Delta p$ — isallobaric change"),
        Line2D([0],[0], color=C_GRAD,lw=2, ls="-",  label=r"$\partial p/\partial x$ — spatial gradient"),
        Line2D([0],[0], color="grey", lw=1, ls="--", label="zero line"),
    ]
    fig.legend(handles=legend_handles, loc="upper center",
               bbox_to_anchor=(0.5, 0.935), ncol=3, fontsize=8,
               frameon=True, edgecolor="#cccccc")
    ax1.set_title(r"① Raw pressure field — $p(x,\, t)$ and $p(x,\, t{+}\Delta t)$",
                  fontsize=10, loc="left", pad=10)
    ax1.plot(X, p1, color=C_PT, lw=2)
    ax1.plot(X, p2, color=C_PTD, lw=2, ls="--")
    ax1.set_ylabel("hPa")
    ax2.set_title(r"② Isallobaric change — $\Delta p(x) = p(t{+}\Delta t) - p(t)$",
                  fontsize=10, loc="left", pad=10)
    ax2.axhline(0, color="grey", lw=1, ls="--")
    ax2.plot(X, dp, color=C_DP, lw=2)
    ax2.fill_between(X, dp, 0, where=dp>=0, color=C_DP, alpha=0.12)
    ax2.fill_between(X, dp, 0, where=dp<0,  color=C_PTD, alpha=0.08)
    ax2.set_ylabel("hPa change")
    ax3.set_title(r"③ Zero isallobar crossing — where $\Delta p = 0$",
                  fontsize=10, loc="left", pad=10)
    ax3.axhline(0, color="grey", lw=1, ls="--")
    ax3.plot(X, dp, color=C_DP, lw=2)
    for c in crossings:
        ax3.plot(c, 0, "o", color="orange", ms=12,
                 markeredgecolor="white", markeredgewidth=1.5)
    ax3.set_ylabel(r"$\Delta p$ (hPa)")
    ax4.set_title(r"④ Spatial gradient — $\partial p/\partial x$ and its maximum",
                  fontsize=10, loc="left", pad=10)
    ax4.axhline(0, color="grey", lw=1, ls="--")
    ax4.plot(X, g, color=C_GRAD, lw=2)
    ax4.plot(x0, gradient(x0, A2, x0, w), "o", color="violet", ms=14,
             markeredgecolor="white", markeredgewidth=1.5)
    ax4.set_ylabel("hPa/°lon")
    for a in (ax1, ax2, ax3, ax4):
        a.set_xticks(LON_TICKS)
        a.set_xticklabels(LON_LABELS, fontsize=8)
        a.set_xlim(120, 270)
        a.grid(alpha=0.15)
    plt.tight_layout(rect=[0, 0, 1, 0.90])
    if savepath:
        fig.savefig(savepath, dpi=150, bbox_inches="tight")
    plt.show()
    if crossings:
        for c in crossings:
            rel = ("ON" if abs(c-x0)<0.5 else "EAST of" if c>x0 else "WEST of")
            print(f"  crossing at {lon_fmt(c)}  |  gradient max at {lon_fmt(x0)}  |  {rel} the max")
    else:
        print(f"  NO crossing  |  gradient max at {lon_fmt(x0)}")
    return crossings, x0
