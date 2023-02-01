from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash

from ..forms.auth import AuthForm
from ..models import User

auth = Blueprint("auth", __name__, url_prefix="/auth", static_folder="../static")


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = AuthForm(request.form)
    errors = []
    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for("user.profile", pk=current_user.id))

        return render_template("auth/login.html", form=form, errors=errors)

    if request.method == "POST":
        if form.register.data:
            return redirect(url_for("user.register_user"))

        if form.submit.data:
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email=email).first()

            if not user or not check_password_hash(user.password, password):
                # Не понял почему-то password и email имеют errors типом "tuple", пришлось пере присваивать "list"
                form.password.errors = ["Check your login details"]
                return render_template(
                    "auth/login.html", form=form, errors=errors
                )
            login_user(user)
            return redirect(url_for("user.profile", pk=user.id))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for(".login"))
