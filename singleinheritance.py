class Animal:
    age = 10

    def speak(self):
        print("speaking")


class Dog(Animal):
    def eat(self):
        print("eating")


d = Dog()
d.eat()
d.speak()
name = d.age
print(name)

print(issubclass(Dog, Animal))
print(isinstance(d, Dog))
