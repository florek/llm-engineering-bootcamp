# Web scraping dla aplikacji LLM

## Po co scraping w LLM Engineering

Modele językowe nie mają dostępu do internetu w czasie rzeczywistym (chyba że używasz narzędzi lub agentów). Aby model „wiedział" o treści strony WWW, trzeba ją najpierw pobrać, oczyścić z HTML i przekazać jako tekst w prompcie — to podstawowy wzorzec integracji danych zewnętrznych z LLM. Stosuje się go w generatorze broszur firmowych i w wielu pipeline'ach RAG.

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

Elementy, które nie niosą treści merytorycznej, należy usunąć z ciała strony przed ekstrakcją tekstu. W praktyce kursu typowo usuwa się m.in.:

- `script` — kod JavaScript,
- `style` — definicje CSS,
- `noscript` — treść alternatywna bez JS,
- `img`, `input` — elementy UI bez wartości tekstowej dla streszczenia.

```python
for tag in soup.body(["script", "style", "img", "input"]):
    tag.decompose()
```

Metoda `decompose()` usuwa tag wraz z dziećmi z drzewa DOM — w przeciwieństwie do samego wyciągnięcia tekstu, całkowicie wycina te elementy ze struktury HTML przed ekstrakcją treści.
## Ekstrakcja tekstu

```python
text = soup.get_text(separator="\n", strip=True)
lines = [line for line in text.splitlines() if line.strip()]
return "\n".join(lines)
```

- `separator="\n"` — każdy blok HTML oddzielony nową linią.
- `strip=True` — obcina białe znaki z każdego fragmentu.
- Filtrowanie pustych linii — czytelniejszy tekst wejściowy dla modelu.

Często łączy się tytuł strony z oczyszczonym tekstem ciała i **obcina wynik do rozsądnego limitu znaków** (np. ok. 2000 w prostym narzędziu labowym) — chroni to okno kontekstu i koszt tokenów przed wrzuceniem całej długiej strony do promptu.

## Ekstrakcja linków

Poza tekstem strony scraper może zebrać odnośniki z elementów `<a>`. Dla każdego linku warto zachować zarówno tekst widoczny dla użytkownika, jak i wartość atrybutu `href` — sam adres nie zawsze wyjaśnia, dokąd prowadzi.

Lista linków pozwala modelowi wskazać podstrony warte dalszego pobrania, np. „O nas”, „Kariera” albo „Kontakt”. To naturalne rozszerzenie prostego streszczania jednej strony w kierunku generatora broszur analizującego wiele powiązanych źródeł.

HTML najlepiej sparsować raz i z tego samego drzewa wyciągnąć potrzebne dane. Powtórne parsowanie identycznej odpowiedzi jest zbędną pracą, a odnośniki bez `href` trzeba pominąć albo jawnie oznaczyć.

## Walidacja URL

Przed pobraniem strony warto sprawdzić poprawność adresu:

```python
parsed = urlparse(url)
if not parsed.scheme or not parsed.netloc:
    raise ValueError(f"Nieprawidłowy adres URL: {url}")
```

Wymagane są scheme (np. `https`) i netloc (domena). Sam string bez protokołu nie przejdzie walidacji.

## Obsługa pustej treści

Po pobraniu i czyszczeniu sprawdź, czy tekst nie jest pusty — strona może być pusta, zablokowana lub oparta wyłącznie o JavaScript renderowany po stronie klienta. Pusty wynik powinien zakończyć się wyjątkiem (np. `ValueError`) zamiast wysyłania pustego promptu do modelu — model bez danych wejściowych może wygenerować halucynację.

## Pułapki

- Strony SPA (React, Vue) często zwracają pusty HTML — scraping nie zastąpi headless browsera.
- Brak User-Agent → częste 403 Forbidden.
- Brak timeout → skrypt może zawisnąć na wolnej stronie.
- Surowy HTML w prompcie — marnowanie tokenów i gorsza jakość odpowiedzi; zawsze czyść przed wysłaniem do modelu.
