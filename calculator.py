""" --Calculator-- """


# pip install tkinter
from tkinter import Tk, Entry, Button, StringVar


class Calculator:
    def __init__(self, app):  
        app.title('Calculator')
        app.geometry('357x420+0+0')
        app.config(bg='black')

        self.equation = StringVar()
        self.entry_value = ''

        # Entry widget placement and styling
        Entry(app, width=17,bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # button placements and styling
        Button(app, width=11, height=4, text='(', relief='flat', bg='white', command=lambda: self.show('(')).place(x=0, y=50)
        Button(app, width=11, height=4, text=')', relief='flat', bg='white', command=lambda: self.show(')')).place(x=90, y=50)
        Button(app, width=11, height=4, text='%', relief='flat', bg='white', command=lambda: self.show('%')).place(x=180, y=50)
        Button(app, width=11, height=4, text='1', relief='flat', bg='white', command=lambda: self.show(1)).place(x=0, y=125)
        Button(app, width=11, height=4, text='2', relief='flat', bg='white', command=lambda: self.show(2)).place(x=90, y=125)
        Button(app, width=11, height=4, text='3', relief='flat', bg='white', command=lambda: self.show(3)).place(x=180, y=125)
        Button(app, width=11, height=4, text='4', relief='flat', bg='white', command=lambda: self.show(4)).place(x=0, y=200)
        Button(app, width=11, height=4, text='5', relief='flat', bg='white', command=lambda: self.show(5)).place(x=90, y=200)
        Button(app, width=11, height=4, text='6', relief='flat', bg='white', command=lambda: self.show(6)).place(x=180, y=200)
        Button(app, width=11, height=4, text='7', relief='flat', bg='white', command=lambda: self.show(7)).place(x=0, y=275)
        Button(app, width=11, height=4, text='8', relief='flat', bg='white', command=lambda: self.show(8)).place(x=90, y=275)
        Button(app, width=11, height=4, text='9', relief='flat', bg='white', command=lambda: self.show(9)).place(x=180, y=275)
        Button(app, width=11, height=4, text='0', relief='flat', bg='white', command=lambda: self.show(0)).place(x=90, y=350)
        Button(app, width=11, height=4, text='.', relief='flat', bg='white', command=lambda: self.show('.')).place(x=180, y=350)
        Button(app, width=11, height=4, text='+', relief='flat', bg='white', command=lambda: self.show('+')).place(x=270, y=200)
        Button(app, width=11, height=4, text='-', relief='flat', bg='white', command=lambda: self.show('-')).place(x=270, y=275)
        Button(app, width=11, height=4, text='/', relief='flat', bg='white', command=lambda: self.show('/')).place(x=270, y=50)
        Button(app, width=11, height=4, text='x', relief='flat', bg='white', command=lambda: self.show('*')).place(x=270, y=125)
        Button(app, width=11, height=4, text='=', relief='flat', bg='white', command=self.solve).place(x=270, y=350)
        Button(app, width=11, height=4, text='C', relief='flat', bg='white', command=self.clear).place(x=0, y=350)

# It will convert the input value into string
    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

# This sets it to an empty string
    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

# This method will evaluate the expression stored in self.entry_value.
    def solve(self):
        try:
            result = eval(self.entry_value) 
            self.equation.set(result)
        except Exception as e:
            self.equation.set('Error')

# Running the application
root = Tk()
# Initializing the calculator class, passing the root as the main window
calculator = Calculator(root)
# this will keeps the application running untill the user closes it.
root.mainloop()
