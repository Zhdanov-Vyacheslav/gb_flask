from gb_web.api import GBWebApi
from gb_web.api.resources.article import ArticleDetail, ArticleList
from gb_web.api.resources.author import AuthorList, AuthorDetail
from gb_web.api.resources.tag import TagList, TagDetail
from gb_web.api.resources.user import UserList, UserDetail


# Убрал создание роутов сюда, что-бы избавить от перегрузки кодом app.py
# Я думаю в принципе все роуты нужно вынести куда-то отдельно и там их скопом регистрировать, но пока так...
def register_api_routes(api: GBWebApi):
    api.route(TagList, "tag_list", "/api/tags", tag="Tag")
    api.route(TagDetail, "tag_detail", "/api/tags/<int:id>", tag="Tag")
    api.route(UserDetail, "user_detail", "/api/users/<int:id>", tag="User")
    api.route(UserList, "user_list", "/api/users", tag="User")
    api.route(ArticleDetail, "article_detail", "/api/articles/<int:id>", tag="Article")
    api.route(ArticleList, "article_list", "/api/articles", tag="Article")
    api.route(AuthorDetail, "author_detail", "/api/authors/<int:id>", tag="Author")
    api.route(AuthorList, "author_list", "/api/authors", tag="Author")
