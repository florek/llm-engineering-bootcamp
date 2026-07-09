# Modele frontier i typy LLM

## Cel kursu vs gotowe narzędzia

Kurs LLM Engineering koncentruje się na **budowaniu własnych rozwiązań** — aplikacji, pipeline'ów i agentów — a nie na biernym korzystaniu z gotowych interfejsów typu ChatGPT czy Claude. Gotowe narzędzia pokazują możliwości frontier models, ale prawdziwa nauka polega na pisaniu kodu, który wywołuje modele, integruje dane i orkiestruje zachowanie systemu.

## Frontier models — siła i koszt

**Frontier models** to największe, najmocniejsze modele komercyjne (np. GPT, Claude, Gemini, Grok). Są wyjątkowo dobre w:

- rozumieniu niuansów języka,
- syntezie informacji z wielu źródeł,
- złożonym rozumowaniu i negocjacji wieloetapowej.

Wymagają klucza API, działają w chmurze i generują **koszty per token**. W społeczności często wyróżnia się Claude ze względu na styl odpowiedzi, ale rankingi i „najmocniejszy model" zmieniają się szybko — w materiale kursu GPT-5 był uznawany za jeden z najpotężniejszych modeli na rynku.

## Zbieżanie możliwości — cena i szybkość

Gdy topowe modele zbliżają się do siebie pod względem jakości odpowiedzi, w decyzjach biznesowych coraz ważniejsze stają się:

- **cena** (koszt tokenów wejściowych i wyjściowych),
- **szybkość** (latency, czas do pierwszej odpowiedzi).

W produkcji trzeba świadomie **balansować inteligencję, cenę i szybkość** — najdroższy model nie zawsze jest optymalny dla każdego zadania. Ta sama aplikacja może używać lekkiego modelu do prostych kroków i frontier modelu tylko tam, gdzie jakość ma kluczowe znaczenie.

## Typy modeli: chat, reasoning, hybrid, base

| Typ | Charakterystyka |
|-----|----------------|
| **Chat** | Dostrojony do rozmowy; szybkie odpowiedzi w formacie dialogu. |
| **Reasoning** | Poświęca więcej czasu na wewnętrzne rozumowanie przed odpowiedzią; lepszy w złożonych problemach, ale wolniejszy. |
| **Hybrid** | Łączy zalety chat i reasoning w jednej ofercie — model sam decyduje, kiedy „myśleć dłużej". |
| **Base** | Model bazowy bez dostrojenia do dialogu; wymaga odpowiednich instrukcji lub fine-tuningu, by prowadzić rozmowę w stylu chat. |

Modele reasoningowe bez ustawionego limitu budżetu myślenia mogą odpowiadać **znacznie dłużej** niż modele chatowe — to ważna pułapka przy projektowaniu UX i kosztów API.

## Porównywanie modeli w praktyce

Aby zrozumieć różnice między modelami, warto uruchomić **to samo zadanie na wielu modelach równolegle** i porównać:

- jakość strategii / odpowiedzi,
- czas reakcji,
- styl komunikacji (dyplomacja, schematy, sojusze w zadaniach wieloagentowych),
- stabilność przy długich łańcuchach rozumowania.

Przykład z kursu: gra wieloagentowa, w której cztery modele (np. GPT, Claude, Gemini, Grok) rywalizują o zasoby, wymieniają wiadomości, tworzą sojusze i tłumaczą swoją strategię. Taki eksperyment daje intuicję, jak modele „myślą" i współdziałają — bez tego trudno świadomie dobierać model do zadania.

## Sztuczka: wymuszenie trybu rozumowania

Prosty trik prompt engineeringu: **każ modelowi wyjaśnić strategię** przed podjęciem decyzji. Wymuszenie artykulacji planu:

- aktywuje głębszy tryb rozumowania,
- poprawia jakość złożonych decyzji,
- ułatwia debugowanie i audyt zachowania modelu.

Zamiast od razu prosić o wynik końcowy, poproś o krok pośredni: „Wyjaśnij swoją strategię, a potem wykonaj akcję." To szczególnie skuteczne przy zadaniach planowania, negocjacji i wieloetapowego problem solvingu.

## Wielomodelowość i równoległe myślenie

W aplikacjach z wieloma agentami (każdy oparty o inny model) kroki rozumowania mogą być wykonywane **równolegle** — wszyscy agenci „myślą" jednocześnie, a orchestrator czeka na wolniejszych (często najcięższy model reasoningowy). Projektując taki system, trzeba uwzględnić:

- różnicę latency między modelami,
- koszt każdego wywołania API,
- spójność formatu odpowiedzi (np. wspólny schemat JSON dla decyzji graczy).

## Open-source vs frontier w eksperymentach

Modele open-source (np. Llama, GPT-OSS) można uruchamiać lokalnie lub na szybkich platformach inference (np. Groq). Są tańsze lub darmowe, ale zwykle słabsze w złożonym rozumowaniu niż flagship frontier. W publicznych demach często używa się mniejszych modeli ze względu na koszt; lokalnie można testować najnowsze flagshipi bez limitu publicznego ruchu.

## UI w kursie: Gradio i Streamlit

W kursie głównie używa się **Gradio** do budowy interfejsów GenAI. **Streamlit** pojawia się w niektórych demo (np. gry wieloagentowe) — oba służą do szybkiego prototypowania UI bez pisania front-endu od zera. Wybór zależy od preferencji i ekosystemu projektu; logika LLM jest niezależna od warstwy UI.

## Leaderboardy i świadomy wybór modelu

Rankingi modeli (leaderboardy) pomagają porównać benchmarki, ale nie zastępują testów na **własnym zadaniu**. Przed wdrożeniem:

1. Zdefiniuj kryteria sukcesu (jakość, czas, koszt).
2. Przetestuj 2–3 kandydatów na reprezentatywnych danych.
3. Wybierz „sweet spot" dla wymagań biznesowych — nie zawsze najdroższy model wygrywa.

## Kierunek dalszej nauki

Po zrozumieniu różnic między modelami kolejne tematy kursu obejmują:

- architekturę **transformera**,
- **Agentic AI** i pętle agentów,
- **context engineering**,
- **tokeny**, okna kontekstu, parametry modelu,
- **koszty API** i optymalizację zużycia tokenów.

To fundament pod budowę agentów, RAG i systemów produkcyjnych.

## Pułapki

- Zakładanie, że najdroższy model jest zawsze najlepszy — często wystarczy tańszy chat lub mniejszy open-source.
- Ignorowanie latency modeli reasoningowych — UX może się pogorszyć bez limitu czasu myślenia.
- Brak testów A/B na własnych danych — leaderboard ≠ Twoje zadanie.
- Porównywanie modeli tylko po jednej odpowiedzi — różnice ujawniają się w wieloetapowych scenariuszach.
