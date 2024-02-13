from rest_framework import serializers
from orders.models import Order, ShippingAddress, OrderItem
from products.models import Product


class OrderSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = self.context.get('request').user
        data = self.context.get('request').data
        order_items = data['orderItems']
        shipping_address = data['shippingAddress']

        # (1) Create order
        order = Order.objects.create(user=user)

        # (2) Create shipping address
        ShippingAddress.objects.create(
            order=order,
            address=shipping_address['address'],
            city=shipping_address['city'],
            postal_code=shipping_address['postalCode'],
            country=shipping_address['country'],
        )

        # (3) Create order items and set order to orderItem relationship
        for item in order_items:
            product = Product.objects.get(id=item['product'])

            item = OrderItem.objects.create(
                product=product,
                order=order,
                name=product.name,
                quantity=item['quantity'],
                price=item['price'],
                image=product.image.url,
            )

            # (4) Update stock
            product.count_in_stock -= item.quantity
            product.save()

        return order

    class Meta:
        model = Order
        fields = '__all__'