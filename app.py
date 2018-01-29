from flask import Flask
from flask import render_template 
app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
	return render_template('home.html')
@app.route('/Q&A')
def Q_and_A():
	return render_template('Q&A.html')	
@app.route('/profile')
def profile():
	return render_template('profile.html')	
@app.route('/About')
def About():
	return render_template('About.html')	
@app.route('/singin')
def singin():
	return render_template('singin.html')	

