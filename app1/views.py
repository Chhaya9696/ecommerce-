from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, CartItem
from django.contrib.auth.forms import AuthenticationForm   # for signin view
from django.contrib.auth import authenticate, login, logout
from .forms import Signupform
from django.db.models import Q

# def flipkart(request):
#     return render(request,'flipkartnew.html')

def product_ordering(request):
    search_query = request.POST.get('search_query')

    if search_query:
        filtered_cakes = Product.objects.filter(Q(name__icontains=search_query))
        context = {'cakes': filtered_cakes, 'search_query': search_query}
    else:
        cakes = Product.objects.all()
        context = {'cakes': cakes}


    return render(request, 'over.html', context)
def product_list(request):
	products = Product.objects.filter(category='dress').values()
	return render(request, 'index.html', {'products': products})
def appliances(request):
	products = Product.objects.filter(category='appliances').values()
	return render(request, 'appliances.html', {'products': products})
def grocery(request):
	products = Product.objects.filter(category='grocery').values()
	# mydata = Member.objects.filter(firstname='Emil').values()
	return render(request, 'grocery.html', {'products': products})

def view_cart(request):
	cart_items = CartItem.objects.filter(user=request.user)
	total_price = sum(item.product.price * item.quantity for item in cart_items)
	return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
	product = Product.objects.get(id=product_id)
	cart_item, created = CartItem.objects.get_or_create(product=product,
													user=request.user)
	cart_item.quantity += 1
	cart_item.save()
	return redirect('view_cart')

def remove_from_cart(request, item_id):
	cart_item = CartItem.objects.get(id=item_id)
	cart_item.delete()
	return redirect('view_cart')


def home(request):
	return HttpResponse('Hello, World!')

def signup(request):
		if request.method == 'POST':
			fm = Signupform(request.POST)
			if fm.is_valid():
				fm.save()
				# Redirect with URL path
				return redirect("signin")
		else:
			fm = Signupform()
		return render(request, 'register.html', {'reg_fm': fm})

def signin(request):
		if request.method == "POST":
			fm = AuthenticationForm(request=request, data=request.POST)
			if fm.is_valid():
				uname = fm.cleaned_data['username']
				upass = fm.cleaned_data['password']
				user = authenticate(username=uname, password=upass)
				# feed = FeedbackEntry()
				if user is not None:
					login(request, user)  # username
					return render(request, 'flipkartnew.html', {'user': user})
				# return redirect("/feedback")

		else:
			fm = AuthenticationForm()
		return render(request, "signin.html", {'user_data': fm})
def signout(request):
		logout(request)
		return redirect("/signin")
