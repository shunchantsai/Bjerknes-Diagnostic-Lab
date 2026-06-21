"""
bjerknes_physics.py — Idealised equatorial pressure diagnostics
Reference: Bjerknes, J. (1969). Monthly Weather Review, 97(3), 163-172.

Model convention (Option 2 — true year-to-year isallobar):
    A scenario compares two ACTIVE states of the see-saw,
        state 1: amplitude so_amp_1   (e.g. 3.5)
        state 2: amplitude so_amp_2   (e.g. 4.2) + a basin-wide global_offset
    so the isallobaric change is
        dp(x) = global_offset - (so_amp_2 - so_amp_1) * tanh((x - x0)/w).
    The zero isallobar (temporal node) sits on the gradient maximum (spatial peak, at x0)
    only when global_offset = 0; a crossing exists only while |global_offset| < (so_amp_2 - so_amp_1).
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# --- Setup and Utilities ---
DEFAULT_X = np.linspace(120, 270, 1200)
# Bjerknes's four isallobar maps cross the equator at 175E, 170W(=190E), 168E, 178E
# -> mean ~178E, "a little west of the dateline on the average". Use this as the
# canonical cold-year node / gradient-maximum longitude.
X0_COLD = 178.0
LON_TICKS = [120, 150, 180, 210, 240, 270]
LON_LABELS = ["120°E", "150°E", "180°", "150°W", "120°W", "90°W"]

def lon_fmt(v):
    if abs(v - 180) < 0.01: return "180°"
    return f"{v:.0f}°E" if v < 180 else f"{360 - v:.0f}°W"

def _trapz(y, x):
    return (np.trapezoid if hasattr(np, "trapezoid") else np.trapz)(y, x)

# --- Physics Model ---
def pressure(x, so_amplitude, x0, w, base, global_offset=0.0):
    """so_amplitude: intensity of the zonal see-saw (Southern Oscillation).
    global_offset: uniform basin-wide mass-exchange bias."""
    return base + global_offset - so_amplitude * np.tanh((x - x0) / w)

def gradient(x, so_amplitude, x0, w):
    # The global_offset constant disappears under differentiation.
    return -(so_amplitude / w) * (1.0 / np.cosh((x - x0) / w)) ** 2

def get_regime(global_offset, delta_amp):
    """Classify the regime. NOTE: the second argument is the AMPLITUDE CHANGE
    (so_amp_2 - so_amp_1), not an absolute amplitude. A crossing exists only
    while |global_offset| < |delta_amp|."""
    if abs(global_offset) >= abs(delta_amp) - 1e-9:
        return "B (No crossing)"
    if abs(global_offset) < 1e-5:
        return "A (Coincident)"
    return "C (East of max)" if global_offset > 0 else "D (West of max)"

def find_zero_crossings(xv, yv):
    s = np.sign(yv)
    out = []
    for i in np.where(np.diff(s) != 0)[0]:          # [0] unpacks the tuple
        dy = yv[i + 1] - yv[i]
        if abs(dy) < 1e-15:                          # guard divide-by-zero
            x_zero = 0.5 * (xv[i] + xv[i + 1])
        else:
            x_zero = xv[i] - yv[i] * (xv[i + 1] - xv[i]) / dy
        if not out or abs(x_zero - out[-1]) > 0.1:
            out.append(float(x_zero))                # float, not 1-element array
    return out

# --- Forcing / cold-content metrics ---
def total_pressure_drop(so_amplitude, x0, w, x_start=120, x_end=270):
    """Integral of |dp/dx| = the total east-west pressure drop ~ 2*so_amplitude.
    WIDTH-INDEPENDENT by construction: spreading the same drop over more longitude
    does not change its integral. Use this to show what the gradient integral CANNOT see."""
    x = np.linspace(x_start, x_end, 1000)
    return _trapz(np.abs(gradient(x, so_amplitude, x0, w)), x)

# Backwards-compatible alias (kept so old references still resolve).
integrated_forcing = total_pressure_drop

def sst_tongue(x, depth, x0, w):
    """Cold-tongue SST anomaly: negative sech^2 bump, peak magnitude `depth` at x0."""
    return -depth * (1.0 / np.cosh((x - x0) / w)) ** 2

def integrated_cold_content(depth, x0, w, x_start=120, x_end=270):
    """Zonally integrated cold anomaly (~ depth * w) — the basin-integrated drive.
    Unlike total_pressure_drop, this GROWS with width at fixed peak depth."""
    x = np.linspace(x_start, x_end, 1000)
    return abs(_trapz(sst_tongue(x, depth, x0, w), x))

# --- Plotting and Diagnostics ---
C_PT, C_PTD, C_DP, C_GRAD = "#1f77b4", "#e8593c", "teal", "purple"

def plot_scenario(so_amp_2, global_offset, so_amp_1=3.5,
                  scenario_title="", subtitle="",
                  x0=X0_COLD, w=22.0, base=1010.0, X=None, savepath=None):
    """Option 2 (two active states). Returns (crossings, gradient_max_longitude, regime)."""
    if X is None: X = DEFAULT_X

    # State 1: baseline active see-saw; State 2: intensified see-saw + global offset.
    p1 = pressure(X, so_amp_1, x0, w, base, global_offset=0.0)
    p2 = pressure(X, so_amp_2, x0, w, base, global_offset=global_offset)

    dp = p2 - p1
    g  = gradient(X, so_amp_2, x0, w)
    crossings = find_zero_crossings(X, dp)
    regime = get_regime(global_offset, so_amp_2 - so_amp_1)

    fig, axes = plt.subplots(2, 2, figsize=(13, 9))
    ax1, ax2, ax3, ax4 = axes.ravel()
    fig.suptitle(scenario_title, fontsize=15, fontweight="bold", y=0.99)
    fig.text(0.5, 0.955, subtitle, fontsize=9, ha="center", va="top",
             color="grey", style="italic", wrap=True)

    legend_handles = [
        Line2D([0], [0], color=C_PT,   lw=2, ls="-",  label=r"$p(t)$ — state 1"),
        Line2D([0], [0], color=C_PTD,  lw=2, ls="--", label=r"$p(t{+}\Delta t)$ — state 2"),
        Line2D([0], [0], color=C_DP,   lw=2, ls="-",  label=r"$\Delta p$ — isallobaric change"),
        Line2D([0], [0], color=C_GRAD, lw=2, ls="-",  label=r"$\partial p/\partial x$ — gradient"),
        Line2D([0], [0], color="grey", lw=1, ls="--", label="zero line"),
    ]
    fig.legend(handles=legend_handles, loc="upper center",
               bbox_to_anchor=(0.5, 0.935), ncol=3, fontsize=8,
               frameon=True, edgecolor="#cccccc")

    # ① Raw pressure
    ax1.set_title(r"① Raw pressure field — $p(x,\,t)$ and $p(x,\,t{+}\Delta t)$",
                  fontsize=10, loc="left", pad=10)
    ax1.plot(X, p1, color=C_PT, lw=2)
    ax1.plot(X, p2, color=C_PTD, lw=2, ls="--")
    ax1.set_ylabel("hPa")

    # ② Isallobaric change
    ax2.set_title(r"② Isallobaric change — $\Delta p(x)=p(t{+}\Delta t)-p(t)$",
                  fontsize=10, loc="left", pad=10)
    ax2.axhline(0, color="grey", lw=1, ls="--")
    ax2.plot(X, dp, color=C_DP, lw=2)
    ax2.fill_between(X, dp, 0, where=dp >= 0, color=C_DP, alpha=0.12)
    ax2.fill_between(X, dp, 0, where=dp < 0,  color=C_PTD, alpha=0.08)
    ax2.set_ylabel("hPa change")

    # ③ Zero isallobar crossing
    ax3.set_title(r"③ Zero isallobar crossing — where $\Delta p = 0$",
                  fontsize=10, loc="left", pad=10)
    ax3.axhline(0, color="grey", lw=1, ls="--")
    ax3.plot(X, dp, color=C_DP, lw=2)
    for c in crossings:
        ax3.plot(c, 0, "o", color="orange", ms=12,
                 markeredgecolor="white", markeredgewidth=1.5)
    ax3.set_ylabel(r"$\Delta p$ (hPa)")

    # ④ Spatial gradient and its extremum
    ax4.set_title(r"④ Spatial gradient — $\partial p/\partial x$ and its extremum",
                  fontsize=10, loc="left", pad=10)
    ax4.axhline(0, color="grey", lw=1, ls="--")
    ax4.plot(X, g, color=C_GRAD, lw=2)
    ax4.plot(x0, gradient(x0, so_amp_2, x0, w), "o", color="violet", ms=14,
             markeredgecolor="white", markeredgewidth=1.5)
    ax4.set_ylabel("hPa/°lon")

    for a in (ax1, ax2, ax3, ax4):
        a.set_xticks(LON_TICKS)
        a.set_xticklabels(LON_LABELS, fontsize=8)
        a.set_xlim(120, 270)
        a.grid(alpha=0.15)

    plt.tight_layout(rect=[0, 0, 1, 0.90])
    if savepath: fig.savefig(savepath, dpi=150, bbox_inches="tight")
    plt.show()

    # self-documenting summary
    if crossings:
        for c in crossings:
            rel = ("ON" if abs(c - x0) < 0.5 else "EAST of" if c > x0 else "WEST of")
            print(f"  {regime}:  crossing at {lon_fmt(c)}  |  gradient max at {lon_fmt(x0)}  |  {rel} the max")
    else:
        print(f"  {regime}:  NO crossing  |  gradient max at {lon_fmt(x0)}")

    return crossings, x0, regime


def plot_width_diagnostic(depth=4.0, so_amplitude=1.0, x0=X0_COLD,
                          w_min=5, w_max=50, n=120,
                          w_1965=15.0, w_1963=30.0, savepath=None):
    """Sweep cold-tongue width and plot BOTH forcing metrics on twin axes:

       * integrated_cold_content (left, teal)  -- GROWS with width  (~ depth*w)
       * total_pressure_drop     (right, grey) -- FLAT  (~ 2A, blind to width)

    The contrast is the point: a gradient-integral diagnostic literally cannot
    distinguish a wide (1963) from a narrow (1965) cold tongue; only a content
    integral can. Returns (widths, cold_content_array, pressure_drop_array)."""
    widths = np.linspace(w_min, w_max, n)
    cold = np.array([integrated_cold_content(depth, x0, w) for w in widths])
    drop = np.array([total_pressure_drop(so_amplitude, x0, w) for w in widths])

    fig, axL = plt.subplots(figsize=(10.5, 5.5))
    axR = axL.twinx()
    l_cold, = axL.plot(widths, cold, color="teal", lw=2.5,
                       label=r"Integrated cold content ($\propto$ depth$\cdot w$) — SEES width")
    l_drop, = axR.plot(widths, drop, color="#9a9a9a", lw=2.5, ls="--",
                       label=r"Total pressure drop ($\approx 2A$) — BLIND to width")
    v65 = axL.axvline(w_1965, color="orange", ls=":", lw=1.8,
                      label=f"~1965 (w={w_1965:.0f}, newly re-established)")
    v63 = axL.axvline(w_1963, color="royalblue", ls=":", lw=1.8,
                      label=f"~1963 (w={w_1963:.0f}, ~4 yr sustained)")

    axL.set_xlabel("Cold tongue width  $w$   (oceanic memory)")
    axL.set_ylabel("Integrated cold content  (°C·°lon)", color="teal")
    axR.set_ylabel("Total pressure drop  (hPa)", color="#777777")
    axL.tick_params(axis="y", labelcolor="teal")
    axR.tick_params(axis="y", labelcolor="#777777")
    axR.set_ylim(0, drop.max() * 1.8)
    axL.set_xlim(w_min, w_max)
    axL.grid(alpha=0.15)
    axL.set_title("Two metrics, one width sweep: which diagnostic can see the cold tongue's history?",
                  fontsize=12, fontweight="bold")
    axL.legend(handles=[l_cold, l_drop, v65, v63], loc="center right", fontsize=8)

    plt.tight_layout()
    if savepath: fig.savefig(savepath, dpi=150, bbox_inches="tight")
    plt.show()

    c65 = integrated_cold_content(depth, x0, w_1965)
    c63 = integrated_cold_content(depth, x0, w_1963)
    d65 = total_pressure_drop(so_amplitude, x0, w_1965)
    d63 = total_pressure_drop(so_amplitude, x0, w_1963)
    print(f"  1965 (w={w_1965:>4.0f}):  cold_content={c65:7.1f}    pressure_drop={d65:.3f}")
    print(f"  1963 (w={w_1963:>4.0f}):  cold_content={c63:7.1f}    pressure_drop={d63:.3f}")
    print(f"  ratio 1963/1965  ->  cold_content {c63/c65:.2f}x   BUT   pressure_drop {d63/d65:.2f}x")
    return widths, cold, drop


def tongue_width_history(forcing, dt=1.0, tau=18.0, w0=5.0, gain=20.0):
    """Leaky-integrator toy for cold-tongue width as a function of upwelling
    forcing history. The ocean responds to a sustained atmospheric impulse with
    a LONG memory timescale tau (Bjerknes: oceanic response lags atmospheric
    forcing far more than the reverse). Width relaxes toward an equilibrium set
    by the instantaneous forcing:

        dw/dt = (w_eq(f) - w) / tau,   w_eq(f) = w0 + gain * f

    `forcing` is a 1-D array (e.g. monthly on/off upwelling, 0..1). With a long
    tau, ~4 yr of sustained forcing (1959->1963) builds a much WIDER tongue than
    a few months of freshly re-established upwelling (before Jan 1965), even when
    the instantaneous forcing at the endpoint is identical."""
    forcing = np.asarray(forcing, dtype=float)
    w = np.empty(forcing.size)
    wi = float(w0)
    for i, f in enumerate(forcing):
        w_eq = w0 + gain * f
        wi = wi + dt * (w_eq - wi) / tau
        w[i] = wi
    return w


def plot_width_history(months=60, tau=18.0, w0=5.0, gain=20.0, dt=1.0, savepath=None):
    """Two upwelling histories reaching January with the SAME instantaneous
    forcing, but different pasts. 1963-like: sustained ~4 yr. 1965-like: a long
    warm interruption (1963-64) then only a few months of re-established
    upwelling. The long ocean memory (tau) makes the endpoint widths differ.

    Returns (w_1963_history, w_1965_history) — arrays of shape (months,)."""
    t = np.arange(months)
    f_1963 = np.ones(months)                       # sustained upwelling throughout
    f_1965 = np.ones(months)
    f_1965[months - 21: months - 3] = 0.0          # ~18-mo warm interruption ...
    # ... then the last 3 months are back ON (already 1.0): "only just begun"
    w_1963 = tongue_width_history(f_1963, dt=dt, tau=tau, w0=w0, gain=gain)
    w_1965 = tongue_width_history(f_1965, dt=dt, tau=tau, w0=w0, gain=gain)

    fig, (axf, axw) = plt.subplots(2, 1, figsize=(11, 6), sharex=True,
                                   gridspec_kw={"height_ratios": [1, 2]})
    axf.step(t, f_1963, where="mid", color="#1f3b73", lw=2,
             label="1963-like: sustained upwelling (~4 yr continuous)")
    axf.step(t, f_1965, where="mid", color="#e8593c", lw=2, ls="--",
             label="1965-like: interrupted (warm epoch ~1963-64, then re-established)")
    axf.set_ylabel("upwelling forcing", fontsize=10)
    axf.set_ylim(-0.2, 1.5)
    axf.grid(alpha=0.15)
    axf.legend(fontsize=8, loc="upper center", ncol=2)

    axw.plot(t, w_1963, color="#1f3b73", lw=2.5,
             label="1963: sustained → WIDE tongue")
    axw.plot(t, w_1965, color="#e8593c", lw=2.5, ls="--",
             label="1965: interrupted, freshly re-established → NARROW")
    axw.scatter([t[-1]], [w_1963[-1]], color="#1f3b73", zorder=5, s=60)
    axw.scatter([t[-1]], [w_1965[-1]], color="#e8593c", zorder=5, s=60)
    axw.annotate(f"  Jan endpoint w={w_1963[-1]:.1f}", xy=(t[-1], w_1963[-1]),
                 fontsize=9, color="#1f3b73", va="center", fontweight="bold")
    axw.annotate(f"  Jan endpoint w={w_1965[-1]:.1f}", xy=(t[-1], w_1965[-1]),
                 fontsize=9, color="#e8593c", va="center", fontweight="bold")
    axw.set_ylabel("cold-tongue width  $w$", fontsize=10)
    axw.set_xlabel("months before the January in question", fontsize=10)
    axw.grid(alpha=0.15)
    axw.legend(fontsize=8, loc="lower right")
    fig.suptitle("Cold-tongue width integrates upwelling history "
                 "(ocean memory ⇒ long lag)", fontsize=13, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    if savepath: fig.savefig(savepath, dpi=150, bbox_inches="tight")
    plt.show()

    print(f"  Endpoint width, 1963-like (sustained):    w = {w_1963[-1]:.2f}")
    print(f"  Endpoint width, 1965-like (interrupted):  w = {w_1965[-1]:.2f}")
    print(f"  Same ON forcing at the endpoint, yet widths differ by "
          f"{w_1963[-1]/max(w_1965[-1], 1e-9):.2f}x — the ocean integrates slowly.")
    return w_1963, w_1965
