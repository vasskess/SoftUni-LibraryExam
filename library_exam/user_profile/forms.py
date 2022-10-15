from django.forms import ModelForm

from library_exam.user_profile.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class DeleteProfileForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs["disabled"] = "disabled"
