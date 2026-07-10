#MinMaxFloats

"""Gathers information about the user.  
Then asks the user for three numbres and finds the minimum of three values."""


name = str(input("What is your name?"))

print("Hi", name, ".  We are going to find the minimum of three numbers.")


number1 = float(input('Enter first integer: '))
number2 = float(input('Enter second integer: '))
number3 = float(input('Enter third integer: '))

minimum = number1  

if number2 < minimum:
    minimum = number2

if number3 < minimum:
    minimum = number3

print('Minimum value is', minimum)


print("The data type of", name, "is", type(name))
print("The data type of", minimum, "is", type(minimum))