class Dictor:
    directors = []

    def __init__(self, name_dictor, mfo_number):
        self.name_dictor = name_dictor
        self.mfo_number = mfo_number
        if self.name_dictor not in [d.name_dictor for d in Dictor.directors]:
            Dictor.directors.append(self)

    def display_info(self):
        return f"Dictor {self.name_dictor} has MFO number {self.mfo_number}"


class Bank(Dictor):
    banks = []

    def __init__(self, name_dictor, mfo_number, bank_name, adress):
        super().__init__(name_dictor, mfo_number)
        self.bank_name = bank_name
        self.adress = adress
        if self.bank_name not in [b.bank_name for b in Bank.banks]:
            Bank.banks.append(self)

    def display_info(self):
        return f"Bank name - {self.bank_name}. His location {self.adress}"


class User(Bank):
    users = {}
    document_counter = 1

    def __init__(self, name_dictor, mfo_number, bank_name, adress, owner_name, account_number, balance):
        Bank.__init__(self, name_dictor, mfo_number, bank_name, adress)
        Dictor.__init__(self, name_dictor, mfo_number)
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance
        self.documents = {}
        User.users[f"{self.owner_name}"] = self.account_number

    def display_info(self):
        return (f"Owner: {self.owner_name}\n"
                f"Bank: {self.bank_name}\n"
                f"Account_number: {self.account_number}\n"
                f"Balance: {self.balance}\n")

    def create_document(self, action, amount):
        doc_number = f"{self.account_number}_Doc{User.document_counter}"
        User.document_counter += 1
        doc = Document(self.mfo_number, self.bank_name, self.adress, self.owner_name, doc_number, action, amount)
        self.documents[doc_number] = doc
        return doc

    def deposit(self, amount):
        self.balance += amount
        print(f"To {self.account_number} add {amount}\n"
              f"Balance: {self.balance}")
        doc = self.create_document("Deposit", amount)
        print(f"Document created: {doc.number_doc}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"From {self.account_number} removed {amount}\n"
                  f"Balance: {self.balance}")
            doc = self.create_document("Withdraw", amount)
            print(f"Document created: {doc.number_doc}")
        else:
            print("Insufficient funds.")

    def transfer(self, target_account, amount):
        if amount <= self.balance:
            self.withdraw(amount)
            target_account.deposit(amount)
            doc = self.create_document("Transfer", amount)
            print(f"Document created: {doc.number_doc}")


class Document:
    def __init__(self, mfo_number, bank_name, adress, owner_name, number_doc, action, amount):
        self.mfo_number = mfo_number
        self.bank_name = bank_name
        self.adress = adress
        self.owner_name = owner_name
        self.number_doc = number_doc
        self.action = action
        self.amount = amount

    def display_info(self):
        return (f"Document info: {self.number_doc}\n"
                f"Owner: {self.owner_name}\n"
                f"Bank: {self.bank_name}\n"
                f"Action: {self.action}\n"
                f"Amount: {self.amount}\n")


directory1 = Dictor("NBU", "134256")
directory2 = Dictor("Private dictor", "162871")
bank1 = Bank("NBU", "134256", "Mono", "Kyiv")
bank2 = Bank("Private dictor", "162871", "Privat-Bank", "Frankivsk")
user1 = User("NBU", "134256", "Mono", "Kyiv", "Alice", "16213", 1000)
user2 = User("Private dictor", "162871", "Privat-Bank", "Frankivsk", "Jon", "15911", 1000)


while True:
    print("Menu\n"
          "1. Dictor info\n"
          "2. Bank info\n"
          "3. User info\n"
          "4. Deposit\n"
          "5. Withdraw\n"
          "6. Transfer\n"
          "7. Document\n"
          "8. Exit")
    choice = input("Enter number: ")
    if choice == "1":
        print([dictor.name_dictor for dictor in Dictor.directors])
        question = input("Choice Dictor(number in dict): ")
        if question == "1":
            print(directory1.display_info())
        elif question == "2":
            print(directory2.display_info())
        else:
            print("Unknown Dictor")
    elif choice == "2":
        print([bank.bank_name for bank in Bank.banks])
        question1 = input("Choice Bank(number in dict): ")
        if question1 == "1":
            print(bank1.display_info())
        elif question1 == "2":
            print(bank2.display_info())
        else:
            print("Unknown Bank")
    elif choice == "3":
        print(f"{User.users}")
        question2 = input("Choice user: ")
        if question2 == "1":
            print(user1.display_info())
        elif question2 == "2":
            print(user2.display_info())
        else:
            print("Unknown user")
    elif choice == "4":
        print(f"{User.users}")
        question3 = input("Choice account: ")
        amount_quest = int(input("Enter amount to deposit: "))
        if question3 == "1":
            user1.deposit(amount_quest)
            print("Deposit done!")
        elif question3 == "2":
            user2.deposit(amount_quest)
            print("Deposit done!")
        else:
            print(f"Unknown user to deposit {amount_quest}$")
    elif choice == "5":
        print(f"{User.users}")
        question3 = input("Choice account: ")
        amount_quest = int(input("Enter amount to withdraw: "))
        if question3 == "1":
            user1.withdraw(amount_quest)
            print("Withdraw done!")
        elif question3 == "2":
            user2.withdraw(amount_quest)
            print("Withdraw done!")
        else:
            print(f"Unknown user to withdraw {amount_quest}$")
    elif choice == "6":
        amount_quest1 = 0
        print(f"{User.users}")
        question4 = input("Choose user: ")
        target = input("Choose target user")
        if question4 == "1" and target == "2":
            amount_quest1 = int(input("Choose amount: "))
            user1.transfer(user2, amount_quest1)
        elif question4 == "2" and target == "1":
            amount_quest1 = int(input("Choose amount: "))
            user2.transfer(user1, amount_quest1)
        else:
            print("Incorrect data!")
    elif choice == "7":
        print(f"{User.users}")
        question5 = input("Choose user: ")
        if question5 == "1":
            for doc in user1.documents.values():
                print(doc.display_info())
        elif question5 == "2":
            for doc in user2.documents.values():
                print(doc.display_info())
    elif choice == "8":
        print("Thanks for using. Goodbye!")
        break
    else:
        print("Unknown command. Try again")
