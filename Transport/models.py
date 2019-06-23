import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from Cart.models import cart
from django.db.models.signals import pre_save, post_save,m2m_changed
User=settings.AUTH_USER_MODEL
# Create your models here.


class Vehicle(models.Model):
	is_car=models.BooleanField(default=False)
	is_truck=models.BooleanField(default=False) 
	is_Bus=models.BooleanField(default=False) 
	is_Tanker=models.BooleanField(default=False)
	tag= models.CharField(max_length=6)
	def publish(self):
		self.save()

	def __str__(self):
		return self.tag

class Brand(models.Model):

	Brand_Name= models.CharField(default="Tesla", max_length=50)
	def publish(self):
		self.save()

	def __str__(self):
		return self.Brand_Name

class AutoMobile(models.Model):
	Vehicle_id= models.ForeignKey(Vehicle, on_delete=models.CASCADE)
	Brands= models.ForeignKey(Brand, on_delete=models.CASCADE, default=1)
	Model=models.CharField(max_length=20)
	Color=models.CharField(max_length=10)
	No_of_Seat= models.PositiveIntegerField()
	image = models.ImageField(upload_to="AutoMobile",default='Users/Model/user.png', blank=True)
	Air_Condition=models.BooleanField(default=True)
	Availability=models.BooleanField(default=True)  
	Cost= models.PositiveIntegerField()  

	def publish(self):
		self.save()

	def __str__(self):
		return self.Brands.Brand_Name+" "+self.Model+" "+self.Vehicle_id.tag

class Rent(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	Automobile = models.ForeignKey(AutoMobile, blank=True, on_delete=models.CASCADE)
	Cart=models.ForeignKey(cart,on_delete=models.CASCADE, null=True, blank=True)
	pickup_date = models.DateTimeField(default=datetime.datetime.now)
	return_date = models.DateTimeField(default=datetime.datetime.now)
	days = models.PositiveIntegerField(default=0)
	# driver=models.BooleanField(default=False)
	Cost = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	def publish(self):
		self.save()

	def __str__(self):
		return self.Automobile.Brands.Brand_Name + " "+ self.Automobile.Model

class Locations(models.Model):
	location = models.CharField(max_length=50)

	def publish(self):
		self.save()
	def __str__(self):
		return self.location


# def post_save_rent_receiver(sender,instance,created, *args, **kwargs):



# post_save.connect(post_save_rent_receiver, sender=Rent)




















# class Bus(models.Model):
# 	Vehicle_id= models.ForeignKey(Vehicle, on_delete=models.CASCADE)
# 	Brands= models.ForeignKey(Brand, on_delete=models.CASCADE, default='Brand')
# 	Model=models.CharField(max_length=20)
# 	Color=models.CharField(max_length=10)
# 	No_of_Seat= models.PositiveIntegerField()
# 	Air_Condition=models.BooleanField(default=True)
# 	Availability=models.BooleanField(default=True)  
# 	Cost= models.PositiveIntegerField()  

# 	def publish(self):
# 		self.save()

# 	def __str__(self):
# 		return self.Brands.Brand_Name+" "+self.Model

# class Truck(models.Model):
# 	Vehicle_id= models.ForeignKey(Vehicle, on_delete=models.CASCADE)
# 	Model=models.CharField(max_length=20)
# 	Color=models.CharField(max_length=10)
# 	Brands=models.ForeignKey(Brand, on_delete=models.CASCADE, default='Brand')
# 	# No_of_Seat= models.PositiveIntegerField()
# 	# Air_Condition=models.BooleanField(default=True)
# 	Truck_Size=models.CharField(max_length=10)

# 	Availability=models.BooleanField(default=True)  
# 	Cost= models.PositiveIntegerField()  

# 	def publish(self):
# 		self.save()

# 	def __str__(self):
# 		return self.Brands.Brand_Name+" "+self.Model

class Booking(models.Model):
	Booking_code=models.CharField(max_length=20)
	Vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

	Customer = models.CharField(max_length=50)
	From= models.CharField(max_length=50)
	To=models.CharField(max_length=50)

	def publish(self):
		self.save()

	def __str__(self):
		return self.Booking_code