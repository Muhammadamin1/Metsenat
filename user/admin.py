from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm
from .models import *
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# class UserAdmin(BaseUserAdmin):
#     form = UserChangeForm
#     fieldsets = (
#         (None, {'fields': ('email', 'password',)}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name')}),
#         (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
#                                        'groups', 'user_permissions')}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#         (_('user_info'), {'fields': ('native_name', 'phone_no')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('first_name', 'last_name', 'username', 'phone', 'email', 'password1', 'password2'),
#         }),
#     )
#     list_display = ['first_name', 'last_name', "phone"]
#     search_fields = ('username', 'first_name', 'last_name')
#     ordering = ('username',)
#
#
# admin.site.register(User, UserAdmin)


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone_number', 'type', 'payment_amount']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number', 'university', 'degree', 'contract_amount')


admin.site.register(University)
