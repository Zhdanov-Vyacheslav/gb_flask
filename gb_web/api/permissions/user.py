from combojsonapi.permission import PermissionMixin, PermissionUser, PermissionForGet, PermissionForPatch
from flask_combo_jsonapi.exceptions import AccessDenied

from gb_web.models import User


class UserPermission(PermissionMixin):
    PATCH_AVAILABLE_FIELDS = [
        "first_name",
        "last_name",
    ]
    GET_AVAILABLE_FIELDS = [
        "id",
        "email",
        "first_name",
        "last_name",
        "is_staff"
    ]

    def patch_permission(self, *args, user_permission: PermissionUser = None, **kwargs) -> PermissionForPatch:
        self.permission_for_patch.allow_columns = (self.PATCH_AVAILABLE_FIELDS, 10)
        return self.permission_for_patch

    def get(self, *args, many=True, user_permission: PermissionUser = None, **kwargs) -> PermissionForGet:
        self.permission_for_get.allow_columns = (self.GET_AVAILABLE_FIELDS, 10)
        return self.permission_for_get

    def patch_data(self, *args, data: dict = None, obj: User = None, user_permission: PermissionUser = None,
                   **kwargs) -> dict:
        permission_for_patch = user_permission.permission_for_patch_permission(model=User)
        return {
            i_key: i_val
            for i_key, i_val in data.items()
            if i_key in permission_for_patch.columns
        }

    # Не нашел способ убрать из API ненужные методы, по этому закрыл через эвент
    def delete(self, *args, obj=None, user_permission: PermissionUser = None, **kwargs) -> bool:
        raise AccessDenied("Method is close")

    def post_data(self, *args, data=None, user_permission: PermissionUser = None, **kwargs) -> dict:
        raise AccessDenied("Method is close")
