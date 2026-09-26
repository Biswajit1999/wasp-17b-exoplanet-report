# Validation

- Every two TESS FITS files and three NIRISS spectrum files are checked against
  the SHA-256 values recorded in `data/SOURCE.md`.
- Each reduction contains 151–155 finite spectral bins spanning approximately
  0.60–2.82 µm with positive reported uncertainties.
- The three flat-model reduced chi-square values reproduce 12.45, 8.68, and
  10.35; all reject a constant eclipse depth under their marginal-error model.
- Negative depths are preserved: 21/155 for transitspectroscopy, 0/151 for
  Ahsoka, and 25/152 for supreme-SPOON. Every negative bin lies below 1 µm.
- Pairwise median absolute differences are 61.5, 41.9, and 41.7 ppm. Median
  absolute independence-reference z values are 0.68, 0.48, and 0.42.
- Generated tables and both spectrum figures are required to be non-empty.
