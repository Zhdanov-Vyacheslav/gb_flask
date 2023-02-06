import click
from werkzeug.security import generate_password_hash


@click.command("init-db", help="create all db")
def init_db():
    from wsgi import app
    from gb_web.extensions import db

    with app.app_context():
        db.create_all()


@click.command("create-users", help="create users")
def create_users():
    from gb_web.models import User
    from gb_web.extensions import db

    from wsgi import app

    with app.app_context():
        users = {
            "name@email.com": {
                "password": generate_password_hash("test"),
                "first_name": "Test",
                "last_name": "Flask"
            },
            "bad@mail.ho": {
                "password": generate_password_hash("test"),
                "first_name": "Oleg",
                "last_name": "Petrov"
            }

        }
        for user, date in users.items():
            db.session.add(User(email=user, **date))
        db.session.commit()
        click.echo("Created users: {}".format(", ".join(users.keys())))


@click.command("create-tags", help="create tags")
def create_tags():
    from gb_web.models.tag import Tag
    from gb_web.extensions import db

    from wsgi import app

    with app.app_context():
        tags = ("flask", "python", "db", "sqlalchemy")
        for tag in tags:
            db.session.add(Tag(name=tag))
        db.session.commit()
        click.echo("Created tags: {}".format(", ".join(tags)))


COMMANDS = [init_db, create_users, create_tags]
