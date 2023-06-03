from django.db import models


class Person(models.Model):
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    num_phone = models.CharField('Номер телефона', max_length=12)
    e_mail = models.EmailField('e-mail', max_length=319)

    def __str__(self):
        return self.e_mail

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
