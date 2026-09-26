"""Reproduction checks for the archived published spectrum."""
from pathlib import Path

import analyze_spectrum as spectrum
import numpy as np


def test_spectrum_analysis_is_finite_and_reproducible():
    result = spectrum.main()
    assert result["n"] == 151
    assert len(result["rows"]) == 3
    assert len(result["pairs"]) == 3
    assert all(np.isfinite(row["chi2"]) and row["dof"] > 0 for row in result["rows"])
    assert all(row["reduced_chi2"] > 8 for row in result["rows"])
    assert [row["negative_bins"] for row in result["rows"]] == [21, 0, 25]
    assert all(pair["median_abs_independence_z"] < 1 for pair in result["pairs"])
    for path in (spectrum.STATS_FILE, spectrum.AGREEMENT_FILE,
                 spectrum.FIGURE_FILE, spectrum.AGREEMENT_FIGURE):
        assert Path(path).is_file() and Path(path).stat().st_size > 100
