# Generated by Django 2.2.7 on 2019-12-02 16:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FindJob', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='createAt',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
