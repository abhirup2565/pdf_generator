from flask import Blueprint,render_template

user_blueprint=Blueprint('user',__name__)

@user_blueprint.route("/user")
def user():
    return render_template('user.html')

@user_blueprint.route("/admin")
def admin():
    return render_template('admin.html')