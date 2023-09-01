"""Add substraction, multiplication and division buttons"""

from tkinter import *

root = Tk()
root.title = "Simple Calculator"

def myClick():
    greet = "Hello " + e.get()
    myLabel = Label(root, text = greet).pack()

def button_clear():
    e.delete(0,END)

def button_click(button):
    global val1 
    if button == "+":
        val1 = e.get()
        button_clear()
    elif button == "=":
        val2 = e.get()
        button_clear()
        e.insert(0, int(val1)+int(val2))
    else:
        e.insert(END, button)

e = Entry(root, width = 40, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
#e.insert(0,"")

b0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click("0"))
b1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click("1"))
b2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click("2"))
b3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click("3"))
b4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click("4"))
b5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click("5"))
b6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click("6"))
b7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click("7"))
b8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click("8"))
b9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click("9"))
b_add = Button(root, text = "+", padx = 39, pady = 20, command = lambda: button_click("+"))
b_equal = Button(root, text = "=", padx = 39, pady = 20, command = lambda: button_click("="))
b_clear = Button(root, text = "Clear", padx = 29, pady = 20, command = button_clear)


b0.grid(row=4, column = 0)
b1.grid(row=3, column = 0)
b2.grid(row=3, column = 1)
b3.grid(row=3, column = 2)
b4.grid(row=2, column = 0)
b5.grid(row=2, column = 1)
b6.grid(row=2, column = 2)
b7.grid(row=1, column = 0)
b8.grid(row=1, column = 1)
b9.grid(row=1, column = 2)
b_add.grid(row=4, column = 1)
b_equal.grid(row=4, column = 2)
b_clear.grid(row=5, column = 2)

root.mainloop()