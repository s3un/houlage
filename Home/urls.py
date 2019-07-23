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
	url(r'^$', views.Home, name='index'),
	url(r'account/', include('Account.urls')),
	url(r'Transport/', include('Transport.urls')),
	url(r'Cart/', include('Cart.urls')),
	url(r'Order/', include('Orders.urls')),
	url(r'^load_brand/$', views.Load_Brand, name='load_brand'),
	url(r'^Dashboard/$', views.dashboard, name='dashboard'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^Admin/$', views.auto_admin, name='auto_admin'),
	url(r'^Create/$', views.car_create.as_view(), name='create_car'),
	url(r'^load_model/$', views.Load_Model, name='load_model'),
	url(r'^load_automobile/$', views.Load_auto, name='load_auto'),
	url(r'^all-user/$', views.All_users, name='all_user'),
	url(r'^a-user/$', views.Load_user, name='load_user'),
	url(r'^block-user/$', views.Block_user, name='block_user'),
	url(r'^unblock-user/$', views.Unblock_user, name='unblock_user'),
	url(r'^Transaction/$', views.Transactions, name='transaction'),
	
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 