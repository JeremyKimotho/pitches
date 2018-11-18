from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from ..models import User,Pitch, Comments
from flask_login import login_required, current_user
from .. import db
import markdown2
from datetime import datetime
from .forms import PitchForm, CommentForm

@main.route('/')
@login_required
def index():
  pitches=Pitch.query.all()
  title = 'Welcome to Jitches'
  return render_template('index.html', title=title, pitches=pitches)

@main.route('/profile/<uname>')
def profile(uname):
  user = User.query.filter_by(username = uname).first()
  # pitches = Pitch.query.filter_by(user=user_id)
  if user is None:
    abort(404)
  return render_template('profile/profile.html', user=user)

@main.route('/writing-pitch', methods=['GET', 'POST'])
@login_required
def write_pitch():
  form = PitchForm()
  if form.validate_on_submit():
    pitch = Pitch(title=form.title.data, body=form.body.data,upvotes=0, downvotes=0, category=form.category.data)

    db.session.add(pitch)
    db.session.commit()
    return redirect(url_for('main.index'))

  title = 'New Pitch'
  return render_template('new_pitch.html', pitch=form, title=title)

@main.route('/upvotes', methods=['GET', 'POST'])
def upvoting(id):
  pitch = Pitch.query.get(id)
  return pitch.add_upvotes()

@main.route('/comment', methods=['GET', 'POST'])
@login_required
def write_comment():
  form = CommentForm()
  if form.validate_on_submit():
    comment = Comments(comment=form.comment.data)

    db.session.add(comment)
    db.session.commit()

    return redirect(url_for('main.index'))

  return render_template('comment.html', comment=form)

