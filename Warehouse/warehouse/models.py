from django.db import models


class Warehouse(models.Model):
    status_ware = (
        ('Новый', ('Новый')),
        ('В ожидании', ('В ожидании')),
        ('На складе', ('На складе')),
        ('Отменен', ('Отменен'))
    )
    number = models.IntegerField(verbose_name='Номер заказа', unique=True)
    title = models.CharField(verbose_name='Название склада', max_length=155)
    store = models.CharField(verbose_name='Магазин', max_length=155)
    status = models.CharField(verbose_name='Статус заказа', choices=status_ware, default=status_ware[0], max_length=20)

    def __str__(self):
        return self.title
