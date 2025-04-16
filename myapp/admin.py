# myapp/admin.py
from django.contrib import admin
from .models import *
admin.site.register(ProductDetails)
admin.site.register(Feedback)
'''
from .models import Product, Cart, CartItem

admin.site.register([Product, Cart, CartItem])
'''