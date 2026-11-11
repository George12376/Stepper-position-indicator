# Stepper-position-indicator

## Členové týmu
Jiří Vocilka, Ondřej Chmela, Martin Kovář, Matěj Nachtnebel

## Problem statement & summary of the solution

Tento projekt řeší přesné vizuální zobrazování polohy pomocí krokového motoru.

* **Nastavení cílové polohy:** Otáčením rotačního enkodéru uživatel nastavuje požadovanou cílovou pozici.
* **Řízení motoru:** Krokový motor automaticky otáčí fyzický ukazatel na nově nastavenou polohu.
* **Zobrazení dat na displeji:** Na displeji se v reálném čase zobrazuje aktuální a cílová poloha včetně stavových informací.
* **Nulování referenční polohy (Re-zero):** Stiskem mikrospínače se kalibruje nulová pozice pro přesné odměřování.
* **Stavová indikace:** RGB LED dioda vizuálně signalizuje provozní stavy systému (pohyb motoru, dosažení cíle, nulování).

## List komponent

Raspberry Pi Pico W\
Nema 17 - krokový motor\
A4988 - motor driver\
Waveshare 1.3 inch- Displej\
2x ky-040 - Encoder\
Mikrospínač - nastavení počátku (re-zero reference)\
RGB Led



