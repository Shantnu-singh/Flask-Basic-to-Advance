from flask import Flask, render_template , jsonify

app = Flask(__name__ , template_folder= "templetes1")

employees_data = {
    1: {
        "name": "Shantnu",
        "age": 30,
        "position": "Data Scientist"
    },
    2: {
        "name": "Aisha",
        "age": 28,
        "position": "Software Engineer"
    },
    3: {
        "name": "Ravi",
        "age": 35,
        "position": "manager"
    },
    4: {
        "name": "Maya",
        "age": 25,
        "position": "UI/UX Designer"
    },
    5: {
        "name": "Ethan",
        "age": 40,
        "position": "manager"
    },
    6: {
        "name": "Olivia",
        "age": 32,
        "position": "manager"
    },
    7: {
        "name": "Noah",
        "age": 27,
        "position": "Data Analyst"
    },
    8: {
        "name": "Ava",
        "age": 38,
        "position": "Sales Manager"
    },
    9: {
        "name": "Liam",
        "age": 33,
        "position": "manager"
    },
    10: {
        "name": "Isabella",
        "age": 26,
        "position": "Finance Analyst"
    }
}
@app.route("/")
def home():
    return render_template("home.html" , title = "Home")

# Jinja

@app.route("/about")
def about():
    return render_template("about.html" , title = "About")

@app.route("/calculate/<int:num>")
def calculate(num):
    return render_template("evaluate.html" , title = "Calculate", number = num)

@app.route("/employees")
def info_em():
    return render_template("employees.html", title = "Employees", info_em = employees_data)

@app.route("/managers")
def managers():
    return render_template("managers.html" , title = "Mangers", info_em = employees_data)


if __name__ == "__main__":
    app.run(debug= True)