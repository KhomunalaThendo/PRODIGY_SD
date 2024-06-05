

import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()
root.geometry("400x300")
root.title("Temperature Convertion")

#Temperature conversion 

def celsius_to_fahrenheit(Celsius):
    return (Celsius * 9/5) +32
    

def celsius_to_kelvin(Celsius):
    return  Celsius+ 273.15
    

def kelvin_to_fahrenheit(Kelvin):
      return (Kelvin - 273.15) * 9/5 + 32
    
def kelvin_to_celsius(Kelvin):
    return Kelvin - 273.15
    

def fahrenheit_to_kelvin(Fahrenheit):
    return (Fahrenheit + 459.67) * 5/9


def fahrenheit_to_celsius(Fahrenheit):
    return (Fahrenheit - 32) * 5/9


def convert_temperature():
    
        value = float(entry.get())
        initial_temp = optionmenu.get()

        if initial_temp == "Celsius":
          fahrenheit_results =   celsius_to_fahrenheit(value)
          kelvin_results =    celsius_to_kelvin(value)
          result_label.configure(text=f"Fahrenheit: {fahrenheit_results:.2f} °F\nKelvin Scale: {kelvin_results:.2f} °K")

        elif initial_temp == "Kelvin Scale":
          celsius_results= kelvin_to_celsius(value)
          fahrenheit_results = kelvin_to_fahrenheit(value)
          result_label.configure(text=f"Celsius: {celsius_results:.2f} °C\nFahrenheit: {fahrenheit_results:.2f} °F")
        
        elif initial_temp == "Fahrenheit":
             kelvin_results = fahrenheit_to_kelvin(value)
             celsius_results = fahrenheit_to_celsius(value)
             result_label.configure(text=f"Celsius: {celsius_results:.2f} °C\nKelvin: {kelvin_results:.2f} K")

             
      

Label = customtkinter.CTkLabel(root, text="Choose initial temperature unit")
Label.pack(padx=20, pady=5)



optionmenu = customtkinter.CTkOptionMenu(root, values=["Celsius", "Fahrenheit", "Kelvin Scale"],)
optionmenu.set("Celsius")
optionmenu.pack(padx = 20, pady= 15)

entry = customtkinter.CTkEntry(root, placeholder_text="Enter temperature")
entry.pack(pady = 10)



button = customtkinter.CTkButton(master=root, text="Convert", command=convert_temperature)
#button.place(relx = 0.5, rely= 0.5, anchor=customtkinter.CENTER)
button.pack(padx= 0, pady=10)

result_label = customtkinter.CTkLabel(root, text="Results:")
result_label.pack(pady=10)

result_label = customtkinter.CTkLabel(root, text="")
result_label.pack(padx=20, pady=10)

root.mainloop()