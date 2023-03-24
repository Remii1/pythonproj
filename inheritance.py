class Animal:
    alive = True

    def sleep(self):
        print("It is sleeping")

    def eat(self):
        print("It is eating")


class Fish(Animal):
    def myfish(self):
        print("This is a fish")


fi = Fish()
fi.sleep()
fi.eat()
fi = Fish()
name = fi.alive
print(name)
fi.myfish
