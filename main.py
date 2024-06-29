from tkinter import *

def calculate():
    miles = float(input_miles.get())
    km = miles * 1.609
    input_km.config(text=f"{km}")

window = Tk()
window.title("Miles to Km converter")
window.minsize(width=400, height=200)

#Label_equal_to
equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=6000, row=30)

#Label_miles
miles_label = Label(text="Miles", font=("Arial", 12, "normal"))
miles_label.config(text="Miles")
miles_label.grid(column=9900, row=6)

#Input_miles
input_miles = Entry(width=10)
input_miles.grid(column=9000, row=6)

#Label_km
Km_label = Label(text="Km", font=("Arial", 12, "normal"))
Km_label.config(text="Km")
Km_label.grid(column=9900, row=30)

#Input_km
input_km = Label(text=f"0")
input_km.grid(column=9000, row=30)

#Button converter
button = Button(text="Calculate", command=calculate)
button.grid(column=9000, row=40)


window.mainloop()