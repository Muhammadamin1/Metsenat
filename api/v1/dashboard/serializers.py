from django.db.models import Sum
from rest_framework import serializers

from application.models import Application
from user.models import *


class DashboardSerializer:
    def __init__(self):
        self.total_sponsored_money = Application.objects.aggregate(Sum('money'))['money__sum']
        self.total_contract_money = Student.objects.aggregate(Sum('contract_amount'))['contract_amount__sum']
        self.total_needed_money = self.total_contract_money - self.total_sponsored_money

    @property
    def data(self):
        return self.__dict__
