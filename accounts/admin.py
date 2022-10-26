from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserChangeForm
from .models import CustomUser
# from django.contrib.auth.models import User
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserChangeForm
    form = CustomUserChangeForm
    model = CustomUser


# Register your models here.
admin.site.register(CustomUser)
