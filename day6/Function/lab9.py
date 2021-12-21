a=input("Enter a string: ")
b=a[::-1]
def pal(a,b):
    if a==b:
        print("Palindrome")
    else:
        print("Not palindrome")
pal(a,b)