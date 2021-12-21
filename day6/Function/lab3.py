limit=int(input("Enter the limit: "))
def showNumbers(limit):
    for i in range(limit+1):
        if i%2==0:
            print(i, " Even")
        else:
            print(i, " Odd")
showNumbers(limit)