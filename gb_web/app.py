from flask import Flask

from gb_web.article.views import article
from gb_web.user.views import user
from gb_web.index.views import index
from gb_web.report.views import report

VIEWS = [
    index,
    user,
    article,
    report
]


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)
