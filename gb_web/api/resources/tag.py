from flask_combo_jsonapi import ResourceList, ResourceDetail

from gb_web.extensions import db
from gb_web.models import Tag
from gb_web.shemas import TagSchema


class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": Tag
    }


class TagList(ResourceList):
    schema = TagSchema
    data_layer = {
        "session": db.session,
        "model": Tag
    }
