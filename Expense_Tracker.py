from tkinter import *
from tkinter import ttk
import tkinter


Window = Tk()
style = ttk.Style(Window)
style.configure('Treeview.Heading', background="green3")

Window.tk.call("source","forest-dark.tcl")
style.theme_use("forest-dark")
Window.minsize(1000,600)
Window.title("Expense Tracker")

frame = ttk.Frame(Window)
frame.pack()

widgets_frame = ttk.LabelFrame(frame,text="Insert Row")
widgets_frame.grid(row=0,column = 0)


name_entry = ttk.Entry(widgets_frame)
name_entry.grid(row = 0,column = 0, sticky="ew")

treeFrame = ttk.Frame(frame)
treeFrame.grid(row=0,column = 1, pady = 10)
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill = "y")

treeview = ttk.Treeview(treeFrame,column=("c1","c2","c3","c4"),show= "headings",height= 8)


treeview.column("# 1",anchor=CENTER)
treeview.heading("# 1", text= "Date")
treeview.column("# 2",anchor=CENTER)
treeview.heading("# 2", text= "Description")
treeview.column("# 3",anchor=CENTER)
treeview.heading("# 3", text= "Amount")
treeview.column("# 4",anchor=CENTER)
treeview.heading("# 4", text= "Action")



treeview.pack()
treeScroll.config(command = treeview.yview)


class Expense:
    def __init__(self, date,description, amount):
        self.date = date
        self.description = description
        self.amount = amount
     

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)
        treeview.insert("", tkinter.END, text=f"Expense Name: {expense.description}", values = (expense.date,expense.description,expense.amount))

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
        print("\nExpense tracker menu")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Total Expenses")
        print("5. Exit")

        choice = input("Enter your choice 1-5: ").strip()

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter the description : ")
            amount = float(input("Enter the amount: "))
            expense = Expense(date, description, amount)
            tracker.add_expense(expense)
            print("Expense added Successfully.")
        elif choice == "2":
            index = int(input("Enter the expense index to remove: ")) - 1
            tracker.remove_expense(index)
        elif choice == "3":
            tracker.view_expenses()
        elif choice == "4":
            tracker.total_expenses()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


    


Window.mainloop()