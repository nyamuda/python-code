class Product :
    def __init__(self,id,name,price,quantity) :
        self.id=id
        self.name=name
        self.price=price
        self.quantity=quantity

    def get_total_price(self) :
        return self.quantity*self.price
    
    def display(self) :
        print(f'{self.name} ({self.quantity}) - ${self.get_total_price():.2f}')