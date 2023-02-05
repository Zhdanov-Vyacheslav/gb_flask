from .user.views import user
from .author.views import author
from .index.views import index
from .report.views import report
from .article.views import article
from .auth.view import auth

VIEWS = [
    user,
    author,
    index,
    report,
    article,
    auth,
]
