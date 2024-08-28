from flask import Flask, url_for , redirect
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>Heyyy, Welocome to home page</h2>"

# 3XX : redirection 

@app.route("/<name>/<int:marks>")
def welcome_steve(name , marks):
    if marks >  30:
        time.sleep(3)
        return redirect(url_for("passed") )
    else:
        time.sleep(3)
        return redirect(url_for("failed") )

@app.route("/passed")
def passed():
    return "<h2>Passed !!!!</h2>"

@app.route("/failed")
def failed():
    return "<h2>Failed !!!!</h2>"

if __name__ == "__main__":
    app.run(debug= True)