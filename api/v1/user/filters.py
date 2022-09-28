from django_filters import rest_framework as filters
from user.models import *


class StudentFilter(filters.FilterSet):
    university = filters.CharFilter(field_name='university', lookup_expr='icontains')

    class Meta:
        model = Student
        fields = [
            'university',
            'degree'
        ]


class SponsorFilter(filters.FilterSet):
    class Meta:
        model = Sponsor
        fields = [
            'payment_amount',
            'created_at'
        ]
