
class Cart():
    def __init__(self, request):
        self.session = request.session
        
        # returning user - ontain his/her existing session
        cart = self.session.get('cart')

        # New user - generate a session key
        if not cart:
            cart = self.session['cart'] = {}
        
        self.cart = cart
        
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
        