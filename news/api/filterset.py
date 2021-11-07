import django_filters
from django_filters import rest_framework

from articles.models import News, Type


class TypeFilter(rest_framework.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr='startswith')

    class Meta:
        model = Type
        fields = ('name', )


class NewsFilter(rest_framework.FilterSet):
    type = django_filters.ModelMultipleChoiceFilter(
        field_name='type__slug',
        to_field_name='slug',
        queryset=Type.objects.all()
        )

    class Meta:
        model = News
        fields = ['type']
