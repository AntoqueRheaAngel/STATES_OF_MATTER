from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html") 

@app.route("/gas")
def gas():
    return render_template("gas.html") 

@app.route("/liquid")
def liquid():
    return render_template("liquid.html")     

@app.route("/solid")
def solid():
    return render_template("solid.html") 

@app.route("/plasma")
def plasma():
    return render_template("plasma.html")     

if __name__ == "__main__":
    app.run(debug = True)
