choice=input("Convert to celsius/farenheit? (C/F)")
if choice=="C":
    a=int(input("Enter temperature in Farenheit: "))
    b=5/9*(a-32)
    print("Temperatue in celsius: {}".format(b))
elif choice=="F":
    a=int(input("Enter temperature in Celsius: "))
    b=(a*9/5)+32
    print("Temperatue in faranheit: {}".format(b))
else:
    print("Enter C or F only.")