# import tkinter as tk
#
# # window details
# window = tk.Tk()
# window.title('My first Gui Project')
# window.minsize(width=500, height=400)
# window.config(padx=30, pady=30)
#
# # label
# my_label = tk.Label(text='I am a label', font=('Calibri', 24, 'bold'))
# my_label.grid(column=0, row=0)  # place and center on top of the screen
#
#
# # my_label.pack(side='left')  # place and left align on screen
# # my_label.pack(expand=True) # place and center in middle of screen
#
# def button_click():
#     my_label.config(text=f'{input.get().title()}')
#
#
# # Button
# button = tk.Button(text='Monitoring, click here', command=button_click)
# button.grid(column=1, row=1)
#
# # new button
# button2 = tk.Button(text='oderint dum metuant', font=('Lucida Sans', 30, 'normal'))
# button2.grid(column=2,row=0)
#
# # input boxes for entry
# input = tk.Entry(width=10)
# input.grid(column=3, row=2)
#
#
#
# # always at the end of code
# window.mainloop()

import tkinter as tk

window = tk.Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=200)
window.config(pady=20, padx=20)

# Entry
miles_entry = tk.Entry()
miles_entry.grid(column=1, row=0)

# miles label
miles_label = tk.Label(text='Miles')
miles_label.grid(row=0, column=2)

# equal label
equal_label = tk.Label(text='is equal to')
equal_label.grid(row=1, column=0)

# KM label
km_label = tk.Label(text='KM')
km_label.grid(row=1, column=2)

# converted num
num = tk.Label(text='')
num.grid(row=1, column=1)


# Convert mile
def convert():
    num.config(text=round(float(miles_entry.get()) / 0.62137273664980675307890191009979, 2))


# Calc button
calc_btn = tk.Button(text='Calculate', command=convert)
calc_btn.grid(row=3, column=1)

window.mainloop()
