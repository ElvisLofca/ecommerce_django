from django.contrib import admin
from orders.models import Order, OrderItem, ShippingAddress

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)