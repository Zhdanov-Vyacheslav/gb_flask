from flask_combo_jsonapi import ResourceList, ResourceDetail

from gb_web.extensions import db
from gb_web.models import Article
from ..events import ArticleListEvent
from ..permissions import ArticlePermission
from ..schemas import ArticleSchema


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
        "permission_patch": [ArticlePermission]
    }


class ArticleList(ResourceList):
    schema = ArticleSchema
    events = ArticleListEvent
    data_layer = {
        "session": db.session,
        "model": Article
    }
