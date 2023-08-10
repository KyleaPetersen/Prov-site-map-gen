import tkinter as tk
from coordinates import *
from main import *
#--------------------------------
# What happens when you hit click
#--------------------------------
def submit_button_clicked():
    
    #get value's for new resident
    user_inputs = {
        'unit': apartment_entry.get(),
        'parking': parking_entry.get(),
    }

    #sets unit number to bottom floor so I only need 1 set of coordinates.
    user_inputs['unit'] = user_inputs['unit'][:1] + "1" + user_inputs['unit'][2:]
    
    #find coordinates for PDF
    
    apt = apartment(str.upper(user_inputs['unit']))
    # parking = parking_spot(str.upper(user_inputs['parking']))
    dumpster = dumpster_spot(str.upper(user_inputs['unit']))
    mailbox = mailbox_bank(str.upper(user_inputs['unit']))

    # #generate new pdf marking the specific places
    generate(apt, dumpster, mailbox)

    root.destroy()
    # Add more code here for further processing or displaying results

#--------------------------------
# Set up the UI
#--------------------------------

# Create the GUI window
root = tk.Tk()
root.title("Map Generator")

# Create input fields for user data

apartment_label = tk.Label(root, text="Apartment:")
apartment_label.pack()
apartment_entry = tk.Entry(root)
apartment_entry.pack()

parking_label = tk.Label(root, text="Parking:")
parking_label.pack()
parking_entry = tk.Entry(root)
parking_entry.pack()

# Create the "Submit" button
submit_button = tk.Button(root, text="Submit", command=submit_button_clicked)
submit_button.pack()

# Start the GUI event loop
root.mainloop()