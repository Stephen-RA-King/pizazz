"""
slow = 1
medium = 0.1
fast = 0.01
"""


# Core Library modules
import time
from random import randint

# First party modules
from pizazz import HC595

CHIPS = 2
hc = HC595(ics=CHIPS)


def led_set(array: list, blink: int, speed: float) -> None:
    if len(array) != CHIPS:
        raise Exception("Length of array  != ICs")

    array = array[0] + array[1]
    total = 0

    for i in range(CHIPS * 8):  # range 0 - 15
        total += array[i] * (2**i)

    for _ in range(blink):
        hc.set_output(total, 65535)
        time.sleep(speed)
        hc.clear()
        time.sleep(speed)

    hc.clear()


def random_led() -> list:
    empty0 = [0, 0, 0, 0, 0, 0, 0, 0]
    empty1 = [0, 0, 0, 0, 0, 0, 0, 0]
    led = randint(0, 15)
    if led < 8:
        empty0[led] = 1
        led_array = [empty0, empty1]
    else:
        empty1[led - 8] = 1
        led_array = [empty0, empty1]
    return led_array


all_green = [[1, 0, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0]]
all_red = [[0, 1, 0, 1, 0, 1, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1]]

pat1 = [[1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 1]]
pat2 = [[0, 0, 0, 0, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0]]

pat4 = [[1, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0]]
pat5 = [[0, 1, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1, 0, 0]]
pat6 = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0]]
pat7 = [[0, 0, 0, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 1]]
pat8 = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 1, 0]]
pat9 = [[0, 1, 0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1, 0, 0]]

pat10 = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
pat11 = [[0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0]]
pat12 = [[0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0]]
pat13 = [[0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0]]
pat14 = [[0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0]]
pat15 = [[0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0]]
pat16 = [[0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0]]
pat17 = [[0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0]]

pat18 = [[1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
pat19 = [[0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
pat20 = [[0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
pat21 = [[0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0]]
pat22 = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1]]
pat23 = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0]]
pat24 = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0]]
pat25 = [[0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0]]

led_set(all_green, 10, 0.1)
led_set(all_red, 10, 0.1)

for _ in range(20):
    led_set(all_green, 1, 0.1)
    led_set(all_red, 1, 0.1)

for _ in range(20):
    led_set(pat1, 1, 0.1)
    led_set(pat2, 1, 0.1)

for _ in range(20):
    led_set(pat4, 1, 0.1)
    led_set(pat5, 1, 0.1)
    led_set(pat6, 1, 0.1)
    led_set(pat7, 1, 0.1)
    led_set(pat8, 1, 0.1)
    led_set(pat9, 1, 0.1)

for _ in range(10):
    led_set(pat10, 1, 0.01)
    led_set(pat11, 1, 0.01)
    led_set(pat12, 1, 0.01)
    led_set(pat13, 1, 0.01)
    led_set(pat14, 1, 0.01)
    led_set(pat15, 1, 0.01)
    led_set(pat16, 1, 0.01)
    led_set(pat17, 1, 0.01)
    led_set(pat16, 1, 0.01)
    led_set(pat15, 1, 0.01)
    led_set(pat14, 1, 0.01)
    led_set(pat13, 1, 0.01)
    led_set(pat12, 1, 0.01)
    led_set(pat11, 1, 0.01)

for _ in range(20):
    led_set(pat18, 1, 0.01)
    led_set(pat19, 1, 0.01)
    led_set(pat20, 1, 0.01)
    led_set(pat21, 1, 0.01)
    led_set(pat22, 1, 0.01)
    led_set(pat23, 1, 0.01)
    led_set(pat24, 1, 0.01)
    led_set(pat25, 1, 0.01)

for _ in range(80):
    led_set(pat18, 1, 0.001)
    led_set(pat19, 1, 0.001)
    led_set(pat20, 1, 0.001)
    led_set(pat21, 1, 0.001)
    led_set(pat22, 1, 0.001)
    led_set(pat23, 1, 0.001)
    led_set(pat24, 1, 0.001)
    led_set(pat25, 1, 0.001)

for _ in range(200):
    leds = random_led()
    led_set(leds, 1, 0.001)
