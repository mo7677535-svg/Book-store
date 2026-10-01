from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

# ------------------------
# Register Form
# ------------------------
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# ------------------------
# Login Form
# ------------------------
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


# ------------------------
# Profile Update Form
# ------------------------
class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('contact_number', 'address', 'profile_photo')
        widgets = {
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter address'}),
            'profile_photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

