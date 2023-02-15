from flask_combo_jsonapi import ResourceList, ResourceDetail

from gb_web.extensions import db
from gb_web.models import User
from ..permissions import UserPermission
from ..schemas import UserSchema


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
        "permission_get": [UserPermission],
        "permission_patch": [UserPermission],
        "permission_delete": [UserPermission],
    }


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
        "permission_post": [UserPermission]
    }
