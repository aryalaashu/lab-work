#  Given a n-digit number. Find the sum of its digits.
number = int(input("enter a number")) 
sumofdigits = 0
for i in str(number):
    sumofdigits += int(i)
print(sumofdigits)
