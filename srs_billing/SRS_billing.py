class user:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email


class plans:
    def __init__(self, p_id, p_name, p_price):
        self.p_id = p_id
        self.p_name = p_name
        self.p_price = p_price


class subscriptions:
    def __init__(self, subs_id, user_id, plan_id, start_date, end_date, status):
        self.subs_id = subs_id
        self.user_id = user_id
        self.plan_id = plan_id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status


class coupons:
    def __init__(self, invoice_id, amount, status, retry_count):
        self.invoice_id = invoice_id
        self.amount = amount
        self.status = status
        self.retry_count = retry_count


class invoice:
    def __init__(self, invoice_id, user_id, amount, invoice_date, status):
        self.invoice_id = invoice_id
        self.user_id = user_id
        self.amount = amount
        self.invoice_date = invoice_date
        self.status = status


class payment:
    def __init__(self, invoice_id, amount, status, retry_count):
        self.invoice_id = invoice_id
        self.amount = amount
        self.status = status
        self.retry_count = retry_count


AVAILABLE_PLANS = {
    "FREE": 0,
    "PRO": 5,
    "BUSINESS": 10
}


def subscribe(subs_id, user_id, plan_id, start_date, end_date):
    # Lookup the price based on the selected plan
    price = AVAILABLE_PLANS.get(plan_id.upper(), 0)

    sub = subscriptions(subs_id, user_id, plan_id.upper(), start_date, end_date, "active")
    inv = invoice(f"INV-{subs_id}", user_id, float(price), start_date, "unpaid")
    pay = payment(inv.invoice_id, float(price), "pending", 0)

    print(f"User {user_id} subscribed to {plan_id.upper()} (${price})!")
    return sub, inv, pay


def upgrade_subscription(subs_id, new_plan_id):
    price = AVAILABLE_PLANS.get(new_plan_id.upper(), 0)
    print(f"Subscription {subs_id} upgraded to {new_plan_id.upper()} (${price})!")


def generate_invoice(user_id, amount, invoice_date):
    inv_id = f"INV-{user_id}"
    print(f"Invoice {inv_id} generated for ${amount}")
    return invoice(inv_id, user_id, amount, invoice_date, "unpaid")


def process_payment(inv_obj):
    pay = payment(inv_obj.invoice_id, inv_obj.amount, "success", 0)
    inv_obj.status = "paid"
    print(f"Payment for {inv_obj.invoice_id} successful!")
    return pay


def show_dashboard(user_obj, sub_obj, inv_list):
    while True:
        print("\n" + "=" * 30)
        print("      BILLING DASHBOARD      ")
        print("=" * 30)
        print(f"User: {user_obj.name} (ID: {user_obj.id})")
        print(f"Plan: {sub_obj.plan_id}")
        print(f"Status: {sub_obj.status}")
        print("-" * 30)

        print("\nOPTIONS: [1] Upgrade Plan  [2] Process Payment  [3] Exit")
        choice = input("Select an option: ")

        if choice == "1":
            new_plan = input("Enter new plan ID: ")
            upgrade_subscription(sub_obj.subs_id, new_plan)
            sub_obj.plan_id = new_plan
        elif choice == "2":
            for inv in inv_list:
                if inv.status == "unpaid":
                    process_payment(inv)
                    break
            else:
                print("No unpaid invoices found.")
        elif choice == "3":
            print("Exiting dashboard...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    test_user = user("user_001", "Kishjan", "alice@gmail.com")

    test_sub, first_inv, first_pay = subscribe("SUB_001", test_user.id, "FREE", "2026-04-06", "2026-05-06")

    second_inv = generate_invoice(test_user.id, 5.0, "2026-04-10")

    show_dashboard(test_user, test_sub, [first_inv, second_inv])

