# file directory: services/users/project/__init__.py


import os, sys #new, std lib
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy #new


#intiatie the app
app = Flask(__name__)

#set config
app_settings = os.getenv('APP_SETTINGS') # new
app.config.from_object(app_settings) # new

# instantiate the db
db = SQLAlchemy(app) #new


#model
class User(db.Model): #new
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email



#esnure the proper config was loaded, add a print statement
#print(app.config, file=sys.stderr)
@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
