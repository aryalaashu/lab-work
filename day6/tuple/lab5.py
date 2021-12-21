#  Write a Python program to add an item in a tuple
a=("a","b","c")
b=list(a)
b.insert(3,"z")
c=tuple(b)
print(c)