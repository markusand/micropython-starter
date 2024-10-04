""" MicroPython start project """

from utime import sleep
from machine import Pin


def main():
    """Main function"""
    led = Pin(2, Pin.OUT)

    while True:
        led.value(not led.value())
        sleep(0.5)


if __name__ == "__main__":
    main()
