from django.contrib.auth.models import AbstractUser
from django.db import models

from metsenat.models import BaseModel


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=13)

    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return self.username


class Student(BaseModel):
    class Type(models.TextChoices):
        BACHELOR = 'Bakalavr'
        MASTER = 'Magister'

    full_name = models.CharField(max_length=200)
    university = models.CharField(max_length=300)
    type = models.CharField(max_length=10, choices=Type.choices, default=Type.BACHELOR)
    phone_number = models.CharField(max_length=13, blank=True, null=True, unique=True)
    contract_amount = models.FloatField(default=0)

    def __str__(self):
        return self.full_name


class Sponsor(BaseModel):
    class Type(models.TextChoices):
        PHYSICAL_PERSON = 'Jismoniy shaxs'
        LEGAL_PERSON = 'Yuridik shaxs'

    student = models.ManyToManyField(Student, blank=True)
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13, blank=True, null=True, unique=True)
    type = models.CharField(max_length=15, choices=Type.choices, default=Type.PHYSICAL_PERSON)
    payment_amount = models.FloatField(default=0)
    organization = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.full_name

    @property
    def total_price(self):
        queryset = self.student.all().aggregate(total_price=models.Sum('contract_amount'))
        return queryset['total_price']
