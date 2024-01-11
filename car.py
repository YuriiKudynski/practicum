class Car:

    def __init__(self, mark, model, year, speed=0):
        self.mark = mark
        self.model = model
        self.year = year
        self.speed = speed

    def __str__(self):
        return f'Car = {self.mark} {self.model}\nYear = {self.year}'

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5
        if self.speed <= 0:
            self.speed = 0
        if self.speed == 0:
            print("Car stoped")

    def get_speed(self):
        print(f"Speed is = {self.speed}")


car1 = Car("Audi", "A4", 2006)
print(car1)

print("Car accelerate")
for _ in range(5):
    car1.accelerate()
    car1.get_speed()

print("Car slow down")
for _ in range(5):
    car1.brake()
    car1.get_speed()


