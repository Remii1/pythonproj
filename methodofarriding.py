class Animal:
    def speak(self):
        print("speaking")


class Dog(Animal):
    def speak(self):
        print("barking")


class Bee(Dog):
    def speak(self):
        print("buzzing")


b = Bee()
b.speak()
d = Dog()
d.speak()
