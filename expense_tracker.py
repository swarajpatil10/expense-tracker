from datetime import date

class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = str(date.today())

    def display(self):
        print(f"{self.date} | {self.category} | ₹{self.amount} | {self.description}")

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        print(f"Expense added successfully.")

    def view_all(self):
        if len(self.expenses) == 0:
            print("No expenses yet.")
        else:
            print("\n--- All Expenses ---")
            for i, expense in enumerate(self.expenses):
                print(f"{i+1}. ", end="")
                expense.display()

    def view_total(self):
        total = sum(e.amount for e in self.expenses)
        print(f"\nTotal spent: ₹{total}")

    def delete_expense(self, index):
        if index < 1 or index > len(self.expenses):
            print("Invalid number.")
        else:
            removed = self.expenses.pop(index - 1)
            print(f"Deleted: {removed.category} ₹{removed.amount}")

    def view_by_category(self):
        if len(self.expenses) == 0:
            print("No expenses yet.")
        else:
            summary = {}
            for expense in self.expenses:
                if expense.category in summary:
                    summary[expense.category] += expense.amount
                else:
                    summary[expense.category] = expense.amount
            print("\n--- Category Summary ---")
            for category, total in summary.items():
                print(f"{category}: ₹{total}")

    def save_to_file(self, filename="expenses.txt"):
        with open(filename, "w") as f:
            for expense in self.expenses:
                f.write(f"{expense.date},{expense.category},{expense.amount},{expense.description}\n")
        print("Expenses saved.")

    def load_from_file(self, filename="expenses.txt"):
        try:
            with open(filename, "r") as f:
                for line in f:
                    parts = line.strip().split(",")
                    expense = Expense(float(parts[2]), parts[1], parts[3])
                    expense.date = parts[0]
                    self.expenses.append(expense)
            print("Expenses loaded.")
        except FileNotFoundError:
            print("No saved data found. Starting fresh.")


tracker = ExpenseTracker()
tracker.load_from_file()

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add expense")
    print("2. View all")
    print("3. View total")
    print("4. View by category")
    print("5. Delete expense")
    print("6. Save and exit")

    choice = input("Choose option: ")

    if choice == "1":
        amount = float(input("Amount: "))
        category = input("Category: ")
        description = input("Description: ")
        tracker.add_expense(amount, category, description)
    elif choice == "2":
        tracker.view_all()
    elif choice == "3":
        tracker.view_total()
    elif choice == "4":
        tracker.view_by_category()
    elif choice == "5":
        tracker.view_all()
        index = int(input("Enter number to delete: "))
        tracker.delete_expense(index)
    elif choice == "6":
        tracker.save_to_file()
        break
    else:
        print("Invalid option.")