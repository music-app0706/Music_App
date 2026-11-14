from app.sources.http import get, post
from urllib.parse import quote

BASE = "https://api.listenbrainz.org/1"
LABS_BASE = "https://labs.api.listenbrainz.org"
SIMILAR_ALGORITHM = "session_based_days_7500_session_300_contribution_5_threshold_10_limit_100_filter_True_skip_30"

def user_top_artists(username: str) -> list[dict]:
    formatted_name = quote(username, safe="")
    data = get(f"{BASE}/stats/user/{formatted_name}/artists", {"range": "all_time", "count": 100})
    if not data:
        return []
    return data["payload"].get("artists", [])

def similar_artists(mbid: str) -> list[dict]:
    data = get(f"{LABS_BASE}/similar-artists/json", {"artist_mbids": mbid, "algorithm": SIMILAR_ALGORITHM})
    if not data:
        return []
    return data

def artist_popularity(mbids: list[str]) -> dict:
    if not mbids:
        return {}
    data = post(f"{BASE}/popularity/artist", {"artist_mbids": mbids})
    if not data:
        return {}
    artists = {artist["artist_mbid"]: artist["total_user_count"] for artist in data}
    return artists

def artist_top_recordings(mbid: str) -> list[dict]:
    formatted_id = quote(mbid, safe="")
    data = get(f"{BASE}/popularity/top-recordings-for-artist/{formatted_id}")
    if not data:
        return []
    return data
