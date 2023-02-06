from flask_combo_jsonapi import ResourceList, ResourceDetail

from gb_web.extensions import db
from gb_web.models import User
from gb_web.shemas import UserSchema


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User
    }


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User
    }
