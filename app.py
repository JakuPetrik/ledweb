from flask import Flask, render_template, request, redirect
from subprocess import Popen
import os

UPLOAD_FOLDER = os.path.join(os.getcwd() + "/program")
program = {"0": "OFF", "1": "ON", "2": "Program"}
RGB = (0, 0, 0)
p = None

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    global program
    program = get_programs()
    if request.method == "POST":
        pass
    cpc = "#%02x%02x%02x" % RGB
    return render_template("index.html", program=program, color=cpc)


@app.route("/program", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        prog_num = request.form.get("button_num")
        led_program(prog_num)
    return redirect("/")


@app.route("/color", methods=["POST"])
def color():
    args = request.form.get("colorpicker").lstrip("#")
    global RGB
    RGB = tuple(int(args[i:i+2], 16) for i in (0, 2, 4))
    prog_file("ON.py")
    return redirect("/")


@app.route("/upload", methods = ["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["fileToUpload"]
        file = os.path.join(UPLOAD_FOLDER, f.filename)
        try:
            f.save(file)
        except:
            print("File error")
    return "file uploaded successfully"


def led_program(prog_num):
    for a in program:
        if a == prog_num:
            prog_file(program[a])


def prog_file(prog_name):
    # file = "{}/{}.py {} {} {}".format(UPLOAD_FOLDER, prog_name, RGB[0], RGB[1], RGB[2])
    file = "{}/{}".format(UPLOAD_FOLDER, prog_name)
    global p
    try:
        if p:
            print("Killing")
            p.kill()
        p = Popen(["python3", file, str(RGB[0]), str(RGB[2]), str(RGB[1])])
        print(p)
    except FileNotFoundError:
        print(FileNotFoundError, "error")
    except OSError:
        print("OS Error", "error")
    except ValueError:
        print("some file error")
    except RuntimeError:
        print("what now?")


def get_programs():
    arr = os.listdir(UPLOAD_FOLDER)
    arr.insert(0, arr.pop(arr.index("ON.py")))
    for a, b in enumerate(arr):
        program[str(a)] = b
    return program


if __name__ == "__main__":
        app.run(host="0.0.0.0")
