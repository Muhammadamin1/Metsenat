from django.db import models
from user.models import *
from metsenat.models import BaseModel


class Application(BaseModel):
    STATUS_CHOICES = (
        ('new', 'Yangi'),
        ('processing', 'Moderatsiyada'),
        ('approved', 'Tasdiqlangan'),
        ('canceled', 'Bekor qilingan')
    )
    status = models.CharField(max_length=64, choices=STATUS_CHOICES, default='new')
    sponsor = models.ForeignKey(Sponsor, related_name='sponsorships', on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, related_name='sponsorships', on_delete=models.CASCADE, null=True)
    money = models.BigIntegerField(null=True)

    def __str__(self):
        return f'{self.sponsor.full_name} -- {self.student.full_name} : {self.money} so\'m'
