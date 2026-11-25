import time
from machine import Pin

print("Pomaly test STEP...")
Pin(18, Pin.OUT).value(0)  # ENA
Pin(19, Pin.OUT).value(1)  # SLP
Pin(20, Pin.OUT).value(1)  # RST
Pin(26, Pin.OUT).value(0)  # MS1
Pin(21, Pin.OUT).value(0)  # MS2
Pin(22, Pin.OUT).value(0)  # MS3
Pin(16, Pin.OUT).value(1)  # DIR

step = Pin(17, Pin.OUT)
for i in range(40):
    step.value(1)
    time.sleep_ms(500)
    step.value(0)
    time.sleep_ms(500)
print("Konec")
