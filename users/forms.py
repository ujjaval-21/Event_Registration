from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"placeholder": "you@example.com", "autocomplete": "email"}
        ),
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )
        widgets = {
            "first_name": forms.TextInput(
                attrs={"placeholder": "First name", "autocomplete": "given-name"}
            ),
            "last_name": forms.TextInput(
                attrs={"placeholder": "Last name", "autocomplete": "family-name"}
            ),
            "username": forms.TextInput(
                attrs={"placeholder": "Choose a username", "autocomplete": "username"}
            ),
        }

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            if name in ("password1", "password2"):
                field.widget.attrs["placeholder"] = (
                    "Create a secure password"
                    if name == "password1"
                    else "Repeat your password"
                )
                field.widget.attrs["autocomplete"] = "new-password"


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={"placeholder": "Enter your username", "autocomplete": "username"}
        ),
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter your password",
                "autocomplete": "current-password",
            }
        ),
    )

    error_messages = {
        "invalid_login": "We couldn’t find an account with that username and password. Please try again.",
        "inactive": "This account is inactive. Please contact support for help.",
    }

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
