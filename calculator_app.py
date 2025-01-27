import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Calculator")
root.geometry("500x600")

def button_click(value):
  x=display_var.get()
  display_var.set(x+value)

def calculate():
  try:
    y= eval(display_var.get())
    display_var.set(y)
  except Exception as e:
    display_var.set(e)  

display_var=tk.StringVar()
display=ttk.Entry(root,textvariable=display_var, font=('arial',14),justify='right')

display.grid(row=0, column=0, columnspan=4, sticky='ewns',padx=5,pady=5)

button_seven=ttk.Button(root, text="7", command=lambda: button_click('7'))
button_seven.grid(row=1, column=0, padx=5, pady= 5, sticky="ewsn")

button_eight=ttk.Button(root, text='8', command=lambda: button_click('8'))
button_eight.grid(row=1, column=1, padx=5, pady=5, sticky='ewsn')

button_nine=ttk.Button(root, text='9', command=lambda: button_click('9'))
button_nine.grid(row=1, column=2, padx=5, pady=5, sticky='ewsn')

button_div=ttk.Button(root, text='/', command= lambda: button_click('/'))
button_div.grid(row=1, column=3, padx=5, pady=5, sticky='ewsn')

button_four=ttk.Button(root, text="4", command=lambda: button_click('4'))
button_four.grid(row=2, column=0, padx=5, pady= 5, sticky="ewsn")

button_five=ttk.Button(root, text='5', command=lambda: button_click('5'))
button_five.grid(row=2, column=1, padx=5, pady=5, sticky='ewsn')

button_six=ttk.Button(root, text='6', command=lambda: button_click('6'))
button_six.grid(row=2, column=2, padx=5, pady=5, sticky='ewsn')

button_mul=ttk.Button(root, text='*', command= lambda: button_click('*'))
button_mul.grid(row=2, column=3, padx=5, pady=5, sticky='ewsn')

button_one=ttk.Button(root, text="1", command=lambda: button_click('1'))
button_one.grid(row=3, column=0, padx=5, pady= 5, sticky="ewsn")

button_two=ttk.Button(root, text='2', command=lambda: button_click('2'))
button_two.grid(row=3, column=1, padx=5, pady=5, sticky='ewsn')

button_three=ttk.Button(root, text='3', command=lambda: button_click('3'))
button_three.grid(row=3, column=2, padx=5, pady=5, sticky='ewsn')

button_sub=ttk.Button(root, text='-', command= lambda: button_click('-'))
button_sub.grid(row=3, column=3, padx=5, pady=5, sticky='ewsn')

button_zero=ttk.Button(root, text="0", command=lambda: button_click('0'))
button_zero.grid(row=4, column=0, padx=5, pady= 5, sticky="ewsn")

button_dot=ttk.Button(root, text='.', command=lambda: button_click('.'))
button_dot.grid(row=4, column=1, padx=5, pady=5, sticky='ewsn')

button_equal=ttk.Button(root, text='=', command=calculate)
button_equal.grid(row=4, column=2, padx=5, pady=5, sticky='ewsn')

button_sum=ttk.Button(root, text='+', command= lambda: button_click('+'))
button_sum.grid(row=4, column=3, padx=5, pady=5, sticky='ewsn')

button_clear=ttk.Button(root, text='c', command=lambda: display_var.set(''))
button_clear.grid(row=5, column=0, columnspan=4,padx=5, pady=5, sticky='ewsn')


for i in range(6):
  root.rowconfigure(i, weight=1)

for j in range(4):
  root.columnconfigure(j, weight=1)  

root.mainloop()