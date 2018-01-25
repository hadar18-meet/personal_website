'''
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String
'''
class UserInfo(db.Model):
	class user(Base):
		__tablename__ = 'user'

		id = Column(Integer, primary_key=True)
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
	name = db.Column(db.String(120))
	subject= db.Column(db.String(120))
	userId= db.Column(db.Integer)

	def __init__(self,name,subject,userId):
		self.name=name
		self.subject=subject
		self.userId=userId



	def __repr__(self):
	    return "<User(name='%s', subject='%s', userId='%i')'>" % (
	                       self.name, self.subject, self.userId, self.pic)


			