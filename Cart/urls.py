from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from allauth.account import views as all_views 
urlpatterns = [
	url(r'^$', views.Cart_home, name='cart_home'),
	url(r'^cart_update/$', views.Cart_Update, name='cart_update'),
	url(r'^Checkout/$', views.CheckoutView, name='checkout'),

]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 