import tkinter as tk
import random

items = ["Sword", "Shield", "Potion", "Bow", "Arrow", "Helmet", "Armor"]
attr_entry = []
player_items = []
num_player_items = 0


#Calculate attribute
def calculateAttributes(event) -> None:
    for x in attr_entry:
        value = random.randint(3,18)
        x.delete(0,tk.END)
        x.insert(0,value)
    return

def addItem(name = "Item", cost = 0) -> None:
    """Add an item to the player's inventory."""
    global num_player_items

    if name in player_items:
        # If entry exists, increment the quantity
        for widget in inventory.winfo_children():
            if isinstance(widget, tk.Label) and widget.cget("text") == name:
                # Find the corresponding quantity entry and increment it
                row = widget.grid_info()["row"]
                for entry in inventory.grid_slaves(row=row, column=2):
                    if isinstance(entry, tk.Entry):
                        current_qty = entry.get()
                        try:
                            entry.delete(0, tk.END)
                            entry.insert(0, str(int(current_qty) + 1))
                        except ValueError:
                            entry.delete(0, tk.END)
                            entry.insert(0, "1")
                return
    # Create a label for the item
    item_label = tk.Label(inventory, text=name)
    item_label.grid(row=num_player_items+2, column=0, sticky=tk.W)
    # Create a label for the cost
    cost_label = tk.Label(inventory, text=f"Cost: {cost}")
    cost_label.grid(row=num_player_items+2, column=1, sticky=tk.W)
    # Create an entry for the quantity
    quantity_entry = tk.Entry(inventory, width=5)
    quantity_entry.grid(row=num_player_items+2, column=2, sticky=tk.W)
    quantity_entry.insert(0, "1")  # Default quantity is 1
    # Add the item to the player's items list
    num_player_items += 1
    player_items.append(name)

    # Move buttons below the last item
    button_random.grid(row=num_player_items+3, column=0)
    button_add_item.grid(row=num_player_items+3, column=1)
    return

def randomItem():
    """Generate a random item from the list."""
    # global num_player_items
    if items:
        item = items[random.randint(0, len(items) - 1)]
        cost = random.randint(1, 100)  # Random cost between 1 and 100
        addItem(item, cost)
    else:
        print("No items available to choose from.")
    return

#Generate a label and an entry; store value in list    
def attrField(name):
    attribute = tk.Label(attributes, text=name)
    attribute.grid(row=len(attr_entry), sticky=tk.E)
    value = tk.Entry(attributes)
    value.grid(row=len(attr_entry), column=1)
    attr_entry.append(value)

    return attribute

# Create TK Window
window = tk.Tk()
window.title("D20 Character Creator")
window.resizable(width=True, height=True)

# Information Section
information = tk.Frame(window)
information.grid(columnspan=2)

name = tk.Label(information, text="Name")
name.grid(row=0, column=0)

char_name = tk.Entry(information)
char_name.grid(row=1, column=0)

information.columnconfigure(0, weight=1)
# Attributes Section
attributes = tk.Frame(window)
attributes.grid(row=1, column=0, rowspan=7)

# Create Labels & Entries For Ability Names
strength = attrField("Strength")
dexterity = attrField("Dexterity")
constitution= attrField("Constitution")
intelligence = attrField("Intelligence")
wisdom = attrField("Wisdom")
charisma = attrField("Charisma")

button_generate = tk.Button(attributes, text="Generate", fg="green")
button_generate.grid(row=6, columnspan=2, sticky=tk.E)
button_generate.bind("<Button-1>", calculateAttributes)

# Skills Section
skill_tree = tk.Frame(window)
skill_tree.grid(row=1, column=1)

skills = tk.Label(skill_tree, text="Skills")
skills.grid(columnspan=2)


# Inventory Section
inventory = tk.Frame(window)
inventory.grid(row=2, column=1)

inventory_label = tk.Label(inventory, text="Inventory")
inventory_label.grid(row=1, columnspan=2)

button_random = tk.Button(inventory, text ="Random")
button_random.grid(row=5, column=0)
button_random.bind("<Button-1>", lambda event: randomItem())

button_add_item = tk.Button(inventory, text ="Add Item")
button_add_item.grid(row=5, column=1)

window.mainloop()