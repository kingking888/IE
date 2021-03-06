from django import forms
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import validate_email

class SignInForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email", help_text="Required. Add a valid email address")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except validate_email.ValidationError:
            raise ValidationError('The email is not valid')
        if User.objects.filter(email__exact=email):
            raise ValidationError('The email is associated to other user')
        else:
            return email
