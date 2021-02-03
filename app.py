from flask import Flask, render_template, request, flash, redirect
from subprocess import Popen

UPLOAD_FOLDER = "/~/rpi_ws281x/python/examples/ledweb"
led_Num = {"0": "OFF", "1": "ON", "2": "Program"}
RGB = (0, 0, 0)

app = Flask(__name__)
app.config[UPLOAD_FOLDER] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pass
    cpc = "#%02x%02x%02x" % RGB
    return render_template("index.html", program=led_Num, color=cpc)


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
    prog_file("ON")
    return redirect("/")


def led_program(prog_num):
    for a in led_Num:
        if a == prog_num:
            prog_file(led_Num[a])


def prog_file(prog_name):
    try:
        p = Popen([UPLOAD_FOLDER+"/"+prog_name+".py", RGB[0], RGB[1], RGB[2]])
    except FileNotFoundError:
        flash(FileNotFoundError, "error")
    except OSError:
        flash("OS Error", "error")
    except:
        pass
        # if p:
        #     p.kill()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
