#Contact management system
import customtkinter
import tkinter as tk
from tkinter import ttk
import json
import os


root = customtkinter.CTk()
root.title("Contact Management")
root.geometry("1080x480")

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")


contacts_file = "contacts.json"

def load_contacts():
    if os.path.exists(contacts_file):
        with open(contacts_file, "r") as file:
            return json.load(file)
    return []

def save_contacts():
    with open(contacts_file, "w") as file:
        json.dump(contacts, file)

contacts = load_contacts()

def add_contacts():

    name_val = name.get()
    number_val = phone_number.get()
    email_val = email.get()

    table.insert('', 'end', values=(name_val, number_val, email_val))
    contacts.append({'name': name_val, 'number': number_val, 'email': email_val})

    name.delete(0, 'end')
    phone_number.delete(0, 'end')
    email.delete(0, 'end')

    save_contacts()

def delete_contacts():

   selected_items = table.selection() 

   if selected_items:
        for item in selected_items:
            values = table.item(item, 'values')
            
            contacts[:] = [contact for contact in contacts if contact['name'] != values[0] or contact['number'] != values[1] or contact['email'] != values[2]]
            table.delete(item)
        
        save_contacts() 


def edit_contacts():
    selected_item = table.selection()
    if selected_item:
        item = table.item(selected_item)
        values = item['values']

        name.delete(0, 'end')
        name.insert(0, values[0])
        phone_number.delete(0, 'end')
        phone_number.insert(0, values[1])
        email.delete(0, 'end')
        email.insert(0, values[2])

        table.delete(selected_item)

        contacts[:] = [contact for contact in contacts if contact['name'] != values[0] or contact['number'] != values[1] or contact['email'] != values[2]]

        save_contacts() 





heading_lbl = customtkinter.CTkLabel(root, text="Contacts")
heading_lbl.pack(pady = 10)

left_frame = customtkinter.CTkFrame(master= root, width=300, height = 400)
left_frame.pack(side = "left", fill = "y", padx = 10, pady = 10)
left_frame.pack_propagate(False)

right_frame = customtkinter.CTkFrame(master= root, width=1050, height = 400)
right_frame.pack(side = "right", fill = "y", padx = 10, pady = 10)
right_frame.pack_propagate(False)


headlbl = customtkinter.CTkLabel(master= left_frame, text="Name")
headlbl.pack( padx = 15)

name = customtkinter.CTkEntry(master= left_frame, placeholder_text="Name")
name.pack(pady = 10 )

phone_numberlbl = customtkinter.CTkLabel(master=left_frame, text="Phone Number")
phone_numberlbl.pack(padx = 10)

phone_number = customtkinter.CTkEntry(master=left_frame, placeholder_text="Phone Number")
phone_number.pack(pady= 10)

emaillbl = customtkinter.CTkLabel(master=left_frame, text="Email Address")
emaillbl.pack(padx = 10)

email= customtkinter.CTkEntry(master = left_frame, placeholder_text="Email Address")
email.pack(pady = 10)


addbtn = customtkinter.CTkButton(master= left_frame, text= "ADD", command=lambda:add_contacts())
addbtn.pack(pady = 10)

deletebtn = customtkinter.CTkButton(master= left_frame, text= "DELETE", command= delete_contacts)
deletebtn.pack(pady = 10)

editbtn = customtkinter.CTkButton(master= left_frame, text= "EDIT", command= edit_contacts)
editbtn.pack(pady = 10)

table = ttk.Treeview(right_frame, columns = ('name', 'number', 'email'), show= "headings" )
table.heading('name', text="FullNames")
table.heading('number', text="Phone Number")
table.heading('email', text="Email Address")
table.pack(fill="both" , expand= True)


for contact in contacts:
    table.insert('', 'end', values=(contact['name'], contact['number'], contact['email']))



root.mainloop()
