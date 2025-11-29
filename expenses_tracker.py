import csv
from datetime import datetime

EXPENSE_FILE = 'expenses.csv'

def initialize_expense_file():
    """Ensures the expense file exists with the correct header."""
    try:
        with open(EXPENSE_FILE, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])
    except FileExistsError:
        pass # File already exists

def add_expense(category, amount, description):
    """Adds a new expense to the CSV file."""
    initialize_expense_file() # Ensure file is ready
    try:
        amount = float(amount)
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(EXPENSE_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("Expense added successfully!")

def view_expenses():
    """Displays all recorded expenses."""
    initialize_expense_file() # Ensure file is ready
    try:
        with open(EXPENSE_FILE, 'r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader) # Skip header
            print(f"{header[0]:<20} {header[1]:<15} {header[2]:<10} {header[3]:<30}")
            print("-" * 75)
            for row in reader:
                print(f"{row[0]:<20} {row[1]:<15} {float(row[2]):<10.2f} {row[3]:<30}")
            if not any(True for _ in reader): # Check if there are no expenses after printing header
                print("No expenses recorded yet.")
    except FileNotFoundError:
        print("No expenses recorded yet.")

def summarize_expenses_by_category():
    """Calculates and displays total expenses per category."""
    initialize_expense_file() # Ensure file is ready
    category_totals = {}
    try:
        with open(EXPENSE_FILE, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader) # Skip header
            for row in reader:
                try:
                    category = row[1]
                    amount = float(row[2])
                    category_totals[category] = category_totals.get(category, 0) + amount
                except (ValueError, IndexError):
                    print(f"Skipping malformed row: {row}")
                    continue
        if not category_totals:
            print("No expenses to summarize.")
            return

        print("\nExpense Summary by Category:")
        for category, total in sorted(category_totals.items()):
            print(f"- {category}: ${total:.2f}")
    except FileNotFoundError:
        print("No expenses recorded yet to summarize.")

def main_menu():
    """Displays the main menu and handles user input."""
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summarize by Category")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter category (e.g., Food, Transport): ")
            amount = input("Enter amount: ")
            description = input("Enter description (optional): ")
            add_expense(category, amount, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            summarize_expenses_by_category()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()