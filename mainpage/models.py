from django.db import models

# Create your models here.
class Departament(models.Model):
    departamentName = models.CharField('Департамент', max_length = 50)

    def __str__(self):
        return self.departamentName

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'

class Employee(models.Model):
    firstName = models.CharField('Имя', max_length = 30)
    middleName = models.CharField('Отчество', max_length = 30)
    lastName = models.CharField('Фамилия', max_length = 30)
    departament = models.ForeignKey(Departament, on_delete = models.CASCADE)

    def __str__(self):
        return self.lastName

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'