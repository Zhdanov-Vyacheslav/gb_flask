from datetime import datetime

from combojsonapi.permission import PermissionMixin, PermissionUser, PermissionForPatch
from flask_combo_jsonapi.exceptions import AccessDenied
from flask_login import current_user

from gb_web.models import Article


class ArticlePermission(PermissionMixin):
    PATCH_AVAILABLE_FIELDS = [
        "text",
        "title",
    ]

    def patch_permission(self, *args, user_permission: PermissionUser = None, **kwargs) -> PermissionForPatch:
        self.permission_for_patch.allow_columns = (self.PATCH_AVAILABLE_FIELDS, 10)
        return self.permission_for_patch

    def patch_data(self, *args, data: dict = None, obj: Article = None, user_permission: PermissionUser = None,
                   **kwargs) -> dict:
        permission_for_patch = user_permission.permission_for_patch_permission(model=Article)
        if current_user.is_staff or hasattr(current_user, "author") and current_user.author.id == obj.author_id:
            result = {
                i_key: i_val
                for i_key, i_val in data.items()
                if i_key in permission_for_patch.columns
            }
            result.setdefault("updated_at", datetime.now())
            return result
        else:
            raise AccessDenied("No access")
