from django.conf.urls import url


from . import views

urlpatterns = [
	url(r'^$', views.IndexView, name="checkoutView"),
	url(r'^remove$', views.removeItem , name="checkout_remove"),
	url(r'^update$', views.updateQuantity, name="checkout_update"),
	url(r'^total$', views.getTotal, name="checkout_update"),
	url(r'^pay$', views.pay, name="checkout_update"),
]