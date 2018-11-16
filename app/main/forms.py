from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import Required

class PitchForm(FlaskForm):
  title=StringField('Pitch Title', validators=[Required()])
  info=TextAreaField('Project Pitch')
  rtime=IntegerField('Expected read time')
  submit=SubmitField('Submit')

class UpdateProfile(FlaskForm):
  add_info=StringField('Your LinkedIn Profile')
  submit=SubmitField('Submit')
