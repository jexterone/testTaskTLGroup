from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255,verbose_name='Название')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

class Employee(models.Model):
    full_name = models.CharField(max_length=255,verbose_name='ФИО')
    position = models.CharField(max_length=255,verbose_name='Должность')
    hire_date = models.DateField(verbose_name='Дата найма')
    salary = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='ЗП')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees',verbose_name='Отдел')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
