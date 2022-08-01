from rest_framework.generics import *
from .serializers import *


class DashboardListAPIVew(ListAPIView):
    queryset = Sponsor.objects.all().distinct()
    serializer_class = DashboardListSerializer
