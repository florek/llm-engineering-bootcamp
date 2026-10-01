# Tokeny i tiktoken

## Czym jest token

Model językowy nie „czyta" tekstu znak po znaku ani słowo po słowie w ludzkim sensie. Tekst jest najpierw dzielony na **tokeny** — fragmenty tekstu (słowa, części słów, znaki specjalne, spacje), którym przypisane są numeryczne identyfikatory. Model operuje na sekwencji tych identyfikatorów: przewiduje **kolejne najbardziej prawdopodobne tokeny** w ciągu.

Tokenizacja ma bezpośredni wpływ na:

- **koszt API** — rozliczenie zwykle idzie per token wejściowy i wyjściowy,
- **okno kontekstu** — limit dotyczy liczby tokenów, nie znaków czy słów,
- **jakość promptu** — zbędny HTML lub powtórzenia marnują budżet tokenów.

## Biblioteka tiktoken

**tiktoken** to tokenizer używany m.in. z modelami GPT. Pozwala w kodzie zobaczyć, jak konkretny model dzieli tekst na tokeny — bez wywoływania API.

Typowy przepływ:

1. Wybierz encoding powiązany z modelem (np. dla wybranego wariantu GPT).
2. **encode** — zamień tekst na listę identyfikatorów tokenów.
3. **decode** — zamień identyfikator (lub listę) z powrotem na tekst.

```python
encoding = tiktoken.encoding_for_model("gpt-4.1-mini")
tokens = encoding.encode("Hi my name is Ed and I like banoffee pie")
token_text = encoding.decode([token_id])
```

`encoding_for_model(...)` dobiera właściwy schemat tokenizacji dla wskazanego modelu — różne modele mogą dzielić ten sam tekst inaczej.

## Encode i decode

- **encode(tekst)** → lista liczb (ID tokenów). To reprezentacja, którą „widzi" model.
- **decode([id, ...])** → tekst odpowiadający tym tokenom. Pojedynczy ID może odpowiadać całemu słowu, fragmentowi słowa albo znakowi ze spacją.

Oglądanie mapowania `id → tekst` buduje intuicję, że token ≠ słowo: jedno słowo może być jednym tokenem albo kilkoma, a spacja często „przykleja się" do tokenu.

## Podgląd tokenów jeden po drugim

Najlepsza intuicja powstaje, gdy po `encode` przechodzisz listę ID i dla każdego robisz `decode([id])`.

Wtedy widać na żywo:

- popularne słowa często są jednym tokenem (często ze spacją na początku, np. `" and"`, `" my"`),
- rzadsze albo złożone słowa rozpadają się na fragmenty.

Przykład: w zdaniu o „banoffee pie” tokenizer może zostawić popularne słowa jako osobne tokeny, a rzadkie „banoffee” rozbić np. na `" ban"` + `"offee"`. To ten sam mechanizm co przy innych rzadkich wyrazach: słownik nie musi znać całego słowa, wystarczą częste kawałki.

## Związek z predykcją

LLM nie „pamięta" rozmowy ani nie „rozumie" w ludzkim sensie — przewiduje kolejne tokeny w sekwencji. Jeśli w sekwencji wejściowej jest informacja „nazywam się Ed", a później pytanie „jak mam na imię?", model z wysokim prawdopodobieństwem wygeneruje tokeny odpowiadające „Ed" — bo to najbardziej prawdopodobna kontynuacja całego ciągu.

## Pułapki

- Liczenie znaków nie równa się liczbie tokenów — ten sam limit znaków może dać różną liczbę tokenów w zależności od języka i encodingu.
- Różne modele → różne tokenizery; nie zakładaj, że ten sam tekst ma zawsze tyle samo tokenów.
- Surowy HTML i nawigacja w prompcie zużywają tokeny bez wartości merytorycznej.
