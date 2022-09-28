from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import *
from .serializers import *
from .filters import *


# ---------------- STUDENT --------------------------

class StudentListAPIView(ListAPIView):
    serializer_class = StudentListSerializer
    filterset_backend = StudentFilter
    filter_backends = [SearchFilter, DjangoFilterBackend]

    def get_queryset(self):
        queryset = Student.objects.all()
        query = self.request.query_params.get('search')
        if query is not None:
            queryset = Student.objects.filter(Q(full_name__icontains=query) |
                                              Q(phone_number__icontains=query) |
                                              Q(university__icontains=query))
        return queryset


class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer


class StudentDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentRetrieveUpdateDestroySerializer


# ---------------- SPONSOR --------------------------

class SponsorListAPIView(ListAPIView):
    serializer_class = SponsorListSerializer
    filterset_backend = SponsorFilter
    filter_backends = [SearchFilter, DjangoFilterBackend]

    def get_queryset(self):
        queryset = Sponsor.objects.all()
        query = self.request.query_params.get('search')
        if query is not None:
            queryset = Sponsor.objects.filter(Q(full_name__icontains=query) |
                                              Q(phone_number__icontains=query) |
                                              Q(organization__icontains=query))
        return queryset


class SponsorCreateAPIView(CreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorCreateSerializer


class SponsorDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorRetrieveUpdateDestroySerializer
