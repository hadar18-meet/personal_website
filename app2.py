from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from flask import render_template 
from flask import request
app = Flask(__name__)

'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
db = SQLAlchemy(app)
'''

@app.route('/home')
def home():
	return render_template('home.html')