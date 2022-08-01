from django.urls import path
from .views import *


urlpatterns = [
    path('list/', DashboardListAPIVew.as_view(), name='dashboard-list')
]
