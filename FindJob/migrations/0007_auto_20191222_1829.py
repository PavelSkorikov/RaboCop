# Generated by Django 2.2.7 on 2019-12-22 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FindJob', '0006_auto_20191214_2108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['createAt']},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['createAt']},
        ),
        migrations.RemoveField(
            model_name='question',
            name='schedule_work',
        ),
    ]
