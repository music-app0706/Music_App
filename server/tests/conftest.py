import pytest

from app.sources import http


@pytest.fixture(autouse=True)
def no_rate_limit_when_replaying(record_mode, monkeypatch):
    """Skip rate-limit and retry waits when tests replay recorded responses.

    Replayed tests never reach a real server, so waiting only slows them down.
    Some recordings include MusicBrainz 503s, which still exercise the retry
    path, just without the backoff. When recording new responses
    (pytest --record-mode=once), the real waits stay on so MusicBrainz isn't
    hit faster than it allows.
    """
    # record_mode comes from pytest-recording; it is "none" unless
    # --record-mode is passed.
    if record_mode == "none":
        monkeypatch.setattr(http, "MIN_INTERVAL", 0.0)
        monkeypatch.setattr(http, "RETRY_BACKOFF", 0.0)
