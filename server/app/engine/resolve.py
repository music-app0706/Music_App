from difflib import SequenceMatcher

from app.sources.musicbrainz import search_artist

MIN_SCORE = 90
MIN_NAME_SIMILARITY = 0.8

def _similar(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def resolve_artist(name: str) -> str | None:
    
    
    cleaned = name.strip()
    if not cleaned:
        return None
    
    results = search_artist(cleaned)
    good = [artist for artist in results if artist.get("score", 0) >= MIN_SCORE 
    and _similar(artist["name"], cleaned) >= MIN_NAME_SIMILARITY]
    
    if not good: 
        return None
    
    for artist in good:
        if artist["name"].lower() == cleaned.lower():
            return artist["id"]
    return good[0]["id"]

def resolve_artists(names: list[str]) -> tuple[dict[str, str], list[str]]:
    matched = {}
    unmatched = []

    for name in names:
        mbid = resolve_artist(name)
        if mbid:
            matched[name] = mbid
        else:
            unmatched.append(name)

    return matched, unmatched