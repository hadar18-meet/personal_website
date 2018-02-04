
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import render_template 
from flask import request
app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
@app.route('/home')
def home():
	return render_template('home.html')
@app.route('/Q&A')
def Q_and_A():
	return render_template('Q&A.html')

@app.route('/profile', methods=['POST', 'GET'])
def profile():
	if request.method == 'GET':
		return render_template('profile.html')
	else:	
		question = request.form['question']
		subject = request.form['subject']
		explanation = request.form['explanation']
		Qustion_Object = Qustion(question, subject, explanation)
		db.session.add(Qustion_Object)
		db.session.commit()
		return render_template('Q&A.html')	

@app.route('/about')
def About():
	return render_template('about.html')	
@app.route('/singin', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def singin():
	if request.method == 'GET':
		return render_template('singin.html')
	else:	
		UserName = request.form['User_name']
		passward = request.form['Passward']
		fullname = request.form['full_name']
		UserInfoObject = UserInfo(UserName, passward, fullname)
		db.session.add(UserInfoObject)
		db.session.commit()
		return render_template('home.html')	

class UserInfo(db.Model):
	# class user(Base):
	__tablename__ = 'user'

	id = db.Column(	db.Integer, primary_key=True)
	UserName = db.Column(db.String(120))
	passward = db.Column(db.String(120))
	fullname = db.Column(db.String(120))
	"""docstring for user"""
	def __init__(self, UserName, passward, fullname):
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

	def __init__(self,question,subject,explanation):
		self.question=question
		self.subject=subject
		self.explanation=explanation
	def __repr__(self):
	    return "<User(question='%s', subject='%s', explanation = '%s')'>" % (
	                       self.question, self.subject, self.explanation)
db.create_all()

			