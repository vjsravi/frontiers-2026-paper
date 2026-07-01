#!/usr/bin/env python3
"""Decision-curve analysis figure (all 11 binaries) at the balanced 50% test prevalence.
Reads the precomputed decision_curves/{b00..b10}.csv from the handoff and renders a
3-column grid of net-benefit-vs-threshold panels. Output: fig_decision_curves.pdf.
"""
import csv, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SRC = "review-comments/handoff_extracted3/handoff/result_tables/decision_curves"
OUT = "fig_decision_curves.pdf"

NAVY = "#1c3d52"
GRAY = "#888888"
LGRAY = "#bbbbbb"

titles = {
    "b00": "B00: acute resp. vs non-resp.",
    "b01": "B01: acute infection vs chronic",
    "b02": "B02: infection vs non-infection",
    "b03": "B03: lower vs upper (LRI vs URI)",
    "b04": "B04: pneumonia vs bronchitis",
    "b05": "B05: pneumonia vs non-pneum. LRI",
    "b06": "B06: sinusitis vs other URI",
    "b07": "B07: GAS vs other pharyngitis",
    "b08": "B08: influenza vs other acute",
    "b09": "B09: COVID-19 vs other acute",
    "b10": "B10: bacterial vs viral",
}
order = ["b00","b01","b02","b03","b04","b05","b06","b07","b08","b09","b10"]

def load(b):
    thr, nbm, nba = [], [], []
    with open(os.path.join(SRC, f"{b}.csv")) as f:
        for row in csv.DictReader(f):
            thr.append(float(row["threshold"]))
            nbm.append(float(row["nb_model"]))
            nba.append(float(row["nb_treat_all"]))
    return thr, nbm, nba

plt.rcParams.update({"font.size": 9, "font.family": "sans-serif", "axes.linewidth": 0.8})
fig, axes = plt.subplots(4, 3, figsize=(9.2, 10.4))
axes = axes.ravel()

for i, b in enumerate(order):
    ax = axes[i]
    thr, nbm, nba = load(b)
    ax.axhline(0.0, color=LGRAY, lw=1.2, label="Treat none")
    ax.plot(thr, nba, color=GRAY, lw=1.3, ls="--", label="Treat all")
    ax.plot(thr, nbm, color=NAVY, lw=1.8, label="Voice model")
    ax.set_xlim(0, 0.8)
    ax.set_ylim(-0.10, 0.55)
    ax.set_title(titles[b], fontsize=8.5)
    ax.grid(True, color="#e6e6e6", lw=0.6)
    ax.set_axisbelow(True)
    if i % 3 == 0:
        ax.set_ylabel("Net benefit")
    if i >= 8:
        ax.set_xlabel("Threshold probability")

# legend in the 12th (empty) slot
axes[11].axis("off")
h, l = axes[0].get_legend_handles_labels()
# reorder so model is first
order_leg = [l.index("Voice model"), l.index("Treat all"), l.index("Treat none")]
axes[11].legend([h[k] for k in order_leg], [l[k] for k in order_leg],
                loc="center", frameon=False, fontsize=10, title="At 50% test prevalence")

fig.tight_layout(h_pad=1.4, w_pad=1.2)
fig.savefig(OUT, bbox_inches="tight")
print("wrote", OUT)
