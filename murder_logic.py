import itertools

suspects = ['Alice', 'Bob', 'Charlie']
locations = ['Library', 'Kitchen']
weapons = ['Wrench', 'Poison']

possibilities = list(itertools.product(suspects, locations, weapons))


def solve_mystery():
    for killer, location, weapon in possibilities:
        clue_a = (location != 'Kitchen') or (killer != 'Alice')
        clue_b = (weapon != 'Wrench') or (killer != 'Bob')
        clue_c = (killer == 'Charlie' and location == 'Kitchen')
        clue_d = (weapon == 'Wrench')

        if clue_a and clue_b and clue_c and clue_d:
            print("🕵️ CASE CRACKED!")
            print(f"Killer: {killer} | Scene: {location} | Weapon: {weapon}")
            return

    print("No solution found. Check the logic again!")


solve_mystery()