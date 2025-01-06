# XTILO_Semestralni_prace
## Simulátor jednopáskového Turingova stroje (Semestrální práce)

## Popis
Simulátor jednopáskového Turingova stroje je software napsaný v jazyce Python. Projekt simuluje Turingův stroj, který realizuje funkci `fun`. Funkce `fun` akceptuje řetězec čísel `x` zakódovaných v binární soustavě, oddělených prázdným symbolem ε, a definuje se jako: `fun(x_1, ..., x_n) = Σ_{i=1}^{n} x_i`. Projekt umožňuje definici konečné množiny stavů, koncových stavů, počátečního stavu a konečné abecedy, včetně prázdného symbolu.

## Použitá abeceda
Abeceda zahrnuje symboly `0, 1, #, a, b, x, d, n`:
- `0, 1`: Binární čísla
- `#`: Prázdný symbol
- `a, b`: Pomocné symboly pro orientaci, které bity byly připočteny v výsledném čísle
- `x`: Pomocný symbol ohraničující číslo, které se přidává k výsledku
- `n`: Ukazuje symboly, které byly již použity v čísle, které momentálně zpracováváme
- `d`: Používáme pro označení čísel, která byla zpracována

## Předpoklady
Pro spuštění tohoto projektu je potřeba mít nainstalovaný Python ve verzi 3.8 nebo vyšší.

## Instalace a spuštění
1. Klonujte repozitář: git clone https://github.com/degtya/XTILO_Semestralni_prace.git
2. Přejděte do složky projektu: python simulate.py

## Zdroje

Tento projekt byl inspirován a částečně založen na konceptech a metodách, které jsem studovala v ruských učebnicích o teorii Turingových strojů. Při hledání řešení a testování funkcionalit projektu jsem také využila online nástroj [Turing Machine Emulator](https://programforyou.ru/calculators/turing-machine-emulator), který byl neocenitelnou pomůckou při simulaci a ověřování algoritmů implementovaných v tomto projektu.

[1] [Tasks on Markov Algorithms (2020)](https://cmcmsu.info/download/cmc.mt.markov.tasks.pdf) 
[2] http://techn.sstu.ru/kafedri/%D0%BF%D0%BE%D0%B4%D1%80%D0%B0%D0%B7%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F/1/MetMat/shaturn/theoralg/3.htm
[3] https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%88%D0%B8%D0%BD%D0%B0_%D0%A2%D1%8C%D1%8E%D1%80%D0%B8%D0%BD%D0%B3%D0%B0
[4] https://www.youtube.com/watch?v=1pyrb01JKKM

## Autor
Bc. Olga Degtiareva
      
