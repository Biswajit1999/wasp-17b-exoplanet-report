from __future__ import annotations
import csv
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "spectra"
FIGURES = ROOT / "figures"
STATS_FILE = FIGURES / "spectrum_statistics.csv"

def flat_test(values, errors):
    values, errors = np.asarray(values, float), np.asarray(errors, float)
    good = np.isfinite(values) & np.isfinite(errors) & (errors > 0)
    values, errors = values[good], errors[good]
    weights = 1 / errors**2
    mean = np.sum(weights * values) / np.sum(weights)
    statistic = np.sum(((values - mean) / errors)**2)
    dof = len(values) - 1
    return {"n": len(values), "mean": mean, "chi2": statistic, "dof": dof,
            "p": chi2.sf(statistic, dof)}

def offset_model_test(wavelength, values, errors, model_wavelength, model_values):
    model = np.interp(wavelength, model_wavelength, model_values)
    weights = 1 / errors**2
    offset = np.sum(weights * (values - model)) / np.sum(weights)
    statistic = np.sum(((values - model - offset) / errors)**2)
    dof = len(values) - 1
    return {"n": len(values), "offset": offset, "chi2": statistic,
            "dof": dof, "p": chi2.sf(statistic, dof), "model": model + offset}

def write_rows(rows):
    fields = sorted({key for row in rows for key in row})
    with STATS_FILE.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader(); writer.writerows(rows)

FIGURE_FILE = FIGURES / "wasp17b_published_spectrum.png"

def load_reductions():
    first = np.loadtxt(DATA / "transitspectroscopy_reduction_negative.dat")
    ahsoka = np.loadtxt(DATA / "ahsoka_reduction.dat")
    spoon = np.loadtxt(DATA / "supreme_spoon_reduction.dat")
    return [("transitspectroscopy", first[:, 0], first[:, 1] * 1e6, first[:, 2] * 1e6),
            ("ahsoka", ahsoka[:, 0], ahsoka[:, 2], ahsoka[:, 3]),
            ("supreme-SPOON", spoon[:, 0], spoon[:, 1], spoon[:, 2])]

def main():
    FIGURES.mkdir(exist_ok=True); reductions = load_reductions(); rows = []
    fig, ax = plt.subplots(figsize=(9.2, 5.3))
    for label, wavelength, depth, error in reductions:
        result = flat_test(depth, error); rows.append({"comparison": label + " vs weighted flat", **result})
        ax.errorbar(wavelength, depth, yerr=error, fmt="o", ms=2.3, alpha=.5, label=label)
    write_rows(rows)
    ax.set(xlabel="Wavelength [micron]", ylabel="Planet/star flux ratio [ppm]",
           title="WASP-17 b: three published JWST NIRISS/SOSS eclipse reductions")
    ax.grid(alpha=.2); ax.legend(frameon=False, fontsize=8); fig.tight_layout()
    fig.savefig(FIGURE_FILE, dpi=190); plt.close(fig)
    return {"rows": rows, "n": min(row["n"] for row in rows)}

if __name__ == "__main__":
    result = main(); print(f"WASP-17 b: three reductions; at least {result['n']} bins each")
