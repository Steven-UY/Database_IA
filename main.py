from tkinter import *
import sqlite3
from tkinter import messagebox
#Testing
def new():
    var_first.set("")
    var_last.set("")
    var_contact_number.set("")
    var_address.set("")
    var_gender.set("")
    var_age.set("")
    var_ID.set("")
    insert_btn["state"] = "active"
    print("NEW")

def delete():
    MsgBox = messagebox.askquestion('DELETE RECORD', 'Are you sure you want to delete this record? This cannot be undone.', icon = 'warning')

    if MsgBpx == 'yes':
        conn = sqlite3.connect('trading.db')
        c = conn.cursor()
        delete_query = "DELETE FROM customer WHERE customer_id=" + str(var_ID.get())
        print(delete_query)
        c.execute(delete_query)
        conn.commit()
        set_data()
        print("DELETED")

def insert():
    print("insert")
    customer = [var_first.get(), var_last.get(), var_contact_number.get(),
               var_address.get(), var_gender.get(), var_age.get(), var_ID.get()]
    insert_query = "INSERT INTO patient VALUES(null, ?, ?, ?)"
    conn = sqlite3.connect('trading.db')
    c = conn.cursor()
    c.execute(insert_query, book)
    conn.commit()
    set_data()

def save():
    print("Saved")


def nav_back():
    print("Back")
    var_recordset_index.set(var_recordset_index.get()-1)
    set_data()


def nav_forward():
    print("Next")
    var_recordset_index.set(var_recordset_index.get()+1)
    set_data()

def add():
    conn = sqlite3.connect('trading.db')
    c = conn.cursor()
    c.execute("Select * FROM customer")
    data = c.fetchall()
    row = data[0]
    print(row[1])
    return data
    conn.commit()
    conn.close()

def set_data():
    data = add()
    row = data[var_recordset_index.get()]
    var_first.set(row[0])
    var_last.set(row[1])
    var_contact_number.set(row[2])
    var_address.set(row[3])
    var_gender.set(row[5])
    var_age.set(row[4])
    var_ID.set(row[6])


root = Tk()
root.geometry("500x500")
root.title("Hello World GUI")

var_recordset_index=IntVar()
var_recordset_index.set(0)

var_first = StringVar(root)
var_last = StringVar(root)
var_contact_number = StringVar(root)
var_address = StringVar(root)
var_gender = StringVar(root)
var_age = StringVar(root)
var_ID = StringVar(root)

app_menu_label = Label(root, text="Edit Patient Information Page")
app_menu_label.grid(row=0, column=1, columnspan=1)

first = Label(root, text="Firstname")
first.grid(padx=20, pady=20, row=2, column=0)
first_entry = Entry(root, textvariable=var_first)
first_entry.grid(row=2, column=1)

last = Label(root, text="Lastname")
last.grid(padx=20, pady=20, row=3, column=0)
last_entry = Entry(root, textvariable=var_last )
last_entry.grid(row=3, column=1)

dob = Label(root, text="DOB")
dob.grid(padx=20, pady=20, row=4, column=0)
dob_entry = Entry(root, textvariable=var_age)
dob_entry.grid(row=4, column=1)

pcontact = Label(root, text="Contact Number")
pcontact.grid(padx=20, pady=20, row=5, column=0)
pcontact_entry = Entry(root, textvariable=var_contact_number)
pcontact_entry.grid(row=5, column=1)

paddress = Label(root, text="Address")
paddress.grid(padx=20, pady=20, row=6, column=0)
paddress_entry =    Entry(root,textvariable=var_address)
paddress_entry.grid(row=6, column=1)

gender = Label(root, text="Gender")
gender.grid(padx=20, pady=20, row=7, column=0)
gender_entry = Entry(root, textvariable=var_gender)
gender_entry.grid(row=7, column=1)

add_btn = Button(root, text="Add Data", command=add)
add_btn.grid(padx=20, pady=20, row=8, column=0)

back_btn = Button(root, text="<", command=nav_back)
back_btn.grid(padx=20, pady=20, row=9, column=0)

forward_btn = Button(root, text=">", command=nav_forward)
forward_btn.grid(padx=20, pady=20, row=10, column=0)

insert_btn = Button(root, text="Insert", command=insert)
insert_btn.grid(padx=20, pady=20, row=10, column=3)

delete_btn = Button(root, text="Delete", command=delete)
delete_btn.grid(padx=20, pady=20, row=10, column=4)

new_btn = Button(root, text="New", command=new)
new_btn.grid(padx=20, pady=20, row=10, column=5)

root.mainloop()



