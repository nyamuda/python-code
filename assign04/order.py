class Order :
    def __init__(self) :
        self.id=""
        self.products=[]
    
    def get_subtotal(self) :
        total=0
        for product in self.products :
            total+=product.get_total_price()
        return total
    
    def get_tax(self) :
        return 0.065*self.get_subtotal()
    
    def get_total(self) :
        return self.get_subtotal()+self.get_tax()
    
    def add_product(self,obj) :
        self.products.append(obj)
    
    def display_receipt(self) :
        print(f'Order: {self.id}')
        for product in self.products :
            product.display()
        print(f'Subtotal: ${self.get_subtotal():.2f}')
        print(f'Tax: ${self.get_tax():.2f}')
        print(f'Total: ${self.get_total():.2f}')
       
