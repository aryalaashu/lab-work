import random
target_num, guess_num=random.randint(1,100),0
while target_num!=guess_num:
    if target_num>guess_num:
        guess_num=int(input("Number you entered is lower: "))
    else:
        guess_num=int(input("Number you entered is higher: "))
print("Well guessed!")