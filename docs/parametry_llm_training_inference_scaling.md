# Parametry modeli LLM, training-time scaling i inference-time scaling

## 1. Co oznacza liczba parametrów?

W opisach modeli językowych często pojawiają się wartości takie jak:

```text
270M
3B
8B
70B
120B
```

gdzie:

```text
M = million = milion
B = billion = miliard
T = trillion = bilion
```

Przykładowo:

```text
270M = 270 milionów parametrów
8B   = 8 miliardów parametrów
120B = 120 miliardów parametrów
```

Parametry to liczby wewnątrz sieci neuronowej, których model uczy się podczas treningu.

Można myśleć o nich jak o ogromnej liczbie „pokręteł”, które są ustawiane tak, aby model coraz lepiej przewidywał kolejne tokeny.

---

## 2. Parametry nie są pojedynczymi faktami

Nie działa to tak:

```text
1 parametr = 1 informacja
```

Wiedza modelu jest rozproszona pomiędzy ogromną liczbą parametrów.

Parametry wspólnie reprezentują m.in.:

- zależności językowe,
- znaczenie słów,
- składnię,
- relacje między pojęciami,
- wzorce występujące w danych treningowych.

---

## 3. Czy więcej parametrów oznacza lepszy model?

Zwykle większa liczba parametrów zwiększa pojemność modelu.

Historycznie często działała zasada:

```text
większy model
+
więcej danych
+
więcej obliczeń
=
lepsze możliwości
```

Ale:

> **więcej parametrów nie oznacza automatycznie lepszego modelu.**

Znaczenie mają również:

- architektura,
- jakość danych,
- sposób treningu,
- tokenizer,
- post-training,
- sposób wykorzystania modelu podczas inferencji.

Dlatego nowoczesny mały model może być znacznie lepszy od starszego modelu o podobnym albo nawet większym rozmiarze.

---

## 4. Przykład historyczny

Dla orientacji:

```text
GPT-2 → około 1,5 miliarda parametrów
GPT-3 → 175 miliardów parametrów
```

W przypadku części nowszych modeli zamkniętych producenci nie publikują dokładnej liczby parametrów.

Dlatego liczby spotykane w internecie dla takich modeli jak GPT-4 należy traktować jako **szacunki**, a nie oficjalne dane.

---

## 5. Różne warianty jednej rodziny modeli

Rodziny modeli często występują w kilku wariantach:

```text
mały
średni
duży
```

albo np.:

```text
nano
mini
pełny model
```

Zwykle mniejszy model oznacza:

```text
+ niższy koszt
+ szybsze działanie
+ mniejsze wymagania sprzętowe
- słabsze możliwości w trudnych zadaniach
```

Większy model:

```text
+ większe możliwości
+ lepsze radzenie sobie z trudnymi zadaniami
- większy koszt
- większe wymagania
```

---

# 6. Training-time scaling

Pierwszy sposób zwiększania możliwości modelu to:

## Training-time scaling

czyli zwiększanie zasobów używanych **podczas treningu**.

W uproszczeniu:

```text
więcej parametrów
+
więcej danych
+
więcej GPU
+
więcej czasu treningu
=
potencjalnie lepszy model
```

Większy model ma większą pojemność i może nauczyć się bardziej skomplikowanych zależności.

---

## 7. Chinchilla scaling laws

Ważnym pojęciem są tzw.:

## Chinchilla scaling laws

Ich główna intuicja jest taka:

> Rozmiar modelu powinien być odpowiednio dopasowany do ilości danych treningowych i ilości dostępnych obliczeń.

Nie wystarczy więc po prostu zwiększać liczby parametrów.

Potrzebna jest równowaga:

```text
liczba parametrów
       ↕
ilość danych
       ↕
ilość obliczeń
```

Ogromny model zbyt słabo wytrenowany na małej liczbie danych nie wykorzysta swojego potencjału.

---

# 8. Co oznacza inference?

Po zakończeniu treningu mamy gotowy model.

Kiedy później uruchamiamy go, aby odpowiedział na pytanie, wykonujemy:

## inference — inferencję

Czyli:

```text
TRENING
dane → model → uczenie parametrów

INFERENCJA
prompt → gotowy model → odpowiedź
```

---

# 9. Inference-time scaling

Drugim sposobem poprawienia jakości działania jest:

## inference-time scaling

Tutaj nie zwiększamy już modelu podczas treningu.

Zamiast tego pozwalamy mu wykonać więcej pracy **w momencie odpowiadania**.

To ważne rozróżnienie:

```text
training-time scaling
→ więcej inwestujemy podczas treningu

inference-time scaling
→ więcej inwestujemy podczas używania modelu
```

---

# 10. Reasoning jako inference-time scaling

Jednym z przykładów inference-time scaling jest **reasoning**.

Zamiast natychmiast wygenerować odpowiedź, model może dostać więcej czasu i obliczeń na rozwiązanie problemu.

Schematycznie:

```text
pytanie
  ↓
analiza problemu
  ↓
kolejne kroki
  ↓
sprawdzenie rozwiązania
  ↓
odpowiedź
```

Nie zmieniamy liczby parametrów.

Zwiększamy ilość pracy wykonywanej podczas inferencji.

---

# 11. Więcej kontekstu również pomaga

Kolejnym sposobem poprawienia działania jest dostarczenie modelowi dodatkowych informacji.

Przykład:

Użytkownik pyta:

> Ile kosztuje bilet do Londynu?

Model sam może nie znać aktualnej ceny.

Jeżeli jednak do wejścia dodamy:

```text
aktualne ceny biletów
+
pytanie użytkownika
```

to model może wykorzystać te dane w odpowiedzi.

---

# 12. RAG

To prowadzi do techniki:

## RAG — Retrieval-Augmented Generation

W RAG:

1. użytkownik zadaje pytanie,
2. system wyszukuje odpowiednie informacje,
3. informacje trafiają do kontekstu modelu,
4. LLM generuje odpowiedź.

Schemat:

```text
pytanie
   ↓
wyszukiwanie danych
   ↓
dokumenty / informacje
   ↓
LLM
   ↓
odpowiedź
```

Model nie musi więc przechowywać całej wiedzy w swoich parametrach.

Może otrzymać potrzebne informacje dopiero podczas wykonywania zadania.

---

# 13. Dwa niezależne sposoby skalowania

Możemy więc wyróżnić dwie ścieżki:

```text
                   JAK POPRAWIĆ MODEL?
                           │
             ┌─────────────┴─────────────┐
             │                           │
             ▼                           ▼

   TRAINING-TIME SCALING        INFERENCE-TIME SCALING

   więcej parametrów            reasoning
   więcej danych                RAG
   więcej GPU                   większy kontekst
   więcej treningu              narzędzia
                                wiele wywołań modelu
```

Obie techniki można stosować jednocześnie.

---

# 14. Dlaczego inference-time scaling stało się tak ważne?

Przez wiele lat rozwój LLM był mocno związany z podejściem:

> Bigger is better.

Czyli:

```text
większy model
więcej parametrów
więcej danych
```

Później zaczęto coraz mocniej rozwijać techniki poprawiające działanie **gotowego modelu**.

Do nich należą m.in.:

- RAG,
- reasoning,
- narzędzia,
- agentic AI,
- wielokrotne wywołania modelu.

Dzięki temu nie zawsze trzeba trenować nowy, większy model, aby poprawić wyniki.

---

# 15. Skala logarytmiczna

Przy porównywaniu wielkości modeli często wykorzystuje się skalę logarytmiczną.

Przykład:

```text
1B
10B
100B
1000B
```

Każdy kolejny krok oznacza:

> 10 razy większą wartość.

Dlatego odległości na takim wykresie nie są liniowe.

---

# 16. Modele open-weight mają bardzo różne rozmiary

Spotykamy modele mające np.:

```text
3B
8B
20B
70B
120B
setki miliardów parametrów
```

Nie należy jednak wybierać modelu wyłącznie na podstawie liczby parametrów.

Nowoczesny model 8B może w wielu zastosowaniach przewyższać dużo starszy model o podobnym albo większym rozmiarze.

---

# 17. Mixture of Experts — MoE

Wiele dużych modeli korzysta z architektury:

## Mixture of Experts

czyli **mieszaniny ekspertów**.

Model składa się z wielu wyspecjalizowanych części.

Nie wszystkie muszą być używane jednocześnie.

Schemat:

```text
                 ┌→ ekspert A
wejście → router ├→ ekspert B
                 ├→ ekspert C
                 └→ ekspert D
```

Router wybiera, którzy eksperci powinni zostać wykorzystani dla danego wejścia.

---

# 18. Parametry całkowite i aktywne

W modelach MoE ważne jest rozróżnienie:

## Total parameters

Całkowita liczba parametrów modelu.

## Active parameters

Liczba parametrów faktycznie używanych podczas konkretnego kroku inferencji.

Możemy więc mieć bardzo duży model, ale podczas generowania pojedynczego tokenu aktywna jest tylko część jego parametrów.

To pozwala łączyć:

```text
dużą pojemność modelu
+
mniejszy koszt pojedynczego obliczenia
```

---

# 19. Najważniejsza intuicja

Parametry są ważne, ale nie mówią całej prawdy o modelu.

Na jego możliwości wpływają razem:

```text
parametry
+
architektura
+
dane treningowe
+
sposób treningu
+
post-training
+
kontekst
+
reasoning
+
RAG
+
narzędzia
```

Dlatego:

> **liczba parametrów nie jest prostą miarą inteligencji modelu.**

---

# 20. Najważniejsze pojęcia

## Parameters

Liczby uczone podczas treningu sieci neuronowej.

## Training-time scaling

Zwiększanie możliwości modelu poprzez więcej parametrów, danych i obliczeń podczas treningu.

## Inference

Uruchomienie już wytrenowanego modelu.

## Inference-time scaling

Zwiększanie jakości poprzez większą ilość pracy wykonywanej podczas używania modelu.

## Reasoning

Dodatkowe obliczenia wykonywane przed udzieleniem finalnej odpowiedzi.

## RAG

Dostarczanie modelowi zewnętrznych informacji potrzebnych do odpowiedzi.

## Mixture of Experts

Architektura, w której tylko wybrane części dużego modelu są aktywowane dla danego wejścia.

---

# 21. Co warto zapamiętać?

1. **Parametry są wartościami uczonymi podczas treningu.**
2. **Więcej parametrów zwykle oznacza większą pojemność, ale nie gwarantuje lepszej jakości.**
3. **Nowoczesny mały model może być lepszy od starszego większego modelu.**
4. **Training-time scaling dotyczy zwiększania zasobów podczas treningu.**
5. **Inference-time scaling dotyczy zwiększania pracy podczas korzystania z gotowego modelu.**
6. **Reasoning i RAG są przykładami inference-time scaling.**
7. **Oba rodzaje skalowania można stosować jednocześnie.**
8. **W Mixture of Experts nie wszystkie parametry są aktywne przy każdym tokenie.**
9. **Sama liczba parametrów nie jest dobrą miarą jakości ani „inteligencji” modelu.**

---

# 22. Jednozdaniowe podsumowanie

> **Możliwości LLM zależą nie tylko od liczby parametrów, lecz także od jakości treningu oraz od tego, ile dodatkowej pracy i informacji dostarczymy modelowi podczas inferencji.**
