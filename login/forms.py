from django import forms
from .models import User
from django.contrib.auth.models import User 
from django.contrib.auth import (
authenticate, 
get_user_model,
login,
logout,
	)

User = get_user_model()


class UserLoginForm(forms.Form):
	username = forms.CharField()
	#email = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)

	class Meta: 
		model = User 
		#fields = ['username', 'email', 'password']
		fields = ['username','password']

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		#email = self.cleaned_data.get("email")
		password = self.cleaned_data.get('password')
		user = authenticate(username= username, password=password) #email=email)

		if username and password:
			if user is None:
				raise forms.ValidationError(("Please enter the correct username and password"))

		return self.cleaned_data


	
	
		return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm): 
	first_name = forms.CharField()
	last_name = forms.CharField()
	phone = forms.CharField()
	first_line = forms.CharField()
	town = forms.CharField()
	postcode = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput, label = 'Confirm Password')
	password2 = forms.CharField(widget= forms.PasswordInput, label= 'Password')
	class Meta: 
		model = User
		fields = [
		'first_name',
		'last_name',
		'username',
		'email',
		'phone',
		'password2',
		'password',
		'first_line',
		'town',
		'postcode',
		]

		
	def clean_password(self):
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password != password2: 
			raise forms.ValidationError("Your password doesn't match!")
		return password


	        