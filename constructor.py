class Employee:
    def __init__(self, firstname, course, age):
         self.firstname = firstname
         self.course = course
         self.age = age

    def info(self):
        print(self.firstname,self.course,self.age)
    def inf(self):
         print(self.course)


e = Employee("Faith","MIT" , "31")
e.info()







