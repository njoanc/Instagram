from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image, Profile, Comments

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['Likes', 'pub_date', 'Profile']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment_post', 'author','commented_image')

class SignUpForm(UserCreationForm):

    class Meta:
        model = User

        fields = ('first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2', )