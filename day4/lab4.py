# Write a program to print absolute value of a number entered by user. E.g.-

# INPUT: 1        OUTPUT: 1

# INPUT: -1        OUTPUT: 1
number = int(input("Enter a number \t"))
absolute = 0
if number <0:
    absolute = number * (-1)
else:
    absolute =number
print("The absolute value is ", absolute)