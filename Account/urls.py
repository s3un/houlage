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
	url(r'^login/$', all_views.LoginView.as_view(), {'template_name':'account/login.html'}, name='account_login'),
	url(r'^SignUp/$', all_views.SignupView.as_view(), {'template_name':'account/signup.html'}, name='account_signup'),
	url(r'^Mail_activate/$', all_views.email_verification_sent, name='account_email_verification_sent'),
	url(r"^confirm-email/(?P<key>[-:\w]+)/$", all_views.confirm_email,
        name="account_confirm_email"),
	url(r'^logout/$', auth_views.logout, name='logout'),
	url(r'^Update-Info/(?P<pk>\d+)/$', views.Info.as_view(), name='info'),
	# url(r'^register/$', views.UserFormView.as_view(), name='register'),
	# url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
	# url(r'^password_reset/$',password_reset,{'template_name':'account/password_reset_form.html'}, name='password_reset'),
	# url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name':'account/password_reset_done.html'}, name='password_reset_done'),
	# url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm,{'template_name':'account/password_reset_confirm.html'}, name='password_reset_confirm'),
	# url(r'^reset/done/$', auth_views.password_reset_complete,{'template_name':'account/password_reset_complete.html'}, name='password_reset_complete'),
]