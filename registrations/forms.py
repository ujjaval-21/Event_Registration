from django import forms


class RegistrationForm(forms.Form):
    """A CSRF-protected form used for registration actions without extra inputs."""

