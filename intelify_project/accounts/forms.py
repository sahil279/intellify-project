from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
	first_name = forms.CharField()
	last_name = forms.CharField()
	phone_number = forms.IntegerField()
	email=forms.EmailField()

	class Meta():
    		model=User
    		fields=['username','email','password1','password2','first_name','last_name','phone_number']