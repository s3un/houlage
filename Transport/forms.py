from django import forms
from .models import Rent

class DateForm(forms.ModelForm):
	driver=forms.BooleanField(required=False, initial=False)
	class Meta:
		model = Rent
		fields = ('pickup_date','return_date')