# Ollama i lokalne modele

## Czym jest Ollama

Ollama to narzędzie do uruchamiania modeli językowych open-source lokalnie na własnym komputerze. Udostępnia serwer HTTP z API kompatybilnym z OpenAI, dzięki czemu ten sam kod kliencki może działać z chmurą i z lokalnym modelem.

## Uruchomienie

1. Zainstaluj Ollamę.
2. Uruchom serwer: `ollama serve` (domyślnie nasłuchuje na porcie **11434**).
3. Pobierz model: `ollama pull llama3.2` (lub inny, np. `deepseek-r1:1.5b`).

Serwer musi działać, zanim wywołasz go z kodu Pythona. Można to sprawdzić prostym żądaniem HTTP na `http://localhost:11434` — jeśli serwer nie odpowiada, kolejne wywołania z kodu też się nie powiodą.

## Różnica między `ollama serve` a `ollama pull`

- **`ollama serve`** — uruchamia lokalny serwer HTTP nasłuchujący na żądania API; sam nie pobiera wag modeli.
- **`ollama pull <model>`** — pobiera pliki wag wybranego modelu na dysk; bez tego wywołanie `chat.completions` zwróci błąd, bo model nie jest dostępny lokalnie.

Oba kroki są niezależne: najpierw uruchamiasz serwer, potem pobierasz potrzebne modele (lub odwrotnie — ważne, że oba są wykonane przed pierwszym wywołaniem z kodu).

## Endpoint API

Ollama wystawia endpoint kompatybilny z OpenAI Chat Completions pod adresem:

`http://localhost:11434/v1`

Pełny URL bazy to ten adres — klient OpenAI SDK dodaje ścieżki API automatycznie.

## Modele używane w ćwiczeniach

- **llama3.2** — lekki model Meta, dobry do prostych zadań (chat, streszczanie).
- **deepseek-r1:1.5b** — mniejszy model reasoningowy DeepSeek; pokazuje, że można przełączać modele bez zmiany reszty kodu.

## Zalety lokalnego inference

- Brak kosztów API per token.
- Dane nie opuszczają maszyny (prywatność).
- Możliwość eksperymentowania bez limitów chmurowych.
- Ten sam interfejs co OpenAI API — łatwa migracja między lokalnym a chmurowym backendem.

## Porównanie z modelami frontier

Lokalne modele open-source mają zwykle mniejsze okno kontekstu i słabsze możliwości niż frontier. Długie treści trzeba obcinać lub przetwarzać partiami. Frontier oferuje wyższą jakość i większe konteksty, ale kosztuje per token i wymaga wysyłania danych do chmury.

## Pułapki

- Serwer musi być uruchomiony przed wywołaniem — inaczej połączenie zostanie odrzucone.
- Model musi być wcześniej pobrany (`ollama pull`) — samo `serve` nie ściąga wag.
- Lokalne modele mają mniejsze okno kontekstu i słabsze możliwości niż frontier — długie treści trzeba obcinać.
