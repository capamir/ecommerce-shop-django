
class Cart():
    def __init__(self, request):
        self.session = request.session
        
        # returning user - ontain his/her existing session
        cart = self.session.get('cart')

        # New user - generate a session key
        if not cart:
            cart = self.session['cart'] = {}
        
        self.cart = cart
        