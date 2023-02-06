from flask_admin import Admin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect

from .admin.views import CustomAdminIndexView
from .api import GBWebApi

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
csrf = CSRFProtect()
admin = Admin(name="Blog Admin Panel", template_mode="bootstrap4", index_view=CustomAdminIndexView())
api = GBWebApi()
