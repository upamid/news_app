from django.shortcuts import get_object_or_404
from rest_framework import serializers

from articles.models import (Type, News)


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('name', 'color')


class ListNewsSerializer(serializers.ModelSerializer):
    type_name = serializers.ReadOnlyField(source='type.name')
    type_color = serializers.ReadOnlyField(source='type.color')

    class Meta:
        model = News
        fields = (
            'id', 'type_name', 'type_color', 'name', 'short_description')


class NewsSerializer(serializers.ModelSerializer):
    type_name = serializers.ReadOnlyField(source='type.name')
    type_color = serializers.ReadOnlyField(source='type.color')

    class Meta:
        fields = (
            'id','type_name', 'type_color', 'name', 'short_description', 'full_description')
        model = News
