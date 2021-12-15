#divisible by 5 and 7
for i in range(1500,2701):
    if i%7==0 and i%5==0:
        print(i)

#user input
a=int(input("Enter a number between 1500 and 2700: "))
if a>=1500 and a<=2700:
    if a%7==0 and a%5==0:
        print("It is divisible by both 5 and 7")
    else:
        print("It is not divisible by both 5 and 7")
else:
    print("It is not between 1500 and 2700")
