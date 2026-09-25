from django import forms

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ("title", "description", "venue", "date", "time", "capacity", "image")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "venue": forms.TextInput(attrs={"class": "form-control"}),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "time": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "capacity": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

    def clean_capacity(self):
        capacity = self.cleaned_data["capacity"]
        if self.instance.pk:
            active_registrations = self.instance.registrations.filter(status="active").count()
            if capacity < active_registrations:
                raise forms.ValidationError(
                    f"Capacity cannot be lower than the {active_registrations} active registrations."
                )
        return capacity
