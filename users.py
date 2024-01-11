class User:

    def __init__(self, first_name, last_name, age, email, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = login_attempts

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts


    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'\nОбнулення значення кількості входів\n')

    def describe_user(self):
        print(f"Name = {self.first_name}, Last Name = {self.last_name}"
              f"\nAge = {self.age}"
              f"\nEmail = {self.email}"
              f"\nКористувач ввійшов {self.login_attempts}")

    def greeting_user(self):
        print(f"\nHello {self.first_name} {self.last_name}!")


class Admin(User):

    def __init__(self, first_name, last_name, age, email, login_attempts=0, privileges=None):
        super().__init__(first_name, last_name, age, email, login_attempts=0)
        if privileges is None:
            privileges = []
        self.privileges = privileges


class Privileges:

    def __init__(self, privileges=None):
        if privileges is None:
            privileges = []
        self.privileges = privileges

    def show_privileges(self):
        print("\nAdmin privileges: ")
        for privileg in self.privileges:
            print(f" - {privileg}")

