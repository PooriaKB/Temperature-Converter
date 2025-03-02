import tkinter as tk
import string

# A Function For Converting Fahrenheit to Celsius
def fahrenheit_to_celsius():
    if validate():
        pass
    else:
        value = float(temp_value.get())
        celsius_value = ( value - 32 )*(5/9)
        temp_value.delete(0,tk.END)
        temp_value.insert(0,celsius_value)

# A Function For Converting Celsius to Fahrenheit
def celsius_to_fahrenheit():
    if validate():
        pass
    else:
        value = float(temp_value.get())
        fahrenheit_value = (value*1.8)+32
        temp_value.delete(0,tk.END)
        temp_value.insert(0,fahrenheit_value)
    
# A Function For Getting Only Digits Not Letters
def validate():
    entry = temp_value.get()
    alphabet = list(string.ascii_lowercase + string.ascii_uppercase)
    for letter in entry:
        if letter in alphabet :
            temp_value.delete(0,tk.END)
            temp_value.insert(0,"Enter Digits Not Letters")
            return True
# A Function For Clearing Guide Text
def on_focus_in(event):
    temp_value.delete(0,tk.END)
            
    
# Application Definition
root = tk.Tk()
root.title("TempConverter")

# Determining The Main Window Size
root.geometry("550x60")
root.resizable(height=False , width=False)

# Specifying An Entry For Temp Value And Two Button For C & F  Temps Converters
root.rowconfigure(0 , minsize =60 , weight=1)
root.columnconfigure([0,1,2] , minsize=60 , weight=1)

# Temp Value Goes Here
guide_text = "Enter Your Temp In F or C To Convert To Desired Unit Use The Unit Button"
temp_value = tk.Entry(bg="black" , fg="white" , width=200)
# A place Holder For How To Use The App
temp_value.insert(0,guide_text)
temp_value.grid(row=0 , column=0 , sticky="nsew")
temp_value.bind("<FocusIn>",on_focus_in)

# A Button For Converting to Celsius 
celsius_btn = tk.Button(
    text="\N{DEGREE CELSIUS}", 
    font=("TkDefaultFont",16 ,"bold"),
    command=fahrenheit_to_celsius)
celsius_btn.grid(row=0 , column=2, sticky="nsew")

# A Button for Converting to Fahrenheit
fahrenheit_btn = tk.Button(
    text="\N{DEGREE FAHRENHEIT}", 
    font=("TkDefaultFont",16),
    command=celsius_to_fahrenheit)
fahrenheit_btn.grid(row=0 , column=1 , sticky="nsew" )


root.mainloop()