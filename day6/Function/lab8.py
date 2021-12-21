a=int(input("Enter a number: "))
if a>1:
    def prime(a):
        c=0
        for i in range(2,a):
            if a%i==0:
                c=c+1
            else:
                pass
        if c>=1:
            print("Composite")
        else:
            print("Prime")
    prime(a)
else:
    print("Not a valid number")