# OpenAI SDK i Chat Completions

## OpenAI Python SDK z Ollamą

Biblioteka `openai` (OpenAI Python SDK) domyślnie łączy się z API OpenAI w chmurze. Można ją skonfigurować do pracy z Ollamą, przekazując własny `base_url` i dowolny `api_key`.

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
