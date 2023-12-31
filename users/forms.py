from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    email = models.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']