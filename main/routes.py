from flask import redirect, render_template, request, url_for, flash, session
from extensions import db
from . import main_bp
from model.auth import auth

@main_bp.route('/')
def index ():
    if 'user' not in session:
        return redirect(url_for("main.login"))
    else:
        return redirect(url_for("main.home"))

@main_bp.route('/home')
def home():
    return render_template("home.html")

@main_bp.route('/signup')
def signup():
    return render_template("signup.html")

@main_bp.route('/signup_click', methods=['POST'])
def signup_click():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    user_name = request.form.get("user_name")
    email = request.form.get("email")
    password = request.form.get("password")
    
    user = auth.query.filter_by(user_name = user_name ).first()

    if user :
        flash("Change username , This username is not avalaible")
        return redirect(url_for("main.signup"))

    session['user'] = user_name
    user_detail = auth(
        first_name = first_name,
        last_name = last_name,
        user_name = user_name,
        email = email,
        password = password
    )    

    db.session.add(user_detail)
    db.session.commit()
    return redirect(url_for("main.home"))

@main_bp.route("/login")
def login():
    return render_template("login.html")

@main_bp.route("/login_click", methods=['POST'])
def login_click():
    user_name = request.form.get("user_name")
    password = request.form.get("password")

    user = auth.query.filter_by(user_name = user_name , password = password).first()

    if not user:
        flash("Invalid username or password")
        return redirect(url_for("main.login"))

    session['user'] = user_name
    return redirect(url_for("main.home"))

@main_bp.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for("main.login"))