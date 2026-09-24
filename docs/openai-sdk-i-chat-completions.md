# OpenAI SDK i Chat Completions

## Czym jest OpenAI Python SDK

Biblioteka `openai` to **lekki klient HTTP** (Python client library) wokół endpointu Chat Completions. Nie zawiera kodu ani wag modelu — tylko ułatwia wywołania API z poziomu Pythona zamiast ręcznego składania JSON i nagłówków. Ten sam wzorzec można zrealizować zwykłym `requests.post` na endpoint `/v1/chat/completions` z nagłówkiem Authorization i payloadem `model` + `messages`.

## OpenAI Compatible Endpoints

Chat Completions API wymyślone przez OpenAI stało się de facto standardem. Inni dostawcy (np. Google Gemini, lokalna Ollama) wystawiają **kompatybilne endpointy** o tej samej strukturze żądań i odpowiedzi. Dzięki temu jeden klient SDK działa z wieloma backendami — wystarczy zmienić `base_url` i `api_key`:

```python
client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=google_api_key,
)
```

Mimo że w kodzie widać klasę `OpenAI`, przy innym `base_url` wywołujesz model innego dostawcy — nie model OpenAI.

## OpenAI Python SDK z Ollamą

Biblioteka `openai` domyślnie łączy się z API OpenAI w chmurze. Można ją skonfigurować do pracy z Ollamą, przekazując własny `base_url` i dowolny `api_key`.

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",
)
```

Parametr `api_key` jest wymagany przez SDK, ale Ollama go nie weryfikuje — wystarczy dowolna wartość (np. `"ollama"`).
## Weryfikacja połączenia z serwerem

Przed pierwszym wywołaniem chat completion warto sprawdzić, czy serwer Ollama odpowiada — np. prostym żądaniem HTTP na `http://localhost:11434`. Jeśli serwer nie działa, wywołanie `client.chat.completions.create()` zakończy się błędem połączenia niezależnie od poprawności reszty kodu.

## Chat Completions

Nazwa **Chat Completions** podkreśla ideę API: dostajesz historię rozmowy (listę wiadomości) i prosisz model, by **dokończył rozmowę** — przewidział kolejną wiadomość asystenta. To nadal predykcja kolejnych tokenów, tylko ujęta w formacie konwersacji.

Główna metoda to `client.chat.completions.create()`:

```python
response = client.chat.completions.create(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "Tell me a fun fact"}
    ],
)
```

Odpowiedź modelu:

```python
response.choices[0].message.content
```

Struktura odpowiedzi jest identyczna jak przy prawdziwym API OpenAI — to kluczowa zaleta kompatybilności. Ten sam kod parsujący działa z chmurą OpenAI i z lokalnym backendem Ollamy.

## Role w messages

Każda wiadomość ma pole `role` i `content`:

| Rola | Zastosowanie |
|------|-------------|
| `system` | Instrukcje globalne dla modelu (ton, format, język odpowiedzi). |
| `user` | Pytanie lub dane od użytkownika. |
| `assistant` | Poprzednie odpowiedzi modelu (historia konwersacji). |

Typowy wzorzec dla zadań produkcyjnych: najpierw `system` (reguły), potem `user` (dane wejściowe). Rola `assistant` służy do przekazywania poprzednich odpowiedzi modelu, gdy budujesz historię wieloetapowej konwersacji.

## Iluzja „pamięci" — wywołania bezstanowe

Każde wywołanie LLM przez API jest **bezstanowe (stateless)**: serwer nie pamięta poprzednich zapytań. Nowe `chat.completions.create()` to zawsze zupełnie nowe żądanie.

Jeśli w pierwszym wywołaniu napiszesz „Nazywam się Ed", a w drugim — osobnej liście messages — zapytasz „Jak mam na imię?", model **nie zna** wcześniejszej informacji. Z perspektywy API nigdy jej nie dostał.

**Iluzja pamięci** powstaje dopiero wtedy, gdy jako inżynier AI sam przekazujesz **całą historię rozmowy** w każdej kolejnej liście `messages`:

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hi! I'm Ed!"},
    {"role": "assistant", "content": "Hi Ed! How can I assist you today?"},
    {"role": "user", "content": "What's my name?"},
]
```

Model przewiduje kolejne tokeny na podstawie całej sekwencji wejściowej. Produkty typu ChatGPT robią dokładnie to samo: przy każdej wiadomości użytkownika w tle wysyłana jest pełna dotychczasowa konwersacja.

### Koszt historii

Tak — za każdą turę płacisz ponownie za **wszystkie dotychczasowe tokeny** historii (plus nową odpowiedź). To zamierzone: chcesz, żeby model „patrzył" na cały kontekst przy predykcji. Dłuższa rozmowa = rosnący koszt wejścia przy każdym kolejnym wywołaniu. Zarządzanie długością historii (skracanie, streszczanie starych tur) to osobne zadanie inżynieryjne.

## Przełączanie modeli
Zmiana modelu to tylko parametr `model` — reszta kodu (klient, messages, parsowanie odpowiedzi) pozostaje bez zmian. Można testować `llama3.2`, `deepseek-r1:1.5b` itd. bez refaktoryzacji. To ułatwia porównywanie jakości i szybkości różnych modeli open-source na tym samym zadaniu.

Ten sam obiekt klienta (`OpenAI`) obsługuje kolejne wywołania z różnymi modelami — wystarczy zmienić wartość `model` w kolejnym `chat.completions.create()`. Nie trzeba tworzyć nowego klienta ani zmieniać `base_url`.

## Podstawowe ćwiczenie inference

Najprostszy przepływ w kursie:

1. Sprawdź, czy serwer Ollama odpowiada (żądanie HTTP na port 11434).
2. Utwórz klienta OpenAI SDK z lokalnym `base_url`.
3. Wywołaj `chat.completions.create()` z jedną wiadomością `user`.
4. Odczytaj `response.choices[0].message.content`.

To punkt wyjścia przed budowaniem pipeline'ów ze scrapowaniem, RAG i agentami.

## Pułapki

- Zapomnienie o `base_url` — SDK połączy się z chmurą OpenAI i wymaga prawdziwego klucza API.
- Brak obsługi pustej odpowiedzi — `message.content` może być `None`; warto użyć `or ""`.
- Brak limitu długości promptu — długi tekst może przekroczyć okno kontekstu modelu; trzeba obcinać wejście przed wysłaniem.
- Zakładanie, że model „pamięta" poprzednie wywołanie — bez przekazania historii w `messages` każde wywołanie startuje od zera.
- Pomijanie roli `assistant` w historii — follow-up bez wcześniejszej odpowiedzi modelu i wcześniejszego `user` nie odtworzy kontekstu rozmowy.
- Ignorowanie rosnącego kosztu przy długich rozmowach — każda tura ponownie rozlicza całą historię wejściową.
