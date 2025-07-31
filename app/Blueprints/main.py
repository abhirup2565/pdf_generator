from flask import Blueprint,render_template,flash,request,session
from app.Models import User
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import create_access_token,create_refresh_token

main_blueprint=Blueprint('main',__name__)

@main_blueprint.route("/")
def home():
    return render_template('index.html')
@main_blueprint.route("/",methods=['POST'])
def signup():
    if request.method=="POST":
        username=request.form.get('username')
        email=request.form.get('email')
        password=generate_password_hash(request.form.get('password')) 
        role=request.form.get('role')
        user=User(username=username,email=email,password=password,role=role)
        user.save()
        flash('You were successfully signed up')
        return render_template('index.html')

@main_blueprint.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password,password):
            access_token=create_access_token(identity=user.email)
            refresh_token=create_refresh_token(identity=user.email)
            print("Access Token:",access_token,"Refresh Token:",refresh_token)
            session['access_token']=access_token
            session['refresh_toke']=refresh_token
    return render_template('login.html')