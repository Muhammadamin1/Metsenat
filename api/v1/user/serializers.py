from django.db.models import Count, Sum
from django.db.models.functions import Coalesce
from rest_framework import serializers

from user.models import *


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = [
            'id',
            'name',
        ]


# ---------------- STUDENT CRUD --------------------------

class StudentListSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)
    gained_money = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            'id',
            'full_name',
            'phone_number',
            'university',
            'degree',
            'contract_amount',
            'gained_money',
        ]

    @staticmethod
    def get_gained_money(student):
        gained_money = student.sponsorships.aggregate(money_sum=Coalesce(Sum('money'), 0))['money_sum']
        return gained_money


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'full_name',
            'phone_number',
            'university',
            'degree',
            'contract_amount',
        ]


class StudentRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'full_name',
            'phone_number',
            'university',
            'degree',
            'contract_amount',
        ]


# ---------------- SPONSOR CRUD --------------------------


class SponsorListSerializer(serializers.ModelSerializer):
    spent_money = serializers.SerializerMethodField()

    class Meta:
        model = Sponsor
        fields = [
            'id',
            'full_name',
            'phone_number',
            'type',
            'payment_amount',
            'organization',
            'spent_money',
        ]

    @staticmethod
    def get_spent_money(sponsor):
        spent_money = sponsor.sponsorships.aggregate(money_sum=Coalesce(Sum('money'), 0))['money_sum']
        return spent_money


class SponsorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = [
            'full_name',
            'phone_number',
            'type',
            'payment_amount',
            'organization',
        ]


class SponsorRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = [
            'id',
            'full_name',
            'phone_number',
            'status',
            'type',
            'payment_amount',
            'organization',
        ]
