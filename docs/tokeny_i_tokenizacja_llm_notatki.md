# Tokeny i tokenizacja w LLM — uporządkowane notatki z wykładu

## 1. Dlaczego w ogóle potrzebujemy tokenów?

Model językowy nie pracuje bezpośrednio na tekście takim, jak widzi go człowiek.

Tekst trzeba najpierw zamienić na elementy, które model potrafi przetwarzać.

Historycznie można było podejść do tego na kilka sposobów:

1. znak po znaku,
2. słowo po słowie,
3. przy użyciu tokenów.

Współczesne LLM-y najczęściej korzystają właśnie z trzeciego podejścia.

---

# 2. Podejście znak po znaku

Najprostszy pomysł to przetwarzanie tekstu:

> znak po znaku

Czyli np. słowo:

```text
kot
```

można potraktować jako:

```text
k
o
t
```

Zaletą takiego podejścia jest bardzo mały słownik.

Mamy przecież tylko ograniczoną liczbę znaków:

- litery,
- cyfry,
- znaki interpunkcyjne,
- znaki specjalne.

Może to oznaczać stosunkowo niewielką liczbę możliwych wejść.

---

# 3. Problem podejścia znakowego

Przy znakach sieć neuronowa musi nauczyć się bardzo dużo sama.

Model musi zrozumieć:

```text
k + o + t = "kot"
```

a następnie jeszcze nauczyć się, co słowo „kot” oznacza.

Czyli sieć musi jednocześnie:

1. składać znaki w większe jednostki,
2. rozpoznawać słowa,
3. przypisywać im znaczenie.

To pozostawia bardzo dużo pracy samej sieci.

---

# 4. Podejście słowo po słowie

Drugą intuicyjną możliwością jest traktowanie każdego słowa jako osobnego elementu wejściowego.

Przykład:

```text
Ala ma kota
```

mogłoby zostać zapisane jako:

```text
"Ala"
"ma"
"kota"
```

To wydaje się naturalne.

Model nie musi już sam składać liter w słowa.

---

# 5. Problem słownika opartego na całych słowach

Problem polega na tym, że liczba możliwych słów jest ogromna.

Mamy:

- zwykłe słowa,
- odmiany,
- nazwiska,
- nazwy miejsc,
- nazwy własne,
- nowe słowa,
- literówki,
- specjalistyczne terminy.

Słownik musiałby być gigantyczny.

A mimo to zawsze pojawiałyby się słowa, których w nim nie ma.

---

# 6. Problem „nieznanego słowa”

Jeżeli słownik zawiera tylko komplet wcześniej znanych słów, to każde nowe słowo może stać się problemem.

Przykładowo:

```text
superhipernowoczesny
```

Jeżeli takiego słowa nie ma w słowniku, model potrzebowałby specjalnego oznaczenia typu:

```text
UNKNOWN
```

To oznaczałoby utratę informacji.

---

# 7. Tokenizacja jako kompromis

Przełomowym podejściem okazało się zastosowanie:

## tokenów

Token może być:

- całym słowem,
- fragmentem słowa,
- pojedynczym znakiem,
- czasem częstym połączeniem kilku elementów.

Czyli tokenizacja znajduje się pomiędzy:

```text
znakami
```

a:

```text
całymi słowami
```

To kompromis.

---

# 8. Dlaczego tokeny działają dobrze?

Tokenizacja pozwala zbudować ograniczony słownik, ale jednocześnie nie ogranicza modelu wyłącznie do pełnych słów.

Jeżeli całe słowo znajduje się w słowniku tokenów, można je potraktować jako jedną jednostkę.

Jeżeli nie, można podzielić je na mniejsze fragmenty.

Przykładowo:

```text
niewiarygodny
```

może zostać podzielony na fragmenty przypominające:

```text
nie
wiary
godny
```

Dokładny podział zależy od konkretnego tokenizera.

---

# 9. Token może być różnej długości

Token nie oznacza zawsze:

```text
1 token = 1 słowo
```

Może być:

```text
1 token = całe słowo
```

albo:

```text
1 token = fragment słowa
```

albo nawet:

```text
1 token = pojedynczy znak
```

Wszystko zależy od tego, jakie fragmenty tekstu znajdują się w słowniku danego tokenizera.

---

# 10. Częste fragmenty mogą mieć własne tokeny

Jeżeli jakiś fragment tekstu pojawia się bardzo często, może być reprezentowany przez pojedynczy token.

To pomaga modelowi działać efektywniej.

Zamiast rozbijać wszystko na pojedyncze litery, może operować na częściej występujących fragmentach.

---

# 11. Dlaczego tokenizacja jest dobrym kompromisem?

Podejście tokenowe łączy zalety obu wcześniejszych pomysłów.

## W porównaniu ze znakami

Model nie musi zawsze sam składać liter w większe jednostki.

## W porównaniu z pełnymi słowami

Nie potrzebujemy gigantycznego słownika wszystkich możliwych słów.

Dlatego tokenizacja jest:

- efektywna,
- praktyczna,
- łatwa do skalowania,
- dobrze dopasowana do współczesnych modeli językowych.

---

# 12. Tokeny a słownik modelu

Każdy model korzysta z określonego:

## vocabulary — słownika tokenów

Słownik zawiera dostępne tokeny.

Każdy token ma przypisany własny identyfikator:

## token ID

Schemat:

```text
"hello" → token ID 1234
```

lub:

```text
"ing" → token ID 5678
```

Dokładne wartości zależą od tokenizera.

---

# 13. Token ID

Po tokenizacji model nie dostaje już tekstu bezpośrednio.

Dostaje numery.

Czyli:

```text
tekst
 ↓
tokenizacja
 ↓
tokeny
 ↓
token IDs
```

Przykładowo:

```text
"Hello world"
```

może zostać zamienione na coś w rodzaju:

```text
[15496, 995]
```

To tylko przykład sposobu reprezentacji — konkretne numery zależą od modelu i tokenizera.

---

# 14. Token to jeszcze nie wektor

To bardzo ważne rozróżnienie.

## Token

jest fragmentem tekstu.

## Token ID

jest numerem przypisanym temu fragmentowi.

Ale to jeszcze nie jest:

## vector — wektor

Wektor pojawia się później.

Schemat:

```text
tekst
 ↓
token
 ↓
token ID
 ↓
embedding / wektor
 ↓
sieć neuronowa
```

---

# 15. Dlaczego nie należy mieszać tokenów z wektorami?

Token jest jednostką tekstową.

Przykład:

```text
"cat"
```

Token ID może być:

```text
12345
```

Natomiast embedding tego tokenu może być wektorem:

```text
[0.12, -0.83, 0.44, ...]
```

To są zupełnie różne rzeczy.

---

# 16. Gdzie pojawiają się wektory?

Po wejściu tokenów do modelu ich identyfikatory są przekształcane do reprezentacji wektorowych.

Te wektory są później używane wewnątrz sieci neuronowej.

Czyli:

```text
tokenizacja
 ↓
token IDs
 ↓
embeddingi
 ↓
transformer
```

Wykład podkreśla jednak, że na tym etapie warto najpierw dobrze zrozumieć tokeny, a dopiero później przejść do wektorów.

---

# 17. Tokenizacja nie jest fundamentalnym prawem

Wykład zwraca uwagę na ważną rzecz:

> Nie ma żadnego fundamentalnego prawa mówiącego, że modele językowe muszą używać tokenów.

Teoretycznie można budować modele:

- znakowe,
- słowowe,
- tokenowe.

Tokenizacja wygrała głównie dlatego, że okazała się bardzo dobrym kompromisem praktycznym.

---

# 18. Efektywność tokenizacji

Tokenizacja pomaga utrzymać rozsądny rozmiar słownika.

Jednocześnie pozwala reprezentować praktycznie dowolny tekst.

Jeżeli model nie ma tokenu odpowiadającego całemu słowu, może zejść do mniejszych fragmentów.

Dzięki temu system jest elastyczny.

---

# 19. Jak model widzi tekst?

Człowiek widzi:

```text
Machine learning is powerful.
```

Model widzi najpierw coś w rodzaju:

```text
["Machine", " learning", " is", " powerful", "."]
```

a potem:

```text
[token_id_1, token_id_2, token_id_3, ...]
```

Dopiero później te identyfikatory są zamieniane na reprezentacje liczbowe używane przez sieć.

---

# 20. Tokenizacja a długość wejścia

Ponieważ model operuje na tokenach, jego limit kontekstu jest zwykle podawany właśnie w tokenach.

Na przykład:

```text
128 000 tokenów
```

nie oznacza:

```text
128 000 słów
```

Liczba słów odpowiadająca konkretnej liczbie tokenów zależy od języka i treści.

---

# 21. Dlaczego tokenizacja ma znaczenie praktyczne?

Tokeny wpływają na:

- długość promptu,
- limit kontekstu,
- koszt zapytania,
- szybkość przetwarzania,
- liczbę kroków wykonywanych przez model.

Dlatego warto rozumieć, że model rozlicza i przetwarza tekst właśnie jako tokeny.

---

# 22. Tokenizer można podejrzeć wizualnie

Wykład wspomina o narzędziu OpenAI do wizualizacji tokenizacji.

Dzięki niemu można zobaczyć:

> Jak konkretny tekst zostaje podzielony na tokeny.

To dobry sposób na zbudowanie intuicji.

Można wkleić zdanie i zobaczyć, które fragmenty tekstu tworzą osobne tokeny.

---

# 23. Najważniejsza ewolucja

Można uprościć historię tak:

```text
znaki
 ↓
za dużo pracy dla sieci

całe słowa
 ↓
za duży słownik

tokeny
 ↓
praktyczny kompromis
```

---

# 24. Co warto zapamiętać?

1. **Token to fragment tekstu używany przez model jako jednostka wejścia.**
2. **Token nie musi być całym słowem.**
3. **Może być słowem, fragmentem słowa albo pojedynczym znakiem.**
4. **Podejście znakowe ma mały słownik, ale wymaga dużo pracy od modelu.**
5. **Podejście słowowe jest intuicyjne, ale prowadzi do ogromnego słownika.**
6. **Tokenizacja jest kompromisem między tymi dwoma podejściami.**
7. **Każdy token ma swój token ID.**
8. **Token ID nie jest tym samym co embedding lub wektor.**
9. **Wektory pojawiają się dopiero później wewnątrz modelu.**
10. **Tokeny wpływają na długość kontekstu, koszt i szybkość działania modelu.**

---

# 25. Całość w jednym schemacie

```text
TEKST
  ↓
TOKENIZACJA
  ↓
TOKENY
  ↓
TOKEN IDs
  ↓
EMBEDDINGI / WEKTORY
  ↓
TRANSFORMER
  ↓
KOLEJNE TOKENY
```

---

# 26. Najważniejsze zdanie

> **Tokenizacja to praktyczny kompromis między przetwarzaniem tekstu znak po znaku a traktowaniem każdego słowa jako osobnej jednostki.**
