# Generated by Django 3.2 on 2021-04-24 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210424_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telegramuser',
            name='current_micro_step',
        ),
    ]
