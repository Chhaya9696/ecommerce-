from django.urls import path
from . import views

urlpatterns = [
	path('index/', views.product_list, name='dress'),
	path('grocery/', views.grocery, name='grocery'),
	path('signup/', views.signup, name='signup'),
	path('signin/', views.signin, name='signin'),
	path('logout/', views.logout, name='logout'),
    path('appliances/', views.appliances, name='appliances'),
	# path('', views.flipkart, name='flipkart'),
	path("",views.product_ordering, name="flipkart"),
	path('cart/', views.view_cart, name='view_cart'),
	path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
	path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
