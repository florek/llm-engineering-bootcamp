# Od LSTM do Agentic AI — uporządkowane notatki z wykładu

## 1. Co było przed transformerami?

Przed erą transformerów jednym z najważniejszych typów modeli do przetwarzania tekstu były **sieci rekurencyjne**, a szczególnie **LSTM (Long Short-Term Memory)**.

LSTM to odmiana sieci RNN (*Recurrent Neural Network*), zaprojektowana tak, aby lepiej radzić sobie z zapamiętywaniem informacji z wcześniejszych fragmentów sekwencji.

### Główna zaleta LSTM

Model przetwarza tekst **krok po kroku** i może przekazywać informacje z jednego kroku do następnego.

Dzięki temu potrafi uwzględniać zależności między wcześniejszymi i późniejszymi elementami tekstu.

### Główny problem LSTM

Przetwarzanie jest **sekwencyjne**.

To znaczy, że aby policzyć krok 10, model musi wcześniej policzyć krok 9, a przed nim krok 8 itd.

Nie da się więc łatwo wykonywać wszystkich obliczeń równolegle.

W praktyce oznaczało to:

- długi czas trenowania,
- duży koszt obliczeniowy,
- problemy ze skalowaniem modeli,
- trudniejsze wykorzystanie ogromnych zbiorów danych.

---

## 2. Dlaczego transformery okazały się przełomem?

Transformer zmienił sposób przetwarzania tekstu.

Najważniejsza różnica polega na tym, że model nie musi analizować tekstu wyłącznie słowo po słowie.

Może analizować wiele elementów sekwencji **równolegle**.

Kluczowym mechanizmem jest tutaj **attention**, czyli mechanizm uwagi.

Pozwala on modelowi ocenić:

> Które fragmenty wejścia są najważniejsze dla aktualnie analizowanego fragmentu?

### Dlaczego to było tak ważne?

Ponieważ obliczenia można było znacznie lepiej wykonywać równolegle na GPU.

To umożliwiło:

- trenowanie większych modeli,
- trenowanie na większych zbiorach danych,
- znacznie szybsze skalowanie,
- powstanie współczesnych dużych modeli językowych.

Transformer nie wygrał tylko dlatego, że był „mądrzejszy”.

Jego ogromną przewagą była przede wszystkim **skalowalność**.

---

## 3. Początkowo wiele osób nie spodziewało się tak dużych możliwości

Na początku duże modele językowe były często postrzegane jako bardzo zaawansowane modele statystyczne.

Ich podstawowe zadanie wygląda przecież stosunkowo prosto:

> Na podstawie wcześniejszych tokenów przewidzieć następny token.

Token może być:

- całym słowem,
- fragmentem słowa,
- znakiem,
- innym elementem tekstu.

Można więc powiedzieć, że model wykonuje bardzo zaawansowane:

**„przewidywanie następnego fragmentu tekstu”**.

Przez pewien czas część osób uważała, że takie modele będą jedynie czymś w rodzaju:

> bardzo rozbudowanego autouzupełniania tekstu.

Okazało się jednak, że przy odpowiednio dużej skali dzieje się coś znacznie ciekawszego.

---

## 4. Emergent intelligence — zdolności pojawiające się wraz ze skalą

Wraz ze wzrostem:

- liczby parametrów,
- ilości danych treningowych,
- mocy obliczeniowej,

modele zaczęły wykazywać zdolności, których wcześniej nie oczekiwano.

Nie tylko generowały tekst wyglądający wiarygodnie.

Zaczęły również wykonywać zadania przypominające rozumowanie, np.:

- odpowiadać na pytania,
- streszczać,
- tłumaczyć,
- pisać kod,
- analizować tekst,
- wykonywać wieloetapowe polecenia,
- łączyć informacje z różnych części kontekstu.

Takie zjawisko bywa określane jako:

## Emergent intelligence

czyli **zdolności pojawiające się wraz ze skalą modelu**.

Idea jest następująca:

> Model nadal przewiduje tokeny, ale przy odpowiednio dużej skali rezultat zaczyna bardzo dobrze imitować zachowania kojarzone z inteligencją.

---

# 5. Prompt engineering

Kiedy pojawiły się pierwsze szeroko dostępne LLM-y, bardzo ważnym pojęciem stało się:

## Prompt engineering

czyli sztuka formułowania poleceń dla modelu.

Przez pewien czas „Prompt Engineer” był nawet osobnym stanowiskiem.

Dobry prompt może zawierać np.:

- kontekst,
- rolę modelu,
- cel zadania,
- przykłady,
- oczekiwany styl odpowiedzi,
- wymagany format,
- ograniczenia.

### Przykład

Zamiast:

> Napisz opis produktu.

można napisać:

> Napisz krótki opis produktu dla sklepu internetowego.  
> Odbiorcą są osoby w wieku 25–40 lat.  
> Styl ma być profesjonalny, ale prosty.  
> Maksymalnie 100 słów.  
> Na końcu dodaj trzy najważniejsze zalety produktu.

Wraz z popularyzacją LLM-ów coraz więcej użytkowników nauczyło się takich technik.

Dlatego samo „prompt engineering” przestało być czymś wyjątkowym.

---

# 6. Copiloty — człowiek pracujący razem z AI

Kolejnym ważnym etapem rozwoju były narzędzia typu **copilot**.

Przykłady:

- GitHub Copilot,
- Microsoft Copilot,
- asystenci AI do pracy z dokumentami,
- asystenci programistyczni.

Idea copilota jest prosta:

> Człowiek nadal wykonuje pracę, ale model AI pomaga mu w jej wykonywaniu.

AI może na przykład:

- pisać fragmenty kodu,
- poprawiać kod,
- streszczać dokument,
- analizować dane,
- tworzyć pierwszą wersję tekstu,
- sugerować rozwiązania,
- wykonywać powtarzalne czynności.

Nie chodzi więc o pełne zastąpienie człowieka.

Chodzi o **współpracę człowieka z modelem**.

---

# 7. Context engineering — następca prompt engineering

Nowszym pojęciem jest:

## Context engineering

Można powiedzieć, że jest to rozszerzenie prompt engineering.

Prompt engineering skupia się głównie na pytaniu:

> Jak napisać dobre polecenie?

Context engineering zadaje szersze pytanie:

> Jak dostarczyć modelowi wszystkie informacje potrzebne do poprawnego wykonania zadania?

Nie chodzi więc tylko o sam prompt.

Do kontekstu mogą trafić również:

- dane firmy,
- dokumenty,
- instrukcje,
- baza wiedzy,
- dane klienta,
- wyniki wyszukiwania,
- historia rozmowy,
- dane pobrane z API,
- wyniki działania innych narzędzi.

---

## 8. Dlaczego kontekst jest tak ważny?

LLM generuje odpowiedź na podstawie tego, co znajduje się w jego **sekwencji wejściowej**.

Jeżeli model nie ma potrzebnej informacji, może:

- odpowiedzieć błędnie,
- zgadywać,
- wygenerować nieaktualne dane.

### Przykład: ceny biletów

Załóżmy, że budujemy system odpowiadający klientom na pytania o ceny biletów.

Model musi otrzymać aktualne ceny jako część kontekstu.

Schemat wygląda wtedy mniej więcej tak:

```text
Pytanie użytkownika
        +
instrukcja systemu
        +
aktualne ceny biletów
        +
inne potrzebne dane
        ↓
       LLM
        ↓
poprawna odpowiedź
```

Nie wystarczy więc powiedzieć modelowi:

> Podaj cenę biletu.

Trzeba mu również dostarczyć **aktualną cenę**.

To właśnie jest sedno context engineering.

---

# 9. Tools — narzędzia dostępne dla LLM

Kolejnym krokiem jest wyposażenie modelu w **tools**, czyli narzędzia.

Narzędzie może być zwykłą funkcją lub API.

Na przykład:

```text
LLM
 ├── wyszukiwarka
 ├── baza danych
 ├── API pogodowe
 ├── system rezerwacji
 ├── kalkulator
 └── funkcja wysyłająca e-mail
```

Model może zdecydować, że do rozwiązania problemu potrzebuje któregoś z tych narzędzi.

Przykład:

Użytkownik:

> Ile kosztuje lot do Londynu jutro?

Model sam nie zna aktualnej ceny.

Może więc:

1. wywołać API przewoźnika,
2. pobrać aktualną cenę,
3. dodać ją do kontekstu,
4. wygenerować odpowiedź.

---

# 10. Agentic AI

Jednym z najważniejszych obecnie kierunków rozwoju AI jest:

## Agentic AI

Nie istnieje jedna idealna definicja agenta, ale często spotyka się dwie.

---

## Definicja 1 — LLM steruje workflow

Agent to system, w którym model językowy decyduje:

> Co powinno wydarzyć się dalej?

Może na przykład:

1. przeanalizować zadanie,
2. zaplanować kroki,
3. wywołać narzędzie,
4. przeanalizować wynik,
5. wykonać kolejny krok,
6. zakończyć zadanie.

Model staje się więc elementem sterującym całym procesem.

---

## Definicja 2 — LLM w pętli z narzędziami

Druga popularna definicja mówi:

> Agent to LLM działający w pętli i mający dostęp do narzędzi.

Schemat może wyglądać tak:

```text
        ┌───────────────┐
        │      LLM      │
        └───────┬───────┘
                │
                ▼
        Co zrobić dalej?
                │
                ▼
        użycie narzędzia
                │
                ▼
          wynik działania
                │
                └──────────────┐
                               │
                               ▼
                              LLM
```

Model może więc być wywoływany wielokrotnie.

Każde wywołanie przybliża go do wykonania całego zadania.

---

# 11. Przykład działania agenta

Załóżmy, że użytkownik mówi:

> Znajdź restaurację na dziś wieczorem i zarezerwuj stolik.

Agent może wykonać następujące kroki:

```text
1. Zrozumienie zadania
        ↓
2. Wyszukanie restauracji
        ↓
3. Sprawdzenie dostępnych terminów
        ↓
4. Wybranie odpowiedniej opcji
        ↓
5. Złożenie rezerwacji
        ↓
6. Potwierdzenie użytkownikowi
```

Każdy krok może oznaczać:

- kolejne wywołanie LLM,
- użycie narzędzia,
- analizę jego wyniku.

---

# 12. Claude Code jako przykład Agentic AI

Dobrym przykładem systemu agentowego jest **Claude Code**.

Podczas pracy można zobaczyć, że system:

1. analizuje zadanie,
2. tworzy plan,
3. buduje listę kroków,
4. wykonuje kolejne działania,
5. sprawdza wyniki,
6. poprawia błędy,
7. przechodzi do kolejnego kroku.

Z punktu widzenia użytkownika może to wyglądać tak, jakby AI samodzielnie „pracowało nad zadaniem”.

Technicznie nadal jest to jednak seria:

```text
input → LLM → output → narzędzie → nowy input → LLM → ...
```

---

# 13. Co oznacza „autonomia” agenta?

W kontekście Agentic AI często używa się słowa:

## autonomia

Nie oznacza ono, że model posiada własną wolę.

Chodzi o coś znacznie bardziej technicznego.

Model może wygenerować w odpowiedzi informację:

> Następnym krokiem powinno być wykonanie X.

System odczytuje tę informację i wykonuje X.

Następnie wynik wraca do modelu.

Można więc powiedzieć, że model:

> **wybiera następny krok procesu**.

I właśnie to często określa się jako autonomiczne działanie agenta.

---

# 14. Najważniejsza rzecz: pod spodem nadal działa ten sam mechanizm

Choć współczesne systemy AI mogą wyglądać bardzo skomplikowanie, ich podstawowy mechanizm nadal jest podobny:

```text
INPUT
  ↓
LLM
  ↓
przewidywanie tokenów
  ↓
OUTPUT
```

Różnica polega na tym, że nowoczesne systemy budują wokół LLM dodatkową infrastrukturę:

```text
LLM
 +
kontekst
 +
pamięć
 +
narzędzia
 +
dane
 +
pętla
 +
planowanie
 =
system agentowy
```

---

# 15. Ewolucja wykorzystania LLM

Można uprościć rozwój współczesnego AI do kilku etapów:

```text
LSTM / RNN
   ↓
Transformer
   ↓
LLM
   ↓
Prompt Engineering
   ↓
Copilots
   ↓
Context Engineering
   ↓
Tools
   ↓
Agentic AI
```

Każdy kolejny krok zwiększa możliwości systemów opartych na modelach językowych.

---

# 16. Krótkie podsumowanie

### LSTM

Przetwarza sekwencję krok po kroku.

Problem:

**trudno wykonywać obliczenia równolegle.**

---

### Transformer

Pozwala znacznie lepiej analizować elementy sekwencji równolegle.

Efekt:

**łatwiejsze skalowanie modeli.**

---

### LLM

Duży model językowy przewidujący kolejne tokeny.

Przy dużej skali pojawiają się bardzo zaawansowane zdolności.

---

### Prompt Engineering

Sztuka formułowania dobrego polecenia dla modelu.

---

### Copilot

AI współpracujące z człowiekiem podczas wykonywania pracy.

---

### Context Engineering

Dostarczanie modelowi wszystkich danych potrzebnych do poprawnego wykonania zadania.

---

### Tools

Funkcje i API, z których model może korzystać.

---

### Agentic AI

System, w którym LLM:

- działa w pętli,
- korzysta z narzędzi,
- analizuje wyniki,
- wybiera kolejne działania,
- wykonuje wieloetapowe zadania.

---

# Najważniejsza myśl z wykładu

> **LLM nadal przede wszystkim przewiduje kolejne tokeny.**

Cała „magia” współczesnych systemów AI powstaje dzięki połączeniu tego mechanizmu z:

- ogromną skalą,
- dobrym kontekstem,
- narzędziami,
- pamięcią,
- planowaniem,
- wielokrotnym wywoływaniem modelu.

To właśnie z takich elementów powstają współczesne systemy Agentic AI.
