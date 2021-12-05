# . Given three integers, print the smallest one. (Three integers should be user input) 
a = int(input("enter the number"))
b = int(input("enter the number"))
c = int(input("enter the number"))
if a<b and a<c:
    print("a is the smallest one")
elif b<a and b<c:
    print("b is the smallest one")
else:
    print("c is the smallest one")