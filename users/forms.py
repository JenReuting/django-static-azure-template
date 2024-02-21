from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    """
    A form for creating new users. Includes all the required fields, plus a repeated password.
    """
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'profile_photo')


class CustomUserChangeForm(UserChangeForm):
    """
    A form for updating users. Includes all the fields on the user, but replaces the password field
    with admin's password hash display field.
    """
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'profile_photo')
