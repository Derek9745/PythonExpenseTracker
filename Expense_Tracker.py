from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
import openpyxl
from datetime import datetime


class Expense:
    def __init__(self, date,description, amount, action, TransID):
        self.date = date
        self.description = description
        self.amount = amount
        self.action = action
        self.TransID = TransID
      
class ExpenseTracker:
    current_ID_Counter = 0
    def __init__(self):
        self.expenses = []
        
    def transaction_id(self):
        ExpenseTracker.current_ID_Counter += 1
        return ExpenseTracker.current_ID_Counter

    def add_expense(self):
        action = "----------------"
        TransID = self.transaction_id()

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

        expense = Expense(TransID, date, description, amount, action)
        self.expenses.append(expense)
        treeview.insert("", tkinter.END, values = (expense.date,expense.description,expense.amount,expense.action,expense.TransID))


    def remove_expense(self):
        selected_item = treeview.selection() 
        if selected_item:  
            treeview.delete(selected_item)
        else:
            messagebox.askretrycancel(title="Input Error", message = "No Row Selected")
       
        
    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        return total

    
    def generate_plot(self):
        self.total_expenses()
        ## create a horizontal bar chart that compares expenses to spending budget

    def add_note(self):
        selected_item = treeview.selection() 
        if selected_item:  
                treeview.set(selected_item, column="Action", value="Note")
        else:
            messagebox.askretrycancel(title="Input Error", message = "No Row Selected")
        
    def load_excel(self):
        path = "C:/Users/hehnd/OneDrive/Desktop/Python/PythonExpenseTracker/Expense_Data.xlsx"
        workbook = openpyxl.load_workbook(path)
        sheet = workbook.active
        list_values = list(sheet.values)
        action = "----------------"
        print(list_values)
        for col_name in list_values[0]:
            col_name = str(col_name)
            treeview.heading(col_name, text=col_name)

        for value_tuple in list_values[1:]:
            TransID = self.transaction_id()
            date_str =value_tuple[0].strftime('%m/%d/%Y')
            description = value_tuple[1]
            amount = value_tuple[2]
            expense = Expense(TransID, date_str, description, amount, action)
            self.expenses.append(expense) 
            treeview.insert('', tkinter.END, values=(expense.date,expense.description,expense.amount, expense.action,expense.TransID))
      
if __name__ == "__main__":

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

    widgets_frame_5 = ttk.LabelFrame(frame, text = "Spending Report Vizualization")
    widgets_frame_5.grid(row = 2, column = 1, padx = 5 , pady = 5)

    widgets_frame_6 = ttk.LabelFrame(frame, text = "Add Note")
    widgets_frame_6.grid(row = 5, column = 0, padx = 5 , pady = 5)

    widgets_frame_7 = ttk.LabelFrame(frame, text = "View Note")
    widgets_frame_7.grid(row = 6, column = 0, padx = 5 , pady = 5)


    plot_label = ttk.Label(widgets_frame_5, text="Plot Label")
    plot_label.grid(row=0, column=1, columnspan=1)

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

    view_data_button = ttk.Button(widgets_frame_3, text = "View Spending Report", command = tracker.generate_plot)
    view_data_button.grid(row=0, column = 0, padx = 5, pady = 5,sticky = "nsew")

    load_data_button = ttk.Button(widgets_frame_4, text = "Load Excel DataSheet", command = tracker.load_excel)
    load_data_button.grid(row=0, column = 0, padx = 5, pady = 5,sticky = "nsew")

    add_note = ttk.Button(widgets_frame_6, text = "Add Note", command = tracker.add_note)
    add_note.grid(row=0, column = 0, padx = 5, pady = 5,sticky = "nsew")

    view_note = ttk.Button(widgets_frame_7, text = "View Note")
    view_note.grid(row=0, column = 0, padx = 5, pady = 5,sticky = "nsew")

    treeFrame = ttk.Frame(frame)
    treeFrame.grid(row=0,column = 1, pady = 10)
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right", fill = "y")
    treeview = ttk.Treeview(treeFrame,column=("Transaction ID","Date","Description","Amount","Action"),show= "headings",height= 8)


    treeview.column("Transaction ID",anchor=CENTER)
    treeview.heading("Transaction ID", text= "Transaction ID")
    treeview.column("Date",anchor=CENTER)
    treeview.heading("Date", text= "Date")
    treeview.column("Description",anchor=CENTER)
    treeview.heading("Description", text= "Description")
    treeview.column("Amount",anchor=CENTER)
    treeview.heading("Amount", text= "Amount")
    treeview.column("Action",anchor=CENTER)
    treeview.heading("Action", text= "Action")


    treeview.pack()
    treeScroll.config(command = treeview.yview)
    Window.mainloop()