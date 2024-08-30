from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///product_db.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

Customer_product = db.Table(
    "cutomer_product",
    db.Column("customer_id" , db.Integer , db.ForeignKey("customers.id")),
    db.Column("product_key" , db.Integer , db.ForeignKey("products.id"))
)
class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer , nullable = False , primary_key = True )
    name = db.Column(db.String(50) , nullable = False )
    email = db.Column(db.String(50) , nullable = False , unique = True)
    items = db.relationship("products" , backref = "owners", secondary = Customer_product)
    
    def __repr__(self):
        return f'Team ({self.name} ,{self.email} , {self.id})'
    
class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer , nullable = False , primary_key = True )
    product = db.Column(db.String(50) , nullable = False)
    price = db.Column(db.Integer , nullable = False )
    
    
    
    def __repr__(self):
        return f'Team ({self.product} , {self.id} ,{self.price})'
    
@app.route("/")
def home():
    return render_template("Home.html")

if __name__ == "__main__":
    app.run(debug=True)
