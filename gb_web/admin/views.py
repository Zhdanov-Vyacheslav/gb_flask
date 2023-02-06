from flask import redirect, url_for
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class CustomAdminIndexView(AdminIndexView):

    @expose()
    def index(self):
        if not (current_user.is_authenticated and current_user.is_staff):
            return redirect(url_for("auth.login"))
        return self.render(self._template)


class TagAdminView(ModelView):
    column_searchable_list = ("name",)
    create_modal = True
    edit_modal = True
    can_export = True
    export_types = ("csv",)


class UserAdminView(ModelView):
    column_exclude_list = ("password",)
    form_excluded_columns = ("password", "email")  # Убираем столбцы из формы редактирования
    column_details_exclude_list = ("password",)
    column_export_exclude_list = ("password",)  # На случай если включат экспорт или найдут эксплойт
    column_editable_list = ("first_name", "last_name", "is_staff")
    can_delete = False
    can_create = False
