from django.db import models


class Store(models.Model):
    status_store = (
        ('Новый', ('Новый')),
        ('В ожидании', ('В ожидании')),
        ('На складе', ('На складе')),
        ('Отменен', ('Отменен'))
    )

    pin_cod = models.IntegerField(verbose_name='ПИН', unique=True)
    title = models.CharField(verbose_name='Название магазина', max_length=155)
    status = models.CharField(verbose_name='Статус заказа', choices=status_store, default=status_store[0], max_length=20)
    warehouse = models.CharField(verbose_name='Склад', max_length=155)

    def __str__(self):
        return f"{self.title} -- {self.warehouse}"
