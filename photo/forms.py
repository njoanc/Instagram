from django import forms
from .models import Comment,Profile,Pic
from django.contrib.auth.forms import AuthenticationForm

class ProfileForm(forms.ModelForm):
	model = Profile
	username = forms.CharField(label='Username',max_length = 30)
	
	bio = forms.CharField(label='Image Caption',max_length=500)
	profile_pic = forms.ImageField(label = 'Image Field')

class ProfileUploadForm(forms.ModelForm):
	class Meta:
		model = Profile
		
		exclude = ['user']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = [ 'comment' ]  

# class SignupForm(UserCreationForm):
#     email = forms.EmailField(max_length=200, help_text='Required')
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Pic
        exclude = ['image_name', 'pub_date','profile','user']
        widgets = {
            'likes': forms.CheckboxSelectMultiple(),
    }


