from app.sources.http import get

BASE = "https://musicbrainz.org/ws/2"

def search_artist(name: str, limit: int = 5) -> list[dict]:
    escaped = name.replace("\\", "\\\\").replace('"', '\\"')
    query = f'artist:"{escaped}"'
    data = get(f"{BASE}/artist", {"query": query, "fmt": "json", "limit": limit})
    return data.get("artists", [])