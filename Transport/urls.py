from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, password_reset
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from . import views
from allauth.account import views as all_views 
urlpatterns = [
	url(r'^Booking/$', views.BookingView, name='bookform'),
	url(r'^Autos/$', views.AutomobileView, name='auto'),
	url(r'^Rent/$', views.RentCreate, name='rent'),
	url(r'^Pickup/$', views.PickUp, name='pickup'),
	url(r'^Remove_Rent/(?P<rpk>\d+)$', views.RemoveRent, name='remove_rent'),
    url(r'^Auto_detail/(?P<pk>\d+)/$', views.Auto_details, name='auto_details'),
    url(r'^order-approve/$', views.Approve_Order, name='approve_order'),
    url(r'^order-cancel/$', views.Cancel_Order, name='cancel_order'),

]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 