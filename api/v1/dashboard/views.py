from rest_framework.generics import *
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


class DashboardListAPIVew(APIView):
    permission_classes = [IsAdminUser]

    @staticmethod
    def get(request, *args, **kwargs):
        dashboard_money_serializer = DashboardSerializer()
        # dashboard_graph_serializer = serializers.DashboardGraphSerializer()
        return Response(data={
            'money_stats': dashboard_money_serializer.data,
            # 'graph_stats': dashboard_graph_serializer.data
        })
