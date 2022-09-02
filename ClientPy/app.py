from tkinter import* 
import register
import login
import register
import requests
import login
import mainpage
import ticket
import bill
import preventive
import invoices

from tkinter import messagebox

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

class windows(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.wm_title("Test Application")
        self.geometry("900x600+0+0")

        container = Frame(self, height=500, width=1000)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (login.LoginFrame, register.Register,  mainpage.MainPage, ticket.Ticket, preventive.PreventiveId, preventive.PreventiveAll,invoices.Invoices, bill.Bill):
            frame = F(container, self)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(login.LoginFrame)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()






if __name__ == "__main__":
    testObj = windows()
    testObj.mainloop()