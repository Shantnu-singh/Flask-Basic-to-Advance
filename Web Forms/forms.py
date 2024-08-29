from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField , PasswordField, SubmitField , BooleanField
from wtforms.validators import DataRequired, Length, Email, optional, EqualTo

class Signup(FlaskForm):
    username = StringField(label= "username" , validators=[DataRequired() , Length(5,30)])
    email = StringField(label= "email" , validators= [Email() , DataRequired()])
    gender = SelectField(label= "gender" , choices= ["Male" , "Female" , "others"] , validators=[optional()])
    dob = DateField(label= "dob" , validators= [DataRequired()])
    password = PasswordField(label= "password" , validators=[DataRequired() , Length(5 , 10)])
    comfirm_password = PasswordField(label= "confirm_password" , validators=[DataRequired() , Length(5 , 10), EqualTo("password")])
    sign_up = SubmitField("Sign Up")


class Login(FlaskForm):
    email = StringField(label= "email" , validators= [Email() , DataRequired()])
    password = PasswordField(label= "password" , validators=[DataRequired() , Length(5 , 10)])
    remember_me = BooleanField(label="remember_me")
    log_in = SubmitField("Log In")


