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

Struktura odpowiedzi jest identyczna jak przy prawdziwym API OpenAI — to kluczowa zaleta kompatybilności.

## Role w messages

Każda wiadomość ma pole `role` i `content`:

| Rola | Zastosowanie |
|------|-------------|
| `system` | Instrukcje globalne dla modelu (ton, format, język odpowiedzi). |
| `user` | Pytanie lub dane od użytkownika. |
| `assistant` | Poprzednie odpowiedzi modelu (historia konwersacji). |

Typowy wzorzec dla zadań produkcyjnych: najpierw `system` (reguły), potem `user` (dane wejściowe). Rola `assistant` służy do przekazywania poprzednich odpowiedzi modelu, gdy budujesz historię wieloetapowej konwersacji.

## Przełączanie modeli

Zmiana modelu to tylko parametr `model` — reszta kodu (klient, messages, parsowanie odpowiedzi) pozostaje bez zmian. Można testować `llama3.2`, `deepseek-r1:1.5b` itd. bez refaktoryzacji.

## Pułapki

- Zapomnienie o `base_url` — SDK połączy się z chmurą OpenAI i wymaga prawdziwego klucza API.
- Brak obsługi pustej odpowiedzi — `message.content` może być `None`; warto użyć `or ""`.
- Brak limitu długości promptu — długi tekst może przekroczyć okno kontekstu modelu; trzeba obcinać wejście przed wysłaniem.
