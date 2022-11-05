from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import *
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['firstName', 'lastName', 'email', 'phoneNumber', 'is_admin']
    search_fields = ('lastName', 'email')

    fieldsets = (
        ('Information', {'fields': ('firstName', 'lastName', 'email', 'phoneNumber', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'last_login')}),
    )
    add_fieldsets = (
        ('Information', {'fields': ('firstName', 'lastName', 'email', 'phoneNumber', 'password1', 'password2')}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'last_login')}),
    )

    list_filter = ['is_admin', 'is_active']
    ordering = ('lastName',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

