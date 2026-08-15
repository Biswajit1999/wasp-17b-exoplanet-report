# WASP-17 b — Real TESS Transit Report

<p align="center">
  <img src="figures/wasp17b_tess_transit.png" alt="Phase-folded real TESS transit light curve of WASP-17 b" width="760">
</p>

One real, public TESS SPOC light curve; one saved NASA Exoplanet Archive
ephemeris; one reproducible flat-versus-box statistical comparison.

**[Open the full report](https://biswajit1999.github.io/wasp-17b-exoplanet-report/)** — the live GitHub Pages version.

## Data sources

- **System parameters** — the saved `pscomppars` row from the [NASA Exoplanet Archive TAP service](https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name%2Chostname%2Cra%2Cdec%2Cpl_orbper%2Cpl_tranmid%2Cpl_trandur%2Cpl_rade%2Cpl_bmasse%2Cpl_eqt%2Cpl_orbsmax%2Csy_dist%2Csy_tmag%2Cst_teff%2Cst_rad%2Cst_mass%2Cdisc_year%2Cdiscoverymethod%2Cdisc_refname%2Cdisc_pubdate%2Cdisc_facility+from+pscomppars+where+pl_name%3D%27WASP-17+b%27&format=csv).
- **Observed photometry** — unmodified MAST file `tess2019140104343-s0012-0000000066818296-0144-s_lc.fits`, TESS Sector 12, DOI [10.17909/t9-nmc8-f686](https://doi.org/10.17909/t9-nmc8-f686). This is a real SPOC reduced light curve, not simulated data.
- Exact URLs, IDs, retrieval date, and SHA-256 checksum are in [`data/SOURCE.md`](data/SOURCE.md).

## Reproduce the analysis

```bash
pip install -r requirements.txt
python scripts/analyze_transit.py
python scripts/analyze_multisector.py
python scripts/analyze_spectrum.py
pytest tests/ -v
```

The script keeps finite `QUALITY == 0` cadences, normalizes `PDCSAP_FLUX`,
applies one symmetric robust outlier rule, and examines ±2.5 published transit
durations around the fixed NASA ephemeris. It compares a weighted constant with
a two-level box whose depth is fitted. Timing and duration are not searched.

## What the numbers show

| Quantity | Result |
|---|---:|
| TESS sector | 12 |
| Cadences in comparison | 3332 |
| Fitted box depth | 8749.2 ± 84.4 ppm |
| Flat χ² / dof / p | 32632.60 / 3331 / < 1e-300 |
| Box χ² / dof / p | 21892.54 / 3330 / < 1e-300 |
| Improvement Δχ² / Δdof / p | 10740.06 / 1 / < 1e-300 |

The fixed-window box improves strongly on a flat light curve for these data. This establishes only how these archived fluxes compare with this
pre-specified box model. It does not independently confirm the planet or identify
an atmosphere.

<!-- MULTISECTOR-UPGRADE-START -->
## Multi-sector robustness and correlated noise

The fixed archive ephemeris was fitted independently in 2 usable sector(s) (S12, S38). Formal depth errors were inflated by sqrt(max(reduced chi-square, 1)) times the residual time-averaging beta factor (observed range 4.66-4.85). The robust inverse-variance depth is 8096.4 +/- 690.3 ppm; Cochran Q = 0.79 for 1 dof (p = 0.3756). These scaled errors address underestimated scatter and short-timescale correlation, but they are not a full Gaussian-process or physical limb-darkened transit fit.

<p align="center"><img src="figures/wasp17b_multisector_transits.png" alt="Independent sector transit fits for WASP-17 b" width="760"></p>

<p align="center"><img src="figures/wasp17b_depth_consistency.png" alt="Sector depth consistency for WASP-17 b" width="760"></p>

<p align="center"><img src="figures/wasp17b_noise_diagnostics.png" alt="Residual RMS time-averaging diagnostic for WASP-17 b" width="760"></p>

The per-sector table is in [`figures/multisector_statistics.csv`](figures/multisector_statistics.csv). Regenerate all three figures with `python scripts/analyze_multisector.py`.
<!-- MULTISECTOR-UPGRADE-END -->

<!-- SPECTRUM-UPGRADE-START -->
## Published planetary spectrum

<p align="center"><img src="figures/wasp17b_published_spectrum.png" alt="Published emission spectrum of WASP-17 b" width="760"></p>

Three independent published NIRISS/SOSS reductions are plotted and tested against their own weighted-flat spectra. Showing all reductions makes pipeline-dependent scatter visible; no molecular abundance is inferred from these flatness tests.

Source: [10.5281/zenodo.14003330](https://zenodo.org/records/14003330) (JWST NIRISS/SOSS). Exact files and checksums are in [`data/SOURCE.md`](data/SOURCE.md); complete numerical results are in [`figures/spectrum_statistics.csv`](figures/spectrum_statistics.csv).
<!-- SPECTRUM-UPGRADE-END -->

## System context

- Radius: 20.96 Earth radii
- Mass: 247.91 Earth masses
- Orbital period: 3.735430 days
- Transit duration: 4.423 hours
- Semi-major axis: 0.0515 AU
- Equilibrium temperature: 1755 K
- Host: WASP-17 · distance 405.91 pc
- Discovery: 2009 by Transit (SuperWASP)

## Limitations

- A box is not a limb-darkened physical transit model and does not retrieve radius ratio, impact parameter, or stellar density.
- Period, mid-transit epoch, and duration are fixed to one NASA composite row; their uncertainties and transit-timing variations are not propagated.
- SPOC PDCSAP processing, crowding corrections, stellar variability, time-correlated noise, and underestimated point uncertainties can make absolute χ² p-values poor even when the relative comparison is informative.
- The χ² improvement uses one additional fitted depth parameter and no timing search. It is not a blind detection false-alarm probability, and nearby-star contamination is not ruled out.
- Published global fits combine sectors, instruments, detrending choices, limb darkening, and astrophysical priors. This deliberately smaller test does not replace them.

## Repository structure

```text
README.md
index.html
requirements.txt
data/                       unmodified TESS FITS + NASA row + SOURCE.md
scripts/analyze_transit.py  real-data analysis and figure generation
figures/                    generated plot + summary_statistics.csv
tests/                      real-data regression tests
.github/workflows/tests.yml CI on every push and pull request
LICENSE                     MIT
```

## References

1. [Anderson et al. 2010](https://ui.adsabs.harvard.edu/abs/2010ApJ...709..159A/abstract) — discovery reference as listed by the NASA Exoplanet Archive.
2. Ricker, G. R. et al. (2015), *Transiting Exoplanet Survey Satellite (TESS)*, JATIS 1, 014003, [doi:10.1117/1.JATIS.1.1.014003](https://doi.org/10.1117/1.JATIS.1.1.014003).
3. TESS Team, *TESS Light Curves — All Sectors*, MAST, [doi:10.17909/t9-nmc8-f686](https://doi.org/10.17909/t9-nmc8-f686); Sector 12 used here.
4. [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/), `pscomppars` TAP row retrieved 2026-08-15.

## Author

Biswajit Jana — [Portfolio](https://biswajit1999.github.io/Biswajit_Jana.github.io/) · [GitHub](https://github.com/Biswajit1999) · [LinkedIn](https://www.linkedin.com/in/biswajit-jana-27011a151/) · [ORCID](https://orcid.org/0009-0002-2411-1891)
