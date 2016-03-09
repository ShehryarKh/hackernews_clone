from django.conf.urls import url,include
from django.contrib import admin
from Hackers import views

urlpatterns=[
	url(r'create/', views.Create.as_view(),name="create"),
	url(r'edit/(?P<slug>[0-9A-Za-z-]+)', views.Edit.as_view(),name="edit"),

]