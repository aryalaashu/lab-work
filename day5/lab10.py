a=input("Input a string: ")
i=0
j=0
for k in a:
    if k.isdigit():
        i=i+1
    elif k.isalpha():
        j=j+1
    else:
        pass
print("Letters", j)
print("Digits", i)