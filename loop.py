import time
import subprocess

try:
    x = 0
    while x < 100:
        print("runnning" + str(x))
        x = x+1
        time.sleep(0.2)
except KeyboardInterrupt:
    print("end")
except subprocess.TimeoutExpired:
    print("well fuck")
