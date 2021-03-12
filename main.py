from machine import Pin, PWM
from utime import sleep

def play_sound(freq):
    buzzer.freq(freq)
    buzzer.duty_u16(2000)
    sleep(.1)
    buzzer.duty_u16(0)

buzzer = PWM(Pin(16))
buttons = [ [6, 523],   #GP6  - C5
            [7, 587],   #GP7  - D5
            [8, 659],   #GP8  - E5
            [9, 698],   #GP9  - F5
            [10, 783] ] #GP10 - G5

for b in buttons:
    b.append(Pin(b[0], Pin.IN, Pin.PULL_DOWN))

while(True):
    for button in buttons:
        if button[2].value() == 1:
            play_sound(button[1])
