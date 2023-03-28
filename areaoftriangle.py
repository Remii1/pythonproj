#program that prints out area of triangle
a = 3
b = 5
c= 7

a = float(input("Enter value:"))
b = float(input("Enter value:"))
c = float(input("Enter value:"))


s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))*0.5
print(area)
