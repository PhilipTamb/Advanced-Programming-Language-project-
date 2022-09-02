import tkinter as tk
from tkinter import ttk

from logging import root
from tkinter import* 
from tkinter import ttk, messagebox
from turtle import width
import requests
import logins
import register
import home
import ticket
import preventive
import invoices
import logout
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

        
def getnome():
    print("getnome")
    url = 'http://localhost:8000/getnomeprofessionist'

    print("email " + session['email'])

    credentials = { 'email': session['email']}

    print("credentials " + credentials["email"])

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, data=credentials, headers=headers)

    print("Status code: ", response.status_code)
    print("text: ", response.text)
    return response.text

class MainView(Frame):
        print("MainView")
        print("in login MainView type :" + str(type(Frame)))
        def __init__(self, *args, **kwargs):
            Frame.__init__(self, *args, **kwargs)
            
            p1 = home.Home(self)
            p2 = ticket.Ticket(self)
            #p3 = preventive.Preventive(self)
            #p4 = invoices.Invoices(self)
            #p5 = logout.Logout(self)

            buttonframe = Frame(self, highlightbackground="blue", highlightthickness=2, width=700, height=250)
            container = Frame(self, highlightbackground="green", highlightthickness=2, width=700, height=250)
            buttonframe.pack(side="left")
            container.pack(side="top", fill="both", expand=True)

            
            p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            #p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            #p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            #p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

            

            b1 = Button(buttonframe, text="Home", command=p1.show)
            b2 = Button(buttonframe, text="Ticket", command=p2.show)
            #b3 = Button(buttonframe, text="Preventive", command=p3.show)
            #b4 = Button(buttonframe, text="Invoices", command=p4.show)
            #b5 = Button(buttonframe, text="Logout", command=p5.show)

            nome = getnome()

            n = Label(buttonframe, text="Benvenuto " + nome, font=("times new roman", 15, "bold"), bg="white", fg="gray")
            n.grid(row = 1, column = 0, pady = 10, padx = 10)
            b1.grid(row = 3, column = 0, pady = 10, padx = 10)
            b2.grid(row = 5, column = 0, pady = 10, padx = 10)
            #b3.grid(row = 7, column = 0, pady = 10, padx = 10)
            #b4.grid(row = 9, column = 0, pady = 10, padx = 10)
            #b5.grid(row = 10, column = 0, pady = 10, padx = 10)

            p1.show()

class App:
    def __init__(self):
        print(type(self))

        self.root = tk.Tk()
        
        if session["logged"]  == 0 :
            self.login = logins.LoginFrame(self.root)
            self.login.pack(side="top", fill="both", expand=True)
        
        if session["logged"]  == 1 :
            print("logged")

            #self.view = self.MainView(self.root)
            self.view = self.Treeview(self)
            self.view.pack(side="top", fill="both", expand=True)
    
        self.root.geometry("900x600+0+0") # Resolution of the page , top, bottom
        self.root.mainloop()


def getTicketProfessionist():
        print("getTicketProfessionist")
        url = 'http://localhost:8000/geticketsprofessionist'

        #print("email " + session['email'])
        credentials = { 'email': session['email']}
        #print("credentials " + credentials["email"])
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(url, data=credentials, headers=headers)

        #print("Status code: ", response.status_code)
        print("text: ", response.text)
        return response.json() 

if __name__ == "__main__":
    app = App()
