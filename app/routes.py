from io import BytesIO
from flask import Flask, render_template, redirect, url_for, request, flash, send_file, abort
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.models import User, Post
from app.forms import LoginForm, RegistrationForm
from werkzeug.urls import url_parse
from datetime import datetime


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
@login_required
def index():
    if request.method =='POST':
        file = request.files['file']

        post = Post(data=file.filename, data2=file.read())
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/new-message', methods=['GET', 'POST'])
@login_required
def new_message():
    # if request.method =='POST':
    #     file = request.files['file']
    #
    #     post = Post(data=file.filename, data2=file.read())
    #     db.session.add(post)
    #     db.session.commit()
    #
    #     return redirect(url_for('yazgylar'))

    return render_template('new-message.html')


@app.route('/<post_id>download', methods=['GET', 'POST'])
@app.route('/index/<post_id>/download', methods=['GET', 'POST'])
@login_required
def yazgy(post_id):
    post = Post.query.filter_by(id=post_id).first()
    return send_file(BytesIO(post.data2), attachment_filename=post.data, as_attachment=True)


@app.route('/yazgylar', methods=['GET', 'POST'])
@login_required
def yazgylar():
    post = Post.query.order_by(Post.id.desc())
    return render_template('yazgylar.html', post=post, user=user)


@app.route('/index/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete(id):
    post = Post.query.get_or_404(id)

    try:
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return "ERROR"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data, surname=form.surname.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(username=form.username.data, surname=form.surname.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()

    return render_template('user.html', user=user)


@app.route('/users')
@login_required
def users():
    u = User.query.all()

    return render_template('users.html', u=u)
