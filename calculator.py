import tkinter as tk
from tkinter import messagebox

def add_number(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)

def add_operation(operation):
    value = calc.get()
    if value[-1] in '**-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)

def calculate():
    value = calc.get()
    if value[-1] in '-**/+*':
        value = value + value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Введите цифры')
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Нельзя это делать')

def test3(digit):
    value = calc.get()

def make_clear():
    calc.delete(0, tk.END)
    calc.insert(0, 0)

def make_number_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 13), command=lambda: add_number(digit))

def make_operation(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), command=lambda: add_operation(operation))

def result(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), command=calculate)

def func_make_clear(operation):
    value = calc.get()
    return tk.Button(text=operation, bd=5, font=('Arial', 13), command=make_clear)

def make_remove(digit):
    value = calc.get()
    return tk.Button(text=digit, bd=5, font=('Arial', 13), command=test3)

def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_number(event.char)
    elif event.char in '+-*/**':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()

def number_pi(digit):
    return tk.Button(text='Pi', bd=5, font=('Arial', 13), command=lambda: add_number(digit))

window = tk.Tk()
window.title('Calculator')
window.geometry('280x325+100+200')
window.config(background='black')
photo = tk.PhotoImage(file='photo.png')
window.iconphoto(False, photo)

window.bind('<Key>', press_key)

calc = tk.Entry(window, justify=tk.RIGHT, font=('Arial', 15), width=25)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='we')

make_number_button('7').grid(row=1, column=0, sticky='wens', padx=5, pady=5)
make_number_button('8').grid(row=1, column=1, sticky='wens', padx=5, pady=5)
make_number_button('9').grid(row=1, column=2, sticky='wens', padx=5, pady=5)
make_number_button('4').grid(row=2, column=0, sticky='wens', padx=5, pady=5)
make_number_button('5').grid(row=2, column=1, sticky='wens', padx=5, pady=5)
make_number_button('6').grid(row=2, column=2, sticky='wens', padx=5, pady=5)
make_number_button('1').grid(row=3, column=0, sticky='wens', padx=5, pady=5)
make_number_button('2').grid(row=3, column=1, sticky='wens', padx=5, pady=5)
make_number_button('3').grid(row=3, column=2, sticky='wens', padx=5, pady=5)
make_number_button('0').grid(row=4, column=1, sticky='wens', padx=5, pady=5)
make_number_button('.').grid(row=5, column=2, sticky='wens', padx=5, pady=5)
number_pi('3.14').grid(row=4, column=0, sticky='wens', padx=5, pady=5)

make_operation('+').grid(row=3, column=3, sticky='wens', padx=5, pady=5)
make_operation('-').grid(row=4, column=3, sticky='wens', padx=5, pady=5)
make_operation('/').grid(row=1, column=3, sticky='wens', padx=5, pady=5)
make_operation('*').grid(row=2, column=3, sticky='wens', padx=5, pady=5)
result('=').grid(row=5, column=3, sticky='wens', padx=5, pady=5)
func_make_clear('C').grid(row=5, column=1, sticky='wens', padx=5, pady=5)
make_remove('<').grid(row=5, column=0, sticky='wens', padx=5, pady=5)
make_operation('**').grid(row=4, column=2, sticky='wens', padx=5, pady=5)



window.grid_columnconfigure(0, minsize=60)
window.grid_columnconfigure(1, minsize=60)
window.grid_columnconfigure(2, minsize=60)
window.grid_columnconfigure(3, minsize=60)

window.grid_rowconfigure(1, minsize=60)
window.grid_rowconfigure(2, minsize=60)
window.grid_rowconfigure(3, minsize=60)
window.grid_rowconfigure(4, minsize=60)
window.grid_rowconfigure(5, minsize=60)

window.mainloop()
