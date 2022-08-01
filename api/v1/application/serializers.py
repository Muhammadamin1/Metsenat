from rest_framework import serializers
from application.models import *


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            'id',
            'sponsor',
            'student',
            'status',
            'spent_money',
        ]
