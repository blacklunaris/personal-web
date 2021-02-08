from flask_wtf import FlaskForm
from wtforms import StringField,Form,TextField,TextAreaField, validators,SubmitField
from wtforms.validators import InputRequired
def ContactForm(Form):
    name=StringField('name',validators=[InputRequired()])
    email=StringField('email',validators=[InputRequired()])
    subject=StringField('subject',validators=[InputRequired()])
    message=StringField('message',validators=[InputRequired()])
    

  
