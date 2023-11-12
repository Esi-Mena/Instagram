from django import forms
from .models import Photo, Comment, User, UserProfile
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Photo

class LoginForm(AuthenticationForm):
    pass

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.' ,widget=forms.EmailInput(attrs={'placeholder': 'Mobile Number or Email'}))
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'caption']
        widgets = {
            'caption': forms.Textarea(attrs={
                'placeholder': 'Add a caption...',
                'class': 'w-full px-0 text-sm text-gray-900 bg-white border-0 dark:bg-gray-800 focus:ring-0 dark:text-white dark:placeholder-gray-400',
                'rows': 4
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Add a comment...'}),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'website', 'profile_picture']

class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['caption']
        