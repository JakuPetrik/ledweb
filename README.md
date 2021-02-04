# ledweb
## Small web app for LEDs

Built on the Raspberri Pi 3b
Using WS2812b 12v LED Strip (30LEDs per strip, using 5 strips)
3.3v to 5v logic level switch
Power supply with 12v 5A

Running a small local Flask web server
Controlling LEDs with rpi_ws281x library

## Webserver:

- display page for color and program choice

- allows to upload more programs and auto detects them

## Installation

1. The package sources are updated:

  `sudo apt-get update`
  
2. We install the required packages (confirm with Y):

 `sudo apt-get install gcc make build-essential python-dev git scons swig`
  
3. Clone the git repo with rpi_ws281x

 `git clone https://github.com/jgarff/rpi_ws281x`
  
4. Enter the downloaded repo

  `cd rpi_ws281x/python`
  
5. Build and install the library

 ` sudo python3 setup.py build 
  sudo python3 setup.py install `
  
6. Try to run the strand test from examples folder (Edit the LED_COUNT)

  `sudo nano examples/strandtest.py`
  `sudo python3 examples/strandtest.py`
  
7. Download the flask library for python

  `pip install Flask`
