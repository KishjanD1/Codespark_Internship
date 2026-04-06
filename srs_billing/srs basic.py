my_user = {
    "name": "Alice",
    "plan": "Free",
    "days_subscribed": 0,
    "money_spent": 0,
}

plans = {
    "Free": 0,
    "Pro": 10,
    "Enterprise": 30
}


def show_dashboard():
    print("      DASHBOARD      ")
    print(f"User: {my_user['name']}")
    print(f"Plan: {my_user['plan']}")
    print(f"Spent: ${my_user['money_spent']}")

def upgrade():
    print("\nAvailable Plans:")
    for name, price in plans.items():
        print(f"- {name}: ${price}")

    new_choice = input("\nWhich plan do you want? ").capitalize()

    if new_choice in plans:
        my_user["plan"] = new_choice
        cost = plans[new_choice]
        my_user["money_spent"] += cost
        print(f"Success! You are now on the {new_choice} plan.")
    else:
        print("Sorry, that plan doesn't exist.")


print(f"Welcome {my_user['name']}!")

while True:
    show_dashboard()
    print("\nOptions: [1] Upgrade Plan  [2] Exit")
    choice = input("Select an option: ")

    if choice == "1":
        upgrade()
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")