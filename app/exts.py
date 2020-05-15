from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired
class NameForm(FlaskForm):
    name = StringField('Account',validators=[DataRequired()],render_kw={'style':'width:60%'})
    passwd = PasswordField('Password',validators=[DataRequired()],render_kw={'style':'width:60%'})
    submit = SubmitField('Submit')
class SearchForm(FlaskForm):
    note = StringField('Search for',validators=[DataRequired()],render_kw={'style':'width:60%'})
    submit = SubmitField('search')
