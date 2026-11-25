# Stepper-position-indicator

![MicroPython](https://img.shields.io/badge/MicroPython-1.24+-blue)
![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi%20Pico-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Členové týmu
* Jiří Vocilka -
* Ondřej Chmela -
* Martin Kovář -
* Matěj Nachtnebel -

## Popis problému a shrnutí řešení

Tento projekt řeší přesné vizuální zobrazování polohy pomocí krokového motoru.

* **Nastavení cílové polohy:** Otáčením rotačního enkodéru uživatel nastavuje požadovanou cílovou pozici.
* **Zapnutí a vypnutí ovladače motoru:** Dlouhým stiskem tlačítka na enkodéru se vypne/zapne ovladač motoru. Při změně zazní tón.
* **Změna rychlosti:** Krátkým stiskem tlačítka na enkodéru se změní rychlost pohybu motoru.
* **Řízení motoru:** Krokový motor automaticky otáčí fyzický ukazatel na nově nastavenou polohu.
* **Zobrazení dat na displeji:** Na displeji se v reálném čase zobrazuje aktuální a cílová poloha včetně stavových informací.
* **Nulování referenční polohy:** Stiskem mikrospínače se kalibruje nulová pozice pro přesné odměřování.
* **Stavová indikace:** RGB LED dioda vizuálně signalizuje provozní stavy systému (pohyb motoru, dosažení cíle, nulování).
  * Červená bliká -> Ovladač motoru vypnutý
  * Zelená -> Nejnižší rychlost
  * Žlutá -> Střední rychlost
  * Oranžová -> Nejvyšší rychlost


## List komponent

| Množství | Komponenta | Popis / Funkce |
| :---: | :--- | :--- |
| 1x | Raspberry&nbsp;Pi&nbsp;Pico&nbsp;W | Řídicí mikrokontrolér (mozek celého systému), zpracovává vstupy a řídí ostatní komponenty. |
| 1x | Nema&nbsp;17 | Krokový motor – automaticky otáčí fyzický ukazatel na nově nastavenou polohu. |
| 1x | A4988 | Motor driver – obvod sloužící k řízení krokového motoru. |
| 1x | 1.30"IIC Ver. 3.0 | Displej – v reálném čase zobrazuje aktuální a cílovou polohu včetně stavových informací. |
| 1x | ky-040 | Rotační enkodér – jeho otáčením uživatel nastavuje požadovanou cílovou pozici. |
| 1x | Mikrospínač | Nastavení počátku (re-zero) – stiskem se kalibruje nulová pozice pro přesné odměřování. |
| 1x | RGB&nbsp;Led | Stavová indikace – vizuálně signalizuje provozní stavy systému (pohyb motoru, dosažení cíle, nulování). |
| 1x | Bzučák HW-508 | Zvuková indikace – zaznění tónu při změně stavu motoru|

## Časování

| Část systému | Jak se spouští | Jak často běží | Co přesně dělá |
| :--- | :--- | :--- | :--- |
| **Enkodér (otáčení)** | Přerušení (`IRQ`) | Okamžitě při otočení | Hned zaznamená změnu polohy, aby se neztratil žádný krok. |
| **Krokový motor** | Asynchronní úloha | 125 Hz až 1000 Hz (pauza 8–1 ms) | Otáčí motorem na cílovou polohu s plynulým rozjezdem. |
| **Tlačítka** | Opakovaná kontrola | 100 Hz (každých 10 ms) | Kontroluje stisk enkodéru (rychlost / vypnutí) a mikrospínač nuly. |
| **OLED displej** | Opakovaná kontrola | ~6,7 Hz (každých 150 ms) | Překreslí údaje na obrazovce, ale jen když se nějaká hodnota změnila. |
| **RGB LED dioda** | Opakovaná kontrola | 10 Hz (každých 100 ms) | Svítí podle zvolené rychlosti, nebo bliká červeně (500 ms), když je motor vypnutý. |
| **Bzučák** | Opakovaná kontrola | 50 Hz (každých 20 ms) | Pípne při zapnutí nebo vypnutí motoru. |

## Softwarové prostředí a verze knihoven

Projekt je naprogramován v jazyce **MicroPython** pro mikrokontrolér **Raspberry Pi Pico W (RP2040)** ve vývojovém prostředí **VS Code** s rozšířením **MicroPico**. Nepoužívá žádné externí balíčky třetích stran instalované přes `mip`/`pip` – veškerá aplikační logika staví na standardních modulech firmwaru a vlastních ovladačích ve složce [`lib`](lib).

### Použité vestavěné knihovny (součást firmwaru MicroPython v1.29.0)
* **`machine`** (`Pin`, `PWM`, `I2C` / `SoftI2C`, `disable_irq`, `enable_irq`) – řízení GPIO pinů, PWM signálů pro RGB LED a bzučák, I2C komunikace s displejem a bezpečné čtení dat z přerušení.
* **`asyncio` (`uasyncio`)** – kooperativní multitasking pro neblokující souběžný běh řízení motoru, čtení vstupů, překreslování OLED displeje, stavové LED a bzučáku.
* **`framebuf`** – grafický framebuffer (`MONO_VLSB`) pro vykreslování textu na OLED displej.
* **`time`**, **`micropython`** (`const`) – mikrosekundové/milisekundové časování krokování a paměťová optimalizace konstant.

### Vlastní a upravené knihovny projektu (`lib/`)
* **[`ssd1306.py`](lib/ssd1306.py)** – vlastní implementace ovladače se stránkovým adresováním pro 1,3" I2C OLED displej 128×64 s řadičem **SH1106** (zachovává kompatibilní rozhraní `SSD1306_I2C`).
* **[`stepper.py`](lib/stepper.py)** – ovládání driveru A4988, nastavení mikrokrokování, automatická kalibrace polohy (*homing*) a softwarové limity pohybu (`0–760` kroků).
* **[`encoder.py`](lib/encoder.py)** – obsluha rotačního enkodéru KY-040 pomocí kvadraturního stavového automatu (Grayův kód) se softwarovým ošetřením zákmitů tlačítka (*debounce*).
* **[`status_led.py`](lib/status_led.py)** – PWM řízení stavové RGB LED pro indikaci rychlosti a stavu povolení driveru.
* **[`buzzer.py`](lib/buzzer.py)** – neblokující generování zvukové signalizace na pasivním bzučáku pomocí PWM.

## Blokový diagram

![Blokový diagram](./Images/Block%20schematic.drawio_V3.png)

## Schéma zapojení

![Schéma zapojení](./Images/Schema_V3.png)

## Testování a ověření

Před finálním sestavením byly jednotlivé moduly otestovány samostatně pomocí skriptů ve složce [`tests`](./tests):

### 1. Stavová indikace ([RGB LED](./tests/RGB_LED.py))
- **Zapojení a funkčnost:** Ověřena správná polarita (společná katoda na `GND`) a funkce aktivních barevných kanálů (červený a zelený).
- **PWM stavy:** Otestováno plynulé míchání barev pro jednotlivé rychlosti (zelená – nízká, žlutá – střední, oranžová – vysoká) i červené blikání (500 ms) při vypnutém motoru.

### 2. Zvuková signalizace ([Pasivní bzučák](./tests/buzzer.py))
- **Generování tónů pomocí PWM:** Ověřeno buzení pasivního měniče signálem PWM (50% střída) a čisté vypnutí výstupu (`duty_u16(0)`) po doznění tónu.
- **Akustická odezva stavů:** Otestováno přehrání dvoutónových signálů pro rozlišení stavu driveru – vzestupná melodie (1200 Hz → 1800 Hz) při zapnutí a sestupná melodie (1800 Hz → 1000 Hz) při vypnutí ovladače motoru.

### 3. Zobrazovací jednotka ([OLED displej](./tests/displej.py))
- **Komunikace a inicializace:** Ověřena detekce displeje (128×64 px) na sběrnici I2C (400 kHz) a správné vykreslování grafiky i textu přes framebuffer.
- **Vykreslování stavů:** Otestováno zobrazení úvodního nulování (`NULOVANI...`), dynamická aktualizace aktuální a cílové polohy při pohybu i indikace stavu motoru (`ZAP`/`VYP`) a zvolené rychlosti.

### 4. Pohon a řízení polohy ([Krokový motor](tests/Test_motor.py))

* **Řídicí logika a režim driveru:** Ověřena správná inicializace driveru A4988 přes GPIO piny – povolení výkonových výstupů (`ENA = 0`), probuzení a uvolnění resetu (`SLP = 1`, `RST = 1`), pevný směr otáčení (`DIR = 1`) a nastavení celokrokového režimu (`MS1`–`MS3 = 0`) při nastaveném proudovém omezení (`Vref` ≈ 0,5 V).
* **Pomalý test krokování (`STEP`):** Otestováno generování 40 pulzů na pinu `STEP` (`GPIO17`) s periodou 1 s (500 ms `HIGH` / 500 ms `LOW`), což umožnilo vizuálně ověřit pravidelné krokování hřídele, správné zapojení cívek motoru i přímé proměření logických úrovní multimetrem.





