from django.urls import path
from .views import *

urlpatterns = [
    path('list/', ApplicationListAPIView.as_view(), name='application-list'),
    path('create/', ApplicationCreateAPIView.as_view(), name='application-create'),
    path('detail/<int:pk>/', ApplicationDetailAPIView.as_view(), name='application-detail'),
]
