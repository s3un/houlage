from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from allauth.account import views as all_views 
urlpatterns = [
	url(r'^create_order/$', views.Order_create, name='order_create'),

]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 