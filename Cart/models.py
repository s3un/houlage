import datetime
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save,m2m_changed
# from Transport.models import AutoMobile
# Create your models here.
User=settings.AUTH_USER_MODEL
class CartManager(models.Manager):
	def new_or_get(self, request):
		booking = cart.objects.filter(user__pk=request.user.pk)
		if booking.count()==1 and request.user.is_authenticated:
			new_obj=False
			carts = self.get_queryset().get(user__pk=request.user.pk)
			return carts, new_obj
		else:
			cart_id=request.session.get('cart_id', None)
			qs= self.get_queryset().filter(id=cart_id)
			# print (request.user)
			if qs.count()==1:
				new_obj=False
				# print("Cart ID exists")
				carts=qs.first()
				if request.user.is_authenticated and carts.user is None:
					carts.user=request.user
					carts.save()
				# print(carts.user)
			else:
				new_obj= True
				carts=  self.new(user=request.user)
				request.session['cart_id']=carts.id
				# print('New ID created')
			return carts, new_obj

	def new(self, user=None):
		user_obj=None
		if user is not None:
			if user.is_authenticated:
				user_obj=user
		return self.model.objects.create(user=user_obj)

		

class cart(models.Model):
	user= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	# automobile = models.ManyToManyField(Rent,blank=True)
	total= models.DecimalField(default=0.00,null=True, max_digits=100, decimal_places=2)
	subtotal= models.DecimalField(default=0.00, null=True, max_digits=100, decimal_places=2)
	timestamp=models.DateTimeField(auto_now_add=True)
	update=models.DateTimeField(auto_now=True)
	# pickup_date = models.DateTimeField(default=datetime.datetime.now)
	# return_date = models.DateTimeField(default=datetime.datetime.now)

	objects= CartManager()

	def __str__(self):
		return str(self.id)

# def m2m_change_cart_receiver(sender,instance,action, *args, **kwargs):
# 	if action =='post_add' or action=='post_clear' or action=='post_remove':
# 		automobile = instance.automobile.all()
# 		total = 0
# 		for x in automobile:
# 			total += x.Automobile.Cost
# 		if instance.subtotal !=total:
# 			instance.subtotal=total
# 			instance.save()
# m2m_changed.connect(m2m_change_cart_receiver, sender=cart.automobile.through)

def pre_save_cart_receiver(sender,instance, *args, **kwargs):
	instance.total = instance.subtotal

pre_save.connect(pre_save_cart_receiver, sender=cart)
