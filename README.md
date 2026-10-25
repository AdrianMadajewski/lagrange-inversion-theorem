# Twierdzenie Lagrange'a o odwracaniu

*czyli jak odwrócić (prawie) każdą funkcję*

[![Build PDF](https://github.com/AdrianMadajewski/lagrange-inversion-theorem/actions/workflows/build.yml/badge.svg)](https://github.com/AdrianMadajewski/lagrange-inversion-theorem/actions/workflows/build.yml)

Prezentacja (Beamer, ok. 30 minut) przygotowana na Koło Naukowe Matematyków UAM.

**[Pobierz najnowszy PDF](https://github.com/AdrianMadajewski/lagrange-inversion-theorem/releases/download/latest/lagrange.pdf)**

## O czym jest prezentacja

Co zrobić, gdy szukamy funkcji odwrotnej do $f$, ale nie potrafimy zapisać jej wzorem? Odpowiedzią są szeregi potęgowe. Twierdzenie Lagrange'a o odwracaniu (*Lagrange Inversion Theorem*) podaje jawny wzór na współczynniki szeregu funkcji odwrotnej.

Jeśli $f$ jest analityczna w otoczeniu $0$, $f(0) = 0$, $f'(0) \neq 0$ oraz $\varphi(x) := x / f(x)$, to funkcja odwrotna ma rozwinięcie $x(y) = \sum_{n \ge 1} a_n y^n$, gdzie

$$
a_n = \frac{1}{n!} \frac{d^{\,n-1}}{dx^{\,n-1}} \Big[ \varphi(x)^n \Big]_{x=0}.
$$

Plan prezentacji:

1. Funkcje analityczne i całka po krzywej na płaszczyźnie zespolonej.
2. Całka po okręgu jednostkowym, rachunek $\oint_{|z|=1} z^p \, dz$ i wzór całkowy Cauchy'ego.
3. Wyprowadzenie wzoru Lagrange'a przez podstawienie $y = f(x)$ i całkowanie przez części.
4. Przykłady, w tym funkcja $W$ Lamberta, czyli odwrotność $x e^x$, z promieniem zbieżności $1/e$.
5. Ogólna wersja twierdzenia (rozwinięcie wokół dowolnego punktu).

## Kompilacja

PDF buduje się automatycznie przy każdym pushu (GitHub Actions) i trafia do wydania [`latest`](https://github.com/AdrianMadajewski/lagrange-inversion-theorem/releases/tag/latest).

Lokalnie:

```bash
pdflatex lagrange.tex
pdflatex lagrange.tex
```

Wymagane pakiety (są w pełnej dystrybucji TeX Live / MiKTeX): `beamer`, `babel` (polish), `lmodern`, `mathtools`, `pgfplots`, `qrcode`. Plik `tlo.png` musi leżeć obok `lagrange.tex`.

## Struktura repozytorium

| Plik | Opis |
|---|---|
| `lagrange.tex` | źródło prezentacji |
| `tlo.png` | tło slajdu tytułowego, portret fazowy funkcji $(z^2-1)(z-2-i)^2/(z^2+2+2i)$ |
| `scripts/tlo.py` | skrypt generujący `tlo.png` (numpy, matplotlib, pillow) |
| `.github/workflows/build.yml` | automatyczna kompilacja do PDF |

## Literatura

- F. Leja, *Funkcje zespolone*, PWN.
- J. Chądzyński, *Wstęp do analizy zespolonej*, PWN, 1999.
- W. Rudin, *Analiza rzeczywista i zespolona*, PWN.
- E. M. Stein, R. Shakarchi, *Complex Analysis*, Princeton University Press, 2003.
- [Lagrange inversion theorem](https://en.wikipedia.org/wiki/Lagrange_inversion_theorem), Wikipedia.

## Autor

Adrian Madajewski, Koło Naukowe Matematyków UAM
