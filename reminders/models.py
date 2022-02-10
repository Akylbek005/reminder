from django.db import models


class Reminders(models.Model):
    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    birthday = models.DateField()

    def __str__(self):
        return f'{self.name} - {self.birthday}'

    class Meta:
        verbose_name = 'Напоминание'
        verbose_name_plural = 'Список напоминаний'
