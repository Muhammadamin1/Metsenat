from django.urls import path
from .views import *

urlpatterns = [
    # Student
    path('students/list/', StudentListAPIView.as_view(), name='student-list'),
    path('students/create/', StudentCreateAPIView.as_view(), name='student-create'),
    path('students/detail/<int:pk>/', StudentDetailUpdateDeleteAPIView.as_view(), name='student-detail'),
    path('students/update/<int:pk>/', StudentDetailUpdateDeleteAPIView.as_view(), name='student-update'),
    path('students/delete/<int:pk>/', StudentDetailUpdateDeleteAPIView.as_view(), name='student-delete'),

    # Sponsor
    path('sponsor/list/', SponsorListAPIView.as_view(), name='sponsor-list'),
    path('sponsor/create/', SponsorCreateAPIView.as_view(), name='sponsor-create'),
    path('sponsor/detail/<int:pk>/', SponsorDetailUpdateDeleteAPIView.as_view(), name='sponsor-detail'),
    path('sponsor/update/<int:pk>/', SponsorDetailUpdateDeleteAPIView.as_view(), name='sponsor-update'),
    path('sponsor/delete/<int:pk>/', SponsorDetailUpdateDeleteAPIView.as_view(), name='sponsor-delete'),
]
