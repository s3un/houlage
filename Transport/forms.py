from django import forms
from .models import Rent, AutoMobile

class DateForm(forms.ModelForm):
	driver=forms.BooleanField(required=False, initial=False)
	class Meta:
		model = Rent
		fields = ('pickup_date','return_date')

class CarForm(forms.ModelForm):
	class Meta:
		model = AutoMobile
		fields ='__all__'