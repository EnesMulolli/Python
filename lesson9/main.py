# class Animal:
#     def sound(self):
#         print("Some animal voices")
#
#
# class Dog(Animal):
#     def sound(self):
#         print("woof woof")
#
#
# class Cat(Animal):
#     def sound(self):
#         print("Meow meow")
#
#
# animal = Animal()
# animal.sound()
#
# dog = Dog()
# dog.sound()
#
#
# cat = Cat()
# cat.sound()
#


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


    def display_info(self):
        print(f"Make : {self.make}, Model: {self.model}, year: {self.year}")

class Car(Vehicle):
    def __init__(self, make, model, year, body_style):
        super().__init__(make, model, year)
        self.body_style = body_style


class ElectricCar(Car):
    def __init__(self, make, model, year, body_style, batery_capacity):
        super().__init__(make, model, year, body_style)
        self.batery_capacity = batery_capacity

    def charge(self):
        print("Charging the batery of electric car!")


tesla = ElectricCar("Tesla", "Cybertruck", 2024, "SQUARE", 100kMAH)
tesla.display_info()
print("Body style:", tesla.body_style)
print("batery capacity:", tesla.batery_capacity)
tesla.charge()



string_length = len("Hello world")
list_length = len([1,2,3,4,5,6,7,8])
tuple_length = len((10,20,30))

print(string_length)
print(list_length)
print(tuple_length)


