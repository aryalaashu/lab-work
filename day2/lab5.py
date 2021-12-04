A = int(input("enter number of students in first class"))
B = int(input("enter number of students in second class"))
C = int(input("enter number of students in third class"))
if A%2==0:
    D = A/2
else:
    D =(A+1)/2
if B%2==0:
    E = B/2
else:
    E =(B+1)/2
if C%2==0:
    F = C/2
else:
    F =(C+1)/2
G= D+E+F
print("number of bench in first class","=",D)
print("number of bench in second class","=",E)
print("number of bench in third classs","=",F)
print("Total no. of bench required","=",G)
