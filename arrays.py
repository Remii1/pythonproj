furniture = ["table", "chair", "stool"]

for x in furniture:

    print(x)

#adding an item in an array
furniture.append("bed")
print(furniture)

#removing an item in an array
furniture.remove("stool")
print(furniture)

#length of an array
x = len(furniture)
print(x)