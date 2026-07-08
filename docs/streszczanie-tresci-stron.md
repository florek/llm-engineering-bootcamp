# Streszczanie treści stron WWW przez LLM

## Podział na funkcje

Pipeline streszczania w ćwiczeniu jest rozdzielony na osobne funkcje:

- **pobieranie i czyszczenie** — osobna funkcja przyjmuje URL, zwraca czysty tekst strony; nie wywołuje modelu,
- **streszczanie** — osobna funkcja przyjmuje tekst i URL, buduje prompt i wywołuje model,
- **orchestracja** — funkcja `main()` waliduje wejście, tworzy klienta, łączy kroki i wypisuje wynik.

Taki podział pozwala testować warstwę danych bez wywoływania LLM (np. mockowanie pobrania strony) i ponownie używać logiki scrapingu w innych pipeline'ach.

## Pipeline streszczania

Typowy przepływ w ćwiczeniu streszczania strony:

1. Pobierz URL (argument CLI lub domyślny adres).
2. Zwaliduj URL (`urlparse`).
3. Pobierz i wyczyść HTML → czysty tekst.
4. Obetnij tekst do limitu znaków.
5. Wyślij do modelu z instrukcją systemową i treścią użytkownika.
6. Wypisz streszczenie.

To wzorzec wielu aplikacji GenAI: **pobierz dane → przygotuj prompt → wywołaj model → zwróć wynik**.

## Ograniczenie długości wejścia

Lokalne modele mają ograniczone okno kontekstu. Długa strona Wikipedia może mieć setki tysięcy znaków — model nie przyjmie całości.

Rozwiązanie: obcięcie tekstu przed wysłaniem, np. do **12 000 znaków**:

```python
truncated = page_text[:MAX_CONTENT_CHARS]
```

Obcięcie od początku strony jest proste, ale skuteczne na start — końcówka długiego artykułu wówczas ginie. W produkcji lepsze strategie to chunking (podział na fragmenty), map-reduce (streszczenie partiami) lub RAG (wyszukiwanie najistotniejszych fragmentów).

## Prompt engineering dla streszczenia

### Wiadomość systemowa

Ustawia reguły globalne:

- język odpowiedzi (np. polski),
- format (zwięzłe punkty),
- styl (konkretny, bez lania wody).

Przykład: *„Streść podaną treść strony internetowej po polsku. Odpowiedź ma być zwięzła, konkretna i w punktach."*

### Wiadomość użytkownika

Zawiera kontekst i dane:

- adres URL (pomaga modelowi zrozumieć źródło),
- treść strony (obcięty tekst).

Format: `Adres strony: {url}\n\nTreść strony:\n\n{truncated}`

## Model i klient

Używany jest lokalny model `llama3.2` przez Ollamę z klientem OpenAI SDK (`base_url` lokalny, `api_key="ollama"`).

## Argumenty CLI

Skrypt przyjmuje opcjonalny URL jako pierwszy argument:

```python
url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL
```

Bez argumentu używany jest domyślny adres (strona o sztucznej inteligencji na polskiej Wikipedii).

## Walidacja i obsługa błędów

Pipeline streszczania sprawdza poprawność danych na dwóch etapach:

- **walidacja URL** — przed pobraniem strony; nieprawidłowy adres (brak scheme lub netloc) kończy się wyjątkiem `ValueError`,
- **walidacja treści** — po pobraniu i czyszczeniu HTML; pusty tekst (strona zablokowana, SPA, błąd serwera) również kończy się `ValueError` zamiast wysyłania pustego promptu do modelu.

Odpowiedź modelu jest bezpiecznie odczytywana przez `response.choices[0].message.content or ""`, bo pole `content` może być `None`.

## Związek z RAG i generatorami broszur

Streszczanie pojedynczej strony to uproszczona wersja pipeline'u generatora broszur:

- zamiast jednej strony → wiele stron firmy,
- zamiast prostego obcięcia → chunking + embeddings + vector DB,
- zamiast jednego streszczenia → strukturalny raport (produkty, zespół, kontakt).

Ten wzorzec (pobierz → oczyść → prompt → model) jest fundamentem bardziej zaawansowanych systemów.

## Pułapki

- Obcięcie od początku strony — końcówka artykułu ginie; przy długich tekstach rozważ chunking.
- Brak wiadomości systemowej — model może odpowiedzieć w złym języku lub formacie.
- Zbyt ogólna instrukcja — odpowiedź będzie rozwlekła; precyzyjny system prompt poprawia jakość.
- Brak walidacji pustej treści — model dostanie pusty prompt i wygeneruje halucynację.
