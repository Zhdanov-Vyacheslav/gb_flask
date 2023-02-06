from combojsonapi.spec import ApiSpecPlugin
from flask_combo_jsonapi import Api


#  Мне показалось такое решение довольно лаконичным, надеюсь на фидбэк по этому поводу в комментарии
class GBWebApi(Api):

    def init_app(self, app=None, blueprint=None, additional_blueprints=None):
        super().init_app(app, blueprint, additional_blueprints)
        self.init_spec_plugin()

    def init_spec_plugin(self):
        tags = {
            "Tag": "Tags API",
            "Article": "Tags API",
            "User": "Tags API",
            "Author": "Tags API",
        }
        spec_plugin = ApiSpecPlugin(app=self.app, tags=tags)
        self.plugins.append(spec_plugin)
        spec_plugin.after_init_plugin(app=None, blueprint=None, additional_blueprints=None)

    @staticmethod
    def check_permissions(view, view_args, view_kwargs, *args, **kwargs):
        pass
