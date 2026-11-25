from machine import Pin, PWM
import time


def test_rgb_stavy():
    print("Test stavů RGB LED spuštěn (ukončíš přes Ctrl+C)")

    # Správné piny podle vašeho zapojení:
    r_pwm = PWM(Pin(14), freq=1000)  # GP14 = červená
    g_pwm = PWM(Pin(13), freq=1000)  # GP13 = zelená
    b_pwm = PWM(Pin(12), freq=1000)  # GP12 = modrá

    def nastav_barvu(r, g, b):
        # Převod 0-255 na rozsah 0-65535 pro MicroPython PWM
        r_pwm.duty_u16(int(r * 65535 / 255))
        g_pwm.duty_u16(int(g * 65535 / 255))
        b_pwm.duty_u16(int(b * 65535 / 255))

    try:
        while True:
            # 1. Červená bliká -> Ovladač motoru vypnutý
            print("Stav: Ovladač motoru vypnutý (Červená bliká)")
            for _ in range(4):
                nastav_barvu(255, 0, 0)
                time.sleep(0.5)
                nastav_barvu(0, 0, 0)
                time.sleep(0.5)

            # 2. Zelená -> Nejnižší rychlost
            print("Stav: Nejnižší rychlost (Zelená)")
            nastav_barvu(0, 255, 0)
            time.sleep(2)

            # 3. Žlutá -> Střední rychlost
            print("Stav: Střední rychlost (Žlutá)")
            nastav_barvu(255, 180, 0)
            time.sleep(2)

            # 4. Oranžová -> Nejvyšší rychlost
            print("Stav: Nejvyšší rychlost (Oranžová)")
            nastav_barvu(255, 45, 0)
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nTest ukončen.")
        nastav_barvu(0, 0, 0)
        r_pwm.deinit()
        g_pwm.deinit()
        b_pwm.deinit()


if __name__ == "__main__":
    test_rgb_stavy()
