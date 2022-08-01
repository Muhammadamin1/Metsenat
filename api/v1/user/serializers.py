from django.db.models import Count, Sum
from rest_framework import serializers

from api.v1.application.serializers import ApplicationSerializer
from user.models import *


# ---------------- STUDENT CRUD --------------------------

class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'full_name',
            'phone_number',
            'university',
            'type',
            'contract_amount',
        ]


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'full_name',
            'phone_number',
            'university',
            'type',
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
            'type',
            'contract_amount',
        ]


# ---------------- SPONSOR CRUD --------------------------


class SponsorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = [
            'id',
            'full_name',
            'phone_number',
            'type',
            'payment_amount',
            'organization',
        ]

    def to_representation(self, instance: Sponsor):
        data = super(SponsorListSerializer, self).to_representation(instance)
        data['application'] = ApplicationSerializer(instance.application.all(), context=self.context, many=True).data

        return data


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
