# LLM Engineering — wprowadzenie

## Czym jest LLM Engineering

LLM Engineering to praktyczne budowanie aplikacji opartych o modele językowe (Large Language Models) i Generative AI. Obejmuje cały cykl życia rozwiązania: od prostego wywołania modelu, przez integrację z danymi zewnętrznymi, po fine-tuning, wdrożenie i systemy agentowe.

## Frontier vs open-source

Modele **frontier** to największe, najmocniejsze modele komercyjne (np. GPT, Claude), dostępne przez API w chmurze. Wymagają klucza API i generują koszty per token.

Modele **open-source** można uruchamiać lokalnie (np. przez Ollamę). Dają kontrolę nad danymi, brak opłat za tokeny i możliwość fine-tuningu, ale wymagają własnego sprzętu i mają zwykle mniejsze możliwości niż frontier.

## Główne obszary kursu

- **Inference** — podstawowe wywołanie modelu (chat completion).
- **RAG** (Retrieval-Augmented Generation) — wzbogacanie odpowiedzi modelu o dane z zewnętrznych źródeł (dokumenty, bazy wektorowe, embeddings).
- **Fine-tuning** — dostosowanie wag modelu do konkretnego zadania (np. QLoRA dla modeli open-source).
- **Function calling** — model decyduje, kiedy wywołać zewnętrzną funkcję/narzędzie.
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
