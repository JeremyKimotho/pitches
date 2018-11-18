from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from ..models import User,Pitch
from flask_login import login_required, current_user
from .. import db
import markdown2
from datetime import datetime
from .forms import PitchForm

@main.route('/')
@login_required
def index():
  title = 'Welcome to Jitches'
  return render_template('index.html', title=title)

@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username = uname).first()
  pitches = Pitch
  if user is None:
    abort(404)
  return render_template('profile/profile.html', user=user)

@main.route('/writing-pitch', methods=['GET', 'POST'])
@login_required
def write_pitch():
  form = PitchForm()
  title = 'New Pitch'
  render_template('new_pitch.html', pitch=form, title=title)



# @main.route('/writing-pitch', methods=['GET', 'POST'])
# @login_required
# def write_pitch():
#   pitch_1 = Pitch('Creation of Facebook', 'Tim Johnson', datetime.now(), 'Mark Zuckerberg was a Harvard undergrad when he came up with the idea of a "hot or not" type of website called Facemash. From that site, Zuckerberg learned how technology could be used to connect people and launched a site called thefacebook.com.', 0, 0, 'Technology')
#   pitch_2 = Pitch('Birth of Bloomberg', 'Tim Johnson', datetime.now(), 'Working as a Wall Street trader in the 1970s, Michael Bloomberg quickly realized financial companies were willing to pay big bucks for reliable business information. Bloomberg launched a business that provided important financial information quickly through dedicated computer terminals.', 0, 0, 'Business')
#   pitch_3 = Pitch('The Coming of an Oracle', 'Tim Johnson', datetime.now(), 'Growing up in Chicago\'s south side, Larry Ellison had a rough childhood, dropping out of college twice. But once he moved to California at age 22 in the mid-1960s, he came across an IBM report about a database-programming language called SQL. Inspired by the IBM paper, Ellison took SQL and created the Oracle database, which could run on non-IBM computers. After a few years, Oracle took off, becoming the most popular database ever sold. Now Oracle is worth $192 billion, and Ellison is one of the richest people in the world with a net worth estimated at around $56 billion.', 0, 0, 'Technology')
#   pitch_4 = Pitch('Microsoft', 'Tim Johnson', datetime.now(),'In 1975, Microsoft cofounders Bill Gates and Paul Allen came across an ad for the Altair 8800, one of the earliest forms of microcomputers. They built a programming language called BASIC, which became the foundational code for Altair 8800. Soon Microsoft built an operating system called DOS and licensed it to IBM. A few years later, Microsoft built Windows, which had a more graphical interface than DOS. Since then, Microsoft has become one of the biggest tech companies ever, dominating the PC and software market. It\'s a $742 billion business spanning servers and data centers, as well as video games and mobile phones. Gates is among the richest men in the world with a net worth approaching $91 billion.', 0, 0, 'Technology')
#   pitch_5 = Pitch('Living in a Cloud', 'Tim Johnson', datetime.now(),'Marc Benioff had a revolutionary idea when he founded Salesforce in 1998. He wanted to deliver software over the web, or the "cloud," making it faster and easier to install and update. Salesforce started out as a service for salespeople, but now it has different software for marketing, customer service, and even data analytics. It\'s one of the fastest business-software companies to ever reach $5 billion in sales, and Benioff is worth about $3.8 billion. He\'s also credited with pioneering the cloud market, which is now one of the hottest areas in tech.', 0, 0, 'Business')
#   pitch_6 = Pitch('Mr. Dallas', 'Tim Johnson', datetime.now(),'Mark Cuban was an early internet entrepreneur in the 1990s, and built a company called Broadcast.com based on the idea of providing customized satellite broadcasts over the web. He later sold Broadcast.com to Yahoo for $5.7 billion. Broadcast.com no longer exists, but there\'s no question Cuban — now worth about $3 billion — is one of the most successful self-made tech entrepreneurs of all time. He\'s also the owner of the Dallas Mavericks and an active startup investor. His role on "Shark Tank" has turned him into a popular TV personality as well.', 0, 0, 'Technology')
#   pitches_1=save_pitch(pitch_1)
#   pitches_2=save_pitch(pitch_2)
#   pitches_3=save_pitch(pitch_3)
#   pitches_4=save_pitch(pitch_4)
#   pitches_5=save_pitch(pitch_5)
#   pitches_6=save_pitch(pitch_6)
#   form = PitchForm()
#   if form.validate_on_submit():
#     new_pitch=Pitch(title=form.title.data, author=form.author.data, posted_at=datetime.now(), body=form.body.data, upvotes=0, downvotes=0, category=form.category.data)
#     written_pitch=save_pitch(new_pitch)
#     return render_template('index.html', user_pitches = written_pitch, pitches_1=pitches_1, pitches_2=pitches_2, pitches_3=pitches_3, pitches_4=pitches_4, pitches_5=pitches_5, pitches_6=pitches_6)
#   title='New Jitch'
#   return render_template('new_pitch.html', pitch = form, title = title)
