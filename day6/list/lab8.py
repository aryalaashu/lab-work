# . Write a Python program to print a specified list after removing the 0th, 4th and 5th 
# elements 
list = [2,3,4,5,6,78,9,2]
list = [x for (i,x) in enumerate(list) if i not in (0,4,5)]
print(list)

for i in list:
    if i!=[0] and i!=[4] and i!=[5]:
        print(i)