from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,userPosts


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'name', 'gender', 'security_question', 'answer', 'birth_date', 'is_active', 'image', 'resume']
    list_editable =['name', 'is_active','resume']


admin.site.register(CustomUser, admin_class=CustomUserAdmin)
admin.site.register(userPosts)