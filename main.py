from flask import Flask, render_template, request
from settlement import calculate_primary_consolidation

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    settlement = None

    if request.method == "POST":

        H = float(request.form["H"])
        Cc = float(request.form["Cc"])
        e0 = float(request.form["e0"])
        sigma0 = float(request.form["sigma0"])
        delta_sigma = float(request.form["delta_sigma"])

        settlement = calculate_primary_consolidation(
            H, Cc, e0, sigma0, delta_sigma
        )

    return render_template("index.html", settlement=settlement)


if __name__ == "__main__":
    app.run(debug=True)