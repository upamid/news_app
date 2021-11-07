from django.conf import settings
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (status, viewsets)
from rest_framework.decorators import action
from rest_framework.response import Response

from articles.models import (Type, News)

from .filterset import NewsFilter
from .serializers import (TypeSerializer, ListNewsSerializer,
                          NewsSerializer)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = ListNewsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = NewsFilter

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = NewsSerializer(instance)
        return Response(serializer.data)
        
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        type = Type.objects.get(name__contains=data['type'])
        serializer = NewsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(type=type)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk, *args, **kwargs):
        kwargs['partial'] = True
        instance = self.get_object()
        instance.id = pk
        instance.save()
        data = request.data.copy()
        type = Type.objects.get(name__contains=data['type'])
        serializer = NewsSerializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(type=type)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class TypeViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
