# Generated by Django 3.2 on 2021-08-19 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210722_0253'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotMode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Режим аудио сообщений')], verbose_name='Тип')),
                ('is_enabled', models.BooleanField(default=False, verbose_name='Включен')),
            ],
            options={
                'verbose_name': 'Режим бота',
                'verbose_name_plural': 'Режимы бота',
            },
        ),
        migrations.AlterField(
            model_name='bottext',
            name='id',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Приветствие (1-е сообщение, должно содержать "{}" для вствки имени)'), (2, 'Приветствие (2-е сообщение)'), (3, 'Приветствие (3-е сообщение)'), (4, 'Приветствие (4-е сообщение)'), (5, 'Вариант ответа 1 (после приветствия)'), (6, 'Вариант ответа 2 (после приветствия)'), (7, 'Текст с предложением отправить аудио'), (8, 'Текст о подтверждении текста с аудио (должно содержать "{}" для вствки текста)'), (9, 'Вариант ответа 1 (подтверждение)'), (10, 'Вариант ответа 2 (опровержение)'), (11, 'Текст переотправки аудио'), (12, 'Текст о способе контакта (1-е сообщение, должно содержать "{}" для вствки имени)'), (13, 'Текст о способе контакта (2-е сообщение)'), (14, 'Текст об отправке номера телефона (шаблон)'), (15, 'Текст о некорректном номере телефона'), (16, 'Заключающее сообщение'), (17, 'Текст ответа на некорректное сообщение'), (18, 'Текст сообщения (ввести свой вариант)')], primary_key=True, serialize=False),
        ),
    ]
