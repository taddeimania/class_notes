
class Person:

    def __init__(self, name):
        self.name = name


class Bike:

    def __init__(self, speeds, owner):
        self.speed = speeds
        self.owner = owner
        self.color = ["grey"]
        self.__layers = 1

    def set_color(self, new_color):
        self.__layers += 1
        self.color.append(new_color)

    def get_colors(self):
        return sorted(self.color)

    def get_layers(self):
        return self.__layers


joel = Person("Joel")
sean = Person("Sean")

bike = Bike(100, joel)
seans_bike = Bike(18, sean)

print("OWNERS==============")
print(bike.owner.name)
print(seans_bike.owner.name)

print(bike)
print("color before we change it")
print(bike.get_colors())
print(bike.get_layers())

print("color after we change it")
bike.set_color("purple")
print(bike.get_colors())
print(bike.get_layers())

print("color of seans bike")
print(seans_bike.get_colors())

for x in range(100):
    bike.set_color("red")

print(bike.get_layers())
print(seans_bike.get_layers())
