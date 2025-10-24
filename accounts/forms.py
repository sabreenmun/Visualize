from django import forms
from django.contrib.auth.models import User
from .models import Profile

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    profile_picture = forms.ImageField(required=False)
    website = forms.URLField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        # save the user first
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

        # create profile
        profile = Profile(
            user=user,
            bio=self.cleaned_data.get('bio', ''),
            profile_picture=self.cleaned_data.get('profile_picture', None),
            website=self.cleaned_data.get('website', '')
        )

        if commit:
            profile.save()

        return user
