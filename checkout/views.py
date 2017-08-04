from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views import generic
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail

from decimal import *
import json
import textwrap

from login.models import User
from shopping.models import Item
from checkout.models import Basket
from login.views import login_view

def IndexView(request):
	"""
	Returns the login screen for the logged in user.
	Checks if basket is empty.
	"""
	try:
		cust = User.objects.get(username=request.user.username)
	except ObjectDoesNotExist:
		#if customer does not exist re-route to login page
		return login_view(request)
	empty = False
	basket = Basket.objects.filter(customer=cust)
	if len(basket) ==0:
		empty = True
	context = {
		'username': cust.username,
		'empty': empty,
		'basket_list': basket
	}
	return render(request, 'checkout/index.html', context)

def removeItem(request):
	"""
	Removes item from logged in customers basket.
	"""
	if request.method == 'POST':
		cust = User.objects.get(username=request.user.username)
		item_id = request.POST["item_id"]
		item = Item.objects.get(id=item_id)
		b_item = Basket.objects.get(customer=cust, item=item)
		if(b_item):
			b_item.delete()
			return HttpResponse(None)
	return HttpResponseBadRequest(None)
	

def updateQuantity(request):
	""""
	Updates the quantity of an item in the logged in customers basket.
	"""
	if request.method == 'POST':
		cust = User.objects.get(username=request.user.username)
		item_id = request.POST["item_id"]
		item = Item.objects.get(id=item_id)
		b_item = Basket.objects.get(customer=cust, item=item)
		if(b_item):
			b_item.quantity = int(request.POST['new_quantity'])
			b_item.save()
			return HttpResponse(None)
	return HttpResponseBadRequest(None)

def getTotal(request):
	"""
	Returns the total from the logged in customers basket.
	"""
	if request.method == 'POST':
		cust = User.objects.get(username=request.user.username)
		basket = Basket.objects.filter(customer=cust)
		total = total_from_basket(basket)
		data = {'total': str(total)}
		return HttpResponse(json.dumps(data), content_type='application/json')
	#if unsuccesful
	return HttpResponseBadRequest(None)

def pay(request):
	"""
	Sends an email confirming order to the logged in customer 

	constants in setting need to be entered to work:
	EMAIL_HOST = ''
	EMAIL_HOST_PASSWORD = ''
	EMAIL_HOST_USER = ""
	EMAIL_PORT = ''
	EMAIL_USE_SSL = True

	"""
	if request.method == 'POST':
		cust = User.objects.get(username=request.user.username)
		basket = Basket.objects.filter(customer=cust)
		total = total_from_basket(basket)

		text = """\
		Hi {0}, 

		Your order has come to {1} GBP.

		Your delivery address is:
		{2}
		{3}
		{4}

		Your order should arrive within 2 or 3 working days.

		Thank you for shopping with Daintree.
		From the team Marcel, Bradley and Grace
		""".format(str(cust.username), str(total),
				   cust.info.first_line, cust.info.town, 
				   cust.info.postcode)

		send_mail(
			'Daintree Order',
			text,
			'daintree-email',
			[cust.email],
			fail_silently=True, # Set to false when email details are added
		)
		if "__iter__" not in dir(basket):
			basket = (basket,)
		for item in basket:
			item.delete()
		return HttpResponse(None)
	#if unsuccesful
	return HttpResponseBadRequest(None)

def total_from_basket(basket):
	"""
	Returns the total from given basket
	"""
	if "__iter__" not in dir(basket):
		basket = (basket,)
	total = Decimal(0)
	for item in basket:
		total = total + (Decimal(item.item.price) * Decimal(item.quantity))
	return total

