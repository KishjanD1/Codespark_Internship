import itertools

suspects = ['Alice', 'Bob', 'Charlie']
locations = ['Library', 'Kitchen']
weapons = ['Wrench', 'Poison']

# Generate every combination
possibilities = list(itertools.product(suspects, locations, weapons))


def solve_mystery():
    for killer, location, weapon in possibilities:
        # 1. If it's the Kitchen, it's NOT Alice.
        clue_a = (location != 'Kitchen') or (killer != 'Alice')

        # 2. If the weapon is a Wrench, Bob is NOT the killer.
        clue_b = (weapon != 'Wrench') or (killer != 'Bob')

        # 3. Charlie was in the Kitchen, and the Kitchen person is the killer.
        clue_c = (killer == 'Charlie' and location == 'Kitchen')

        # 4. The Wrench WAS the weapon used.
        clue_d = (weapon == 'Wrench')

        # If all clues are True at the same time:
        if clue_a and clue_b and clue_c and clue_d:
            print("🕵️ CASE CRACKED!")
            print(f"Killer: {killer} | Scene: {location} | Weapon: {weapon}")
            return

    print("No solution found. Check the logic again!")


solve_mystery()