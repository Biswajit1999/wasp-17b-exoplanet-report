# Methods and inference boundary

## Shared-observation reduction comparison

The three committed spectra are independent *reductions* of one NIRISS/SOSS
secondary-eclipse observation, not independent observing replicates. Each is
tested against its own inverse-variance weighted constant eclipse depth. The
flat-model chi-square is therefore a descriptive structure test conditional
on the supplied marginal errors; it is not a molecular detection statistic.

For every reduction pair, the second spectrum is linearly interpolated onto
the first spectrum's grid over their common wavelength range. We report the
median signed and absolute difference, RMS difference, and a normalized
difference using the quadrature sum of reported errors. Because the pipelines
share photons and systematic effects, that normalized quantity is labelled an
`independence z` reference and is not assigned a probability.

Negative eclipse depths are retained. They are permissible noise realizations
and nuisance-fit outcomes, especially below 1 µm where reflected and thermal
components are difficult to separate. The repository does not censor them or
replace them with a positivity prior.

## Claim boundary

The 6.4-sigma water detection, supersolar water abundance, and non-inverted
temperature-pressure profile come from the peer-reviewed Gressier et al.
retrieval (AJ 169, 57), not from the flat-line or cross-pipeline diagnostics in
this repository. No abundance posterior or temperature profile is reproduced.
