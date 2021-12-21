limit=int(input("Enter a limit: "))
def multiple(limit):
    for i in range(1,limit+1):
        if i%3==0 or i%5==0:
            print(i)
multiple(limit)