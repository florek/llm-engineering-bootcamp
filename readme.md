# LLM Engineering 8 Weeks

Repozytorium szkoleniowe tworzone podczas przerabiania kursu **Mastering Generative AI and LLMs: An 8-Week Hands-On Journey**.

Celem projektu jest praktyczne poznanie budowania aplikacji opartych o modele językowe, Generative AI, RAG, fine-tuning oraz agentów AI.

## Zakres nauki

Repozytorium obejmuje ćwiczenia i projekty związane z praktycznym LLM engineeringiem:

* Generative AI,
* modele frontier i open-source,
* Hugging Face,
* LangChain,
* Gradio,
* RAG,
* embeddings,
* vector databases,
* QLoRA,
* fine-tuning,
* function calling,
* AI agents,
* multimodal AI,
* deployment aplikacji LLM.

## Projekty

W ramach kursu rozwijane są praktyczne aplikacje LLM:

1. Generator broszur firmowych oparty o analizę stron internetowych.
2. Multimodalny agent obsługi klienta dla linii lotniczej.
3. Narzędzie generujące notatki i zadania ze spotkań audio.
4. System konwertujący kod Python do zoptymalizowanego C++.
5. Knowledge worker oparty o RAG.
6. Predykcja cen produktów przy użyciu modeli frontier.
7. Fine-tuning modelu open-source do predykcji cen.
8. Autonomiczny system agentowy wyszukujący okazje i powiadamiający użytkownika.

## Główne technologie

* Python
* LLM APIs
* Open-source LLMs
* Hugging Face
* LangChain
* Gradio
* RAG
* Vector Databases
* QLoRA
* Fine-tuning
* AI Agents

## Cel repozytorium

To repozytorium nie jest gotową aplikacją produkcyjną.
Służy do nauki, eksperymentowania i utrwalania wiedzy z zakresu LLM engineeringu.

Najważniejsze cele:

1. Zrozumieć praktyczne zastosowania modeli językowych.
2. Nauczyć się budować realne aplikacje GenAI.
3. Porównać modele frontier i open-source.
4. Przećwiczyć RAG, fine-tuning i agentic workflows.
5. Przejść od prostego inference do trenowania i wdrażania aplikacji.
6. Utrwalać wiedzę w kodzie, dokumentacji i quizach.

## Wymagania

Repozytorium zakłada znajomość podstaw Pythona.
Kurs nie wymaga zaawansowanej matematyki ani wcześniejszego doświadczenia z Machine Learningiem.

## Struktura repozytorium

```text
src/          # kod, ćwiczenia i projekty z kursu
docs/         # notatki i podsumowania wiedzy z kursu
docs/quiz/    # quizy utrwalające materiał
src/docs/     # kopia robocza notatek (zsynchronizowana z docs/)
```

## Ćwiczenia

### `src/p1.py` — podstawowe inference przez Ollamę

Skrypt sprawdza połączenie z serwerem Ollama i wywołuje chat completion dla dwóch modeli (`llama3.2`, `deepseek-r1:1.5b`) tym samym klientem OpenAI SDK.

Wymagania:

* uruchomiona Ollama (`ollama serve`),
* pobrane modele: `ollama pull llama3.2`, `ollama pull deepseek-r1:1.5b`

Uruchomienie:

```bash
python src/p1.py
```

### `src/p2.py` — streszczenie strony przez Ollamę

Skrypt pobiera treść wskazanej strony WWW, czyści HTML i wysyła ją do lokalnego modelu `llama3.2` przez Ollamę.

Wymagania:

* uruchomiona Ollama (`ollama serve`),
* pobrany model: `ollama pull llama3.2`

Uruchomienie:

```bash
python src/p2.py
python src/p2.py https://example.com
```

## Status

Repozytorium rozwijane stopniowo podczas realizacji 8-tygodniowego programu nauki.

## Nazwa kursu

**Mastering Generative AI and LLMs: An 8-Week Hands-On Journey**
