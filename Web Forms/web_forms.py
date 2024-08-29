from flask import Flask, render_template, redirect , url_for, flash
from forms import Signup , Login

app = Flask(__name__ , template_folder = 'templetes')
app.config["SECRET_KEY"] = "398874KJDFDIJCBSCKJD"

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html" , title = "Home")


@app.route("/login" , methods = ["GET" , "POST"])
def login():
    log_in = Login()
    if log_in.validate_on_submit():
        if log_in.email.data == "ab@gmail.com" and log_in.password.data == "123456":
            return redirect(url_for("home"))    
    return render_template("login.html" , title = "Login" , form = log_in)

@app.route("/signup" , methods = ["GET" , "POST"])
def signup():
    log_in = Signup()
    if log_in.validate_on_submit():
        flash(f"Sucessful Login {log_in.username.data} !!!")
        return redirect(url_for("home"))
    return render_template("signup.html" , title = "Signup" , form = log_in)

if __name__ == "__main__":
    app.run(debug= True)

# CSRF( cross side request forgery ) : attraker --> "trick" by attackers at end-user, can be prevent by csrf tokens
# WTform : liberary in python, used for data and to generate validation and csrf tokens
