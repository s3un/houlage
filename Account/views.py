from django.shortcuts import render,HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import CustomUser
# Create your views here.
def Mail_active(request):
	template ='Account/Mail_active.html'

	return HttpResponse('Check Mail For Confirmation mail')

class Info(UpdateView):
	model=CustomUser
	fields = ['first_name','last_name','license']
	template_name = 'Account/Customer_update_form.html'
	success_url= reverse_lazy('dashboard')