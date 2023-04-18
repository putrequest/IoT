import time
import os
import usb_hid
import supervisor
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

ascii = bytes(range(32, 127)).decode()

timerBreakShort = 1.0
timerBreakLong = 1.0

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

def attack():
    keyboard.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(timerBreakShort)
    text = "echo Hello"
    text = text.replace('"', '')
    layout.write(f'cmd /D /K "{text}"\n')

if __name__ == "__main__":
    attack()