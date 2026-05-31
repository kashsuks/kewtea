"""
code.py — KMK firmware entry point for the kewtea keyboard.

Targets a Pro Micro NRF52840 (nice!nano-compatible) running CircuitPython.
Defines the 3×10 key matrix, single-layer QWERTY keymap, and an SSD1306
OLED that displays elapsed uptime. No build step required — edit this file
directly on the CIRCUITPY USB drive and the changes take effect on save.

Required libraries (copy to CIRCUITPY/lib/ from the Adafruit bundle):
  - adafruit_displayio_ssd1306
  - adafruit_display_text
"""

import time
import busio
import displayio
import terminalio
import microcontroller
from adafruit_display_text import label
import adafruit_displayio_ssd1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation


# ── Display ───────────────────────────────────────────────────────────────────

displayio.release_displays()

_i2c = busio.I2C(
    scl=microcontroller.pin.P0_20,  # header pin 6
    sda=microcontroller.pin.P0_17,  # header pin 5
)
_bus = displayio.I2CDisplay(_i2c, device_address=0x3C)
_display = adafruit_displayio_ssd1306.SSD1306(_bus, width=128, height=32)

_root = displayio.Group()
_display.root_group = _root

_time_label = label.Label(
    terminalio.FONT,
    text='00:00:00',
    color=0xFFFFFF,
    x=32,
    y=15,
)
_root.append(_time_label)

_boot_time = time.monotonic()


# ── Uptime extension ──────────────────────────────────────────────────────────

class UptimeDisplay:
    """KMK extension that refreshes the OLED with elapsed uptime once per second.

    Uses the board's monotonic clock rather than wall-clock time because no
    hardware RTC is present. Replace _render with an RTC read when one is added.

    Attributes:
        _label: The displayio Label updated each tick.
        _last_tick: Monotonic timestamp of the last display update.
    """

    def __init__(self, time_label: label.Label) -> None:
        """
        Args:
            time_label: Label widget whose text is overwritten each second.
        """
        self._label = time_label
        self._last_tick = 0.0

    def _render(self) -> None:
        """Formats elapsed seconds as HH:MM:SS and pushes it to the label."""
        elapsed = int(time.monotonic() - _boot_time)
        h = elapsed // 3600
        m = (elapsed % 3600) // 60
        s = elapsed % 60
        self._label.text = f'{h:02d}:{m:02d}:{s:02d}'

    def during_bootup(self, keyboard: KMKKeyboard) -> None:
        pass

    def before_matrix_scan(self, keyboard: KMKKeyboard) -> None:
        """Called each scan cycle — throttled to one display update per second."""
        now = time.monotonic()
        if now - self._last_tick >= 1.0:
            self._last_tick = now
            self._render()

    def after_matrix_scan(self, keyboard: KMKKeyboard) -> None:
        pass

    def before_hid_send(self, keyboard: KMKKeyboard) -> None:
        pass

    def after_hid_send(self, keyboard: KMKKeyboard) -> None:
        pass

    def on_powersave_enable(self, keyboard: KMKKeyboard) -> None:
        pass

    def on_powersave_disable(self, keyboard: KMKKeyboard) -> None:
        pass


# ── Keyboard ──────────────────────────────────────────────────────────────────

keyboard = KMKKeyboard()

keyboard.row_pins = (
    microcontroller.pin.P0_04,  # ROW0 — Q..P
    microcontroller.pin.P0_00,  # ROW1 — A..SEMI
    microcontroller.pin.P0_01,  # ROW2 — Z..DOT
)

keyboard.col_pins = (
    microcontroller.pin.P0_05,  # COL0
    microcontroller.pin.P0_06,  # COL1
    microcontroller.pin.P0_07,  # COL2
    microcontroller.pin.P0_08,  # COL3
    microcontroller.pin.P0_09,  # COL4
    microcontroller.pin.P0_10,  # COL5
    microcontroller.pin.P0_13,  # COL6
    microcontroller.pin.P0_14,  # COL7
    microcontroller.pin.P0_15,  # COL8
    microcontroller.pin.P0_16,  # COL9
)

keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.extensions.append(UptimeDisplay(_time_label))

keyboard.keymap = [
    [
        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,
        KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,

        KC.A,    KC.S,    KC.D,    KC.F,    KC.G,
        KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN,

        KC.Z,    KC.X,    KC.C,    KC.V,    KC.SPC,
        KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,
    ]
]

if __name__ == '__main__':
    keyboard.go()
