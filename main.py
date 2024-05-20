#Code Alpha Task 2: Expense Tracker 
#It is a expense tracker that the user can use to update their daily expenditure and track it

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, simpledialog
import datetime as dt
from mydb import *

data = Database(db='expense.db')

count = 0
selected_rwid = 0
total_balance = 0

def ask_total_balance():
    global total_balance
    total_balance = simpledialog.askfloat("Total Balance", "Please enter your total balance:")

def saverecord():
    global data
    data.insertrecords(item_name=item_name.get(), item_price=item_amt.get(), purchase_date=transaction_date.get())
    refreshData()

def setdate():
    date = dt.datetime.now()
    dopvar.set(f'{date:%d %B %Y}')

def clearentries():
    item_name.delete(0, 'end')
    item_amt.delete(0, 'end')
    transaction_date.delete(0, 'end')

def fetch_records():
    global count
    f = data.fetchrecord('SELECT rowid, * FROM expense_record')
    for rec in f:
        tv.insert(parent='', index='end', iid=rec[0], values=(rec[0], rec[1], rec[2], rec[3]))

def select_record(event):
    global selected_rwid
    selected = tv.focus()
    val = tv.item(selected, 'values')

    try:
        selected_rwid = val[0]
        namevar.set(val[1])
        amtvar.set(val[2])
        dopvar.set(val[3])
    except IndexError:
        pass

def update_record():
    global selected_rwid

    selected = tv.focus()
    if not selected_rwid:
        messagebox.showwarning("Select record", "Please select a record to update")
        return

    try:
        data.updaterecord(namevar.get(), amtvar.get(), dopvar.get(), selected_rwid)
        refreshData()
    except Exception as ep:
        messagebox.showerror('Error', ep)

    clearentries()

def totalbalance():
    global total_balance
    f = data.fetchrecord(query="SELECT sum(item_price) FROM expense_record")
    total_expense = 0
    for i in f:
        for j in i:
            total_expense = j
    remaining_balance = total_balance - total_expense
    messagebox.showinfo('Current Balance', f"Total Expense: {total_expense} \nBalance Remaining: {remaining_balance}")

def refreshData():
    for item in tv.get_children():
        tv.delete(item)
    fetch_records()

def deleteRow():
    global selected_rwid
    if not selected_rwid:
        messagebox.showwarning("Select record", "Please select a record to delete")
        return
    data.removerecord(selected_rwid)
    refreshData()

def delete_all_records():
    data.delete_all_records()
    refreshData()
    messagebox.showinfo("Information", "All records have been deleted.")

main = Tk()
main.title('Expense Tracker')

ask_total_balance()

f = ('Times new roman', 14)
namevar = StringVar()
amtvar = IntVar()
dopvar = StringVar()

f2 = Frame(main)
f2.pack()

f1 = Frame(main, padx=10, pady=10)
f1.pack(expand=True, fill=BOTH)

Label(f1, text='ITEM NAME', font=f).grid(row=0, column=0, sticky=W)
Label(f1, text='ITEM PRICE', font=f).grid(row=1, column=0, sticky=W)
Label(f1, text='PURCHASE DATE', font=f).grid(row=2, column=0, sticky=W)

item_name = Entry(f1, font=f, textvariable=namevar)
item_amt = Entry(f1, font=f, textvariable=amtvar)
transaction_date = Entry(f1, font=f, textvariable=dopvar)

item_name.grid(row=0, column=1, sticky=EW, padx=(10, 0))
item_amt.grid(row=1, column=1, sticky=EW, padx=(10, 0))
transaction_date.grid(row=2, column=1, sticky=EW, padx=(10, 0))

cur_date = Button(
    f1,
    text='Current Date',
    font=f,
    bg='#d9ed92',
    command=setdate,
    width=15
)

submit_btn = Button(
    f1,
    text='Save Record',
    font=f,
    command=saverecord,
    bg='#1a759f',
    fg='white'
)

clr_btn = Button(
    f1,
    text='Clear Entry',
    font=f,
    command=clearentries,
    bg='#48cae4',
    fg='white'
)

quit_btn = Button(
    f1,
    text='Exit',
    font=f,
    command=lambda: main.destroy(),
    bg='#ffb703',
    fg='white'
)

total_bal = Button(
    f1,
    text='Total Balance',
    font=f,
    bg='#fb5607',
    fg='white',
    command=totalbalance
)

update_btn = Button(
    f1,
    text='Update',
    bg='#fb8500',
    command=update_record,
    fg='white',
    font=f
)

del_btn = Button(
    f1,
    text='Delete',
    bg='#e76f51',
    fg='white',
    command=deleteRow,
    font=f
)

del_all_btn = Button(
    f1,
    text='Delete All',
    bg='#f4a261',
    fg='white',
    command=delete_all_records,
    font=f
)

cur_date.grid(row=3, column=1, sticky=EW, padx=(10, 0))
submit_btn.grid(row=0, column=2, sticky=EW, padx=(10, 0))
clr_btn.grid(row=1, column=2, sticky=EW, padx=(10, 0))
quit_btn.grid(row=2, column=2, sticky=EW, padx=(10, 0))
total_bal.grid(row=0, column=3, sticky=EW, padx=(10, 0))
update_btn.grid(row=1, column=3, sticky=EW, padx=(10, 0))
del_btn.grid(row=2, column=3, sticky=EW, padx=(10, 0))
del_all_btn.grid(row=3, column=3, sticky=EW, padx=(10, 0))

tv = ttk.Treeview(f2, selectmode='browse', columns=(1, 2, 3, 4), show='headings', height=8)
tv.pack(side="left")

tv.column(1, anchor=CENTER, stretch=NO, width=70)
tv.column(2, anchor=CENTER)
tv.column(3, anchor=CENTER)
tv.column(4, anchor=CENTER)
tv.heading(1, text="Serial no")
tv.heading(2, text="Item Name")
tv.heading(3, text="Item Price")
tv.heading(4, text="Purchase Date")

tv.bind("<ButtonRelease-1>", select_record)

scrollbar = Scrollbar(f2, orient='vertical')
scrollbar.configure(command=tv.yview)
scrollbar.pack(side="right", fill="y")
tv.config(yscrollcommand=scrollbar.set)

style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

main.mainloop()
