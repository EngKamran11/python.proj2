# ============================================
# Project 2: Expense Tracker
# Developed By: Kamran Ali
# Description:
# This program records user expenses,
# calculates the total expense,
# average expense,
# highest expense,
# and lowest expense.
# ============================================

def display_menu():
    print("\n" + "=" * 45)
    print("           EXPENSE TRACKER SYSTEM")
    print("=" * 45)
    print("Enter your expenses one by one.")
    print("Enter 0 to finish.")
    print("=" * 45)


def get_expenses():
    expenses = []
    total = 0

    while True:

        try:
            expense = float(input("Enter Expense (0 to stop): Rs. "))

            if expense == 0:
                break

            if expense < 0:
                print("Expense cannot be negative.")
                continue

            expenses.append(expense)
            total += expense

        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    return expenses, total


def show_report(expenses, total):

    print("\n")
    print("=" * 45)
    print("            EXPENSE REPORT")
    print("=" * 45)

    if len(expenses) == 0:
        print("No expenses entered.")
        return

    print(f"Number of Expenses : {len(expenses)}")
    print(f"Total Expense      : Rs. {total:.2f}")
    print(f"Average Expense    : Rs. {total/len(expenses):.2f}")
    print(f"Highest Expense    : Rs. {max(expenses):.2f}")
    print(f"Lowest Expense     : Rs. {min(expenses):.2f}")

    print("\nExpense List")

    for i, value in enumerate(expenses, start=1):
        print(f"{i}. Rs. {value:.2f}")

    print("=" * 45)
    print("Thank You!")
    print("=" * 45)


def main():

    display_menu()

    expenses, total = get_expenses()

    show_report(expenses, total)


main()