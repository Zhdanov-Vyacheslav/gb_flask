from flask_combo_jsonapi import ResourceList, ResourceDetail

from gb_web.api.events import ArticleListEvent
from gb_web.extensions import db
from gb_web.models import Article
from gb_web.shemas import ArticleSchema


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article
    }


class ArticleList(ResourceList):
    schema = ArticleSchema
    events = ArticleListEvent
    data_layer = {
        "session": db.session,
        "model": Article
    }
