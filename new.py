class Restaurant:

    food = "Chicken"
    meat = "Pork"
    def pick(self):
        print("I love eating")

    def two(self):
        print("I love cooking")


class Eatery(Restaurant):
    def myeatery(self):
        print("I love baking")

ea = Eatery()
name = ea.meat
print(name)
name = ea.food
print(name)
ea.two()
ea.pick()
ea.myeatery()
