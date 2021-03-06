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
    random_place = random.randrange(strip.numPixels())
    i = 2
    for j in range(2,-1,-1):
        for k in range(3,1,-1):
            strip.setPixelColor(random_place - j,
                                Color(int(color[0] / k),
                                      int(color[1] / k),
                                      int(color[2] / k)))
            strip.setPixelColor(random_place+j,
                                Color(int(color[0] / k),
                                      int(color[1] / k),
                                      int(color[2] / k)))
            strip.show()
            time.sleep(100 / 1000.0)
    for j in range(2, -1, -1):
        for k in range(3,0,-1):
            if k == 0:
                for j in range(2, -1, -1):
                    strip.setPixelColor(random_place - j, Color(0, 0, 0))
                    strip.setPixelColor(random_place + j, Color(0, 0, 0))
                continue
            strip.setPixelColor(random_place - j,
                                Color(int(color[0] - color[0] / k),
                                      int(color[1] - color[1] / k),
                                      int(color[2] - color[2] / k)))
            strip.setPixelColor(random_place + j,
                                Color(int(color[0] - color[0] / k),
                                      int(color[1] - color[1] / k),
                                      int(color[2] - color[2] / k)))
            strip.show()
            time.sleep(100 / 1000.0)
    time.sleep(200/1000.0)
    # random_place = random.randrange(strip.numPixels())
    # for j in range(2,-1,-1):
    #     strip.setPixelColor(random_place-j, color)
    #     strip.setPixelColor(random_place+j, color)
    #     strip.show()
    #     time.sleep(100/1000.0)
    # random_place = random.randrange(strip.numPixels())
    # for k in range(2,-1,-1):
    #     strip.setPixelColor(random_place-j, color)
    #     strip.setPixelColor(random_place+j, color)
    #     strip.show()
    #     time.sleep(100/1000.0)
    time.sleep(200 / 1000.0)


# def color_off(strip):
#     for i in range(strip.numPixels()):
#         strip.setPixelColor(i, 0)
#         strip.show()


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
            integer_map = map(int, args.color)
            color = list(integer_map)
            while True:
                rand_color(strip, color)
                rand_color(strip, color)
                rand_color(strip, color)
                # color_off(strip)
    except KeyboardInterrupt:
        sys.exit(0)
