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
        time.sleep(1)
        return redirect(url_for("passed" , sname = name, marks_ = marks)  )
    else:
        time.sleep(1)
        return redirect(url_for("failed" , sname = name, marks_ = marks) )

@app.route("/passed/<sname>/<int:marks_>")
def passed(sname , marks_):
    return f"<h2>hey{sname}, You have Passed with {marks_} !!!!</h2>"

@app.route("/failed/<sname>/<int:marks_>")
def failed(sname , marks_):
    return f"<h2>hey{sname}, You have Failed with {marks_} !!!!</h2>"

if __name__ == "__main__":
    app.run(debug= True)