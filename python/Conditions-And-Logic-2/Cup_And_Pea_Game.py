# A street magician has brought a classic cup-and-pea trick to the city.
# On a table, three cups are placed in a row. At the start, there is a pea under the first cup.
# The magician performs a number of moves. In each move, two cups are swapped.
# The total number of swaps is given as n.
# Everyone knows that before the trick begins, the pea is under the first cup.
# The magician, knowing your reputation in programming, asks you to write a program
# that determines the final position of the pea after all the swaps are completed.

total = int(input("The number of displacements: "))
places = []
for x in range(total):
    values = list(map(int, input("Enter values: ").split()))
    new_values = [None, None]
    for i in range(2):
        match values[i]:
            case 1:
                new_values[i] = "first"
            case 2:
                new_values[i] = "second"
            case 3:
                new_values[i] = "third"
    places.append(new_values)

second_counter = 0
for place in places:
    second_counter += 1
    print(f"By moving the {place[0]} and {place[1]} place bowls, the peas go under the {place[1]} place bowl.")
    if second_counter == total:
        print(f"Finally, the peas under the bowl are in {place[1]} place.")