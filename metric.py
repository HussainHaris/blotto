import round
import csv

allArmies = []

newArmy = []

with open("armies.csv") as file:
    for i, line in enumerate(file):
        parsed_list = line.split()[0].split(",")

        combo = list(map(int, parsed_list))
        allArmies.append(combo)

while True:
    try:
        print("\nCurrent winner: {}".format(allArmies[-1]))
        newArmy = input("\nPlease enter a combination: Ex) 20 20 20 20 20 0 0 0 0 0 \n")
        newArmy = list(map(int, newArmy.split()))
        if sum(newArmy) != 100:
            print("\nEnter an army with 100 soldiers (with integers spaced apart)")
            print("\nNeed {} more soldiers".format(100 - sum(newArmy)))
        elif len(newArmy) != 10:
            print("10 integers were expected...")
        else:
            break
    except ValueError:
        print("Bad input...follow the example")

win_all = True
for army in allArmies:
    result = round.round(army, newArmy).evaluate()
    if result[0] != newArmy:
        win_all = False
        print("LOST TO:\n {}".format(result[0]))

if win_all:
    with open('armies.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(newArmy)
    print("\nWON! {}".format(newArmy))
else:
    print("\n :(")


