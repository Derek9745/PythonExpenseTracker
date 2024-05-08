
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import openpyxl
from datetime import datetime
from tkinter import scrolledtext 
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class Expense:
    def __init__(self, date,description, amount, note, TransID):
        self.date = date
        self.description = description
        self.amount = amount
        self.note = note
        self.TransID = TransID
      
class ExpenseTracker:
    current_ID_Counter = 0
    def __init__(self):
        self.expenses = []
             
    def transaction_id(self):
        ExpenseTracker.current_ID_Counter += 1
        return ExpenseTracker.current_ID_Counter

    def add_expense(self):
        if len(name_entry.get()) != 0 and len(date_entry.get()) != 0 and len(amount_entry.get()) != 0:
                try:
                    description = name_entry.get()
                    amount = float(amount_entry.get())
                    date = datetime.strptime(date_entry.get(),'%m/%d/%Y')
                    note = "----------------"
                    TransID = self.transaction_id()
                    expense = Expense(TransID, date, description, amount, note)
                    self.expenses.append(expense)
                    treeview.insert("", tk.END, values = (expense.date,expense.description,expense.amount,expense.note,expense.TransID))
                except ValueError:
                    messagebox.askretrycancel(title="Input Error", message = "Invalid input. Please enter a valid input")
        else:
            messagebox.askretrycancel(title="Input Error", message = "Invalid input. All input fields are empty. No row added")

    def remove_expense(self):
        selected_item = treeview.selection() 
        values = treeview.item(selected_item, "values")
        if values:
            transID = values[0]
            for expense in self.expenses:
                if expense.TransID == transID:
                    self.expenses.remove(expense)
                    break  # Stop looping once the expense is found and removed
            treeview.delete(selected_item)
       

        else:
            messagebox.askretrycancel(title="Input Error", message = "No Row Selected")
            
        
    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        return total

    
    def generate_plot(self, budget):
        total_expenses = self.total_expenses()

        # Data for plotting
        categories = ["Expenses", "Budget"]
        values = [total_expenses, budget]

        # Create bar plot
        fig, ax = plt.subplots()
        ax.barh(categories, values, color=['blue', 'green'])
        ax.set_xlabel('Amount')
        ax.set_title('Expenses vs Spending Budget')

        # Embed the plot into the GUI
        canvas = FigureCanvasTkAgg(fig, master=plot_label)
        canvas.draw()
        #canvas.get_tk_widget().configure(width=250, height=125)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)






    def add_note(self):
        selected_item = treeview.selection() 
        if selected_item:  
            if note_entry.get("1.0", "end-1c") != "":
                treeview.set(selected_item, column="Note", value="note")
                note = note_entry.get("1.0", tk.END)
                conn = sqlite3.connect("notes.db")
                cursor = conn.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)")
                cursor.execute("INSERT INTO notes (content) VALUES (?)", (note,))
                conn.commit()
                conn.close()
            else:
                messagebox.askretrycancel(title="Input Error", message = "No Text Entered")
        else:
            messagebox.askretrycancel(title="Input Error", message = "No Row Selected")


    def view_note(self):
        selected_item = treeview.selection()
        if selected_item:
            values = treeview.item(selected_item, "values")
            note = values[4]
            if note != "----------------":
                conn = sqlite3.connect("notes.db")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM notes")
                notes = cursor.fetchall()
                conn.close()

                view_window = tk.Toplevel(Window)
                view_window.title("View Notes")
                view_text = tk.Text(view_window)
                for note in notes:
                    view_text.insert(tk.END, note[1] + "\n")
                view_text.pack()
            else:
                messagebox.askretrycancel(title="Input Error", message = "No note created for this expense")
            #bring up text from note into textview

        else:
            messagebox.askretrycancel(title="Input Error", message = "No Row Selected")

    def delete_note(self):
        selected_item = treeview.selection()
        if selected_item:
            values =  treeview.item(selected_item, "values")
            note = values[4]
            if note == "note":
                treeview.set(selected_item, column="Note", value="----------------")
                conn = sqlite3.connect("notes.db")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM notes")
                conn.commit()
                conn.close()
            else: 
                messagebox.askretrycancel(title = "Input Error", message = "No note created for this expense")
        else:
            messagebox.askretrycancel(title="Input Error", message = "No Row Selected")


    def load_excel(self):
        path = "C:/Users/hehnd/OneDrive/Desktop/Python/PythonExpenseTracker/Expense_Data.xlsx"
        workbook = openpyxl.load_workbook(path)
        sheet = workbook.active
        list_values = list(sheet.values)
        note = "----------------"
        print(list_values)
        for col_name in list_values[0]:
            col_name = str(col_name)
            treeview.heading(col_name, text=col_name)

        for value_tuple in list_values[1:]:
            TransID = self.transaction_id()
            date_str =value_tuple[0].strftime('%m/%d/%Y')
            description = value_tuple[1]
            amount = value_tuple[2]
            expense = Expense(TransID, date_str, description, amount, note)
            self.expenses.append(expense) 
            treeview.insert('', tk.END, values=(expense.date,expense.description,expense.amount, expense.note,expense.TransID))
      
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

    command_frame = ttk.LabelFrame(frame,text = "Commands")
    command_frame.grid(row = 0, column = 0,padx = 20, pady = 10)

    widgets_frame = ttk.LabelFrame(command_frame,text="Insert Row")
    widgets_frame.grid(row=0,column = 0, padx = 20, pady = 10)

    widgets_frame_2 = ttk.LabelFrame(command_frame,text="Delete Row")
    widgets_frame_2.grid(row=1,column = 0, padx = 20, pady = 5)

    widgets_frame_3 = ttk.LabelFrame(command_frame,text="View Spending Report")
    widgets_frame_3.grid(row=2,column = 0, padx = 20, pady = 5)

    outer_frame = ttk.LabelFrame(frame, text = "DashBoard")
    outer_frame.grid(row = 2, column = 0, padx = 5 , pady = 2, columnspan = 3)

    widgets_frame_4 = ttk.LabelFrame(command_frame,text="Load Excel DataSheet")
    widgets_frame_4.grid(row=3,column = 0, padx = 20, pady = 5)

    widgets_frame_5 = ttk.LabelFrame(outer_frame, text = "Spending Report Vizualization")
    widgets_frame_5.grid(row = 0, column = 1, padx = 5 , pady = 5)

    widgets_frame_6 = ttk.LabelFrame(command_frame, text = "Add Note")
    widgets_frame_6.grid(row = 4, column = 0, padx = 5 , pady = 5)

    widgets_frame_7 = ttk.LabelFrame(command_frame, text = "View Note")
    widgets_frame_7.grid(row = 5, column = 0, padx = 5 , pady = 5)

    widgets_frame_8 = ttk.LabelFrame(command_frame, text = "Delete Note")
    widgets_frame_8.grid(row = 6, column = 0, padx = 5 , pady = 5)


    plot_label = ttk.Label(widgets_frame_5, text="Plot Label")
    plot_label.grid(row=0, column=1)

    note_text_entry = ttk.LabelFrame(outer_frame, text = "Note Text Entry")
    note_text_entry.grid(row = 0, column = 0, padx = 5 , pady = 2)


    note_entry = scrolledtext.ScrolledText(note_text_entry, wrap=tk.WORD, width=110, height=13, font=("Calibri", 12))
    note_entry.grid(row =0, column =0, padx = 5,pady = 5)


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

    view_data_button = ttk.Button(widgets_frame_3, text = "View Spending Report", command = lambda: tracker.generate_plot(1500))
    view_data_button.grid(row=0, column = 0, padx = 5, pady = 5,sticky = "nsew")

    load_data_button = ttk.Button(widgets_frame_4, text = "Load Excel DataSheet", command = tracker.load_excel)
    load_data_button.grid(row=0, column = 0, padx = 5, pady = 5,sticky = "nsew")

    add_note = ttk.Button(widgets_frame_6, text = "Add Note", command = tracker.add_note)
    add_note.grid(row=0, column = 0, padx = 5, pady = 5,sticky = "nsew")

    view_note = ttk.Button(widgets_frame_7, text = "View Note", command = tracker.view_note)
    view_note.grid(row=0, column = 0, padx = 5, pady = 5,sticky = "nsew")

    delete_note = ttk.Button(widgets_frame_8, text = "Delete Note", command = tracker.delete_note)
    delete_note.grid(row=0, column = 0, padx = 5, pady = 5,sticky = "nsew")

    treeFrame = ttk.Frame(frame)
    treeFrame.grid(row=0,column = 1, pady = 0)
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right", fill = "y")
    treeview = ttk.Treeview(treeFrame,column=("Transaction ID","Date","Description","Amount","Note"),show= "headings",height= 29)
    treeview.pack()


    treeview.column("Transaction ID",anchor=CENTER)
    treeview.heading("Transaction ID", text= "Transaction ID")
    treeview.column("Date",anchor=CENTER)
    treeview.heading("Date", text= "Date")
    treeview.column("Description",anchor=CENTER)
    treeview.heading("Description", text= "Description")
    treeview.column("Amount",anchor=CENTER)
    treeview.heading("Amount", text= "Amount")
    treeview.column("Note",anchor=CENTER)
    treeview.heading("Note", text= "Note")


    
    treeScroll.config(command = treeview.yview)
    Window.mainloop()