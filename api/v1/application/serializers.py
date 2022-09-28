from rest_framework import serializers

from api.v1.application.validators import validate_sponsorship_money_on_create
from api.v1.user.serializers import StudentListSerializer, SponsorListSerializer
from application.models import *


class ApplicationSerializer(serializers.ModelSerializer):
    student = StudentListSerializer(read_only=True)
    sponsor = SponsorListSerializer(read_only=True)

    class Meta:
        model = Application
        fields = [
            'id',
            'sponsor',
            'student',
            'status',
            'money',
        ]

    def create(self, validated_data):
        instance = validate_sponsorship_money_on_create(validated_data)
        return instance
