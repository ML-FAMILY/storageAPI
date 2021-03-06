from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils.database import *
from config.secrets import DB_URI


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# JUST TO CREATE TABLES
#create_tables(app)

@app.route('/')
def hello_world():  # put application's code here

    return 'Hello World!'


if __name__ == '__main__':
    app.run()
