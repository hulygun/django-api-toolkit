import os
from collections import OrderedDict

import sys
from django.conf import settings
from django.apps import apps
from django.conf.urls import url, include




class DefaultModelSerializer(object):
    def __init__(self, name='REST API', description=''):
        self.name = name
        self.description = description

    def generate_root(self, request):

        from rest_framework.reverse import reverse
        from rest_framework.response import Response
        from rest_framework.decorators import api_view

        index = OrderedDict((
            ('Auth', OrderedDict((
                ('Получение токена по логину/паролю', reverse('get_token', request=request)),
                ('Обновление токена', reverse('refresh_token', request=request)),
                ('Проверка токена', reverse('check_token', request=request)),
            ))),
        ))
        project_apps = settings.PROJECT_APPS
        for app_name in project_apps:
            index[app_name.capitalize()] = {}
            models = dict(apps.all_models[app_name])
            for name, model in models.items():
                model_dict = {}
                from rest_framework.reverse import reverse_lazy
                model_dict[name] = reverse_lazy('api:{}-list'.format(name.lower()), request=request)
                index[app_name.capitalize()].update(model_dict)

        def root_view(request):
            return Response(index)

        root_view.__name__ = self.name
        root_view.__doc__ = self.description

        return api_view(['GET'])(root_view)(request)


    def register_models(self):
        from .models import RestModel
        from rest_framework.routers import SimpleRouter
        router = SimpleRouter()
        for app_name in settings.PROJECT_APPS:
            models = dict(apps.all_models[app_name]).values()
            for model in models:
                if RestModel in model.__bases__:
                    router.register(*model._rest_endpoint())

        return router

    def urls(self):
        ROOT_ROUTE = getattr(settings, 'API_ENDPOINT', 'api')
        return [
            url(r'^{root_route}$'.format(root_route=ROOT_ROUTE), self.generate_root),
            url(r'^{root_route}/'.format(root_route=ROOT_ROUTE), include(self.register_models().urls, namespace='api')),
        ]



class APIManager(object):
    def __init__(self, root, settings):
        self.root = os.path.abspath(os.path.dirname(root))
        self.settings = settings

    def apply(self):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api_tools.settings")
        os.environ.setdefault('API_ROOT', self.root)
        os.environ.setdefault('PROJECT_SETTINGS', self.settings)

    def set_app_dir(self, path):
        sys.path.insert(0, os.path.join(self.root, path))


