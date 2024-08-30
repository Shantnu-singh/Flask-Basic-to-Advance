from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ipl_sd.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Team(db.Model):
    __tablename__ = "teams"
    id = db.Column(db.Integer , nullable = False , primary_key = True )
    team = db.Column(db.String(50) , nullable = False )
    state = db.Column(db.String(50) , nullable = False )
    members = db.relationship("Player" , backref = "team")
    
    def __repr__(self):
        return f'Team ({self.state} ,{self.state})'
    
class Player(db.Model):
    __tablename__ = "players"
    id = db.Column(db.Integer , nullable = False , primary_key = True )
    name = db.Column(db.String(50) , nullable = False , unique = True)
    nationlity = db.Column(db.String(50) , nullable = False )
    team_id = db.Column(db.Integer , db.ForeignKey("teams.id"))
    
    
    
    def __repr__(self):
        return f'Team ({self.name} , {self.id} ,{self.nationlity})'
    
@app.route("/")
def home():
    return render_template("Home.html")

if __name__ == "__main__":
    app.run(debug=True)
