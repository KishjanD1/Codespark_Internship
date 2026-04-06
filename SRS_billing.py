class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email


class Plan:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Subscription:
    def __init__(self, user_id, plan_id, start_day):
        self.user_id = user_id
        self.plan_id = plan_id
        self.start_day = start_day
        self.next_billing_day = start_day + 30
        self.status = "Active"


current_day = 1

plans = {
    "Free": Plan("free", "Free", 0),
    "Pro": Plan("pro", "Pro", 10),
    "Enterprise": Plan("enterprise", "Enterprise", 30)
}

my_user = User(1, "Alice", "alice@example.com")
my_subscription = None
my_money_spent = 0


def show_dashboard():
    print("      DASHBOARD     ")
    print(f"User: {my_user.name}")
    print(f"Current Day: {current_day}")

    if my_subscription:
        print(f"Plan: {my_subscription.plan_id.capitalize()}")
        print(f"Status: {my_subscription.status}")
        print(f"Next Bill Day: {my_subscription.next_billing_day}")
    else:
        print("Plan: None (No subscription)")

    print(f"Total Spent: ${my_money_spent}")


def upgrade():
    global my_subscription, my_money_spent

    print("\nAvailable Plans:")
    for key, p in plans.items():
        print(f"- {p.name}: ${p.price}")

    choice = input("\nWhich plan do you want? ").capitalize()

    if choice in plans:
        selected_plan = plans[choice]

        if not my_subscription:
            my_subscription = Subscription(my_user.id, selected_plan.id, current_day)
        else:
            my_subscription.plan_id = selected_plan.id

        my_money_spent += selected_plan.price
        print(f"Success! You are now on the {selected_plan.name} plan.")
    else:
        print("Plan not found.")


def advance_time():
    global current_day
    days_to_add = int(input("How many days to advance? "))
    current_day += days_to_add
    print(f"Time advanced by {days_to_add} days. It is now Day {current_day}.")


print(f"Welcome {my_user.name}!")

while True:
    show_dashboard()
    print("\nOptions: 1 Upgrade  2 Advance Time  3 Exit")
    choice = input("Select an option: ")

    if choice == "1":
        upgrade()
    elif choice == "2":
        advance_time()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")