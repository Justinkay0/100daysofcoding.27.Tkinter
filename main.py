import tkinter as tk

# window details
window = tk.Tk()
window.title('My first Gui Project')
window.minsize(width=500, height=400)

# label
my_label = tk.Label(text='I am a label', font=('Calibri', 24, 'bold'))
my_label.grid(column=0, row=0)  # place and center on top of the screen


# my_label.pack(side='left')  # place and left align on screen
# my_label.pack(expand=True) # place and center in middle of screen

def button_click():
    my_label.config(text=f'{input.get().title()}')


# Button
button = tk.Button(text='Monitoring, click here', command=button_click)
button.grid(column=1, row=1)

# new button
button2 = tk.Button(text='oderint dum metuant', font=('Lucida Sans', 30, 'normal'))
button2.grid(column=2,row=0)

# input boxes for entry
input = tk.Entry(width=10)
input.grid(column=3, row=2)



# always at the end of code
window.mainloop()
