class Customer:
    def __init__(self) :
        self.id=""
        self.name=""
        self.orders=[]
    
    def get_order_count(self) :
        return len(self.orders)
    
    def get_total(self) :
        total_price=0
        for order in self.orders :
            total_price+=order.get_total()
        return total_price
    
    def add_order(self,obj) :
        self.orders.append(obj)
    
    def display_summary(self) :
        print(f"Summary for customer '{self.id}':")
        print(f'Name: {self.name}')
        print(f'Orders: {self.get_order_count()}')
        print(f'Total: ${self.get_total():.2f}')
    
    def display_receipts(self) :
        print(f"Detailed receipts for customer '{self.id}':")
        print(f'Name: {self.name}')
        for order in self.orders :
            print("")
            order.display_receipt()
        

