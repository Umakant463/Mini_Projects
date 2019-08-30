import math
print ("========== SIMPLE CALCULATOR ===========  \n \n   ")
print ("--- Enter two numbers  ---- \n  ")
num1 = int(input('Enter first number : '))
num2 = int(input('Enter second number : '))

# Addition of numbers
def add(a,b):
	return (a + b)

#First checks the largest among two numbers and then subtract the smaller from larger.	
def sub(a,b):
	if a > b:
		return (a - b)
	elif b > a:
		return (b - a)
#Given numbers are same it will return zero.
	elif a == b:
		return (0)
#Multiplication of numbers		
def mul(a,b):
	return (a * b)
#Divides the Given numbers.	
def div(a,b):
	return (a / b)
#Gives the remainder after dividing Numbers.
def rem(a,b):
	return (a % b)

print ("Select the Operation you want to perform : ")
print (" 1. Addtion \n 2. Subtraction \n 3. Multiplication \n 4. Divide \n 5. Check Remainder \n")
input = int(input("Enter your input : "))
input -= 1

list = [add(num1,num2) , sub(num1,num2), mul(num1,num2), div(num1,num2), rem(num1,num2)]

u_choice = list[input]

print ("Answer :  ",u_choice)
print("==========  THANK YOU FOR USING SIMPLE CALCULATOR  ===============")
