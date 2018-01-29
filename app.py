from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import render_template 
from flask import request
app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
@app.route('/home')
@app.route('/')
def home():
	return render_template('home.html')
@app.route('/Q&A')
def Q_and_A():
	return render_template('Q&A.html')	
@app.route('/profile', methods=['POST'])
def profile():
	return render_template('profile.html')	
@app.route('/About')
def About():
	return render_template('About.html')	
@app.route('/singin', methods=['POST'])
def singin():
	UserName = request.form['User_name']
	passward = request.form['Passward']
	fullname = request.form['full_name']
	db.session.add(UserInfo)
	db.session.commit()
	return render_template('singin.html')	

class UserInfo(db.Model):
	# class user(Base):
	__tablename__ = 'user'

	id = db.Column(	db.Integer, primary_key=True)
	UserName = Column(db.String(120))
	passward = Column(db.String(120))
	fullname = Column(db.String(120))
	"""docstring for user"""
	def __init__(self, UserName, passward, fullname):
		super(user, self).__init__()
		self.UserName = UserName
		self.passward = passward
		self.fullname = fullname
	def check_pass(self, psw):
		return psw==self.password
	def __repr__(self):
		return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)


class Qustion(db.Model):
	__tablename__ = 'Qustion'

	id = db.Column(db.Integer, primary_key=True)
	question = db.Column(db.String(120))
	subject = db.Column(db.String(120))
	explanation =db.Column(db.String(120))
	userId= db.Column(db.Integer)

	def __init__(self,name,subject,userId):
		self.name=name
		self.subject=subject
		self.userId=userId



	def __repr__(self):
	    return "<User(name='%s', subject='%s', userId='%i')'>" % (
	                       self.name, self.subject, self.userId, self.pic)
db.create_all()

			