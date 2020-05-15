from flask import Flask,render_template,session,redirect,url_for,request,g
from flask_bootstrap import Bootstrap
from functools import wraps
from exts import *
from models import exist,add,lookup,db
import config
app = Flask(__name__)
bootstap = Bootstrap(app)
app.config.from_object(config)
db.init_app(app)
#xian zhi deng lu
def log_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_name'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('index'))
    return wrapper

@app.route('/',methods=['GET','POST'])
def index():
    form = NameForm()
    message = 'Welcome!'
    if form.validate_on_submit():
        roles = exist(form.name.data,form.passwd.data)
        if roles:
            session['user_name'] = form.name.data
            return redirect(url_for('user',name=form.name.data))
        else:
            message = 'Imput error!'
    return render_template('index.html',form=form,name=message)

@app.route('/user/<name>',methods=['GET','POST'])
@log_required
def user(name):
    search = SearchForm()
    if request.method=="POST":
    # if search.validate_on_submit():
        l = search.note.data
    else:
        l = ''
    ls = lookup(l)
    return render_template('user.html',name=name,search=search,ls=ls)

@app.route('/role/<name>',methods=['GET','POST'])
@log_required
def role(name):
    ls = lookup(name)
    return render_template('role.html',role=ls)

@app.route('/register',methods=['GET','POST'])
def register():
    form = NameForm()
    note = 'Register now!'
    if form.validate_on_submit():
        if add(form.name.data,form.passwd.data):
            return redirect(url_for('index'))
        else:
            note = 'Register error!'
    return render_template('register.html',note=note,form=form)

@app.route('/logout',methods=['GET','POST'])
def logout():
    session.pop('user_name')
    # del session('user_name')
    return redirect(url_for('index'))

@app.context_processor
def my_context_processor():
    user_name = session.get('user_name')
    if user_name:
        return {'user_name':user_name}
    return {}

if __name__ == '__main__':
    app.run()
