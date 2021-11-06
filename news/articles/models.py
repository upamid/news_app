from django.contrib.auth.models import User
from django.db import models
from news import settings

# from users.models import CustomUser


class Type(models.Model):
    name = models.CharField(
        verbose_name='Название типа новости',
        blank=False,
        max_length=200,
        help_text='Укажите название типа новости'
    )
    color = models.CharField(
        verbose_name=(u'Color'),
        max_length=7,
        help_text=(u'HEX color, as #RRGGBB'),
        )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Slug'
        )

    class Meta:
        verbose_name = 'Тип',
        verbose_name_plural = 'Типы'
        ordering = ['id']


class News(models.Model):
    type = models.ManyToManyField(
        Type,
        blank=True,
        through='TypeNews',
        related_name='types',
        verbose_name='Типы',
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        blank=False,
        help_text='Напишите название новости'
    )
    short_description = models.TextField(
        verbose_name='краткое описание новости',
        blank=False,
        help_text='Добавьте сюда краткое описание новости'
    )
    full_description = models.TextField(
        verbose_name='полное описание новости',
        blank=False,
        help_text='Добавьте сюда полное описание новости'
    )

    class Meta:
        verbose_name = 'Новость',
        verbose_name_plural = 'Новости'
        ordering = ['id']


class TypeNews(models.Model):
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name='Тип новости'
    )
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name='Новость'
    )

    class Meta:
        verbose_name = 'Тип в новости',
        verbose_name_plural = 'Типы в новостях'
        ordering = ['id']