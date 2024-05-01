
from tkinter import *
from tkinter import ttk
import tkinter
from tkcalendar import Calendar


class Expense:
    def __init__(self, date,description, amount):
        self.date = date
        self.description = description
        self.amount = amount
      
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        date = date_entry.get()   
        description = name_entry.get()
        amount = float(amount_entry.get())
        expense = Expense(date, description, amount)
        self.expenses.append(expense)
        treeview.insert("", tkinter.END, text=f"Expense Name: {expense.description}", values = (expense.date,expense.description,expense.amount))
    

    def remove_expense(self,index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
          
            print("Expense removed successfully.")
        else:
            print("Error, Invalid Input Parameter")

   
    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: $ {total:.2f}")

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
widgets_frame.grid(row=0,column = 0, padx = 20, pady = 10)

widgets_frame_2 = ttk.LabelFrame(frame,text="Delete Row")
widgets_frame_2.grid(row=2,column = 0, padx = 20, pady = 5)

widgets_frame_3 = ttk.LabelFrame(frame,text="View Spending Report")
widgets_frame_3.grid(row=3,column = 0, padx = 20, pady = 5)

widgets_frame_4 = ttk.LabelFrame(frame,text="Load Excel DataSheet")
widgets_frame_4.grid(row=4,column = 0, padx = 20, pady = 5)

name_entry = ttk.Entry(widgets_frame)
name_entry.insert(0,"Name")
name_entry.bind("<FocusIn>", lambda e: name_entry.delete("0","end"))
name_entry.grid(row = 0,column = 0, padx = 5, pady = 5,sticky="ew")

date_entry = ttk.Spinbox(widgets_frame, from_= 18, to = 100)
date_entry.insert(0,"Date")
date_entry.grid(row=1, column = 0, padx = 5, pady = 5,sticky = "ew")

amount_entry = ttk.Entry(widgets_frame)
amount_entry.insert(0,"Amount")
amount_entry.bind("<FocusIn>", lambda e: amount_entry.delete("0","end"))
amount_entry.grid(row = 2,column = 0,padx = 5, pady = 5, sticky="ew")

tracker = ExpenseTracker()

insert_button = ttk.Button(widgets_frame, text = "Insert", command=tracker.add_expense)
insert_button.grid(row=3, column = 0, padx = 5, pady = 5,sticky = "nsew")

delete_button = ttk.Button(widgets_frame_2, text = "Delete", command = tracker.remove_expense)
delete_button.grid(row=0, column = 0, padx = 5, pady = 5,sticky = "nsew")

view_data_button = ttk.Button(widgets_frame_3, text = "View Data")
view_data_button.grid(row=0, column = 0, padx = 5, pady = 5,sticky = "nsew")

load_data_button = ttk.Button(widgets_frame_4, text = "Load Excel Datasheet")
load_data_button.grid(row=0, column = 0, padx = 5, pady = 5,sticky = "nsew")



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
Window.mainloop()