# Generated by Django 3.2.16 on 2022-11-20 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0006_alter_bb_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='kind',
            field=models.CharField(choices=[(None, 'Выберите тип публикуемого объявления'), ('b', 'Куплю'), ('s', 'Продам'), ('c', 'Обменяю'), ('r', 'Аренда')], default='s', max_length=1, verbose_name='Тип объявления'),
        ),
    ]
