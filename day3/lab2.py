# WAP which accepts marks of four subjects and display total marks, percentage and grade. 
# Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail 
math= int(input("enter marks in math"))
english = int(input("enter marks in english"))
science = int(input("enter marks in science"))
computer = int(input("enter marks in computer"))
per = ((math+english+science+computer)/400)*100
print("the percentage is",per,"%")

if per>90:
    print("congratulation you have scored A+")
elif per>=80 and per<90:
    print("you have scored A")
elif per>=60 and per<80:
    print("yoou have scored B")
elif per>=40 and per<60:
    print("you have scored C")
elif per<40:
    print("sorry you have failed your examination")