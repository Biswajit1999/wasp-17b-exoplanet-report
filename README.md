# WASP-17 b: Water Emission from an Inflated Hot Jupiter
<!-- RESEARCH-IDENTITY-START -->
**Independent research report by [Biswajit Jana](https://biswajit1999.github.io/Biswajit_Jana.github.io/)** · [Live report](https://biswajit1999.github.io/wasp-17b-exoplanet-report/) · [ORCID](https://orcid.org/0009-0002-2411-1891) · [Complete research portfolio](https://biswajit1999.github.io/Biswajit_Jana.github.io/research/exoplanets/)
<!-- RESEARCH-IDENTITY-END -->





<!-- TARGET-IDENTITY-START -->
<p align="center">
  <img src="assets/artist_concept.webp" alt="Artist's interpretation of WASP-17 b near its host star" width="900">
</p>

<p align="center"><em>AI-generated artist's interpretation informed by the measured system properties; not a direct image.</em></p>

**Inflated hot Jupiter · dayside emission · JWST + TESS**

An exceptionally inflated giant planet examined through a corrected TESS transit and three independent reductions of its JWST/NIRISS dayside emission spectrum.
<!-- TARGET-IDENTITY-END -->
<p align="center">
  <img src="figures/wasp17b_tess_transit.png" alt="Phase-folded real TESS transit light curve of WASP-17 b" width="760">
</p>


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
python scripts/analyze_atmospheric_evidence.py
pytest tests/ -v
```

The script keeps finite `QUALITY == 0` cadences, normalizes `PDCSAP_FLUX`, and applies one symmetric robust outlier rule. A local linear null is compared with a circular quadratic-limb-darkened transit. The archive period and predicted phase are retained, while midpoint, radius ratio, impact parameter, baseline, and baseline slope are fitted inside a bounded window. The limb-darkening coefficients and scaled semi-major axis are fixed and disclosed in the CSV.

## What the corrected fit shows

| Quantity | Result |
|---|---:|
| TESS sector | 12 |
| Cadences in fitted window | 4044 |
| Transit support | ΔBIC ≥ 10 |
| Midpoint correction | +1.444 h ± 0.34 min |
| Model mid-transit depth | 16785.5 ± 100.3 ppm |
| Radius ratio Rp/Rs | 0.12090 |
| Fitted / published duration | 4.280 / 4.423 h |
| Linear null χ² / dof / BIC | 34111.14 / 4042 / 34127.75 |
| Transit χ² / dof / BIC | 3993.76 / 4039 / 4035.28 |
| ΔBIC (null − transit) | 30092.46 |

The timing-adjusted transit is strongly preferred by ΔBIC = 30092.5. Its fitted midpoint is +1.444 hours from the historical prediction; the model's mid-transit depth is 16785.5 ± 100.3 ppm. A fitted timing correction can diagnose ephemeris drift, but this single-sector fit is not a replacement for a global transit-timing analysis.

<!-- MULTISECTOR-UPGRADE-START -->
## Multi-sector robustness and correlated noise

The archive prediction was timing-adjusted independently in 2 fitted sector(s) (S12, S38), of which 2 meet Delta BIC >= 10. Formal depth errors were inflated by sqrt(max(reduced chi-square, 1)) times the residual time-averaging beta factor (observed range 1.28-1.46). The robust inverse-variance model depth across supported sectors is 16828.0 +/- 89.3 ppm; Cochran Q = 0.14 for 1 dof (p = 0.7131). These scaled errors address underestimated scatter and short-timescale correlation, but they are not a full Gaussian-process or physical limb-darkened transit fit.

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

<!-- ATMOSPHERE-EVIDENCE-START -->
## Atmospheric evidence: detection, limit, or unknown?

<p align="center"><img src="figures/molecular_evidence.png" alt="Source-graded atmospheric evidence for WASP-17 b" width="820"></p>

All three archived reductions reject a wavelength-independent dayside spectrum. The molecular attribution is taken from the paper's atmospheric retrieval rather than inferred from the flat-spectrum test reproduced here.

| Species | Status | Evidence | Basis |
|---|---|---|---|
| H2O | reported detection | 6.4 sigma | peer-reviewed/preprint retrieval |
| CO / CO2 | not established here | no repository retrieval | wavelength structure alone is non-specific |
| O2 | no evidence | not reported | no molecular-oxygen inference |

Primary source: [Gressier et al. 2024, JWST-TST DREAMS](https://arxiv.org/abs/2410.08149). The table is also available as [`data/atmospheric_evidence.csv`](data/atmospheric_evidence.csv). Oxygen-bearing species such as H2O, CO2, and SO2 are **not** evidence for molecular oxygen (O2) or a biosignature.
<!-- ATMOSPHERE-EVIDENCE-END -->

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

- The orbit is assumed circular and the quadratic limb-darkening coefficients are fixed representative values; they are not atmosphere-grid interpolations.
- The scaled semi-major axis is derived from the saved composite semi-major axis and stellar radius; their uncertainties are not propagated.
- Midpoint freedom corrects accumulated ephemeris error but introduces a bounded timing search. ΔBIC, not a naïve one-parameter p-value, is used as the support gate.
- PDCSAP processing, dilution, stellar variability, transit-timing variations, and long-timescale covariance can still bias the inferred geometry.
- Radius ratio, impact parameter, and fixed limb darkening are correlated. Published global fits with physical priors and simultaneous detrending remain authoritative.

## Repository structure

```text
README.md
index.html
requirements.txt
data/                       unmodified TESS FITS + NASA row + SOURCE.md
scripts/analyze_transit.py  timing-adjusted limb-darkened transit fit
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
