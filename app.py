from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

module = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        errors = ""
        if request.method == "POST":
            modulname = None
            try:
                modulname = float(request.form["modulname"])
            except:
                errors += "<p>{!r} ist kein Modulname. Bitte geben Sie einen Modulnamen ein.</p>\n".format(request.form["modulname"])
        return render_template("index.html", module = module)

    module.append(request.form["modulname"])
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug = True)

