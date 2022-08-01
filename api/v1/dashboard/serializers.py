from rest_framework import serializers
from user.models import *


class DashboardListSerializer(serializers.ModelSerializer):
    total_payment_amount = serializers.SerializerMethodField(read_only=True)
    total_contract_amount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Sponsor
        fields = [
            'total_payment_amount',
            'payment_amount',
            'total_contract_amount'
        ]

    def get_total_payment_amount(self, obj: Sponsor):
        queryset = Sponsor.objects.all()
        cash = 0
        for payment in queryset:
            cash += payment.payment_amount
        return cash

    def get_total_contract_amount(self, obj: Sponsor):
        return obj.total_price
