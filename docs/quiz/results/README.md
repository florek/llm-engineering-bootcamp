# Historia wyników

| Data | Wynik | % | Braki | Link |
|------|-------|---|-------|------|
| 09.07.2026 | 19/20 | 95% | brak | [09.07.2026_results.md](09.07.2026_results.md) |
| 08.07.2026 | 18/20 | 90% | brak | [08.07.2026_results.md](08.07.2026_results.md) |
| 07.07.2026 | 18/20 | 90% | 2, 12 | [07.07.2026_results.md](07.07.2026_results.md) |
| 06.07.2026 | 18/20 | 90% | 20 | [06.07.2026_results.md](06.07.2026_results.md) |
| 18.06.2026 | 16/20 | 80% | 2, 13, 18 | [18.06.2026_results.md](18.06.2026_results.md) |
| 17.06.2026 | 17/20 | 85% | 7, 17 | [17.06.2026_results.md](17.06.2026_results.md) |

## Statystyki

- Najlepszy wynik: 19/20 (95%) — 09.07.2026
- Najgorszy wynik: 16/20 (80%) — 18.06.2026
- Średnia ze wszystkich prób: 17,7/20 (88%)
- Ostatnie 5 wyników: 09.07.2026 (95%), 08.07.2026 (90%), 07.07.2026 (90%), 06.07.2026 (90%), 18.06.2026 (80%)

## Najczęstsze obszary do poprawy

1. **[Python]** — 8 błędów łącznie (`decompose`, `urlparse`, `separator` w `get_text`, `raise_for_status`, parser `html.parser`)
2. **[RAG]** — 3 błędy łącznie (limit znaków, ewolucja pipeline'u do generatora broszur)
3. **[GenAI]** — 2 błędy łącznie (skutek obcięcia tekstu, walidacja pustej treści przed wywołaniem LLM)
4. **[LLM]** — 1 błąd (rozróżnienie modelu hybrid od multimodalnego)
5. **[API]** — 1 błąd (rola `assistant` w tablicy `messages`)
