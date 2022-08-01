from django.db import models
from user.models import *
from metsenat.models import BaseModel


class Application(BaseModel):
    class Status(models.TextChoices):
        NEW = 'Yangi'
        MODERATE = 'Modiratsiyada'
        APPROVED = 'Tasdiqlangan'
        CANCELED = 'Bekor qilingan'
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.NEW)
    sponsor = models.ManyToManyField(Sponsor, related_name='application')
    student = models.ManyToManyField(Student, related_name='application')
    spent_money = models.FloatField(default=0)

