import round
import csv

print("Welcome to Colonel Blotto")

list_one = [0]
list_two = [0]

while True:
    try:
        first_combo = input("\nPlease enter player one's combination: Ex) 20 20 20 20 20 0 0 0 0 0 \n")
        list_one = list(map(int, first_combo.split()))
        if sum(list_one) != 100:
            print("\nEnter an army with 100 soldiers (with integers spaced apart)")
        elif len(list_one) != 10:
            print("10 integers were expected...")
        else:
            break
    except ValueError:
        print("Bad input...follow the example")


while True:
    try:
        second_combo = input("\nPlease enter player two's combo: \n")
        list_two = list(map(int, second_combo.split()))
        if sum(list_two) != 100:
            print("Please enter an army with 100 soldiers (with integers spaced apart)")
        else:
            break
    except ValueError:
        print("Bad input...follow the example")

result = round.blottoFight(list_one, list_two).evaluate()

with open('armies.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(result[0])

print("\nThe winning combination is {} with a score of: {}.".format(result[0], result[1]))

