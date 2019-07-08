from django.shortcuts import render, HttpResponse,redirect
from Transport.models import Vehicle,AutoMobile, Brand, Rent,Locations
from .forms import AutoMobileForm
from django.views.generic import CreateView
from Orders.models import order
from django.conf import settings
from Account.models import CustomUser
User = settings.AUTH_USER_MODEL
# Create your views here.
def Home(request):
	template= 'Home/index.html'
	vehic =Vehicle.objects.all()
	brands= Brand.objects.all()
	name = request.session.get('firstname')
	context={
	'vehic':vehic,
	'brands':brands,
	'name':name,
	}
	return render(request, template, context)

# def VehicleView(request):
# 	template='Home/index.html'
def Load_Brand(request):
	vehicle = request.GET.get('Vehicle')
	veh = Vehicle.objects.get(tag=vehicle)
	brands = Brand.objects.all()
	context = {
	'veh':veh,
	'brands':brands,
	}
	return render(request, 'Transport/cbrands.html',context)
def Load_Model(request):
	template='Transport/cmodel.html'
	vehi = request.GET.get('vehicle')
	bran=request.GET.get('brand_tag')
	veh = Vehicle.objects.get(pk=vehi)
	brands = Brand.objects.get(pk=bran)
	modl= AutoMobile.objects.filter(Brands=bran, Vehicle_id=vehi)
	context = {
	'veh':veh,
	'brands':brands,
	'modl':modl,
	}
	return render(request, template,context)
def Load_auto(request):
	template='Transport/cars.html'
	if request.method == 'POST':
		vehicle=request.POST.get('vehicle')
		brand=request.POST.get('Brand')
		# print (brand)
		model=request.POST.get('Model')
		automobile = AutoMobile.objects.get(Vehicle_id__tag=vehicle,Brands=brand, Model=model )
		context={
		'vehicle':vehicle,
		'brand':brand,
		'model':model,
		'automobile':automobile,
		}		
		# c=automobile.Brands.Brand_Name + ' '+ automobile.Model
		return render(request,template,context)
def dashboard(request):
	template="Home/dashboard.html"
	user_info=CustomUser.objects.get(pk=request.user.pk)
	rent = Rent.objects.filter(user=request.user)
	rent_count=Rent.objects.filter(user=request.user).count()
	vehic= Vehicle.objects.all()
	orders= order.objects.filter(user=request.user).count
	context={
	'user':user_info,
	'rent_count':rent_count,
	'orders':orders,
	'rent':rent,
	'vehic':vehic,
	}
	return render(request,template,context)

def auto_admin(request):
	template="Home/admin.html"
	automobiles = AutoMobile.objects.all()
	users = CustomUser.objects.all()
	orders = order.objects.all()
	locations=Locations.objects.all()
	context ={
	"automobiles":automobiles,
	"users":users,
	"orders":orders,
	"locations":locations,
	}
	return render(request,template,context)

class car_create(CreateView):
	template_name='Home/create.html'
	form_class=AutoMobileForm
	def get(self,request):
		form=self.form_class(None)
		context={
		'form':form,
		}
		return render(request, self.template_name, context)

	def post(self,request, **kwargs):
		form=self.form_class(request.POST,  request.FILES)
		if form.is_valid():
			create=form.save(commit=False)
			c= form.cleaned_data
			create.save()
			return redirect('auto_admin')

def contact(request):
	template="Home/contact.html"

	return render (request,template)