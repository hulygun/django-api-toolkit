from django.db import models


class RestModel(models.Model):

    class Rest:
        """
        rest meta class
        """
        queryset = '__all__'
        fields = '__all__'

    class Meta:
        abstract = True

    @classmethod
    def _rest_queryset(cls):
        params = getattr(cls.Rest, 'queryset', None)
        if params and params != '__all__':
            return params(cls.objects)

        else:
            return cls.objects.all()

    @classmethod
    def _rest_serializer(cls):
        from rest_framework_json_api import serializers
        meta = type('Meta', (), {'model': cls, 'fields': cls.Rest.fields})
        serializer = type('Serializer', (serializers.ModelSerializer,), {'Meta': meta})

        return serializer

    @classmethod
    def _rest_endpoint(cls):
        from rest_framework import viewsets
        viewset = type('Viewset', (viewsets.ModelViewSet,),
                       {'queryset': cls._rest_queryset(), 'serializer_class': cls._rest_serializer(),
                        '__doc__': cls.__doc__, })
        name = getattr(cls.Rest, 'name', getattr(cls.Meta, 'verbose_name_plural', cls.__name__))
        route = getattr(cls.Rest, 'route', name).lower()
        viewset.__name__ = name
        return (r'{}'.format(route), viewset, route)