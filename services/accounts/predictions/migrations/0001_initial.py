# Generated by Django 3.2.23 on 2023-12-13 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Predict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('READY', 'Ready')], default='PENDING', max_length=20, verbose_name='Статус')),
                ('predict', models.JSONField(blank=True, null=True, verbose_name='Прогноз')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Время создания')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Время обновление')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]
