"""Checksum regression tests for every archived scientific input."""

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "data/tess2019140104343-s0012-0000000066818296-0144-s_lc.fits": "110b82c33046c716e86c09051e35bb1f55414f45f8a9122d3aaeecdcbf729aea",
    "data/tess2021118034608-s0038-0000000066818296-0209-s_lc.fits": "4836a46e320309dd76860d9c09187fa179b012c7b1dd7dacf7b74a5d091c8464",
    "data/spectra/transitspectroscopy_reduction_negative.dat": "ed4f3e84e1cfdaa6b999e3458e2a37081c05db4e91679bf889d8bf3cc0936d46",
    "data/spectra/ahsoka_reduction.dat": "7db13a522679b1b79316cc4997cd80eeadb3125625123af967fb51a54634a49c",
    "data/spectra/supreme_spoon_reduction.dat": "a18927ffea5a9f73e58020f8ab134294f06a538c3aadbbc80569fd59f124d65c",
}


def test_inputs_match_source_manifest():
    manifest = (ROOT / "data" / "SOURCE.md").read_text(encoding="utf-8")
    for relative, expected in EXPECTED.items():
        path = ROOT / relative
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected
        assert path.name in manifest and expected in manifest
