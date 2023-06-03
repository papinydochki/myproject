# Generated by Django 4.2 on 2023-05-28 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('num_phone', models.CharField(max_length=12, verbose_name='Услуга')),
                ('e_mail', models.CharField(max_length=319, verbose_name='e-mail')),
            ],
        ),
    ]