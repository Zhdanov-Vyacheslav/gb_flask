from flask_combo_jsonapi import Api
from flask_combo_jsonapi.exceptions import PluginMethodNotImplementedError


#  Пересмотрел способ, и сделал возможность добавление плагинов после инициализации апи


class GBWebApi(Api):

    def init_plugins(self):
        for i_plugin in self.plugins:
            try:
                i_plugin.after_init_plugin(app=None, blueprint=None, additional_blueprints=None)
            except PluginMethodNotImplementedError:
                pass

    @staticmethod
    def check_permissions(view, view_args, view_kwargs, *args, **kwargs):
        pass
