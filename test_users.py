from users import User, Admin, Privileges

person1 = User("Jon", "Travolta", 30, "jon@example.com", )
person1.increment_login_attempts()
person1.increment_login_attempts()
person1.increment_login_attempts()
person1.increment_login_attempts()
person1.describe_user()
person1.greeting_user()
person1.reset_login_attempts()
person1.describe_user()

admin = Admin("Jony", "English", 20, "english@example.com",
              privileges=Privileges(["Allowed to add message", "Allowed to delete users"]))

admin.privileges.show_privileges()

