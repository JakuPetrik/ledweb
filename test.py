import argparse

test = {0: "OFF", 1: "ON", 2: "Program"}
print(test)
test[3] = "OLA"
print(test)
for a in test:
    if a == "1":
        print("OLA")
    print(a)

parser = argparse.ArgumentParser()
parser.add_argument("color", action="append", help="Input color r,g,b")
parser.add_argument("color", action="append", help="Input color r,g,b")
parser.add_argument("color", action="append", help="Input color r,g,b")
args = parser.parse_args()

# print(type(int(args.color[1])))
print(args.color[0],args.color[1])