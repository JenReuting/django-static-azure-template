from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = [
        'email', 'first_name', 'last_name', 'phone_number', 'is_staff', 'is_superuser', 'date_joined', 'profile_photo',
    ]
    list_filter = [
        'email',
        'is_staff',
        'is_superuser',
        ]
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('phone_number', 'first_name', 'last_name', 'profile_photo',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_superuser', 'profile_photo',)}
         ),
    )
    search_fields = ('email', 'phone_number', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
