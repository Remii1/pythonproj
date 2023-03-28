class Employee:
    def task(self):
        print("Employs")


class Manager(Employee):
    def role(self):
        print("Manages")


class Chef(Manager):
    def info(self):
        print("Works at a hotel")


c = Chef()
c.role()
c.info()
c.task()
