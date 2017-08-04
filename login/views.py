from django.contrib.auth import (
authenticate, 
get_user_model,
login,
logout,
	)
from django import forms
from django.shortcuts import render, HttpResponseRedirect
from .forms import UserLoginForm, UserRegisterForm
from django.views.generic import View
from django.conf import settings


def login_view(request):
	print(request.user.is_authenticated()) #just to check if im actually logged in
	title = "Login"
	template = "form.html"
	#t = loader.get_template('login/form.html')
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get('password')
		user = authenticate (username= username,password= password) 
		login(request, user)
		print(request.user.is_authenticated()) #shows if loged in
		#redirect
		return HttpResponseRedirect('/shopping/')

	return render(request, 'login/form.html', {"form": form, "title": title})
	

#next define register view and logout view 

def register_view(request):
	title ="Register"
	template = "register.html"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get('password')
		first_name = form.cleaned_data.get("first_name")
		last_name = form.cleaned_data.get("last_name")
		email = form.cleaned_data.get("email")
		user.set_password(password)
		user.save()

		user.info.first_line = form.cleaned_data.get("first_line")
		user.info.phone = form.cleaned_data.get("phone")
		user.info.town = form.cleaned_data.get("town")
		user.info.postcode  = form.cleaned_data.get("postcode")
		user.save()
		
		new_user = authenticate(username= username, password = password)
		login(request, new_user)
		return HttpResponseRedirect('/shopping/')
	return render(request, "login/register.html", { "form": form, "title": title})


def logout_view(request):
	 logout(request)
	 #redirect
	 return login_view(request)