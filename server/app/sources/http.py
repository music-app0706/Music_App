import time

import httpx

USER_AGENT = "MusicApp/0.1 (https://github.com/music-app0706/Music_App)"

_last_request = 0.0
MAX_RETRIES = 3

def get(url: str, params: dict | None = None) -> dict:
    global _last_request
    for attempt in range(MAX_RETRIES + 1):
        wait = 1.0 - (time.monotonic() - _last_request)
        if wait > 0:
            time.sleep(wait)

        response = httpx.get(url, params=params, headers={"User-Agent": USER_AGENT}, timeout=10)
        _last_request = time.monotonic()

        if response.status_code == 503 and attempt < MAX_RETRIES:
            time.sleep(2 ** attempt)
            continue 

        response.raise_for_status()
        return response.json()