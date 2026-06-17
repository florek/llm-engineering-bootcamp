import sys
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from openai import OpenAI

OLLAMA_BASE_URL = "http://localhost:11434/v1"
OLLAMA_MODEL = "llama3.2"
DEFAULT_URL = "https://pl.wikipedia.org/wiki/Sztuczna_inteligencja"
MAX_CONTENT_CHARS = 12000


def fetch_page_text(url: str) -> str:
    response = requests.get(
        url,
        timeout=30,
        headers={"User-Agent": "Mozilla/5.0 (compatible; LLMBootcamp/1.0)"},
    )
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    text = soup.get_text(separator="\n", strip=True)
    lines = [line for line in text.splitlines() if line.strip()]
    return "\n".join(lines)


def summarize_page(
    client: OpenAI,
    page_text: str,
    url: str,
) -> str:
    truncated = page_text[:MAX_CONTENT_CHARS]
    response = client.chat.completions.create(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Streść podaną treść strony internetowej po polsku. "
                    "Odpowiedź ma być zwięzła, konkretna i w punktach."
                ),
            },
            {
                "role": "user",
                "content": f"Adres strony: {url}\n\nTreść strony:\n\n{truncated}",
            },
        ],
    )
    return response.choices[0].message.content or ""


def main() -> None:
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        raise ValueError(f"Nieprawidłowy adres URL: {url}")
    client = OpenAI(
        base_url=OLLAMA_BASE_URL,
        api_key="ollama",
    )
    page_text = fetch_page_text(url)
    if not page_text.strip():
        raise ValueError(f"Nie udało się pobrać treści ze strony: {url}")
    summary = summarize_page(
        client=client,
        page_text=page_text,
        url=url,
    )
    print(summary)


if __name__ == "__main__":
    main()
