from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>Welcome to the home page<h2>"

@app.route("/about")
def about():
    return "<h2>Welcome to the about page<h2>"


if __name__ == "__main__":
    app.run(debug= True)