from rpi_ws281x import *
import time
import argparse
import sys
import random


# LED strip configuration:
LED_COUNT = 100      # Number of LED pixels.
LED_PIN = 18      # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 200     # Set to 0 for darkest and 255 for brightest
LED_INVERT = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


# Choose random place and light it up
def rand_color(strip, color):
    random_place = random.randrange(LED_COUNT)
    for j in range(2,-1,-1):
        strip.setPixelColor(random_place-j, color)
        strip.setPixelColor(random_place+j, color)
        strip.show()
        time.sleep(200/1000.0)
    time.sleep(500 / 1000.0)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("color", action="append", help="Input color r,g,b")
    parser.add_argument("color", action="append", help="Input color r,g,b")
    parser.add_argument("color", action="append", help="Input color r,g,b")
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    try:
        if args:
            while True:
                rand_color(strip, Color(int(args.color[0]), int(args.color[1]), int(args.color[2])))
    except KeyboardInterrupt:
        sys.exit(0)
