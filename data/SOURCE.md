# Data sources

## TESS light curve

- File: `tess2019140104343-s0012-0000000066818296-0144-s_lc.fits`
- Archive: Mikulski Archive for Space Telescopes (MAST), TESS SPOC light-curve product
- TESS sector: 12
- TIC target ID: 66818296
- MAST observation ID: 65176458
- MAST data URI: `mast:TESS/product/tess2019140104343-s0012-0000000066818296-0144-s_lc.fits`
- Exact download URL: <https://mast.stsci.edu/api/v0.1/Download/file?uri=mast:TESS%2Fproduct%2Ftess2019140104343-s0012-0000000066818296-0144-s_lc.fits>
- Collection DOI: [10.17909/t9-nmc8-f686](https://doi.org/10.17909/t9-nmc8-f686) (TESS 2-minute light curves, all sectors; sector 12 used here)
- Retrieved: 2026-08-15
- SHA-256: `110b82c33046c716e86c09051e35bb1f55414f45f8a9122d3aaeecdcbf729aea`

The FITS file is stored unmodified. The analysis reads `TIME`, `PDCSAP_FLUX`,
`PDCSAP_FLUX_ERR`, and `QUALITY`. PDCSAP flux is the SPOC light curve with common
instrumental trends removed and aperture/crowding corrections applied; this does
not make it free of residual stellar or instrumental systematics.

## System parameters

- File: `system_parameters.csv`
- Service: NASA Exoplanet Archive TAP, `pscomppars` table
- Exact query: <https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name%2Chostname%2Cra%2Cdec%2Cpl_orbper%2Cpl_tranmid%2Cpl_trandur%2Cpl_rade%2Cpl_bmasse%2Cpl_eqt%2Cpl_orbsmax%2Csy_dist%2Csy_tmag%2Cst_teff%2Cst_rad%2Cst_mass%2Cdisc_year%2Cdiscoverymethod%2Cdisc_refname%2Cdisc_pubdate%2Cdisc_facility+from+pscomppars+where+pl_name%3D%27WASP-17+b%27&format=csv>
- Retrieved: 2026-08-15

The saved row is the input actually used by `scripts/analyze_transit.py`; the
analysis does not query a changing live service at run time.


## Additional TESS sectors for robustness analysis

All are unmodified standard-cadence SPOC light curves from the same [MAST TESS collection](https://doi.org/10.17909/t9-nmc8-f686).

- Sector 12: `tess2019140104343-s0012-0000000066818296-0144-s_lc.fits` (2,041,920 bytes)
  - MAST URI: `mast:TESS/product/tess2019140104343-s0012-0000000066818296-0144-s_lc.fits`
  - SHA-256: `110b82c33046c716e86c09051e35bb1f55414f45f8a9122d3aaeecdcbf729aea`
- Sector 38: `tess2021118034608-s0038-0000000066818296-0209-s_lc.fits` (1,952,640 bytes)
  - MAST URI: `mast:TESS/product/tess2021118034608-s0038-0000000066818296-0209-s_lc.fits`
  - SHA-256: `4836a46e320309dd76860d9c09187fa179b012c7b1dd7dacf7b74a5d091c8464`

## Published planetary spectrum

- Archive record: [10.5281/zenodo.14003330](https://zenodo.org/records/14003330)
- Data type: emission; instrument: JWST NIRISS/SOSS
- `data/spectra/transitspectroscopy_reduction_negative.dat` — SHA-256 `6a73427b23ba2e285d6e5809c7a8eb9859ad582c64d41ecec487ebda13b7e621`
- `data/spectra/ahsoka_reduction.dat` — SHA-256 `82518db351fab231ad138f358427d4af44536dead1ca5717f01e5ed11418200b`
- `data/spectra/supreme_spoon_reduction.dat` — SHA-256 `8b3200bf61ba929e81528d9fba72fe9542b69bb9737a80ff610f62cc6adddf30`
