from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
	url('^$',views.index,name = 'index'),
	url('^show_graph$',views.show,name = 'show'),
]
