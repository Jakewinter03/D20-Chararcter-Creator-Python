from tkinter import *
import random

attr_entry = []

#Calculate attribute
def calculateAttributes(event):
    
    for x in attr_entry:
        value = random.randint(3,18)
        x.delete(0,END)
        x.insert(0,value)
    return

#Generate a label and an entry; store value in list    
def attrField(name):
    attribute = Label(attributes, text=name)
    attribute.grid(row=len(attr_entry), sticky=E)
    value = Entry(attributes)
    value.grid(row=len(attr_entry), column=1)
    attr_entry.append(value)

    return attribute

# Create TK Window
window = Tk()
window.title("D20 Character Creator")
window.resizable(width=False, height=False)

# Information Section
information = Frame(window)
information.grid(columnspan=2)

name = Label(information, text="Name")
name.grid(row=0, column=0)

char_name = Entry(information)
char_name.grid(row=1, column=0)

information.columnconfigure(0, weight=1)
# Attributes Section
attributes = Frame(window)
attributes.grid(row=1, column=0, rowspan=7)

# Create Labels & Entries For Ability Names
strength = attrField("Strength")
dexterity = attrField("Dexterity")
constitution= attrField("Constitution")
intelligence = attrField("Intelligence")
wisdom = attrField("Wisdom")
charisma = attrField("Charimsa")

button_generate = Button(attributes, text="Generate", fg="green")
button_generate.grid(row=6, columnspan=2, sticky=E)
button_generate.bind("<Button-1>", calculateAttributes)

# Skills Section
skill_tree = Frame(window)
skill_tree.grid(row=1, column=1)

skills = Label(skill_tree, text="Skills")
skills.grid(columnspan=2)


# Inventory Section
inventory = Frame(window)
inventory.grid(row=2, column=1)

items = Label(inventory, text="Inventory")
items.grid(row=1, columnspan=2)

button_random = Button(inventory, text ="Random")
button_random.grid(row=5, column=0)

button_add_item = Button(inventory, text ="Add Item")
button_add_item.grid(row=5, column=1)

window.mainloop()