# Given the integer N - the number of minutes that is passed since midnight - how many

# hours and minutes are displayed on the 24h digital clock?

# The program should print two numbers: the number of hours (between 0 and 23) and the

# number of minutes (between 0 and 59).

# For example, if N = 150, then 150 minutes have passed since midnight - i.e. now is 2:30

# am. So, the program should print 2 30.
n = int(input("enter minute passed"))
hours = n//60
hour_remns = n%60
#minute = hour_rem//60
print("the given minute takes",hours,":",hour_remns)
