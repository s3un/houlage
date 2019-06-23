import datetime
from django.db import models
from Cart.models import cart
from Houlage.utils import unique_order_id_generator
from django.db.models.signals import pre_save,post_save 
from django.conf import settings
User=settings.AUTH_USER_MODEL
# Create your models here.

class Status(models.Model):

	status=models.CharField(max_length=50)

	def __str__(self):
		return self.status

	

class order(models.Model):
	order_id = models.CharField(max_length=20, blank=True)
	user=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	Carts = models.ForeignKey(cart, on_delete=models.CASCADE)
	status= models.ForeignKey(Status, on_delete=models.CASCADE, default=1)
	# user =models.ForeignKey(User, default=1)

	order_total= models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	def __str__(self):
		return self.order_id

	def update_total(self):
		cart_total=self.Carts.total
		User=self.Carts.user
		new_total= cart_total
		self.order_total=new_total
		self.user=User
		self.save()
		return new_total


def pre_save_order_id_create_receiver(sender,instance, *args, **kwargs):
	if not instance.order_id:
		instance.order_id=unique_order_id_generator(instance)


pre_save.connect(pre_save_order_id_create_receiver, sender=order)

def post_save_cart_total(sender,instance,created,*args, **kwargs):
	carts= instance
	cart_id=carts.id
	if not created:
		carts=instance
		cart_total=carts.total
		cart_id=carts.id
		# driver_cost=0
		# print(driver_cost)
		qs= order.objects.filter(Carts__id=cart_id)
		if qs.count()==1:
			# driver_cost=0
			# print(driver_cost)
			order_obj=qs.first()
			order_obj.update_total()
post_save.connect(post_save_cart_total, sender=cart)

def post_save_order(sender,instance,created,*args, **kwargs):
	# print(instance.driver)
	if created:
		# driver_cost=5000
		instance.update_total()
post_save.connect(post_save_order, sender=order)