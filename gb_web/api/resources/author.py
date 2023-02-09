from flask_combo_jsonapi import ResourceList, ResourceDetail

from gb_web.extensions import db
from gb_web.models import Author
from ..schemas import AuthorSchema


class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author
    }


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        "session": db.session,
        "model": Author
    }
