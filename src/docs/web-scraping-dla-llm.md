# Web scraping dla aplikacji LLM

## Po co scraping w LLM Engineering

Modele językowe nie mają dostępu do internetu w czasie rzeczywistym (chyba że używasz narzędzi/agentów). Aby model „wiedział" o treści strony WWW, trzeba ją najpierw pobrać, oczyścić z HTML i przekazać jako tekst w prompcie — to podstawowy wzorzec integracji danych zewnętrznych z LLM. Stosuje się go w generatorze broszur firmowych i w wielu pipeline'ach RAG.

## Pobieranie strony — requests

```python
response = requests.get(
    url,
    timeout=30,
    headers={"User-Agent": "Mozilla/5.0 (compatible; LLMBootcamp/1.0)"},
)
response.raise_for_status()
```

- **timeout** — zapobiega wiszącym połączeniom.
- **User-Agent** — wiele serwerów blokuje domyślny UA biblioteki `requests`; własny UA zmniejsza ryzyko odrzucenia.
- **raise_for_status()** — rzuca wyjątek przy kodach HTTP 4xx/5xx zamiast cicho przetwarzać błąd.

## Parsowanie HTML — BeautifulSoup

```python
soup = BeautifulSoup(response.text, "html.parser")
```

Parser `html.parser` jest wbudowany w Pythona — nie wymaga dodatkowych zależności systemowych.

## Czyszczenie HTML

Elementy, które nie niosą treści merytorycznej, należy usunąć:

```python
for tag in soup(["script", "style", "noscript"]):
    tag.decompose()
```

- `script` — kod JavaScript.
- `style` — definicje CSS.
- `noscript` — treść alternatywna bez JS.

Metoda `decompose()` usuwa tag wraz z dziećmi z drzewa DOM.

## Ekstrakcja tekstu

```python
text = soup.get_text(separator="\n", strip=True)
lines = [line for line in text.splitlines() if line.strip()]
return "\n".join(lines)
```

- `separator="\n"` — każdy blok HTML oddzielony nową linią.
- `strip=True` — obcina białe znaki z każdego fragmentu.
- Filtrowanie pustych linii — czytelniejszy tekst wejściowy dla modelu.

## Walidacja URL

Przed pobraniem strony warto sprawdzić poprawność adresu:

```python
parsed = urlparse(url)
if not parsed.scheme or not parsed.netloc:
    raise ValueError(f"Nieprawidłowy adres URL: {url}")
```

Wymagane są scheme (np. `https`) i netloc (domena). Sam string bez protokołu nie przejdzie walidacji.

## Obsługa pustej treści

Po pobraniu i czyszczeniu sprawdź, czy tekst nie jest pusty — strona może być pusta, zablokowana lub oparta wyłącznie o JavaScript renderowany po stronie klienta.

## Pułapki

- Strony SPA (React, Vue) często zwracają pusty HTML — scraping nie zastąpi headless browsera.
- Brak User-Agent → częste 403 Forbidden.
- Brak timeout → skrypt może zawisnąć na wolnej stronie.
- Surowy HTML w prompcie — marnowanie tokenów i gorsza jakość odpowiedzi; zawsze czyść przed wysłaniem do modelu.
