import argparse
import subprocess
import sys
import signal
import time

test = {0: "OFF", 1: "ON", 2: "Program"}
t = None
print(test)
test[3] = "OLA"
print(test)
for a in test:
    if a == "1":
        print("OLA")
    print(a)

if not t:
    print(t)
    print("true?")

t = subprocess.Popen(['python', 'loop.py'])

time.sleep(2)
if t:
    print("Killing")
    t.kill()

# parser = argparse.ArgumentParser()
# parser.add_argument("color", action="append", help="Input color r,g,b")
# parser.add_argument("color", action="append", help="Input color r,g,b")
# parser.add_argument("color", action="append", help="Input color r,g,b")
# args = parser.parse_args()

# print(type(int(args.color[1])))
# print(args.color[0],args.color[1])
sys.exit()

