from os import getenv, path

from flask import Flask
from json import load

from commands import COMMANDS
from .admin.views import admin_views_init
from .extensions import db, login_manager, migrate, csrf, admin
from .models import User
from .views import VIEWS

base_dir = path.dirname(__file__)

config_dir = base_dir[:base_dir.rfind("/")] if base_dir.rfind("/") != -1 else base_dir[:base_dir.rfind("\\")]
CONFIG_PATH = getenv("CONFIG_PATH", path.join(config_dir, "dev_config2.json"))
DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI", None)


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_file(CONFIG_PATH, load)
    if DATABASE_URI:
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    # register_admin_views()
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)
    admin.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)


def register_commands(app: Flask):
    for command in COMMANDS:
        app.cli.add_command(command)


def register_admin_views():
    admin_views_init()
