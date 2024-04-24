class Expense:
    def __init__(self, date,description, amount): # type: ignore
        self.date = date
        self.description = description
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

def add_expense(self, expense):
    self.expenses.append(expense)

def remove_expense(self,index):
    if 0 <= index < len(self.expenses):
        del self.expenses[index]
        print("Expense removed successfully.")
    else:
        print("Error, Invalid Input Parameter")

def view_expenses(self):
    if len(self.expenses) == 0:
        print("No expenses found.")
    else:
        print("Expense List:")
        for i, expense in enumerate (self.expenses, start = 1):
            print(f"{i}. Date: {expense.date}, Description: {expense.description}, Amount: ${expense.amount:.2f}")

def total_expenses(self):
    total = sum(expense.amount for expense in self.expenses)
    print(f"Total Expenses: $ {total:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n expense tracker menu")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Total Expenses")
        print("5. Exit")

choice = input("Enter your choice 1-5")

if choice == "1":
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the description : ")
    amount = float(input("Enter the amount: "))
    expense = Expense(date, description, amount)
    tracker.add_expense(expense)
