from curses import window
from logging import root
from tkinter import* 
from tkinter import ttk, messagebox
import logins
import register
from typing import Dict

payload = {
        'nome': ' ',
        'cognome': ' ',
        'professione': ' ',
        'partitaiva': ' ',
        'citta': ' ',
        'indirizzo': ' ',
        'telefono': ' ',
        'email': ' ',
        'password': ' '}

session = {'email': ' ',
           'logged': 0
          }

class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()
    

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)

class MainView(Frame):
    print(Frame)
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = register.Register(self)
        p2 = logins.Login(self)
        p3 = Page3(self)

        print(p1)

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Button(buttonframe, text="Registration", command=p1.show)
        b2 = Button(buttonframe, text="Login", command=p2.show)
        b3 = Button(buttonframe, text="Main Menu", command=p3.show)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()

def main():
    root = Tk()
    root.config(bg="white")
    root.title("INSTAFIX")
    main = MainView(root)
   # obj = register.Register(root)
    main.pack(side="top", fill="both", expand=True)
    root.geometry("1350x700+0+0") # Resolution of the page , top, bottom
    root.mainloop()

if __name__ == "__main__":
    main()




