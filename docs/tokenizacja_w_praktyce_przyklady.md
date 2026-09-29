# Tokenizacja w praktyce — jak tekst zamienia się na tokeny

## 1. Częste słowa często stają się pojedynczym tokenem

Jeżeli tekst zawiera bardzo popularne słowa, tokenizer może przypisać każdemu z nich osobny token.

Przykład zdania:

```text
an important sentence for my class of AI engineers
```

Może zostać podzielony mniej więcej tak:

```text
an
 important
 sentence
 for
 my
 class
 of
 AI
 engineers
```

W takim przypadku wiele popularnych słów trafia do pojedynczych tokenów.

---

## 2. Różne modele mogą mieć różne tokenizery

W interfejsie tokenizera można wybrać model.

To ważne, ponieważ różne modele mogą mieć:

- inny słownik tokenów,
- trochę inne zasady podziału tekstu,
- inny sposób kodowania rzadkich słów.

Nie oznacza to jednak, że trzeba obsesyjnie wybierać model tylko na podstawie „wydajności tokenizacji”.

To po prostu jedna z decyzji architektonicznych podjętych podczas tworzenia modelu.

---

## 3. Token może zawierać spację przed słowem

To bardzo ważny szczegół.

Token często nie reprezentuje wyłącznie:

```text
important
```

ale raczej:

```text
 important
```

czyli słowo razem ze spacją przed nim.

Ta spacja niesie informację:

> tutaj zaczyna się nowe słowo.

Dlatego tokenizer często rozróżnia:

```text
" important"
```

od:

```text
"important"
```

w środku innego słowa.

---

## 4. Początek słowa i fragment słowa to nie zawsze ten sam token

Załóżmy słowo:

```text
important
```

i inne słowo:

```text
unimportant
```

Tokenizer może potraktować je inaczej.

Na początku samodzielnego słowa może istnieć token:

```text
 important
```

ale w słowie:

```text
unimportant
```

możemy dostać:

```text
un
important
```

lub inny podział zależny od tokenizera.

Najważniejsza idea:

> token reprezentujący początek słowa może być inny niż token reprezentujący ten sam fragment wewnątrz słowa.

---

## 5. Rzadkie słowa są dzielone na kilka tokenów

Jeżeli słowo jest mniej popularne, może zostać rozbite na kilka fragmentów.

Przykład:

```text
exquisitely
```

może zostać podzielony na kilka mniejszych tokenów.

Podobnie:

```text
handcrafted
```

może zostać rozłożone na:

```text
hand
crafted
```

To pozwala modelowi reprezentować słowo, nawet jeśli całe słowo nie występuje jako osobny token w słowniku.

---

## 6. Tokenizer wykorzystuje fragmenty, które pojawiają się często

Przykładowe słowo:

```text
handcrafted
```

może korzystać z tokenów odpowiadających fragmentom:

```text
hand
crafted
```

Takie fragmenty mają już własne reprezentacje i mogą być używane także w innych słowach.

To może pomagać modelowi szybciej uczyć się znaczenia podobnych konstrukcji.

---

## 7. Zmyślone lub bardzo rzadkie słowa też można zakodować

Tokenizer nie musi znać całego słowa.

Jeżeli pojawi się słowo nietypowe, może je rozłożyć na mniejsze części.

Dzięki temu nawet nieznane wcześniej słowo może zostać zapisane przy użyciu istniejącego słownika tokenów.

Schemat:

```text
rzadkie słowo
     ↓
mniejsze fragmenty
     ↓
znane tokeny
```

---

## 8. Przykład z mniej typowym zdaniem

W materiale pokazano zdanie zawierające rzadsze słowa.

W takim przypadku:

- popularne słowa pozostają pojedynczymi tokenami,
- rzadsze słowa rozpadają się na kilka tokenów,
- zmyślone słowa również mogą być reprezentowane jako kombinacja mniejszych fragmentów.

To pokazuje elastyczność tokenizacji.

---

## 9. Liczba znaków a liczba tokenów

W jednym z przykładów:

```text
66 znaków
```

zostało zamienionych na:

```text
18 tokenów
```

W innym:

```text
50 znaków
```

zostało zamienionych na:

```text
9 tokenów
```

To pokazuje, że:

> liczba tokenów nie jest bezpośrednio równa liczbie znaków ani liczbie słów.

---

# 10. Tokenizacja liczb

Tokenizer może również dzielić liczby na fragmenty.

W przykładzie liczba:

```text
3.1415926535897793
```

została podzielona na mniejsze części.

W materiale pokazano intuicję, że część sekwencji cyfr może być grupowana w tokeny obejmujące kilka cyfr.

---

## 11. Dlaczego liczby są ciekawe?

Sposób tokenizacji liczb wpływa na to, jak model otrzymuje zadania matematyczne.

Długa liczba może być podzielona na kilka tokenów:

```text
123456789
```

na przykład jako kilka fragmentów.

To oznacza, że model nie zawsze „widzi” całą liczbę jako pojedynczą jednostkę.

---

## 12. Dawniejsze problemy modeli z matematyką

W materiale wspomniano, że starsze modele potrafiły mieć problemy z większymi liczbami.

Jednym z proponowanych wyjaśnień było to, że:

- krótsze liczby mogły być reprezentowane prościej,
- dłuższe były dzielone na kilka tokenów,
- model musiał wykonywać operacje na kilku fragmentach jednocześnie.

Współczesne modele radzą sobie z tym znacznie lepiej.

---

# 13. Tokenizer jako narzędzie edukacyjne

Warto samemu eksperymentować z tokenizerem.

Dzięki temu można zobaczyć:

- które słowa są pojedynczymi tokenami,
- które słowa są dzielone,
- jak traktowane są liczby,
- jak tokenizowany jest kod,
- jak różne modele dzielą ten sam tekst.

To bardzo dobry sposób na zbudowanie intuicji.

---

# 14. Reguła orientacyjna: około 4 znaki na token

W materiale podano prostą regułę:

> **1 token ≈ 4 znaki**

To tylko przybliżenie.

Może być użyteczne, gdy znamy liczbę znaków i chcemy oszacować liczbę tokenów.

Przykład:

```text
4000 znaków
≈
1000 tokenów
```

---

# 15. Druga reguła: 1 token ≈ 0,75 słowa

Bardzo popularne przybliżenie:

```text
1 token ≈ 0,75 słowa
```

Czyli:

```text
1000 tokenów ≈ 750 słów
```

To również jest tylko orientacyjna reguła.

Najlepiej działa dla typowego tekstu w języku angielskim.

---

# 16. Przykład: milion tokenów

Jeżeli:

```text
1000 tokenów ≈ 750 słów
```

to:

```text
1 000 000 tokenów
≈
750 000 słów
```

W materiale jako intuicyjne porównanie użyto całych dzieł Szekspira.

Pełny zbiór jego dzieł ma około:

```text
900 000 słów
```

czyli około:

```text
1,2 miliona tokenów
```

według podanej reguły orientacyjnej.

---

# 17. Dlaczego mówi się o cenie za milion tokenów?

Dostawcy modeli często podają ceny w jednostkach:

```text
koszt za 1 milion tokenów
```

Dzięki powyższym proporcjom można zbudować sobie intuicję, ile tekstu to faktycznie oznacza.

---

# 18. Reguły tokenowe działają najlepiej dla zwykłego angielskiego

Przybliżenie:

```text
1 token ≈ 4 znaki
```

lub:

```text
1 token ≈ 0,75 słowa
```

najlepiej sprawdza się dla typowego tekstu angielskiego.

Nie zawsze działa równie dobrze dla:

- kodu,
- matematyki,
- terminologii naukowej,
- nietypowych nazw,
- rzadkich słów,
- innych języków.

---

# 19. Kod może zużywać więcej tokenów

Kod zawiera:

- nazwy zmiennych,
- symbole,
- nawiasy,
- operatory,
- nietypowe ciągi znaków.

Dlatego kod może być tokenizowany mniej „gęsto” niż zwykły tekst.

Przykładowo:

```python
customer_invoice_total_v2
```

może zostać rozbite na wiele tokenów.

---

# 20. Tekst naukowy i matematyczny także może być droższy tokenowo

Specjalistyczna terminologia może zawierać:

- długie słowa,
- symbole,
- liczby,
- wzory.

To oznacza, że liczba tokenów może rosnąć szybciej niż w zwykłym tekście.

---

# 21. Praktyczna intuicja

Dobrze mieć „wyczucie”, ile tokenów zajmuje dany materiał.

Można eksperymentować z:

```text
zwykłym tekstem
kodem
liczbami
terminologią techniczną
```

i porównywać wyniki w tokenizerze.

---

# 22. Najważniejsza różnica: częste vs rzadkie słowa

Możemy uprościć działanie tokenizera tak:

```text
częste słowo
→ często 1 token

rzadkie słowo
→ kilka tokenów

bardzo nietypowe słowo
→ jeszcze mniejsze fragmenty
```

To pozwala utrzymać ograniczony słownik, ale jednocześnie reprezentować praktycznie dowolny tekst.

---

# 23. Najważniejsze pojęcie: token początku słowa

Warto szczególnie zapamiętać:

```text
" word"
```

i:

```text
"word"
```

nie muszą być tym samym tokenem.

Spacja może być częścią tokenu i informować model, że zaczyna się nowe słowo.

---

# 24. Co warto zapamiętać?

1. **Popularne słowa często mieszczą się w pojedynczym tokenie.**
2. **Rzadkie słowa są dzielone na kilka mniejszych tokenów.**
3. **Spacja przed słowem może być częścią tokenu.**
4. **Token początku słowa może różnić się od tokenu używanego wewnątrz słowa.**
5. **Różne modele mogą używać różnych tokenizerów.**
6. **Liczby również są dzielone na tokeny.**
7. **1000 tokenów to orientacyjnie około 750 słów w typowym angielskim tekście.**
8. **1 token to orientacyjnie około 4 znaki.**
9. **Kod, matematyka i tekst naukowy często zużywają więcej tokenów niż zwykły tekst.**
10. **Najlepszy sposób na zbudowanie intuicji to samodzielne eksperymentowanie z tokenizerem.**

---

# 25. Całość w jednym schemacie

```text
TEKST
  ↓
czy fragment jest częsty?
  │
  ├── TAK
  │    ↓
  │  jeden token
  │
  └── NIE
       ↓
   podział na mniejsze fragmenty
       ↓
   kilka tokenów
```

---

# 26. Najważniejsze zdanie

> **Tokenizer stara się używać częstych fragmentów jako pojedynczych tokenów, a rzadsze słowa rozbija na mniejsze części, dzięki czemu może efektywnie reprezentować praktycznie dowolny tekst.**
