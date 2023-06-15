import tkinter as tk

calculator = ""
def clear():
    global calculator
    calculator=""
    result_screen.delete(1.0, "end")

def press(symbol):
    global calculator
    calculator += str(symbol)
    result_screen.delete(1.0,"end")
    result_screen.insert(1.0, calculator)

def evaluate():
    global calculator
    try:
        calculator=str(eval(calculator))
        result_screen.delete(1.0,"end")
        result_screen.insert(1.0, calculator)
    except:
        clear()
        result_screen.insert(1.0,"error")


gui = tk.Tk()
gui.title('Calculator')
gui.geometry("360x590")
gui.configure(background='#2A363B')

result_screen=tk.Text(gui, height=5, width=24, font=("Brush Script Std",20),fg='white',bg='#6C5B7B')
result_screen.grid(row=1, column=1, columnspan=4)
button_1=tk.Button(gui, text='1', fg='#2A363B', bg='#FF847C', command=lambda: press("1"),height=2, width=5,
                   font=("Brush Script Std",20))
button_1.grid(row=3, column=1)
button_2=tk.Button(gui, text='2', fg='#2A363B', bg='#FF847C', command=lambda: press("2"),height=2, width=5,
                   font=("Brush Script Std",20))
button_2.grid(row=3, column=2)
button_3=tk.Button(gui, text='3', fg='#2A363B', bg='#FF847C', command=lambda: press("3"),height=2, width=5,
                   font=("Brush Script Std",20))
button_3.grid(row=3, column=3)
button_4=tk.Button(gui, text='4', fg='#2A363B', bg='#FF847C', command=lambda: press("4"),height=2, width=5,
                   font=("Brush Script Std",20))
button_4.grid(row=4, column=1)
button_5=tk.Button(gui, text='5', fg='#2A363B', bg='#FF847C', command=lambda: press("5"),height=2, width=5,
                   font=("Brush Script Std",20))
button_5.grid(row=4, column=2)
button_6=tk.Button(gui, text='6', fg='#2A363B', bg='#FF847C', command=lambda: press("6"),height=2, width=5,
                   font=("Brush Script Std",20))
button_6.grid(row=4, column=3)
button_7=tk.Button(gui, text='7', fg='#2A363B', bg='#FF847C', command=lambda: press("7"),height=2, width=5,
                   font=("Brush Script Std",20))
button_7.grid(row=5, column=1)
button_8=tk.Button(gui, text='8', fg='#2A363B', bg='#FF847C', command=lambda: press("8"),height=2, width=5,
                   font=("Brush Script Std",20))
button_8.grid(row=5, column=2)
button_9=tk.Button(gui, text='9', fg='#2A363B', bg='#FF847C', command=lambda: press("9"),height=2, width=5,
                   font=("Brush Script Std",20))
button_9.grid(row=5, column=3)
button_0=tk.Button(gui, text='0', fg='#2A363B', bg='#FF847C', command=lambda: press("0"),height=2, width=5,
                   font=("Brush Script Std",20))
button_0.grid(row=6, column=2)
button_C=tk.Button(gui, text='C', fg='#2A363B', bg='#FF847C', command=clear,height=2, width=5,
                   font=("Brush Script Std",20))
button_C.grid(row=2, column=1)
button_dot=tk.Button(gui, text='.', fg='#2A363B', bg='#FF847C', command=lambda: press("."),height=2, width=5,
                   font=("Brush Script Std",20))
button_dot.grid(row=6, column=1)
button_open=tk.Button(gui, text='(', fg='#2A363B', bg='#FF847C', command=lambda: press("("),height=2, width=5,
                   font=("Brush Script Std",20))
button_open.grid(row=2, column=2)
button_close=tk.Button(gui, text=')', fg='#2A363B', bg='#FF847C', command=lambda: press(")"),height=2, width=5,
                   font=("Brush Script Std",20))
button_close.grid(row=2, column=3)
button_mul=tk.Button(gui, text='*', fg='#2A363B', bg='#c06c84', command=lambda: press("*"),height=2, width=5,
                   font=("Brush Script Std",20))
button_mul.grid(row=4, column=4)
button_div=tk.Button(gui, text='/', fg='#2A363B', bg='#c06c84', command=lambda: press("/"),height=2, width=5,
                   font=("Brush Script Std",20))
button_div.grid(row=5, column=4)
button_sub=tk.Button(gui, text='-', fg='#2A363B', bg='#c06c84', command=lambda: press("-"),height=2, width=5,
                   font=("Brush Script Std",20))
button_sub.grid(row=3, column=4)
button_add=tk.Button(gui, text='+', fg='#2A363B', bg='#c06c84', command=lambda: press("+"),height=2, width=5,
                   font=("Brush Script Std",20))
button_add.grid(row=2, column=4)
button_equal=tk.Button(gui, text='=', fg='#2A363B', bg='#c06c84', command=evaluate,height=2, width=11,
                   font=("Brush Script Std",20))
button_equal.grid(columnspan=2, column=3, row=6)

gui.mainloop()