# Generated by Django 4.1.6 on 2023-02-17 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_at',
            field=models.DateField(default=' ', verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='article',
            name='end_at',
            field=models.DateField(default=' ', verbose_name='Дата дедлайна'),
        ),
    ]
