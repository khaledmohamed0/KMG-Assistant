from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = "__all__"

        widgets = {

            "client": forms.Select(attrs={
                "class": "form-select"
            }),

            "image": forms.FileInput(attrs={
                "class": "form-control"
            }),

            "idea": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "caption": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5
            }),

            "publish_at": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local"
                }
            ),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),

            "notes": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),

            "alt_text": forms.TextInput(attrs={
                "class": "form-control"
            })

        }