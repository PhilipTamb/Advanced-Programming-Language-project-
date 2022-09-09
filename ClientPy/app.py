from tkinter import* 
import register
import login
import register
import login
import mainpage
import ticket
import bill
import preventive
import invoices

session = {'id': ' ',
           'logged': 0
          }

class windows(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.wm_title("INSTAFIX")
        self.geometry("900x600+0+0")
        container = Frame(self, height=500, width=1000)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        for F in (login.LoginFrame, register.Register,  mainpage.MainPage, ticket.Ticket, preventive.PreventiveId, preventive.PreventiveAll,invoices.Invoices, bill.Bill):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(login.LoginFrame)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    testObj = windows()
    testObj.mainloop()