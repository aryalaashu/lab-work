a=input("Enter a word: ")
print(a[::-1])
j=len(a)-1
while j>=0:
    print(a[j],end="")
    j=j-1