a=int(input("Enter a number of rows: "))
def star(a):
    for i in range(a+1):
        for j in range(i):
            print("*",end=" ")
        print()
star(a)