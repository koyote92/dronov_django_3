# Generated by Django 3.2.16 on 2022-11-19 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_auto_20221120_0102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rubric',
            options={'ordering': ['name'], 'verbose_name': 'Рубрика', 'verbose_name_plural': 'Рубрики'},
        ),
    ]
