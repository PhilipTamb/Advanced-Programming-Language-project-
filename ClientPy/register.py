
from tkinter import*
from tkinter import ttk
import requests
import main
from tkinter import ttk

class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

def validation_form(self,payload):
        
        symbols = ('`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|')
        numbers = ('1','2','3','4','5','6','7','8','9','0')
        at = point = symbols_point =  numbers_point =  length_password =  length_nome = length_cognome = length_p_iva = length_indirizzo = 0
        
        for i in range(len(payload['email'])) :
            if payload['email'][i] == '@' :
                at = at + 1
                print("email @ = +1")

            if payload['email'][-3:-2] == '.' or payload['email'][-4:-3] == '.':
                point = point + 1
                print("email . = +1")

        for i in range(len(payload['password'])) :
            for j in range(len(symbols)):
                if payload['password'][i] == symbols[j] :
                    symbols_point = symbols_point + 1
                    print("password simbols = +1")
           
            for z in range(len(numbers)):
                if payload['password'][i] == numbers[z] :
                    numbers_point = numbers_point + 1
                    print("password number = +1")

        if len(payload['password']) > 5 :
                    length_password = 1
                    print("password lenght = +1")
        
        if len(payload['nome']) > 2 :
                    length_nome = 1
                    print("length_nome = +1")
        
        if len(payload['cognome']) > 2 :
                    length_cognome = 1
                    print("length_cognome = +1")
        
        if len(payload['partitaiva']) > 5 :
                    length_p_iva =  1

        if len(payload['indirizzo']) > 5 :
                    length_indirizzo = 1
        
        
        print(f"at: ", at," point: ", point , "  numbers_point: ", numbers_point , "  symbols_point: ", symbols_point , "lenght :" , length_password)


        if length_password <1 or point <1 or  at <1 or symbols_point <1 or numbers_point <1 or length_nome <1 or length_cognome <1 or length_p_iva <1 or length_indirizzo <1:
            top = Toplevel(self)
            top.geometry("750x250")
            top.title("Error Registration")
            Label(top, text= "Inserire tutti i campi correttamente!", font=('Mistral 18 bold'),fg="red").place(x=50,y=50)
            Label(top, text= "- L'email deve essere del formato: example@dominio.it", font=('Mistral 13 bold')).place(x=50,y=100)
            Label(top, text= "- La password deve essere formata da almeno 6 caratteri \n di cui almeno uno speciale e almeno un numero", font=('Mistral 13 bold')).place(x=50,y=140)
            top.mainloop()

class Register(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Label(self, text="This is page 1")
       label.pack(side="top", fill="both", expand=True)

       


       title = Label(self, text="Registrati qui", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=270, y=30)
       nome = Label(self, text="Nome", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
       self.nome = Entry(self, font=("times new roman", 15), bg="lightgray")
       self.nome.place(x=220, y=100, width=250)
       
       f_cognome = Label(self, text="Cognome", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=140)
       self.cognome = Entry(self, font=("times new roman", 15), bg="lightgray")
       self.cognome.place(x=220, y=140, width=250)
       
       f_professione = Label(self, text="Professione", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=180)
       self.professione = ttk.Combobox(self, font=("times new roman", 13), state='readonly', justify=CENTER)
       self.professione['values']=("Edilizia", "Idraulica","Giardinaggio","Climatizzazione e riscaldamento","Telecomunicazioni","Rete elettrica ed elettrodomestici")
       self.professione.place(x=220, y=180, width=250)
       self.professione.current(0)
       
       f_partitaiva = Label(self, text="Partita IVA", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=220)
       self.partitaiva= Entry(self, font=("times new roman", 15), bg="lightgray")
       self.partitaiva.place(x=220, y=220, width=250)
       
       f_citta = Label(self, text="Città", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=260)
       self.citta = Entry(self, font=("times new roman", 15), bg="lightgray")
       self.citta.place(x=220, y=260, width=250)
       
       f_indirizzo = Label(self, text="Indirizzo", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=300)
       self.indirizzo = Entry(self, font=("times new roman", 15), bg="lightgray")
       self.indirizzo.place(x=220, y=300, width=250)
       
       f_telefono = Label(self, text="Telefono", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=340)
       self.telefono = Entry(self, font=("times new roman", 15), bg="lightgray")
       self.telefono.place(x=220, y=340, width=250)
       
       f_email = Label(self, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=380)
       self.email = Entry(self, font=("times new roman", 15), bg="lightgray")
       self.email.place(x=220, y=380, width=250) 
       
       f_password = Label(self, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=420)
       self.password = Entry(self, font=("times new roman", 15), bg="lightgray")
       self.password.place(x=220, y=420, width=250)

       def registration_function():
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

        validation_form(self,payload)

        print(payload)
        
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        response = requests.post(url, data=payload, headers=headers)

        print("Status code: ", response.status_code)
        print("Status code: ", response.text)

        if response.text == "Credenziali corrette":
            main.session['email'] = self.email.get()
            main.session['logged'] = 1
            print(main.session['email'])
            print(main.session['logged'] )

            top = Toplevel(self)
            top.geometry("750x250")
            top.title("Account Creato")
            Label(top, text= "Account creato correttamente!", font=('Mistral 18 bold'),fg="black").place(x=50,y=50)
            
            top.mainloop()

        
        if response.text == "Email esistente":
            top = Toplevel(self)
            top.geometry("750x250")
            top.title("Error Registration")
            Label(top, text= "Inserire tutti i campi correttamente!", font=('Mistral 18 bold'),fg="red").place(x=50,y=50)
            Label(top, text= "- L'email inserita ha già un account", font=('Mistral 13 bold')).place(x=50,y=100)
            top.mainloop()

    

    
       btn_register = Button(self,  text="Sign In", command=registration_function, font=("times new roman",19), bd=0, cursor="hand2").place(x=365, y=480) 



