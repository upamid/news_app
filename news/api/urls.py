from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (NewsViewSet, TypeViewSet)

v1_router = DefaultRouter()
v1_router.register('news', NewsViewSet, basename='news')
v1_router.register('type', TypeViewSet, basename='type')

urlpatterns = [
    path('', include(v1_router.urls)),
]