# Stepper-position-indicator

## Členové týmu
Jiří Vocilka, Ondřej Chmela, Martin Kovář, Matěj Nachtnebel

## Popis problému a shrnutí řešení

Tento projekt řeší přesné vizuální zobrazování polohy pomocí krokového motoru.

* **Nastavení cílové polohy:** Otáčením rotačního enkodéru uživatel nastavuje požadovanou cílovou pozici.
* **Zapnutie a vypnutie ovládača motoru:** Dlhým stlačeným tlačidla na enkodéri sa vypne/ zapne ovládač motora. Zaznie tón pri zmene.
* **Zmena rýchlosti:**Krátkym stlačením tlačidla na enkodéri sa zmení rýchlosť pohybu motoru.
* **Řízení motoru:** Krokový motor automaticky otáčí fyzický ukazatel na nově nastavenou polohu.
* **Zobrazení dat na displeji:** Na displeji se v reálném čase zobrazuje aktuální a cílová poloha včetně stavových informací.
* **Nulování referenční polohy :** Stiskem mikrospínače se kalibruje nulová pozice pro přesné odměřování.
* **Stavová indikace:** RGB LED dioda vizuálně signalizuje provozní stavy systému (pohyb motoru, dosažení cíle, nulování).
  * Červená bliká -> Ovládač motora vypnutý 
  * Zelená -> Najnižšia rýchlosť 
  * Žltá -> Stredná rýchlosť
  * Oranžová -> Najrýchlejšia rýchlosť


## List komponent

| Množství | Komponenta | Popis / Funkce |
| :---: | :--- | :--- |
| 1x | Raspberry&nbsp;Pi&nbsp;Pico&nbsp;W | Řídicí mikrokontrolér (mozek celého systému), zpracovává vstupy a řídí ostatní komponenty. |
| 1x | Nema&nbsp;17 | Krokový motor – automaticky otáčí fyzický ukazatel na nově nastavenou polohu. |
| 1x | A4988 | Motor driver – obvod sloužící k řízení krokového motoru. |
| 1x | Waveshare&nbsp;1.3&nbsp;inch | Displej – v reálném čase zobrazuje aktuální a cílovou polohu včetně stavových informací. |
| 2x | ky-040 | Rotační enkodér – jeho otáčením uživatel nastavuje požadovanou cílovou pozici. |
| 1x | Mikrospínač | Nastavení počátku (re-zero) – stiskem se kalibruje nulová pozice pro přesné odměřování. |
| 1x | RGB&nbsp;Led | Stavová indikace – vizuálně signalizuje provozní stavy systému (pohyb motoru, dosažení cíle, nulování). |



