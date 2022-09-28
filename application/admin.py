from django.contrib import admin
from .models import *


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'sponsor', 'student', 'money')
