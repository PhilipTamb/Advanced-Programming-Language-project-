
from curses import window
from tkinter import*
from tkinter import ttk, messagebox
import requests
from typing import Dict


class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Registration Page")  # For Title of the page
        self.root.geometry("1350x700+0+0")    # Resolution of the page , top, bottom
        self.root.config(bg="white")

    

        # ===Register Frame===
        window = Frame(self.root, bg="white")
        window.place(x=480, y=85, width=700, height=550)

        title = Label(window, text="Registrati qui", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=270, y=30)

        # --------First Row
        f_nome = Label(window, text="Nome", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        self.nome = Entry(window, font=("times new roman", 15), bg="lightgray")
        self.nome.place(x=220, y=100, width=250)

        f_cognome = Label(window, text="Cognome", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=140)
        self.cognome = Entry(window, font=("times new roman", 15), bg="lightgray")
        self.cognome.place(x=220, y=140, width=250)

        f_professione = Label(window, text="Professione", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=180)
        self.professione = ttk.Combobox(window, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.professione['values']=("Edilizia", "Idraulica","Giardinaggio","Climatizzazione e riscaldamento","Telecomunicazioni","Rete elettrica ed elettrodomestici")
        self.professione.place(x=220, y=180, width=250)
        self.professione.current(0)

        f_partitaiva = Label(window, text="Partita IVA", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=220)
        self.partitaiva= Entry(window, font=("times new roman", 15), bg="lightgray")
        self.partitaiva.place(x=220, y=220, width=250)


        f_citta = Label(window, text="Città", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=260)
        self.citta = Entry(window, font=("times new roman", 15), bg="lightgray")
        self.citta.place(x=220, y=260, width=250)

        f_indirizzo = Label(window, text="Indirizzo", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=300)
        self.indirizzo = Entry(window, font=("times new roman", 15), bg="lightgray")
        self.indirizzo.place(x=220, y=300, width=250)

        f_telefono = Label(window, text="Telefono", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=340)
        self.telefono = Entry(window, font=("times new roman", 15), bg="lightgray")
        self.telefono.place(x=220, y=340, width=250) 

        f_email = Label(window, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=380)
        self.email = Entry(window, font=("times new roman", 15), bg="lightgray")
        self.email.place(x=220, y=380, width=250) 

        f_password = Label(window, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=420)
        self.password = Entry(window, font=("times new roman", 15), bg="lightgray")
        self.password.place(x=220, y=420, width=250)



        # Register Button with Image

        btn_register = Button(window,  text="Sign In", command=self.registration_function, font=("times new roman",19), bd=0, cursor="hand2").place(x=365, y=480)
       # btn_page = Button(window,  text="Sign Up", command=self.login_page, font=("login_page new roman",18), bd=0, cursor="hand2").place(x=220, y=480)




    def registration_function(self):
        url = 'http://localhost:8000/register_professionist'

        payload = {
            'nome': self.nome.get(),
            'cognome': self.cognome.get(),
            'professione': self.professione.get(),
            'partitaiva': self.partitaiva.get(),
            'citta': self.citta.get(),
            'indirizzo': self.indirizzo.get(),
            'telefono': self.telefono.get(),
            'email': self.email.get(),
            'password': self.password.get()}

        
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        
        response = requests.post(url, data=payload, headers=headers)

        print("Status code: ", response.status_code)
        print("Printing Entire Post Request")
        print(response.json())


        print(payload)
        #x = requests.post(url,json=payload)
       # x = requests.post(url,user_agent,data=json.dumps(payload))
        #print("X --> ", x )
       # print("X --> ", x.status_code )
        
'''
root = Tk()
obj = Register(root)
root.mainloop()
'''