import tkinter as tk
from tkinter import *
from functools import partial


def Loginform():
    window = tk.Tk()
    window.title("INSTAFIX")
    window.geometry("650x700")
    window.configure(background = "gray")

    variable = StringVar(window)
    variable.set("Seleziona la Professione") # default value
    option_wrk = ["Edilizia", "Idraulica","Giardinaggio","Climatizzazione e riscaldamento","Telecomunicazioni","Rete elettrica ed elettrodomestici"]

    title = nomeForm = Label(window, text = "Registrati", font="ar 18 bold",borderwidth=2,relief="groove",width = 6, height = 1).grid(row = 1, column = 2, ipadx="50",ipady="15",padx="30",pady="30")
    nomeForm = Label(window, text = "Nome: ", font="ar 12 bold",borderwidth=2, relief="groove",width = 6, height = 1 ).grid(row = 2, column = 1, ipadx="40",ipady="5",padx="20",pady="10")
    cognomeForm = Label(window, text = "Cognome: ", font="ar 12 bold",borderwidth=2,relief="groove",width = 6, height = 1).grid(row = 3, column = 1,ipadx="40",ipady="5",padx="20",pady="10")
    professioneForm = Label(window, text = "Professione: ",font="ar 12 bold",borderwidth=2,relief="groove",width = 6, height = 1).grid(row = 4, column = 1,ipadx="40",ipady="5",padx="20",pady="10")
    partita_ivaForm = Label(window, text = "Partita IVA: ",font="ar 12 bold",borderwidth=2,relief="groove",width = 6, height = 1).grid(row = 5, column = 1,ipadx="40",ipady="5",padx="20",pady="10")
    #cittaForm = Label(window, text = "Citta: ",font="ar 12 bold",borderwidth=2,relief="groove",width = 6, height = 1).grid(row = 6, column = 1,ipadx="40",ipady="5",padx="20",pady="10")
    indirizzoForm =  Label(window, text = "Indirizzo: ",font="ar 12 bold",borderwidth=2,relief="groove",width = 6, height = 1).grid(row = 7, column = 1,ipadx="40",ipady="5",padx="20",pady="10")
    emailForm =  Label(window, text = "Email: ",font="ar 12 bold",borderwidth=2,relief="groove",width = 6, height = 1).grid(row = 8, column = 1,ipadx="40",ipady="5",padx="20",pady="10")
    passwordForm =  Label(window, text = "Password: ",font="ar 12 bold",borderwidth=2,relief="groove",width = 6, height = 1).grid(row = 9, column = 1,ipadx="40",ipady="5",padx="20",pady="10")

    nome_var = StringVar
    cognome_var  = StringVar
    professione_var  = StringVar
    partita_iva_var  = StringVar
    citta_var  = StringVar
    indirizzo_var  = StringVar
    email_var = StringVar
    password_var = StringVar
    nome1 = StringVar
    nome1 = "nnnnn"

    nome = Entry(window).grid(row = 2,column = 2,ipadx="20")
    cognome = Entry(window, textvariable = cognome_var).grid(row = 3,column = 2,ipadx="20")
    professione = OptionMenu(window, variable, *option_wrk ).grid(row = 4,column = 2,ipadx="5")
    partita_iva = Entry(window, textvariable = partita_iva_var).grid(row = 5,column = 2,ipadx="20")
    citta = Entry(window, textvariable = citta_var).grid(row = 6,column = 2,ipadx="20")
    indirizzo = Entry(window, textvariable = indirizzo_var).grid(row = 7,column = 2,ipadx="20")
    email = Entry(window, textvariable = email_var).grid(row = 8,column = 2,ipadx="20")
    password = Entry(window, textvariable = password_var).grid(row = 9,column = 2,ipadx="20")

    def registration_function(nome):
     print("registration")
     print(" ",nome.get(self))   
   # print(" ",cognome_var.get())

    btn = Button(window, text="Submit", command=lambda: registration_function(cognome_var) ).grid(row = 10, column = 3)
#btn = Button(window, text="Submit", command=partial(registration_function, nome1) ).grid(row = 10, column = 3)
    window.mainloop()

Loginform()