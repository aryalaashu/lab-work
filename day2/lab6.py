# You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each

# of the 10 stops on the way. How long will the bus journey take? Alternatively, you could

# run to university. You jog the first mile at 7mph; then run the next two at15mph; before

# jogging the last at 7mph again. Will this be quicker or slower than the bus?
bus = (4/(25/60)+2*10)
print(" minutes for bus","=",bus)
jogging = (1/(7/60)+2/(15/60)+1/(7/60))
print(" minutes for jogging","=",jogging)
if bus>jogging:
    print("bus is quicker than jogging")
else:
    print("Jogging is quicker than bus")
