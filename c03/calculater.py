
from calcfunction import *	
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

add = addition(num1, num2) #function call
sub = subtraction(num1, num2) #function call

print(num1, "+", num2, "=", add)
print(num1, "-", num2, "=", sub)
