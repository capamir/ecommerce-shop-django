from store.models import Product
from decimal import Decimal


class Cart():
    def __init__(self, request):
        self.session = request.session
        
        # returning user - ontain his/her existing session
        cart = self.session.get('cart')

        # New user - generate a session key
        if not cart:
            cart = self.session['cart'] = {}
        
        self.cart = cart

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['total_price'] = Decimal(item['price']) * item['quantity']
            yield item
        
    def add(self, product, qty):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }
        self.cart[product_id]['quantity'] += qty
        self.save()
    
    def save(self):
        self.session.modified = True
    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    