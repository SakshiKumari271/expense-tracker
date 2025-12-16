# Expense Tracker (CLI)

expenses = []
categories = set()
expense_id = 1

print("💰 Expense Tracker Started")

while True:
    print("\nChoose an option:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Spent")
    print("4. Exit")
    print("5. Filter Expenses (amount wise)")
    print("6. Category-wise Total")

    choice = input("Enter choice (1-6): ")

    match choice:

        case "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ").title()
            description = input("Enter description: ")

            categories.add(category)

            expense = (expense_id, amount, category, description)
            expenses.append(expense)
            expense_id += 1

            print("✅ Expense added successfully!")

        case "2":
            if not expenses:
                print("No expenses yet.")
            else:
                print("\n--- All Expenses ---")
                for exp in expenses:
                    print(f"ID:{exp[0]} | ₹{exp[1]} | {exp[2]} | {exp[3]}")

        case "3":
            total = 0
            for exp in expenses:
                total += exp[1]
            print(f"💰 Total Spent: ₹{total}")

        case "5":
            limit = float(input("Show expenses above amount: "))
            filtered_expenses = [exp for exp in expenses if exp[1] > limit]

            if not filtered_expenses:
                print("No expenses found above this amount.")
            else:
                print("\n--- Filtered Expenses ---")
                for exp in filtered_expenses:
                    print(f"ID:{exp[0]} | ₹{exp[1]} | {exp[2]} | {exp[3]}")

        case "6":
            if not expenses:
                print("No expenses to analyze.")
            else:
                category_totals = {}

                for exp in expenses:
                    category = exp[2]
                    amount = exp[1]

                    if category in category_totals:
                        category_totals[category] += amount
                    else:
                        category_totals[category] = amount

                print("\n--- Category-wise Total ---")
                for cat, total in category_totals.items():
                    print(f"{cat} → ₹{total}")

        case "4":
            print("👋 Exiting Expense Tracker")
            break

        case _:
            print("❌ Invalid option, try again")
