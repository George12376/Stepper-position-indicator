## Blokový diagram

![Blokový diagram](./Images/Block%20schematic.drawio.png)

## Schéma zapojení

![Schéma zapojení](./Images/Schema_V1.png)


## Správanie
Boot - ziskanie počiatočnej polohy

RGB indication
Červená bliká -> Ovládač motora vypnutý 
Zelená -> Najnižšia rýchlosť 
Žltá -> Stredná rýchlosť
Oranžová -> Najrýchlejšia rýchlosť

SW na enkódery
Krátke stlačenie -> zmena rýchlosti 
Dlhé stlačenie -> Zapnutie / vypnutie ovládaču motora ( po znova zapnutí znova nastavenie 0 pozície)

Buzzer
pri prechode medzi zap a vyp zabzučí 

Enkóder 
Podľa smeru otáčania sa bude otáčať aj motor

Display 
Zobrazuje aktuálny uhol motora voči nule a rýchlosť na jeden step encoderu
