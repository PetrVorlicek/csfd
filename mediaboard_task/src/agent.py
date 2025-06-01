import requests


def fetch_page(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text


def get_ledger_suffix(index: int) -> str:
    url_suffix = "zebricky/filmy/nejlepsi/"

    match index:
        case 0:
            return url_suffix
        case index if index in range(1, 10):
            return f"{url_suffix}?from={index*100}"
        case _:
            raise ValueError("Invalid index for best movie page.")
