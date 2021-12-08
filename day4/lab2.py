# Write a Python program to sum three given integers. However, if two or more values are

# equal sum will be zero.
num1 = int(input("enter the number"))
num2 = int(input("enter the number"))
num3 = int(input("enter the number"))

sum= num1+num2+num3

if num1==num2 or num2==num3 or num3==num1:
    print("0")
else:
    print("the sum of given number =",sum )
