#  Given a n-digit number. Find the sum of its digits.
number = int(input("enter a number")) 
sumofdigits = 0
for digit in str(number):
    sumofdigits += int(digit)
print(sumofdigits)