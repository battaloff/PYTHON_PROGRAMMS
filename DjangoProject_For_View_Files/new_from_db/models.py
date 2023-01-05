from django.db import models


class Files(models.Model):
    EQUIPMENT_CHOICES = [
        ('BLUE', 'Синяя'),
        ('GREEN', 'Зелёная'),
        ('AURORA', 'Аврора B0'),
        ('THERMAL', 'Термальная'),
        ('FIRST', 'Первая'),
    ]

    OPERATOR_CHOICES = [
        ('YURA', 'Юрий'),
        ('ZIYO', 'Зийо'),
        ('AZIZ', 'Азиз'),
        ('DIMA', 'Дмитрий'),
        ('ANDREY', 'Андрей'),
        ('OLEG', 'Олег'),
    ]

    STAGE_CHOICES = [
        ('UNREADY', 'На машине'),
        ('READY', 'Готов'),

    ]

    PUNCH_CHOICES = [
        ('PUNCH', 'Панч'),
        ('PUNCH_BEND', 'Панч+Загиб'),
    ]

    company_name = models.CharField("Фирма", max_length=40, blank=True)
    qty = models.CharField("Шт.", max_length=40, blank=True)
    file_name = models.CharField("Название", max_length=65, blank=True, null=True)
    plate_size = models.CharField("Размер", max_length=40, blank=True)
    equipment = models.CharField("Машина", max_length=40, choices=EQUIPMENT_CHOICES, blank=True)
    add_date_time = models.DateTimeField(verbose_name="Дата", null=False, blank=False, auto_now_add=True)
    punch = models.CharField("Панч", max_length=255, choices=PUNCH_CHOICES, blank=True)
    stage = models.CharField(verbose_name="Состояние", max_length=255, choices=STAGE_CHOICES, default='На машине')
    operator = models.CharField("Вывел", max_length=255, choices=OPERATOR_CHOICES, blank=True)
    ready_datetime = models.DateTimeField(null=True, blank=True, auto_now=True, verbose_name='Время готовности')

    def __str__(self):
        return self.file_name

    class Meta:
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
        unique_together = ['company_name', 'qty', 'file_name', 'plate_size', 'add_date_time']

