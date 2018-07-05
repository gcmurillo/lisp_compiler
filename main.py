from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Frame, Label, Entry
from lisp_parser import validate

class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Lambda Lisp Compiler")
        self.pack(fill=BOTH, expand=True)
        global value
        value = 0
        global expr
        expr = StringVar()
        global res
        res = StringVar()

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Lambda Expression :", width=18)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1,textvariable=expr)
        entry1.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        btnplus = Button(frame3, text="Validate", width=8, command=self.validate)
        btnplus.pack(side=LEFT, anchor=N, padx=5, pady=5)

        frame4 = Frame(self)
        frame4.pack(fill=X)

        lbl3 = Label(frame4, text="Result :", width=10)
        lbl3.pack(side=LEFT, padx=5, pady=5)

        result = Entry(frame4,textvariable=res)
        result.pack(fill=X, padx=5, expand=True)

    def errorMsg(self,msg):
        if msg == 'error':
            tkinter.messagebox.showerror('Error!', 'Enter your expression')

    def validate(self):
        if expr.get() == '':
            self.errorMsg('error')
        else:
            result = validate(expr.get())
            res.set(result)

def main():
    root = Tk()
    root.geometry("300x140")
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()