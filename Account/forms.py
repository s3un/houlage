from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.socialaccount.forms import SignupForm
from allauth.account.forms import SetPasswordField,PasswordField
from .models import CustomUser

class SocialForm(SignupForm):
	
	password1 = SetPasswordField(min_length=6, label='Enterpassword')
	password2 = PasswordField(min_length=6, label='Rente password again')
	
	def clean_password2(self):
		if("password1" in self.cleaned_data and "password2" in self.cleaned_data):
			if(self.cleaned_data["password1"] !=self.cleaned_data["password2"]):
				raise forms.ValidationError(("Password mismatch"))
			

	def signup(self,request,user):
		user.set_password(self.user,self.cleaned_data["password1"] )
		user.save()

class CustomUserChangeForm(UserChangeForm):

	class Meta(UserChangeForm):
		model = CustomUser
		fields = ('username', 'email','license','picture','address','phone')

class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('username', 'email','first_name','last_name')
# class UserLoginForm(LoginForm):
# 	cla

