class Student:
    firstame = "eMobilis"
    lastname = "Technology"

    def course(self):
        print("I study python")


stu = Student()
stu.course()
name = stu.firstame
print(name)
name = stu.lastname
print(name)


class Employee:
    name = "Faith"
    id = "256"

    def course(self):
        print("I work at eMobilis")

    def hi(self):
        print("My name is Karimi")


em = Employee()
em.course()
name = em.name
print(name)
name = em.id
print(name)
em.hi()





