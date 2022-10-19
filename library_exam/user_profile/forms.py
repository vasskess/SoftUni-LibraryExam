from django.forms import ModelForm
from django import forms
from library_exam.user_profile.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "image_url": forms.URLInput(attrs={"placeholder": "URL"}),
        }


class DeleteProfileForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs["disabled"] = "disabled"
