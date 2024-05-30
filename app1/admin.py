from django.contrib import admin
from .models import Product, CartItem

admin.site.register(Product)
admin.site.register(CartItem)



# class CityAdmin(admin.ModelAdmin):
#     list_display = Product.objects.filter(name='searchv').values()
# 	return render(request, 'appliances.html', {'products': products})
# admin.site.register(product, CityAdmin)