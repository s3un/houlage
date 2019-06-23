from django.shortcuts import render,HttpResponse
from django.conf import settings
from .models import order
import stripe
stripe.api_key=settings.STRIPE_SECRET_KEY
# Create your views here.

def Order_create(request):
	if request.method=="POST":
		token =request.POST.get('stripeToken')
		cost = request.POST.get('cost')
		order_total=request.POST.get('order_total')
		print (order_total)
		print(cost)
		checkout_amount= float(order_total) + float(cost)
		charge = stripe.Charge.create(
			amount=checkout_amount,
			currency = 'ngn',
			description='Rental charges',
			source=token,
			)
	return HttpResponse("successful")
	

