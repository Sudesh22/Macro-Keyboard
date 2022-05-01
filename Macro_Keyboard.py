import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

btn1_pin= board.GP3
btn2_pin= board.GP10
btn3_pin= board.GP16
btn4_pin= board.GP17

keyboard = Keyboard(usb_hid.devices)

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

while True:
    if btn1.value:
        keyboard.press(Keycode.ALT, Keycode.TAB)          #Action: ALT-TAB Use: Switching Windows
        time.sleep(0.1)
        keyboard.release(Keycode.ALT, Keycode.TAB)
    if btn2.value:
        keyboard.press(Keycode.WINDOWS, Keycode.TWO)      #Action: WINDOWS-2 Use: Opening VSCode
        time.sleep(0.1)
        keyboard.release(Keycode.WINDOWS, Keycode.TWO)
    if btn3.value:
        keyboard.press(Keycode.CONTROL, Keycode.F2)       #Action: CTRL-F2  Use: Changing names of all variables
        time.sleep(0.1)                                   #                      having similar name
        keyboard.release(Keycode.CONTROL, Keycode.F2)
    if btn4.value:
        keyboard.press(Keycode.CONTROL, Keycode.D)        #Action: CTRL-D  Use: Toggle Mic in Google Meet
        time.sleep(0.1)                                                
        keyboard.release(Keycode.CONTROL, Keycode.D)
    time.sleep(0.1)
