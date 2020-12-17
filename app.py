from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests


app = Flask(__name__)

app.config["ENV"] = 'development'
app.config["SECRET_KEY"]=b'_5#y2L"F4Q8z\n\xec]/'

# change the following .db file name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Anna-Levy.db'
# this line is to prevent SQLAlchemy from throwing a warning
# if you don't get one with out it, feel free to remove
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# this is our model (aka table)
class Bitcoin(db.Model):
    __tablename__ = "bitTable"
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String, nullable=False)
    Price = db.Column(db.String, nullable=False)
    _24h = db.Column(db.String, nullable=False)
    _7d = db.Column(db.String, nullable=False)
    Market_Cap = db.Column(db.String, nullable=False)
    Volume = db.Column(db.String, nullable=False)
    Circulating_Supply = db.Column(db.String, nullable=False)


@app.route('/api', methods=['GET'])
def get_data():
    table = Bitcoin.query.all()
    d = {row.id:[row.Name,row.Price,row._24h,row._7d,row.Market_Cap,row.Volume,row.Circulating_Supply] for row in table}
    return jsonify(d)

@app.route('/', methods=['GET'])
def home():
    table = Bitcoin.query.all()
    d = []
    for row in table: 
        coin_dict = {
            "Name" : row.Name,
            "Price" : row.Price,
            "_24h" : row._24h,
            "_7d" : row._7d,
            "Market_Cap" : row.Market_Cap,
            "Volume" : row.Volume,
            "Circulating_Supply" : row.Circulating_Supply
        }
        d.append(coin_dict)
    return render_template("home.html", data=d)


if __name__ == '__main__':
    app.run(debug=True)
    
    
