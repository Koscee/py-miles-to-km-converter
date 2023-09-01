from tkinter import *


def convert():
    miles = miles_input.get()
    miles = float(miles) if miles else 0
    kilometers = round(miles * 1.609, 3)
    km_value["text"] = kilometers


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=100, pady=100)

miles_input = Entry(width=10, font=("Courier", 14, "bold"))
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles", font=("Arial", 11, "bold"))
miles_label.config(padx=10, pady=10)
miles_label.grid(row=0, column=2)

is_equal_to_label = Label(text="⇅", font=("Arial", 24, "bold"))
is_equal_to_label.config(pady=10)
is_equal_to_label.grid(row=1, column=1)

km_value = Label(text="0", font=("Courier", 14, "bold"))
km_value.config(padx=10, pady=20)
km_value.grid(row=2, column=1)

km_label = Label(text="Km", font=("Arial", 11, "bold"))
km_label.config(padx=10, pady=10)
km_label.grid(row=2, column=2)

cal_btn = Button(text="Calculate", font=("Tahoma", 13), command=convert)
cal_btn.grid(row=3, column=1)

window.mainloop()
