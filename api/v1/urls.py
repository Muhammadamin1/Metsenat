from django.urls import path, include

urlpatterns = [
    path('user/', include('api.v1.user.urls')),
    # path('application/', include('api.v1.application.urls')),
    path('dashboard/', include('api.v1.dashboard.urls')),
]
