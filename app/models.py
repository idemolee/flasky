from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_,and_
db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    account = db.Column(db.String(16),unique=True)
    passwd = db.Column(db.String(18))
    def __repr__(self):
        return '<User %r>' % self.account
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16))
    num = db.Column(db.Integer)
    detail = db.Column(db.String(100))
def exist(u,p):
    act = User.query.filter_by(account=u).first()
    if act and (act.passwd == p):
        return True
    else:
        return False
def add(u,p):
    user = User()
    if not user.query.filter_by(account=u).first():
        a = User(account=u,passwd=p)
        db.session.add(a)
        db.session.commit()
        return True
    else:
        return False
def lookup(u):
    if u=='':
        ls = db.session.query(Role).all()
    else:
        ls = Role.query.filter(or_(Role.name==u,str(Role.num)==str(u))).all()
    return ls
