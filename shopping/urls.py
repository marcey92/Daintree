from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.shoppingView, name="shoppingView"),
	url(r'^add$', views.addView , name="addView"),
]