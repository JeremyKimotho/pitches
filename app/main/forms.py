from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField, SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
  title=StringField('Pitch Title', validators=[Required()])
  body=TextAreaField('Project Pitch')
  author=TextAreaField('Your name as it\'ll be displayed')
  rtime=IntegerField('Expected read time')
  category=SelectField('Category', choices=[('Business'), ('Technology'), ('Business'), ('Misc.')])
  submit=SubmitField('Submit')

class UpdateProfile(FlaskForm):
  add_info=StringField('Your LinkedIn Profile')
  submit=SubmitField('Submit')
