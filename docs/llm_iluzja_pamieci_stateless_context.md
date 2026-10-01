# Iluzja pamięci w LLM — stateless API i historia rozmowy

## 1. Najważniejsza idea lekcji

Jedna z najważniejszych rzeczy do zrozumienia przy pracy z LLM jest następująca:

> **Pojedyncze wywołanie modelu jest bezstanowe — stateless.**

Model sam z siebie nie pamięta poprzedniego wywołania API.

Jeżeli chcemy, aby rozmowa wyglądała tak, jakby model pamiętał wcześniejsze wiadomości, musimy przekazywać mu historię rozmowy ponownie przy każdym kolejnym wywołaniu.

To właśnie tworzy **iluzję pamięci**.

---

## 2. Załadowanie konfiguracji

Na początku aplikacja ładuje plik:

```text
.env
```

Znajdują się w nim sekrety i zmienne środowiskowe, np.:

```text
OPENAI_API_KEY
```

Dzięki temu aplikacja może korzystać z API bez wpisywania klucza bezpośrednio w kodzie.

W praktyce często używa się `load_dotenv(override=True)`, żeby wartości z pliku `.env` nadpisały ewentualne starsze zmienne w środowisku procesu — wtedy klient czyta aktualny klucz z konfiguracji projektu.

---

## 3. Klient OpenAI

Następnie tworzymy instancję klienta biblioteki OpenAI.

Ważne:

> Utworzenie klienta nie oznacza jeszcze uruchomienia modelu.

Klient jest po prostu wygodną warstwą do wykonywania żądań HTTP do API.

```text
Python
  ↓
OpenAI client
  ↓
HTTP request
  ↓
API
  ↓
LLM
```

---

## 4. Jak wygląda pojedyncze wywołanie?

Do modelu przekazujemy listę wiadomości.

Każda wiadomość zawiera m.in.:

```text
role
content
```

Przykład:

```python
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "Hi, I'm Ed."
    }
]
```

---

## 5. Role w rozmowie

### `system`

Instrukcja określająca zachowanie modelu.

```text
You are a helpful assistant.
```

### `user`

Wiadomość użytkownika.

```text
Hi, I'm Ed.
```

### `assistant`

Poprzednia odpowiedź modelu.

```text
Hi, Ed. Nice to meet you.
```

---

## 6. Pierwsze wywołanie

Przykład:

```text
system:
You are a helpful assistant.

user:
Hi, I'm Ed.
```

Model może odpowiedzieć:

```text
Hi, Ed. Nice to meet you.
```

Na pierwszy rzut oka wygląda więc tak, jakby model „dowiedział się”, że użytkownik ma na imię Ed.

---

## 7. Drugie wywołanie bez historii

Następnie wysyłamy nowe żądanie:

```text
system:
You are a helpful assistant.

user:
What's my name?
```

Model może odpowiedzieć:

```text
I don't know your name.
```

Dlaczego?

Ponieważ to jest **całkowicie nowe wywołanie**.

Model nie wie, że kilka sekund wcześniej otrzymał wiadomość:

```text
Hi, I'm Ed.
```

---

## 8. Każde wywołanie jest stateless

To kluczowy punkt.

Za każdym razem:

```text
request
  ↓
input sequence
  ↓
LLM
  ↓
output sequence
```

Model dostaje tylko to, co znajduje się w aktualnym wejściu.

Nie ma automatycznej pamięci poprzednich żądań.

---

## 9. Model przewiduje następne tokeny od nowa

Każde wywołanie modelu sprowadza się do:

```text
aktualna sekwencja wejściowa
        ↓
model
        ↓
przewidywanie kolejnych tokenów
```

Model nie korzysta z ukrytej historii poprzednich requestów.

Jeżeli informacji nie ma w aktualnym wejściu, model jej nie zna.

---

## 10. Skąd więc bierze się „pamięć” w czacie?

Rozwiązanie jest bardzo proste.

Przy każdym kolejnym wywołaniu przekazujemy modelowi:

> **całą dotychczasową historię rozmowy.**

Czyli zamiast:

```text
What's my name?
```

wysyłamy:

```text
system:
You are a helpful assistant.

user:
Hi, I'm Ed.

assistant:
Hi, Ed. Nice to meet you.

user:
What's my name?
```

---

## 11. Model wtedy „pamięta”

Po otrzymaniu pełnej historii model może odpowiedzieć:

```text
Your name is Ed.
```

Nie dlatego, że pamięta poprzednią rozmowę.

Tylko dlatego, że informacja:

```text
Hi, I'm Ed.
```

znajduje się ponownie w aktualnej sekwencji wejściowej.

---

## 12. To jest iluzja pamięci

Użytkownik ma wrażenie:

```text
model pamięta rozmowę
```

ale technicznie dzieje się:

```text
aplikacja przechowuje historię
        ↓
przekazuje ją ponownie
        ↓
model otrzymuje pełny kontekst
        ↓
generuje odpowiedź zgodną z historią
```

To właśnie autor nazywa **illusion of memory**.

---

## 13. Model nie pamięta — aplikacja pamięta

To bardzo ważne rozróżnienie.

### LLM

Jest bezstanowy pomiędzy niezależnymi wywołaniami.

### Aplikacja

Może przechowywać:

- wcześniejsze wiadomości użytkownika,
- odpowiedzi modelu,
- instrukcję systemową.

Następnie składa z tego nowe wejście.

---

## 14. Przykład pełnej listy wiadomości

```python
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "Hi, I'm Ed."
    },
    {
        "role": "assistant",
        "content": "Hi, Ed. Nice to meet you."
    },
    {
        "role": "user",
        "content": "What's my name?"
    }
]
```

Model widzi wszystko naraz.

---

## 15. Dlaczego odpowiedź „Ed” jest naturalna?

Jeżeli sekwencja zawiera:

```text
My name is Ed.
What's my name?
```

to bardzo prawdopodobnym kolejnym ciągiem tokenów jest:

```text
Your name is Ed.
```

Jeżeli natomiast wejście zawiera tylko:

```text
What's my name?
```

to bardziej prawdopodobne jest:

```text
I don't know your name.
```

To nadal jest przewidywanie kolejnych tokenów na podstawie aktualnego wejścia.

---

## 16. Pięć najważniejszych punktów

1. **Każde wywołanie jest stateless.**
2. **Historia rozmowy musi być przekazana ponownie.**
3. **To tworzy iluzję pamięci.**
4. **Model nadal przewiduje kolejne tokeny.**
5. **Pamięć rozmowy kosztuje tokeny.**

---

## 17. Rosnąca historia oznacza rosnący kontekst

Załóżmy rozmowę:

```text
1. Hi, I'm Ed.
2. Hello Ed.
3. What's my name?
4. Your name is Ed.
5. What did I ask before?
```

Przy piątym wywołaniu aplikacja może przesłać wszystkie wcześniejsze wiadomości.

Czyli wejście stale rośnie.

---

## 18. Dlaczego trzeba za to płacić?

Jeżeli przy każdym wywołaniu przesyłamy historię ponownie, te tokeny są ponownie przetwarzane.

Powód jest prosty:

> Model musi ponownie przeanalizować kontekst, aby wygenerować kolejną odpowiedź.

To nie jest „ukryta opłata za błąd projektu”. To zamierzone zachowanie: chcemy, żeby model przy każdej turze realnie „patrzył” na całą dotychczasową sekwencję — a to wymaga obliczeń i dlatego generuje koszt.

---

## 19. Więcej kontekstu = więcej obliczeń

Porównajmy:

```text
What's my name?
```

z:

```text
pełna historia rozmowy
+
What's my name?
```

W drugim przypadku model musi przeanalizować więcej tokenów.

```text
więcej tokenów wejściowych
        ↓
więcej obliczeń
        ↓
większy koszt
```

---

## 20. Koszt pojedynczych tokenów jest mały, ale się kumuluje

W materiale podkreślono, że pojedyncze tokeny wejściowe są zwykle bardzo tanie.

Jednak przy:

- bardzo długich rozmowach,
- dużej liczbie użytkowników,
- długich dokumentach,

koszt zaczyna mieć znaczenie.

---

## 21. Długa rozmowa może kosztować coraz więcej

Przykład:

```text
request 1 → 100 tokenów historii
request 2 → 300 tokenów historii
request 3 → 600 tokenów historii
request 4 → 1000 tokenów historii
```

Jeżeli za każdym razem przesyłamy wszystko od początku, koszt wejścia rośnie wraz z długością rozmowy.

---

## 22. Kontekst rozmowy to część input sequence

Sekwencja wejściowa może zawierać:

```text
system prompt
+
wcześniejsze wiadomości użytkownika
+
wcześniejsze odpowiedzi assistant
+
aktualne pytanie
```

Dopiero całość trafia do modelu.

---

## 23. Chat nie jest magiczną pamięcią modelu

Interfejs rozmowy może wyglądać tak:

```text
User: Hi, I'm Ed.
Assistant: Hi Ed.
User: What's my name?
Assistant: Ed.
```

Ale technicznie drugie wywołanie może wyglądać tak:

```text
[
  system,
  user #1,
  assistant #1,
  user #2
]
```

To aplikacja buduje historię.

---

## 24. Dlaczego to jest ważne dla inżyniera AI?

Przy budowaniu aplikacji trzeba świadomie zdecydować:

- jakie wiadomości przechowywać,
- ile historii przekazywać,
- czy skracać stare wiadomości,
- czy robić streszczenia,
- jak kontrolować koszt,
- jak zmieścić historię w limicie kontekstu.

Bez zrozumienia bezstanowości trudno poprawnie budować systemy konwersacyjne.

---

## 25. Typowy schemat aplikacji czatowej

```text
użytkownik wysyła wiadomość
        ↓
aplikacja pobiera historię
        ↓
dodaje nową wiadomość
        ↓
wysyła całość do LLM
        ↓
LLM generuje odpowiedź
        ↓
aplikacja zapisuje odpowiedź
        ↓
następna wiadomość
```

---

## 26. Przykład pseudo-kodu

```python
messages = [
    {"role": "system", "content": "You are helpful."}
]

messages.append({
    "role": "user",
    "content": "Hi, I'm Ed."
})

response = call_llm(messages)

messages.append({
    "role": "assistant",
    "content": response
})

messages.append({
    "role": "user",
    "content": "What's my name?"
})

response = call_llm(messages)
```

Kluczowe jest to, że `messages` zawiera wcześniejszą historię.

---

## 27. Co warto zapamiętać?

1. **Wywołania LLM przez API są bezstanowe.**
2. **Model sam nie pamięta poprzedniego requestu.**
3. **Historia rozmowy jest przechowywana przez aplikację.**
4. **Przy każdym wywołaniu historia może być przesyłana ponownie.**
5. **Role `system`, `user` i `assistant` budują strukturę rozmowy.**
6. **To właśnie pełny kontekst tworzy iluzję pamięci.**
7. **LLM nadal przewiduje kolejne tokeny na podstawie aktualnego wejścia.**
8. **Dłuższa historia oznacza więcej tokenów wejściowych.**
9. **Więcej tokenów oznacza więcej obliczeń i większy koszt.**
10. **Zrozumienie tego mechanizmu jest podstawą budowania aplikacji konwersacyjnych.**

---

## 28. Całość w jednym schemacie

```text
PIERWSZE WYWOŁANIE

system
+
user: "Hi, I'm Ed."
        ↓
       LLM
        ↓
assistant: "Hi Ed."


DRUGIE WYWOŁANIE

system
+
user: "Hi, I'm Ed."
+
assistant: "Hi Ed."
+
user: "What's my name?"
        ↓
       LLM
        ↓
assistant: "Your name is Ed."
```

---

## 29. Najważniejsze zdanie

> **LLM nie pamięta poprzedniej rozmowy — to aplikacja przekazuje mu historię ponownie, dzięki czemu model może wygenerować odpowiedź zgodną z wcześniejszym kontekstem.**
