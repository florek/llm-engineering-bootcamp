# Context window i koszty API w LLM — uporządkowane notatki

## 1. Czym jest context window?

**Context window**, czyli **okno kontekstowe**, to maksymalna liczba tokenów, które model może wziąć pod uwagę podczas generowania kolejnych tokenów.

Można o nim myśleć jako o maksymalnym rozmiarze wejścia, które model potrafi obsłużyć.

Jeżeli przekroczymy ten limit:

```text
input > context window
```

model nie będzie w stanie poprawnie obsłużyć całego wejścia.

---

## 2. Context window to nie tylko ostatnia wiadomość

To bardzo ważne.

Do kontekstu nie trafia wyłącznie najnowsza wiadomość użytkownika.

Może tam znajdować się:

```text
system prompt
+
cała historia rozmowy
+
wcześniejsze odpowiedzi modelu
+
aktualna wiadomość
+
dodatkowy kontekst, np. RAG
```

Czyli okno kontekstowe obejmuje całą sekwencję wejściową.

---

## 3. Iluzja pamięci a context window

Jeżeli wcześniej powiedzieliśmy:

```text
Hi, my name is Ed.
```

a potem pytamy:

```text
What's my name?
```

to model może odpowiedzieć poprawnie tylko wtedy, gdy wcześniejsza część rozmowy nadal znajduje się w aktualnym kontekście.

Czyli:

```text
poprzednia rozmowa
+
nowe pytanie
=
input sequence
```

Model nie „pamięta” tego magicznie — dostaje tę historię ponownie.

---

## 4. Każda nowa odpowiedź powiększa historię

Po wygenerowaniu odpowiedzi modelu ta odpowiedź również może zostać dodana do historii.

Schemat:

```text
user #1
assistant #1
user #2
assistant #2
user #3
...
```

Przy kolejnym wywołaniu całość może znów trafić do modelu.

To oznacza, że rozmowa stopniowo zużywa coraz większą część context window.

---

## 5. Co jeszcze zajmuje miejsce w kontekście?

Poza historią rozmowy do kontekstu mogą trafiać również:

- przykłady few-shot,
- dokumenty pobrane przez RAG,
- instrukcje systemowe,
- dane biznesowe,
- wyniki narzędzi,
- dodatkowe informacje potrzebne do zadania.

Dlatego context window jest bardzo ważnym ograniczeniem podczas projektowania aplikacji LLM.

---

## 6. Few-shot prompting i kontekst

Jeżeli używamy kilku przykładów:

```text
pytanie → odpowiedź
pytanie → odpowiedź
pytanie → odpowiedź
```

to wszystkie te przykłady również zajmują miejsce w oknie kontekstowym.

Im więcej przykładów, tym więcej tokenów wejściowych.

---

## 7. RAG też zużywa context window

W RAG pobieramy zewnętrzne dokumenty i dodajemy je do wejścia modelu.

Czyli:

```text
pytanie
+
dokument 1
+
dokument 2
+
dokument 3
=
większy input
```

To poprawia odpowiedzi, ale zwiększa zużycie okna kontekstowego i koszt wejścia.

---

# 8. Po co duże context window?

Duże okno kontekstowe pozwala modelowi analizować bardzo długie materiały.

Na przykład:

- całe książki,
- długie dokumentacje,
- duże rozmowy,
- wiele plików,
- obszerne wyniki RAG.

Jeżeli chcielibyśmy przekazać modelowi ogromną książkę, potrzebujemy odpowiednio dużego context window.

---

## 9. Context window a duże dokumenty

W materiale pojawia się intuicja:

```text
całe dzieła Szekspira
≈ około 1,2 mln tokenów
```

Aby zmieścić tak duży materiał w jednym wejściu, potrzebny byłby model z bardzo dużym oknem kontekstowym.

---

# 10. Koszty API

Korzystanie z aplikacji typu ChatGPT i korzystanie z API to dwie różne rzeczy.

W aplikacji możemy mieć:

```text
Free
Plus
Pro
inne subskrypcje
```

Natomiast API zazwyczaj działa w modelu:

## pay per use

czyli płacimy za faktyczne użycie.

---

## 11. Od czego zależy koszt API?

Najczęściej od:

```text
liczby input tokens
+
liczby output tokens
```

Czyli płacimy za:

- tokeny wysyłane do modelu,
- tokeny generowane przez model.

---

## 12. Input tokens

Input tokens obejmują całą sekwencję wejściową.

Czyli nie tylko:

```text
ostatnią wiadomość
```

ale też:

```text
system prompt
historię rozmowy
RAG
few-shot examples
dodatkowy kontekst
```

---

## 13. Dlaczego historia rozmowy zwiększa koszt?

Jeżeli przy każdym wywołaniu przesyłamy pełną historię, model musi ją ponownie przetworzyć.

Przykład:

```text
request 1 → 100 tokenów
request 2 → 500 tokenów
request 3 → 1000 tokenów
request 4 → 2000 tokenów
```

Koszt wejścia może więc rosnąć wraz z długością rozmowy.

---

## 14. To nie jest „niesprawiedliwe” — model wykonuje więcej obliczeń

Jeżeli chcemy, żeby model brał pod uwagę całą historię, musi ją przetworzyć.

Czyli:

```text
więcej kontekstu
↓
więcej obliczeń
↓
większy koszt
```

Gdybyśmy wysłali tylko najnowszą wiadomość, byłoby taniej, ale model straciłby kontekst.

---

# 15. Output tokens

Output tokens to tokeny generowane przez model.

Przykład:

```text
prompt → 500 input tokens
odpowiedź → 200 output tokens
```

Koszt może być liczony osobno dla wejścia i wyjścia.

---

## 16. Reasoning tokens również kosztują

W modelach reasoningowych część dodatkowych tokenów może być zużywana na wewnętrzne rozumowanie.

W materiale podkreślono, że:

> nawet jeśli użytkownik nie widzi całego procesu rozumowania, obliczenia nadal są wykonywane i mogą wpływać na koszt.

Czyli koszt odpowiedzi może być wyższy niż sugerowałaby sama długość widocznego tekstu.

---

# 17. Koszty mogą być mniej przewidywalne przy reasoning

Jeżeli model wykonuje różną ilość dodatkowej pracy w zależności od problemu, liczba tokenów związanych z reasoningiem może się zmieniać.

To oznacza, że koszt pojedynczego zapytania nie zawsze jest idealnie przewidywalny.

---

# 18. Ceny zwykle podaje się za milion tokenów

Dostawcy modeli często pokazują ceny jako:

```text
$X za 1 mln input tokens
$Y za 1 mln output tokens
```

To ważne, ponieważ cena za pojedynczy token jest bardzo mała.

---

## 19. Małe zapytania są zwykle bardzo tanie

Jeżeli pojedyncze zapytanie zawiera tylko kilkanaście lub kilkadziesiąt tokenów, koszt może być bardzo mały.

To szczególnie prawdziwe podczas:

- eksperymentowania,
- nauki,
- małych projektów.

Koszty stają się ważniejsze przy dużej skali.

---

# 20. Skala zmienia wszystko

Przy systemie obsługującym:

```text
tysiące użytkowników
wiele równoległych rozmów
agent loops
długie konteksty
```

koszty mogą szybko rosnąć.

Wtedy trzeba analizować:

```text
koszt per użytkownik
koszt per request
koszt per workflow
```

---

# 21. Agent loops mogą szybko zużywać tokeny

Agent może wywoływać model wielokrotnie:

```text
LLM
↓
tool
↓
LLM
↓
tool
↓
LLM
↓
...
```

Każdy krok oznacza kolejne wywołanie i dodatkowe tokeny.

Dlatego agenci mogą zużywać znacznie więcej tokenów niż pojedynczy prosty prompt.

---

# 22. Tańsze warianty modeli

Duże rodziny modeli często mają kilka wersji:

```text
duży
mini
nano
```

Mniejszy wariant:

```text
+ tańszy
+ szybszy
- zwykle słabszy
```

Dlatego do prostych zadań nie zawsze trzeba używać największego modelu.

---

# 23. Caching

Kolejna technika obniżania kosztów to:

## caching

Jeżeli wysyłamy wielokrotnie ten sam lub bardzo podobny początek wejścia, część pracy może zostać wykorzystana ponownie.

Wtedy koszt input tokens może być niższy.

---

## 24. Dlaczego caching pomaga?

Załóżmy, że każdy request zawiera bardzo długi system prompt:

```text
10 000 tokenów stałych instrukcji
+
nowe pytanie użytkownika
```

Jeżeli ten sam fragment jest wielokrotnie wykorzystywany, caching może ograniczyć koszt ponownego przetwarzania tej części.

---

# 25. Okna kontekstowe różnych modeli

Różne modele oferują różne rozmiary context window.

W materiale pokazano przykłady od około:

```text
100k tokenów
```

do nawet:

```text
1 mln tokenów
```

Warto pamiętać, że dokładne limity modeli zmieniają się z czasem.

---

# 26. Duży context window nie oznacza, że zawsze trzeba go wypełniać

To, że model potrafi przyjąć ogromny kontekst, nie oznacza, że zawsze warto wysyłać maksymalną ilość danych.

Większy input oznacza:

- większy koszt,
- więcej obliczeń,
- potencjalnie większe opóźnienie,
- większą ilość nieistotnych informacji.

Dobrze jest przekazywać przede wszystkim dane potrzebne do rozwiązania zadania.

---

# 27. Context window jako ograniczenie architektury

Podczas budowania aplikacji trzeba świadomie zarządzać kontekstem.

Możliwe strategie:

```text
przycinanie historii
streszczanie starszych wiadomości
RAG
wybieranie najważniejszych dokumentów
caching
```

To wszystko pomaga kontrolować rozmiar wejścia.

---

# 28. Leaderboardy modeli

W materiale wspomniano także o rankingach i zestawieniach modeli.

Takie zestawienia mogą pokazywać m.in.:

- context window,
- ceny input tokens,
- ceny output tokens,
- wydajność,
- wyniki benchmarków.

To przydatne przy wyborze modelu do konkretnego zastosowania.

---

# 29. Co warto porównywać przy wyborze modelu?

Nie tylko jakość.

W praktyce liczą się również:

```text
context window
input cost
output cost
latency
reasoning capability
multimodalność
```

Dobry wybór modelu zależy od konkretnego zastosowania.

---

# 30. Najważniejsze zależności

```text
dłuższa historia
↓
więcej input tokens
↓
więcej obliczeń
↓
większy koszt
```

oraz:

```text
większe context window
↓
możliwość obsługi większej ilości danych
```

ale nie oznacza to, że zawsze powinniśmy wykorzystywać cały dostępny limit.

---

# 31. Całość w jednym schemacie

```text
SYSTEM PROMPT
      +
HISTORIA ROZMOWY
      +
RAG / DOKUMENTY
      +
NOWE PYTANIE
      ↓
INPUT TOKENS
      ↓
CONTEXT WINDOW
      ↓
LLM
      ↓
REASONING / GENEROWANIE
      ↓
OUTPUT TOKENS
      ↓
KOSZT API
```

---

# 32. Co warto zapamiętać?

1. **Context window to maksymalna liczba tokenów, które model może uwzględnić.**
2. **Do kontekstu wchodzi cała historia rozmowy, a nie tylko ostatnia wiadomość.**
3. **RAG, few-shot prompting i instrukcje systemowe również zajmują context window.**
4. **API zazwyczaj rozlicza input tokens i output tokens.**
5. **Im dłuższa rozmowa, tym większy może być koszt wejścia.**
6. **Reasoning również wymaga obliczeń i może zwiększać koszt.**
7. **Małe pojedyncze wywołania są zwykle bardzo tanie.**
8. **Koszty stają się ważne przy dużej skali i agent loops.**
9. **Caching może obniżyć koszt powtarzających się inputów.**
10. **Różne modele mają różne context windows i różne ceny.**
11. **Duże okno kontekstowe jest potężne, ale trzeba nim rozsądnie zarządzać.**

---

# 33. Najważniejsze zdanie

> **Context window określa, ile informacji model może wziąć pod uwagę naraz, a każda dodatkowa informacja w tym kontekście zwiększa liczbę input tokens, ilość obliczeń i potencjalny koszt API.**
