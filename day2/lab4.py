# N students take K apples and distribute them among each other evenly. The remaining

# (the indivisible) part remains in the basket. How many apples will each single student

# get? How many apples will remain in the basket? The program reads the numbers N and

# K. It should print the two answers for the questions above.
n = int(input("enter the number of apple"))
s = int(input("enter the number of student"))
number_of_apple= n//s
basket= n%s
print("each student gets",number_of_apple)
print("there are",basket,"remaining")