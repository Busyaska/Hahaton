from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model


User = get_user_model()


class Sight(models.Model):
    title = models.CharField('Название')
    description = models.TextField('Описание')
    latitude = models.FloatField('Широта', validators=[MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.FloatField('Долгота', validators=[MinValueValidator(-180), MaxValueValidator(180)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author', verbose_name='автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'
