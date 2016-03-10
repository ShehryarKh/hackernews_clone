from django.conf.urls import url,include
from django.contrib import admin
from Hackers import views
from .views import logout_

urlpatterns=[
	url(r'create/', views.Create.as_view(),name="create"),
	url(r'register/', views.Register.as_view(),name="register"),
	url(r'login/', views.Login.as_view(),name="login"),
	url(r'logout/', logout_, name="logout"),

	url(r'edit/(?P<slug>[0-9A-Za-z-]+)', views.Edit.as_view(),name="edit"),
	url(r'delete/(?P<slug>[0-9A-Za-z-]+)', views.Delete.as_view(),name="delete"),


]