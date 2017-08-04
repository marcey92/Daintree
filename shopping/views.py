from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from login.models import User
from shopping.models import Item
from checkout.models import Basket
from login.views import login_view

# main view
def shoppingView(request):
	# see if there is a logged in user
	try:
		c = User.objects.get(username=request.user.username)
	except ObjectDoesNotExist:
		return login_view(request)

	# render shopping/index.html
	items = Item.objects.all()
	# get number of items in basket
	basketItems = Basket.objects.filter(customer=c)
	context = {
		'username': request.user.username,
		'basketNum': len(basketItems),
		'items': items
	}
	return render(request, 'shopping/index.html', context)

def addView(request):
	""""
		add item to basket
	"""
	if request.method == 'POST':
		c = User.objects.get(username=request.user.username)
		item_id = request.POST["item_id"]
		item = Item.objects.get(id=item_id)
		q = 0
		# check to see if item is already in basket
		# if so just update quantity
		try:
			checkB = Basket.objects.get(item=item)
			# item already exists increment quantity
			q = checkB.quantity + 1
			# remove old item
			checkB.delete();
		except Basket.DoesNotExist:
			q = 1;

		if(item):
			b = Basket(customer=c,item=item, quantity=q)
			b.save()
			return HttpResponse(None)
		return HttpResponseBadRequest(None)

"""
	To add item to basket:
	from login.models import Customer
	from checkout.models import Basket

	get Customer like
		c = Customer.objects.get(user_name='marcey')
	
	get Item like
		i = Item.objects.get(name='BIG DILDO')

	add to basket like (maybe get quantity and then +1)
		q = 1
		b = Basket(customer=c,item=i, quantity=q)
		b.save()

	to delete item:
		b = Basket.objects.get(customer=c, item=i)
		b.delete()

	should maybe add functionality to add more than one item

"""