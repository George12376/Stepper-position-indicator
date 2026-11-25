from machine import Pin, PWM
import time

class Buzzer:
    def __init__(self, pin_num):
        self.pwm = PWM(Pin(pin_num))
        self.pwm.duty_u16(0)

    def _tone(self, freq, duration):
        self.pwm.freq(freq)
        self.pwm.duty_u16(32768)
        time.sleep(duration)
        self.off()

    def beep_driver_on(self):
        # Zvuk při zapnutí ovladače motoru
        self._tone(1200, 0.1)
        time.sleep(0.05)
        self._tone(1800, 0.15)

    def beep_driver_off(self):
        # Zvuk při vypnutí ovladače motoru
        self._tone(1800, 0.1)
        time.sleep(0.05)
        self._tone(1000, 0.2)

    def off(self):
        self.pwm.duty_u16(0)


# Test bzucaku
buzzer = Buzzer(13)

print("1. Ovladac motoru ZAPNUTYabuzzer.beep_driver_on()
time.sleep(1.5)

print("2. Ovladac motoru VYPNUTY")
buzzer.beep_driver_off()
