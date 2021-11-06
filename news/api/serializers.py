from django.shortcuts import get_object_or_404
from djoser.serializers import UserSerializer
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers, status
from rest_framework.response import Response

from articles.models import (Type, News, TypeNews)
from users.models import CustomUser


class UserSerializer(UserSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = (
            'first_name',
            'last_name',
            'username',
            'id',
            'email',)
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            }


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name', 'color', 'slug')


class TypeNewsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='type.id')
    name = serializers.ReadOnlyField(source='type.name')
    color = serializers.ReadOnlyField(source='type.color')
    slug = serializers.ReadOnlyField(source='type.slug')

    class Meta:
        model = TypeNews
        fields = ('id', 'name', 'color', 'slug')


class ListNewsSerializer(serializers.ModelSerializer):
    types = TypeNewsSerializer(
        source='typenews_set',
        many=True,
        required=False
        )

    class Meta:
        model = News
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    tags = TypeNewsSerializer(
        source='typenews_set',
        many=True,
        required=False
        )

    class Meta:
        fields = (
            'id', 'type', 'name', 'short_description', 'full_description')
        model = News

    def create(self, validated_data):
        types = validated_data.pop('typenews_set')
        news = News.objects.create(**validated_data)
        for type in types:
            current_type = get_object_or_404(Type, id=type.get('type').get('id'))
            TypeNews.objects.create(
                tag=current_type, news=news)
        return news

    def update(self, instance, validated_data):
        types = validated_data.pop('tagrecipe_set')
        News.objects.filter(id=instance.id).update(**validated_data)
        news = get_object_or_404(News, id=instance.id)
        news.type.remove()
        news_types = TypeNews.objects.filter(
            type_id=instance.id
            )
        if not news_types:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        news_types.delete()
        for type in types:
            current_type = get_object_or_404(Type, id=type.get('type').get('id'))
            TypeNews.objects.create(
                tag=current_type, news=news)
        return news

