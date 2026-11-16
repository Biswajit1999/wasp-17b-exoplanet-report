# Scientific methods and limitations

WASP-17 b: two independent diagnostics: (1) weighted paired-reduction offset with user-assumed within-bin cross-pipeline correlation, (2) contiguous-bin deletion stability. Both reductions share photons. Wavelength grids must be aligned before calling; no cross-wavelength covariance or interpolation covariance is inferred. These are sensitivity diagnostics, not detection significance. Tests use synthetic values. AI-assisted implementation; Biswajit Jana requested as sole Git author/committer. No real-data result is claimed.

Run: `python -m unittest discover -s tests -p 'test_pipeline_robustness.py'`.
