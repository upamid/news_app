from django.db import models

class Type(models.Model):
    name = models.CharField(
        verbose_name='Название типа новости',
        blank=False,
        unique=True,
        max_length=200,
        help_text='Укажите название типа новости'
    )
    color = models.CharField(
        verbose_name=(u'Color'),
        max_length=7,
        unique=True,
        help_text=(u'HEX color, as #RRGGBB'),
        )

    class Meta:
        verbose_name = 'Тип',
        verbose_name_plural = 'Типы'
        ordering = ['id']


class News(models.Model):
    type = models.ForeignKey(
        Type,
        related_name='type',
        verbose_name='Тип',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        blank=False,
        help_text='Напишите название новости'
    )
    short_description = models.CharField(
        verbose_name='краткое описание новости',
        max_length=200,
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
