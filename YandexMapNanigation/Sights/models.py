from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth import get_user_model



User = get_user_model()


class Category(models.Model):
    title = models.CharField('Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Sight(models.Model):
    title = models.CharField('Название', max_length=128)
    description = models.TextField('Описание')
    city = models.CharField('Город', max_length=64)
    street = models.CharField('Улица', max_length=64)
    house_number = models.PositiveSmallIntegerField('Дом')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sights', verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='Другое',
                                 related_name='sights', verbose_name='Категория')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'


class Rating(models.Model):
    sight = models.ForeignKey(Sight, on_delete=models.CASCADE, related_name='ratings', verbose_name='Достопримечательность')
    rating = models.PositiveSmallIntegerField('Оценка', validators=[MaxValueValidator(10)])
    comment = models.TextField('Комментарий')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings', verbose_name='Автор')

    def __str__(self):
        return self.rating

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
