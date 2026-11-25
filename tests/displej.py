from machine import Pin, I2C
import framebuf
import time


class OLED_I2C(framebuf.FrameBuffer):
    def __init__(self, width, height, i2c, addr=0x3C):
        self.width = width
        self.height = height
        self.i2c = i2c
        self.addr = addr
        self.buffer = bytearray(self.height // 8 * self.width)
        super().__init__(self.buffer, self.width, self.height, framebuf.MONO_VLSB)
        self.init_display()

    def write_cmd(self, cmd):
        self.i2c.writeto(self.addr, bytearray([0x80, cmd]))

    def init_display(self):
        for cmd in (
            0xAE, 0xD5, 0x80, 0xA8, self.height - 1,
            0xD3, 0x00, 0x40, 0x8D, 0x14, 0x20, 0x02,
            0xA1, 0xC8, 0xDA, 0x12, 0x81, 0xCF,
            0xD9, 0xF1, 0xDB, 0x40, 0xA4, 0xA6, 0xAF
        ):
            self.write_cmd(cmd)
        self.fill(0)
        self.show()

    def show(self):
        for page in range(self.height // 8):
            self.write_cmd(0xB0 + page)
            self.write_cmd(0x00)  # Pokud bude na pravém okraji 1.3" displeje šum, změň 0x00 na 0x02
            self.write_cmd(0x10)
            start = page * self.width
            self.i2c.writeto(self.addr, b'\x40' + self.buffer[start:start + self.width])


def test_oled_stavy():
    print("Test stavů OLED displeje spuštěn (ukončíš přes Ctrl+C)")

    # Inicializace I2C0 na pinech GP4 (SDA) a GP5 (SCK):
    i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
    devices = i2c.scan()
    if not devices:
        raise RuntimeError("Displej nenalezen! Zkontroluj zapojení SDA (GP4) a SCK (GP5).")

    oled = OLED_I2C(128, 64, i2c, addr=devices[0])

    def zobraz_nulovani():
        oled.fill(0)
        oled.rect(4, 14, 120, 36, 1)
        oled.text("NULOVANI...", 22, 28)
        oled.show()

    def aktualizuj_displej(aktualni_poloha, cilova_poloha, rychlost, motor_zapnuty):
        oled.fill(0)
        oled.text("STEPPER INDICATOR", 0, 0)
        oled.hline(0, 10, 128, 1)

        oled.text(f"Aktualni: {aktualni_poloha}", 0, 18)
        oled.text(f"Cilova:   {cilova_poloha}", 0, 30)

        oled.hline(0, 42, 128, 1)
        stav = "ZAP" if motor_zapnuty else "VYP"
        oled.text(f"Motor: {stav}", 0, 47)
        oled.text(f"Rychl: {rychlost}", 0, 56)
        oled.show()

    try:
        while True:
            # 1. Nulování referenční polohy
            print("Stav: Nulování referenční polohy")
            zobraz_nulovani()
            time.sleep(2)

            # 2. Simulace pohybu motoru k cílové poloze
            print("Stav: Pohyb motoru k cílové poloze")
            for poloha in range(0, 121, 30):
                aktualizuj_displej(
                    aktualni_poloha=poloha,
                    cilova_poloha=120,
                    rychlost="Stredni",
                    motor_zapnuty=True
                )
                time.sleep(0.8)

            # 3. Ovladač motoru vypnutý
            print("Stav: Ovladač motoru vypnutý")
            aktualizuj_displej(
                aktualni_poloha=120,
                cilova_poloha=120,
                rychlost="Nejvyssi",
                motor_zapnuty=False
            )
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nTest ukončen.")
        oled.fill(0)
        oled.show()


if __name__ == "__main__":
    test_oled_stavy()
