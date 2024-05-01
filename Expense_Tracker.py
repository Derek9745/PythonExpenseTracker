from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
import openpyxl
from datetime import datetime


def load_excel():
        path = "C:/Users/hehnd/OneDrive/Desktop/Python/PythonExpenseTracker/Expense_Data.xlsx"
        workbook = openpyxl.load_workbook(path)
        sheet = workbook.active
        list_values = list(sheet.values)
        print(list_values)
        for col_name in list_values[0]:
            col_name = str(col_name)
            treeview.heading(col_name, text=col_name)

        for value_tuple in list_values[1:]:
            treeview.insert('', tkinter.END, values=value_tuple)


class Expense:
    def __init__(self, date,description, amount):
        self.date = date
        self.description = description
        self.amount = amount
      
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        while True:
            try:
                date = date_entry.get()
                datetime.strptime(date, '%m/%d/%Y')
                break
            except ValueError:
                retry = messagebox.askretrycancel(title="Input Error", message = "Invalid input. Please enter a valid date input")
                if not retry:
                    return  
                 
        description = name_entry.get()

        while True:
            try:
                amount = float(amount_entry.get())
                break
            except ValueError:
                retry = messagebox.askretrycancel(title="Input Error", message = "Invalid input. Please enter a valid numerical input")
                if not retry:
                    return 

        expense = Expense(date, description, amount)
        self.expenses.append(expense)
        treeview.insert("", tkinter.END, text=f"Expense Name: {expense.description}", values = (expense.date,expense.description,expense.amount))
    

    def remove_expense(self):
        selected_item = treeview.selection() 
        if selected_item:  
            treeview.delete(selected_item)
        else:
            messagebox.askretrycancel(title="Input Error", message = "No Row Selected")
       
        
    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: $ {total:.2f}")

    def view_spending_report(self):
        return
    
    


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

date_entry = ttk.Entry(widgets_frame)
date_entry.insert(0,"Date")
date_entry.bind("<FocusIn>", lambda e: date_entry.delete("0","end"))
date_entry.grid(row=1, column = 0, padx = 5, pady = 5,sticky = "ew")

amount_entry = ttk.Entry(widgets_frame)
amount_entry.insert(0,"Amount")
amount_entry.bind("<FocusIn>", lambda e: amount_entry.delete("0","end"))
amount_entry.grid(row = 2,column = 0,padx = 5, pady = 5, sticky="ew")

tracker = ExpenseTracker()

insert_button = ttk.Button(widgets_frame, text = "Insert", command=tracker.add_expense)
insert_button.grid(row=3, column = 0, padx = 5, pady = 5,sticky = "nsew")

delete_button = ttk.Button(widgets_frame_2, text = "Delete Selected Row", command = tracker.remove_expense)
delete_button.grid(row=0, column = 0, padx = 5, pady = 5,sticky = "nsew")

view_data_button = ttk.Button(widgets_frame_3, text = "View Spending Report", command = tracker.view_spending_report)
view_data_button.grid(row=0, column = 0, padx = 5, pady = 5,sticky = "nsew")

load_data_button = ttk.Button(widgets_frame_4, text = "Load Excel Datasheet", command = load_excel)
load_data_button.grid(row=0, column = 0, padx = 5, pady = 5,sticky = "nsew")



treeFrame = ttk.Frame(frame)
treeFrame.grid(row=0,column = 1, pady = 10)
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill = "y")

treeview = ttk.Treeview(treeFrame,column=("Date","Description","Amount"),show= "headings",height= 8)

treeview.column("Date",anchor=CENTER)
treeview.heading("Date", text= "Date")
treeview.column("Description",anchor=CENTER)
treeview.heading("Description", text= "Description")
treeview.column("Amount",anchor=CENTER)
treeview.heading("Amount", text= "Amount")


treeview.pack()
treeScroll.config(command = treeview.yview)
Window.mainloop()