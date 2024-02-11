import sqlite3
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

# def get_db_connection():
#     conn = sqlite3.connect('database.db')
#     conn.row_factory = sqlite3.Row
#     return conn
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    arrive_dt = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    depart_dt = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
   

    def __repr__(self):
        return f'<Trip {self.city}>'

@app.route('/')
def index():
    trips = Trip.query.all()
    return render_template('index.html', trips=trips)