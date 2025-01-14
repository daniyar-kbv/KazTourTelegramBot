# Generated by Django 3.2 on 2021-04-22 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('my_order', models.PositiveIntegerField(default=0, verbose_name='Позиция')),
            ],
            options={
                'verbose_name': 'Ответ на вопрос',
                'verbose_name_plural': 'Ответы на вопрос',
            },
        ),
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('with_own_option', models.BooleanField(verbose_name='Со своим вариантом')),
                ('my_order', models.PositiveIntegerField(default=0, verbose_name='Позиция')),
            ],
            options={
                'verbose_name': 'Вопрос опроса',
                'verbose_name_plural': 'Вопросы опроса',
            },
        ),
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия')),
                ('current_step', models.PositiveSmallIntegerField(choices=[(1, 'Приветсвие'), (2, 'Аудио или текст'), (3, 'Опрос'), (4, 'Способ контакта'), (5, 'Номер телефона')], default=1, verbose_name='Текущий шаг')),
            ],
            options={
                'verbose_name': 'Пользователь Telegram',
                'verbose_name_plural': 'Пользователи Telegram',
            },
        ),
    ]
