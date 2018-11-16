from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):
  title=StringField('Pitch Title', validators=[Required()])
  info=TextAreaField('Project Pitch')
  submit=SubmitField('Submit')

class UpdateProfile(FlaskForm):
  add_info=StringField('Your LinkedIn Profile')
  submit=SubmitField('Submit')
