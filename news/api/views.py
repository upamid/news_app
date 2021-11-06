from django.conf import settings
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (permissions, status, views,
                            viewsets)
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from articles.models import (Type, News, TypeNews)

from users.models import CustomUser

from .filterset import NewsFilter, TypeFilter
from .pagination import CustomPagination
from .permissions import (IsAdmin, IsAuthorOrAdmin,
                          IsSuperuser)
from .serializers import (TypeSerializer, ListNewsSerializer,
                          NewsSerializer,UserSerializer)

BASE_USERNAME = 'User'


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    lookup_field = 'username'
    permission_classes = (permissions.IsAuthenticated, IsSuperuser | IsAdmin,)

    @action(
        detail=False,
        permission_classes=(permissions.IsAuthenticated,),
        methods=['get', 'patch'],
        url_path='me')
    def get_or_update_self(self, request):
        if request.method != 'GET':
            serializer = self.get_serializer(
                instance=request.user,
                data=request.data,
                partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        else:
            serializer = self.get_serializer(
                request.user,
                many=False)
            return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = CustomUser.objects.all()
        author = get_object_or_404(queryset, pk=pk)
        user = self.request.user
        serializer = UserSerializer(author, user, context={'user_id': request.user.id})
        return Response(serializer.data)


class NewsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrAdmin,)
    queryset = News.objects.all()
    serializer_class = ListNewsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = NewsFilter
    pagination_class = CustomPagination

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user_id": self.request.user.id})
        return context

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['tags'] = [{'id': idx} for idx in data['tags']]
        serializer = NewsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk, *args, **kwargs):
        kwargs['partial'] = True
        instance = self.get_object()
        instance.id = pk
        instance.save()
        data = request.data.copy()
        data['tags'] = [{'id': idx} for idx in data['tags']]
        serializer = NewsSerializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=self.request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrAdmin,)
    pagination_class = None
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
