from django import forms
from .models import Client


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client

        fields = "__all__"

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "instagram_username": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "facebook_page": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "access_token": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4
            }),

            "active": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            })

        }