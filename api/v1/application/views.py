from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import *
from .serializers import *


class ApplicationListAPIView(ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['sponsor__full_name', 'sponsor__organization', 'student__full_name']


class ApplicationCreateAPIView(ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationDetailAPIView(ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
