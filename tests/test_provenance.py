"""Checksum regression tests for every archived scientific input."""

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "data/tess2019140104343-s0012-0000000066818296-0144-s_lc.fits": "110b82c33046c716e86c09051e35bb1f55414f45f8a9122d3aaeecdcbf729aea",
    "data/tess2021118034608-s0038-0000000066818296-0209-s_lc.fits": "4836a46e320309dd76860d9c09187fa179b012c7b1dd7dacf7b74a5d091c8464",
    "data/spectra/transitspectroscopy_reduction_negative.dat": "6a73427b23ba2e285d6e5809c7a8eb9859ad582c64d41ecec487ebda13b7e621",
    "data/spectra/ahsoka_reduction.dat": "82518db351fab231ad138f358427d4af44536dead1ca5717f01e5ed11418200b",
    "data/spectra/supreme_spoon_reduction.dat": "8b3200bf61ba929e81528d9fba72fe9542b69bb9737a80ff610f62cc6adddf30",
}


def test_inputs_match_source_manifest():
    manifest = (ROOT / "data" / "SOURCE.md").read_text(encoding="utf-8")
    for relative, expected in EXPECTED.items():
        path = ROOT / relative
        content = path.read_bytes()
        if path.suffix == ".dat":
            content = content.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        assert hashlib.sha256(content).hexdigest() == expected
        assert path.name in manifest and expected in manifest
