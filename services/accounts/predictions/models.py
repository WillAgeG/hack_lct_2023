from django.db import models

STATUS_CHOICES = [
    ('PENDING', 'Pending'),
    ('READY', 'Ready'),
]


class Predict(models.Model):
    status = models.CharField(
        verbose_name='Статус',
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )
    predict = models.JSONField(
        verbose_name='Прогноз',
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        'users.User',
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(
        verbose_name='Время создания',
        auto_now_add=True,
        db_index=True
    )
    modified = models.DateTimeField(
        verbose_name='Время обновление',
        auto_now=True
    )
