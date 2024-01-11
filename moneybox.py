class MoneyBox:

    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        if self.coins + v <= self.capacity:
            print("You can add mobey")
            return True
        else:
            print("You cant add money")
            return False

    def add_money(self, v):
        if self.can_add(v):
            self.coins += v
            print("Money add")
        else:
            print("Money dont add")

    def get_balance(self):
        print(f'Balance = {self.coins}')


my_box = MoneyBox(20)
my_box.get_balance()
my_box.can_add(20)
my_box.add_money(20)
my_box.get_balance()
my_box.can_add(5)
my_box.add_money(5)
