from flask import Flask, render_template , jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>Heyyy, Welocome to home page</h2>"

# @app.route("/welcom/steve")
# def welcome_steve():
#     return "<h2>Heyyy ,steve Welocome to home page</h2>"

# @app.route("/welcom/peter")
# def welcome_peter():
#     return "<h2>Heyyy ,peter Welocome to home page</h2>"
# name = "shatnu"

@app.route("/welcome/<name>")
def welcome_steve(name):
    return f"<h2>Heyyy {name.title()},  Welocome to home page</h2>"

if __name__ == "__main__":
    app.run(debug= True)