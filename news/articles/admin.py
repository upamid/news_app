from django.contrib import admin

from .models import Type, News

admin.site.register(Type)


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'short_description',
        )
    search_fields = (
        'name',
        'type')
    list_filter = (
        'name',
        'type')


admin.site.register(News, NewsAdmin)

