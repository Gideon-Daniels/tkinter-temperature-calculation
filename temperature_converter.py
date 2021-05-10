from tkinter import *

window = Tk()

window.geometry("750x500")  # Setting screen size (width,height)
window.title("Temperature Converter")

c_input = StringVar()
f_input = StringVar()
results = StringVar()

# Functions
def activate_celsius_converter():
    c_entry.configure(state="normal")
    celsius_to_fahrenheit_label.configure(state="normal")
    f_entry.configure(state="readonly")
    fahrenheit_to_celsius_label.configure(state="disabled")


def activate_fahrenheit_converter():
    f_entry.configure(state="normal")
    fahrenheit_to_celsius_label.configure(state="normal")
    c_entry.configure(state="readonly")
    celsius_to_fahrenheit_label.configure(state="disabled")


def clear():
    c_entry.configure(state="normal")
    f_entry.configure(state="normal")
    c_entry.delete(0, END)
    f_entry.delete(0, END)
    results.set(" ")
    # celsius_to_fahrenheit_label.configure(state="disabled")
    # fahrenheit_to_celsius_label.configure(state="disabled")


def conversion():
    get_number = float(c_entry.get())
    get_number_two = float(f_entry.get())
    f = get_number * 9/5 + 32  # Formulae for celsius to fahrenheit conversion
    c = (get_number_two - 32) * 5/9 # Formulae for fahrenheit to celsius conversion
    output = "Celsius To Fahrenheit = " + "\t" + str(f) + "\n" + "Fahrenheit To Celsius = " + "\t" + str(c)
    return results.set(output)


def exit_program():
    return window.destroy()


# Entry widget
c_entry = Entry(window, textvariable=c_input, state=DISABLED)
f_entry = Entry(window, textvariable=f_input, state=DISABLED)

# Label
results_label = Label(window, textvariable=results, bg="green", width=35, height=10,)
celsius_to_fahrenheit_label = Label(window, text="Celsius To Fahrenheit", state=DISABLED)
fahrenheit_to_celsius_label = Label(window, text="Fahrenheit To Celsius", state=DISABLED)

# Button widgets
# Activation Buttons
activate_c_button = Button(window, text="Activate Celsius to Fahrenheit Converter", command=activate_celsius_converter)
activate_f_button = Button(window, text="Activate Fahrenheit to Celsius Converter",
                           command=activate_fahrenheit_converter)

# Calculation Button
calc_conversion_button = Button(window, text="Calculating Conversion", command=conversion)

# Exit and Clear Buttons
exit_button = Button(window, text="Exit", command=exit_program)
clear_button = Button(window, text="Clear", command=clear)

# placing widgets
# Placing Labels
celsius_to_fahrenheit_label.place(x=200, y=100)
fahrenheit_to_celsius_label.place(x=500, y=100)
results_label.place(x=300, y=300)

# Placing text entries
c_entry.place(x=200, y=150)
f_entry.place(x=500, y=150)

# Placing Buttons
activate_c_button.place(x=200, y=250)
activate_f_button.place(x=500, y=250)
calc_conversion_button.place(x=100, y=300)
clear_button.place(x=600, y=300)
exit_button.place(x=600, y=350)

window.mainloop()
