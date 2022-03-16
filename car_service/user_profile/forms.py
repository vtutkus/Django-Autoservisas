from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        
class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)