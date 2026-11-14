import time

import httpx

USER_AGENT = "MusicApp/0.1 (https://github.com/music-app0706/Music_App)"

_last_request = 0.0
MAX_RETRIES = 3

def _request(method: str, url: str, params: dict | None = None, json: dict | None = None, headers: dict | None = None) -> dict | list | None:
    global _last_request
    for attempt in range(MAX_RETRIES + 1):
        wait = 1.0 - (time.monotonic() - _last_request)

        if wait > 0:
            time.sleep(wait)

        all_headers = {"User-Agent": USER_AGENT} | (headers or {})

        response = httpx.request(method, url, params=params, json=json, headers=all_headers, timeout=10)
        _last_request = time.monotonic()

        if response.status_code == 503 and attempt < MAX_RETRIES:
            time.sleep(2 ** attempt)
            continue

        if response.status_code == 204:
            return None

        response.raise_for_status()
        return response.json()


def get(url: str, params: dict | None = None, headers: dict | None = None) -> dict | list | None:
    return _request("GET", url, params=params, headers=headers)

def post(url: str, json: dict, headers: dict | None = None) -> dict | list | None:
    return _request("POST", url, json=json, headers=headers)
