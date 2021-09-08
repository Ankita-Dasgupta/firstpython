import turtle


import tkinter as tk
pen = turtle.Turtle()

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart():
    pen.fillcolor('pink')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

def txt():
    pen.up()
    pen.setpos(-68, 95)
    pen.down()
    pen.color('deep pink')
    style = ('Courier', 12, 'bold')
    pen.write(" heart ", font=style)

heart()
txt()
pen.ht()
tk.mainloop()
turtle.done()
tk._exit()