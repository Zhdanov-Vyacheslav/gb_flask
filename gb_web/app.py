from os import getenv, path

from combojsonapi.permission import PermissionPlugin
from combojsonapi.event import EventPlugin
from combojsonapi.spec import ApiSpecPlugin
from flask import Flask
from json import load

from commands import COMMANDS
from .admin.views import TagAdminView, UserAdminView
from .api.routes import register_api_routes
from .extensions import db, login_manager, migrate, csrf, admin, api
from .models import User, Tag
from .views import VIEWS

CONFIG_PATH = getenv("CONFIG_PATH", path.join(path.dirname(__file__), "config.json"))
DATABASE_URI = getenv("SQLALCHEMY_DATABASE_URI", None)
SECRET_KEY = getenv("SECRET_KEY", None)


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_json(CONFIG_PATH, load)
    if SECRET_KEY:
        app.config["SECRET_KEY"] = SECRET_KEY
    if DATABASE_URI:
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    register_admin_views()
    register_api_plugins(app)
    register_api_routes(api)
    return app


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)
    admin.init_app(app)
    api.init_app(app)

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
    # Если не добавлять endpoint, происходит конфликт с базовыми blueprint`ами, а name отвечает только за имя в меню в
    # итоге либо менять имя у всех blueprint`ов (для создания стандарта) или использовать endpoint, а вынесено в
    # отельную функцию, для того чтобы исключить цикличный импорт, идея как сделать "красивее"
    # может прийти позже, а пока так...
    admin.add_view(TagAdminView(Tag, db.session, endpoint="a_tag", category="Models"))
    admin.add_view(UserAdminView(User, db.session, endpoint="a_user", category="Models"))


def register_api_plugins(app: Flask):
    tags = {
        "Tag": "Tags API",
        "Article": "Tags API",
        "User": "Tags API",
        "Author": "Tags API",
    }
    api.plugins.append(ApiSpecPlugin(app=app, tags=tags))
    api.plugins.append(EventPlugin())
    api.plugins.append(PermissionPlugin())
    api.init_plugins()
