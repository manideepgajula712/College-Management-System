from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User as DefaultUser
from django.contrib.auth.models import Group

from .models import User, Role


# Remove default Django User and Group
try:
    admin.site.unregister(DefaultUser)
except:
    pass

try:
    admin.site.unregister(Group)
except:
    pass


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')