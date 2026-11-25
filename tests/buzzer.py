from machine import Pin, PWM
import time


def test_buzzer_stavy():
    print("Test stavů bzučáku spuštěn (ukončíš přes Ctrl+C)")

    # Inicializace bzučáku na pinu GP13 (podle schématu):
    buzzer_pwm = PWM(Pin(13))
    buzzer_pwm.duty_u16(0)

    def zahraj_ton(frekvence, doba_trvani):
        buzzer_pwm.freq(frekvence)
        buzzer_pwm.duty_u16(32768)  # 50 % střída pro čistý zvuk
        time.sleep(doba_trvani)
        buzzer_pwm.duty_u16(0)

    try:
        while True:
            # 1. Zapnutí ovladače motoru -> Vzestupný tón
            print("Stav: Ovladač motoru zapnutý (Vzestupný tón)")
            zahraj_ton(1200, 0.1)
            time.sleep(0.05)
            zahraj_ton(1800, 0.15)
            time.sleep(2)

            # 2. Vypnutí ovladače motoru -> Sestupný tón
            print("Stav: Ovladač motoru vypnutý (Sestupný tón)")
            zahraj_ton(1800, 0.1)
            time.sleep(0.05)
            zahraj_ton(1000, 0.2)
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nTest ukončen.")
        buzzer_pwm.duty_u16(0)
        buzzer_pwm.deinit()


if __name__ == "__main__":
    test_buzzer_stavy()
