from datetime import datetime
from django.shortcuts import render, redirect
from .models import cart
from Transport.forms import DateForm
from Transport.models import AutoMobile,Rent,Locations
from Orders.models import order
from django.db.models import Avg, Max, Min, Sum, Count
from django.conf import settings
# import stripe
#
# stripe.api_key=settings.STRIPE_SECRET_KEY
# Create your views here.


def Cart_home(request):
	template= 'Cart/cart_home.html'
	# print (request.user.pk)
	carts = cart.objects.filter(user__pk=request.user.pk)
	cart_id=request.session.get('cart_id', None)
	dateform= DateForm()
	rents_check=Rent.objects.filter(user__pk=request.user.pk)
 	# cart_id is not None
	if carts.exists() and request.user.is_authenticated and rents_check.exists():
		# cart_id=request.session.get('cart_id', None)
		# print(cart_id)
		# carts_obj= cart.objects.get(id=cart_id)
		# print(carts_obj.automobile.all())
		rents= Rent.objects.filter(user__pk=request.user.pk).aggregate(Sum('Cost'))
		rents_cost=rents['Cost__sum']
		rents_obj=Rent.objects.filter(user__pk=request.user.pk)
			# days_sum=days_sum+ 
		Cart_rent_obj=cart.objects.get(user__pk=request.user.pk)
		Cart_rent_obj.subtotal=rents_cost
		Cart_rent_obj.save()
		carts = cart.objects.get(user__pk=request.user.pk)
		print(carts)
		# carts.subtotal=rents_cost
		if rents_obj.exists():
			context={
			'rents_obj':rents_obj,
			'carts':carts,
			'dateform':dateform,
			}
			return render (request, template, context)
		else:
			return HttpResponse('Failed here')
	else:
		carts, new_obj=cart.objects.new_or_get(request)
		rents= Rent.objects.filter(user__pk=request.user.pk, Cart__id=cart_id).aggregate(Sum('Cost'))
		rents_cost=rents['Cost__sum']
		rents_obj=Rent.objects.filter(user__pk=request.user.pk, Cart__id=cart_id)
			# days_sum=days_sum+ 
		Cart_rent_obj=cart.objects.filter(user__pk=request.user.pk, id=cart_id)
		# print()
		if Cart_rent_obj.count()==1:
			Cart_rent=Cart_rent_obj.first()
			print(Cart_rent)
			Cart_rent.subtotal=rents_cost
			Cart_rent.save()
			carts = cart.objects.get(user__pk=request.user.pk, id=cart_id)
			# print(carts)
		context={
		'carts':carts,
		'rents_obj':rents_obj,
		}
		return render (request, template, context)

def Cart_Update(request):
	# automobile_id = request.POST.get('automobile')
	# if automobile_id is not None:
	# 	try:
	# 		automobile_obj=AutoMobile.objects.get(pk=automobile_id)
	# 	except AutoMobile.DoesNotExist:
	# 		print('Does Not exist')
	# 	carts, new_obj=cart.objects.new_or_get(request)
	# 	carts.automobile.add(automobile_obj)
	return redirect('cart_home')

def CheckoutView(request):
	template = 'Cart/Checkout.html'

	if request.method=="POST":
		carts, new_obj=cart.objects.new_or_get(request)
		order_obj=None
		if new_obj:
			return redirect('cart_home')
		else:
			order_obj, new_order_obj = order.objects.get_or_create(Carts=carts)
			rents= Rent.objects.filter(user__pk=request.user.pk, Cart=carts).count()
			locations = Locations.objects.all();
			context={
			'carts':carts,
			'order':order_obj,
			'rents':rents,
			'locations':locations,
			}
		return render(request, template,context)
	return redirect('cart_home')


