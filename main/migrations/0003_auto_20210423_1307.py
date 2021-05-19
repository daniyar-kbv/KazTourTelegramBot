# Generated by Django 3.2 on 2021-04-23 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_questionanswer_question'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questionanswer',
            options={'ordering': ['my_order'], 'verbose_name': 'Ответ на вопрос', 'verbose_name_plural': 'Ответы на вопрос'},
        ),
        migrations.AlterModelOptions(
            name='surveyquestion',
            options={'ordering': ['my_order'], 'verbose_name': 'Вопрос опроса', 'verbose_name_plural': 'Вопросы опроса'},
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='current_sub_step',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Текущий подшаг'),
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Сортировка'),
        ),
        migrations.AlterField(
            model_name='surveyquestion',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Сортировка'),
        ),
    ]
