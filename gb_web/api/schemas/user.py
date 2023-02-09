from combojsonapi.utils import Relationship
from marshmallow_jsonapi import Schema, fields


class UserSchema(Schema):
    class Meta:
        type_ = "user"
        self_url = "user_detail"
        self_url_kwargs = {"id": "<id>"}
        self_url_many = "user_list"

    id = fields.Int(as_string=True)
    email = fields.Str(allow_none=False, required=True)
    first_name = fields.Str(allow_none=False, required=True)
    last_name = fields.Str(allow_none=False, required=True)
    is_staff = fields.Bool(allow_none=False)

    author = Relationship(
        nested="AuthorSchema",
        attribute="author",
        related_url="author_detail",
        related_url_kwargs={"id": "<id>"},
        schema="AuthorSchema",
        type_="author",
        many=False
    )