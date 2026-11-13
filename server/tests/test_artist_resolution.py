import pytest

from app.engine.resolve import resolve_artist, resolve_artists

RADIOHEAD = "a74b1b7f-71a5-4011-9441-d0b5e4122711"
NIRVANA = "5b11f4ce-a62d-471e-81fc-a69a8278c7da"

@pytest.mark.vcr
def test_known_artist_resolves():
    assert resolve_artist("Radiohead") == RADIOHEAD

@pytest.mark.vcr
def test_ambiguous_name_picks_best_match():
    assert resolve_artist("Nirvana") == NIRVANA

@pytest.mark.vcr
def test_messy_input_still_resolves():
    assert resolve_artist("  radiohead  ") == RADIOHEAD

@pytest.mark.vcr
def test_unknown_artist_is_unmatched():
    matched, unmatched = resolve_artists(["Radiohead", "zzqx not a real band 9381"])
    assert matched == {"Radiohead": RADIOHEAD}
    assert unmatched == ["zzqx not a real band 9381"]