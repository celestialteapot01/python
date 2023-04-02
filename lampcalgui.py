import tkinter as tk

#Chat-AI was used to help write this. It(?) helped me solve problems and explain why my code wasn't working (I broke it a lot xD) 
# and helped make it look nicer. As I learn more Python, I hope to be able to make more improvements :) - SD, April 2023

# Define the GUI layout
root = tk.Tk()
root.title("Lamp Hour Calculator")

font = ("Arial", 14)  # Define font family and size

fixture_label = tk.Label(root, text="Fixture:", font=font)
fixture_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")
fixture_options = ["MegaPointe", "BMFL"] #This can be added to if needed, just remember to put the rest of the coding in!
fixture_var = tk.StringVar()
fixture_select = tk.OptionMenu(root, fixture_var, *fixture_options)
fixture_select.config(font=("Arial", 14))
fixture_select.grid(row=0, column=1, padx=5, pady=5, sticky="W")

hours_label = tk.Label(root, text="Resettable Lamp Hours:", font=font) 
hours_label.grid(row=1, column=0, padx=5, pady=5, sticky="W")
hours_input = tk.Entry(root)
hours_input.grid(row=1, column=1, padx=5, pady=5, sticky="W")

calculate_btn = tk.Button(root, text="Calculate", font=font)
calculate_btn.grid(row=2, column=0, padx=5, pady=5, sticky="W")

clear_btn = tk.Button(root, text="Clear", font=font)
clear_btn.grid(row=2, column=1, padx=5, pady=5, sticky="W")

result_label = tk.Label(root, text="Actual Lamp Hours:", font=font,)
result_label.grid(row=3, column=0, padx=5, pady=5, sticky="W")
result_output = tk.Label(root, text="", font=("Arial", 14), justify="center")
result_output.grid(row=3, column=1, padx=5, pady=5, sticky="W")

change_lamp_message = tk.Label(root, text="", anchor="center", font=font)
change_lamp_message.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="W")

def calculate_handler():
    fixture = fixture_select.cget("text")
    hours = int(hours_input.get())
    fixture = fixture_var.get()

    if fixture == "MegaPointe":
        hours_remaining = 1500 - hours #Max recommended lamp hours from the manual. It can be 2000 if using eco-mode...no one uses eco-mode.
        result_output.config(text= str(hours_remaining), font=("Arial", 14),bg="green") #puts the hours in a green box
        change_lamp_message.config(text="")
        if hours_remaining >= 800: #if there are less than 800 or equal to 800hrs left, then CHANGE THE LAMP is displayed
            change_lamp_box = tk.Label(root, text="CHANGE THE LAMP", bg="yellow", font=("Arial", 18), anchor="center") #change the lamp in a yellow box in the centre
            change_lamp_box.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="WE")
    elif fixture == "BMFL":
        hours_remaining = 750 - hours #Max recommended lamp hours from the manual
        result_output.config(text=str(hours_remaining), font=("Arial", 14), bg="green") #GREEN BOX!
        change_lamp_message.config(text="")
        if hours_remaining >= 500: #see above note, but 500hrs.
            change_lamp_box = tk.Label(root, text="CHANGE THE LAMP", bg="yellow",font=("Arial", 18), anchor="center")
            change_lamp_box.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="WE")
    else:
        tk.messagebox.showerror("Error", "Invalid fixture selection.")

#DO NOT TOUCH ANYTHING BELOW THIS!

def clear_handler(): #makes the clear function work
    fixture_select.configure(text=fixture_options[0]) #sets the menu
    hours_input.delete(0, tk.END) #clears content of hours_input
    result_output.config(text="") #clears content of result_output
    change_lamp_message.config(text="") #clears change lamp message
    for widget in root.winfo_children(): #these make sure the widget functions work
        if isinstance(widget, tk.Label) and widget.cget("bg") == "yellow": #these make sure the widgets functions work
            widget.destroy() #gets rid of change lamp message if leftover

calculate_btn.config(command=calculate_handler) #makes the calculate button work
clear_btn.config(command=clear_handler) #makes the clear button work

root.mainloop() #keeps the window open so user can keep using
