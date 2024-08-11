from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User

        fields = ('email', 'password1', 'password2', 'country', 'phone_number', 'avatar')


class UserProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'password', 'country', 'phone_number', 'avatar')

