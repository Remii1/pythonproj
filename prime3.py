import math

# Accept user input as a float number
num = float(input("Enter a number: "))

# Convert the float number to an integer
num = int(num)


if num <= 1:
    print(num, "is not a prime number")
elif num > 1:
    # Check for factors up to the square root of the number
    for i in range(2, int(math.sqrt(num))+1):
        if (num % i) == 0:
            print(num, "is not a prime number")

            break

        else:
            print(num, "is a prime number")

