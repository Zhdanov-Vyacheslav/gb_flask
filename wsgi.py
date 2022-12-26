from werkzeug.security import generate_password_hash

from gb_web.app import create_app, db

app = create_app()


@app.cli.command("init-db", help="create all db")
def init_db():
    db.create_all()


@app.cli.command("create-users", help="create users")
def create_users():
    from gb_web.models import User
    db.session.add(
        User(email="name@email.com", password=generate_password_hash("test"))
    )
    db.session.commit()
