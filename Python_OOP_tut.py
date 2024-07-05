class Item:
    pay_rate = 0.8 # 20% discount
    all = []
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate


print(Item.all)

for instance in Item.all:
    print(instance.name)

