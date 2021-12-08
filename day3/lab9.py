# Take username and password from user and check it again for the three times whether the user has entered the right
# username and password. If yes then print a message "Logged in Successfully", if not then print invalid credentials
# for consecutive 3 times and if the limit exceeds than print "Attempt finished".

username = str(input("enter your username"))
password = str(input("enter your password"))
for i in range(3):
    username = str(input("enter your username"))
    password = str(input("enter your password"))
    if username ==  "Aashutosh":
        password == "logged in"
        print("Logged in")
    break
else:
    print("Attempt finished")

