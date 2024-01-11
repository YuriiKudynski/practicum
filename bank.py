class Bank:

    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def display_balance(self):
        print(f"Balance = {self.balance}")

    def get_money(self, amount):
        self.__balance += amount
        print(f"До рахунку додано {amount}")

    def insert_money(self, amount):
        try:
            if amount < self.__balance:
                self.__balance -= amount
                print(f"З рахунку знято {amount}")
            else:
                raise ValueError("Недостатньо коштів")
        except ValueError as e:
            print(e)


acc = Bank(100)
acc.get_money(20)
acc.insert_money(100)
acc.display_balance()
acc2 = Bank(2000)
acc2.display_balance()