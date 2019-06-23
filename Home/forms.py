from django import forms
from Transport.models import AutoMobile

class AutoMobileForm(forms.ModelForm):
    class Meta:
        model = AutoMobile
        exclude=[]