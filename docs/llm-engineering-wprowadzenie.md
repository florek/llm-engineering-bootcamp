# LLM Engineering — wprowadzenie

## Czym jest LLM Engineering

LLM Engineering to praktyczne budowanie aplikacji opartych o modele językowe (Large Language Models) i Generative AI. Obejmuje cały cykl życia rozwiązania: od prostego wywołania modelu, przez integrację z danymi zewnętrznymi, po fine-tuning, wdrożenie i systemy agentowe.

## Frontier vs open-source

Modele **frontier** to największe, najmocniejsze modele komercyjne (np. GPT, Claude, Gemini), dostępne przez API w chmurze. Wymagają klucza API i generują koszty per token. Są wyjątkowo dobre w rozumieniu niuansów i syntezie informacji, ale ranking „najlepszego" modelu szybko się zmienia.

Modele **open-source** można uruchamiać lokalnie (np. przez Ollamę) lub na platformach inference. Dają kontrolę nad danymi, brak lub niższe opłaty za tokeny i możliwość fine-tuningu, ale wymagają własnego sprzętu lub infrastruktury i mają zwykle mniejsze możliwości niż frontier.

Gdy topowe modele zbliżają się jakościowo, w produkcji coraz ważniejsze stają się **cena i szybkość** — trzeba świadomie balansować inteligencję, koszt i latency.

## Typy modeli

- **Chat** — dostrojony do dialogu; szybkie odpowiedzi konwersacyjne.
- **Reasoning** — więcej wewnętrznego rozumowania; lepszy w złożonych zadaniach, ale wolniejszy.
- **Hybrid** — łączy chat i reasoning; model decyduje, kiedy myśleć dłużej.
- **Base** — model bazowy bez dostrojenia do rozmowy; wymaga instrukcji lub fine-tuningu do formatu chat.

Prosty trik: poproś model o **wyjaśnienie strategii** przed działaniem — wymusza to głębszy tryb rozumowania i ułatwia audyt odpowiedzi.

## Główne obszary kursu

- **Inference** — podstawowe wywołanie modelu (chat completion).
- **RAG** (Retrieval-Augmented Generation) — wzbogacanie odpowiedzi modelu o dane z zewnętrznych źródeł (dokumenty, bazy wektorowe, embeddings).
- **Fine-tuning** — dostosowanie wag modelu do konkretnego zadania (np. QLoRA dla modeli open-source).
- **Function calling** — model decyduje, kiedy wywołać zewnętrzną funkcję lub narzędzie. W przeciwieństwie do zwykłego inference (tylko tekst na wyjściu), function calling pozwala modelowi zwrócić strukturalne żądanie wywołania narzędzia — np. pobrania danych z API, zapisu do bazy lub uruchomienia kalkulacji. To fundament agentów AI i integracji LLM z zewnętrznymi systemami.
- **AI Agents** — autonomiczne systemy łączące LLM z narzędziami, pamięcią i pętlą planowania.
- **Multimodal AI** — modele przetwarzające tekst, obraz, audio itd.

## Kluczowe technologie

Python, LLM APIs, Hugging Face, LangChain, Gradio, embeddings, vector databases, QLoRA, fine-tuning, AI agents.

## Projekty kursu (kierunek rozwoju)

1. Generator broszur firmowych na podstawie analizy stron WWW.
2. Multimodalny agent obsługi klienta.
3. Notatki i zadania ze spotkań audio.
4. Konwersja Python → zoptymalizowany C++.
5. Knowledge worker oparty o RAG.
6. Predykcja cen produktów (frontier).
7. Fine-tuning open-source do predykcji cen.
8. Autonomiczny system agentowy wyszukujący okazje.

## Wymagania wstępne

Znajomość podstaw Pythona. Kurs nie wymaga zaawansowanej matematyki ani wcześniejszego doświadczenia z Machine Learningiem.

## Ścieżka nauki

Od prostego inference → integracja z danymi (scraping, RAG) → fine-tuning → wdrożenie → agenci AI.

## Architektura prostego pipeline'u GenAI

Wzorzec powtarzany w ćwiczeniach kursu:

1. Przygotuj dane wejściowe (np. pobierz i oczyść tekst ze strony).
2. Zbuduj prompt (wiadomość systemowa + wiadomość użytkownika).
3. Wywołaj model przez API (chmura lub lokalny serwer).
4. Odczytaj i zwróć wynik z odpowiedzi.

Ten schemat skaluje się od jednego streszczenia do RAG, agentów i systemów produkcyjnych.

## Modularność pipeline'u

W ćwiczeniach kursu warstwy pipeline'u są rozdzielane na osobne funkcje lub moduły:

- **warstwa danych** — pobranie i oczyszczenie tekstu ze źródła zewnętrznego,
- **warstwa LLM** — zbudowanie promptu i wywołanie modelu,
- **warstwa orchestracji** — walidacja wejścia, obsługa argumentów CLI, łączenie kroków w `main()`.

Taki podział ułatwia testowanie (np. mockowanie pobrania strony bez wywoływania modelu), ponowne użycie logiki i rozbudowę pipeline'u w kierunku RAG lub agentów bez przepisywania całego skryptu.

## Embeddings i bazy wektorowe

W RAG tekst dzieli się na fragmenty, zamienia na wektory liczbowe (**embeddings**) i zapisuje w **bazie wektorowej**. Przy zapytaniu użytkownika system wyszukuje najbardziej podobne fragmenty i dołącza je do promptu modelu. To rozwiązanie problemu ograniczonego okna kontekstu — zamiast obcinać dokument, model dostaje tylko istotne partie treści.

## Inference

**Inference** to podstawowe wywołanie wytrenowanego modelu: wysłanie promptu i odczytanie odpowiedzi. Jest punktem wyjścia całej ścieżki nauki — od prostego chat completion po RAG, fine-tuning i agenty.
