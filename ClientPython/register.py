from tkinter import*
from tkinter import ttk, messagebox
import requests
from tkinter import messagebox
import login
from PIL import Image, ImageTk

def validation_form(payload):
        
        symbols = ('`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|')
        numbers = ('1','2','3','4','5','6','7','8','9','0')
        at = point = symbols_point =  numbers_point =  length_password =  length_nome = length_cognome = length_p_iva = length_indirizzo = length_telefono = length_citta = 0
        
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
                    
        if len(payload['telefono']) > 9 :
                  length_telefono = 1

        if len(payload['citta']) > 2 :
                  length_citta = 1
        
        
        print(f"at: ", at," point: ", point , "  symbols_point: ", symbols_point, "  numbers_point: ", numbers_point ,"  length_password: ", length_password, " length_nome: ", length_nome , " length_cognome: ", length_cognome, " length_p_iva: ",  length_p_iva,  " length_indirizzo: ", length_indirizzo, " length_telefono: ", length_telefono, " length_citta: ", length_citta )


        if  at <1  or point <1 or symbols_point <1 or numbers_point <1 or length_password<1 or length_nome <1 or length_cognome <1 or length_p_iva <1 or length_indirizzo <1 or length_telefono <1 or length_citta <1:
            messagebox.showwarning('Errore nella Registrazione', "Inserire tutti i campi correttamente! \n " +
            "- L'email deve essere del formato: example@dominio.it \n"+
            "- La password deve essere formata da almeno 6 caratteri \n di cui almeno un simbolo speciale e almeno un numero")
            return "no"
        else: return "ok"

class Register(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        buttonframe = Frame(self, highlightbackground="gray", bg="gray92", highlightthickness=2, width=700, height=250)
        buttonframe.pack(side="top", fill="x")

        imgframe = Frame(buttonframe, bg="gray92", highlightthickness=2, width=200, height=200)
        imgframe.grid(row = 0, column = 1, pady = 10, padx = 10)

        load = Image.open("./img/instafix.png")
        render = ImageTk.PhotoImage(load)
        img = Label(imgframe, image=render)
        img.image = render
        img.pack(side="top",anchor=CENTER)

        b1 = Button(buttonframe, text="Login",  command=lambda: controller.show_frame(login.LoginFrame) )
        b2 = Button(buttonframe, text="Registrati",  command=lambda: controller.show_frame(Register) )

        b1.grid(row = 0, column = 4, pady = 10, padx = 20)
        b2.grid(row = 0, column = 8, pady = 10, padx = 20)

        frameLogin = Frame(self,name= "frameTable" , highlightthickness=2, width=900, height=900)
        frameLogin.pack(expand=True, fill="both", anchor=CENTER,  padx = 5)

        title = Label(frameLogin, text="Registrati qui", font=("times new roman", 20, "bold"),  fg="Black").pack(side="top",anchor=CENTER,  pady = 20, padx = 50)

        leftframe = Frame(frameLogin,name= "leftframe" , highlightthickness=2, )
        leftframe.pack(side="left",expand=True, fill="both", padx=(100, 0), pady=(10, 0) )


        rightframe = Frame(frameLogin,name= "rightframe" , highlightthickness=2)
        rightframe.pack(side="right" ,expand=True,fill="both", padx=(0, 100), pady=(10, 0))

        nome = Label(leftframe, text="Nome", font=("times new roman", 15, "bold"),  fg="gray").pack(side="top",anchor=CENTER,  pady = 5)
        self.nome = Entry(rightframe, font=("times new roman", 15), bg="lightgray")
        self.nome.pack(side="top",anchor=CENTER,  pady = 5)
        
        f_cognome = Label(leftframe, text="Cognome", font=("times new roman", 15, "bold"),  fg="gray").pack(side="top",anchor=CENTER,  pady = 5)
        self.cognome = Entry(rightframe, font=("times new roman", 15), bg="lightgray")
        self.cognome.pack(side="top",anchor=CENTER,  pady = 5)
        
        f_professione = Label(leftframe, text="Professione", font=("times new roman", 15, "bold"),  fg="gray").pack(side="top",anchor=CENTER,  pady = 5)
        self.professione = ttk.Combobox(rightframe, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.professione['values']=("Edilizia", "Idraulica","Giardinaggio","Climatizzazione e riscaldamento","Telecomunicazioni","Rete elettrica ed elettrodomestici")
        self.professione.pack(side="top",anchor=CENTER,  pady = 5)

        self.professione.current(0)
        
        f_partitaiva = Label(leftframe, text="Partita IVA", font=("times new roman", 15, "bold"),  fg="gray").pack(side="top",anchor=CENTER,  pady = 5)
        self.partitaiva= Entry(rightframe, font=("times new roman", 15), bg="lightgray")
        self.partitaiva.pack(side="top",anchor=CENTER,  pady = 5)
        
        f_citta = Label(leftframe, text="Città", font=("times new roman", 15, "bold"),  fg="gray").pack(side="top",anchor=CENTER,  pady = 5)
        self.citta = Entry(rightframe, font=("times new roman", 15), bg="lightgray")
        self.citta.pack(side="top",anchor=CENTER,  pady = 5)
        
        f_indirizzo = Label(leftframe, text="Indirizzo", font=("times new roman", 15, "bold"),  fg="gray").pack(side="top",anchor=CENTER,  pady = 5)
        self.indirizzo = Entry(rightframe, font=("times new roman", 15), bg="lightgray")
        self.indirizzo.pack(side="top",anchor=CENTER,  pady = 5)
        
        f_telefono = Label(leftframe, text="Telefono", font=("times new roman", 15, "bold"),  fg="gray").pack(side="top",anchor=CENTER,  pady = 5)
        self.telefono = Entry(rightframe, font=("times new roman", 15), bg="lightgray")
        self.telefono.pack(side="top",anchor=CENTER,  pady = 5)
        
        f_email = Label(leftframe, text="Email", font=("times new roman", 15, "bold"),  fg="gray").pack(side="top",anchor=CENTER,  pady = 5)
        self.email = Entry(rightframe, font=("times new roman", 15), bg="lightgray")
        self.email.pack(side="top",anchor=CENTER,  pady = 5)
        
        f_password = Label(leftframe, text="Password", font=("times new roman", 15, "bold"),  fg="gray").pack(side="top",anchor=CENTER,  pady = 5)
        self.password = Entry(rightframe, font=("times new roman", 15), bg="lightgray")
        self.password.pack(side="top",anchor=CENTER,  pady = 5)

        def registration_function(*args):
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
            
            res_controll = validation_form(payload)
            print("res_controll " + res_controll)

            if( res_controll == 'ok'):
                headers = {'Content-Type': 'application/x-www-form-urlencoded'}
                response = requests.post(url, data=payload, headers=headers)

                if response.text == "Account creato":
                    messagebox.showinfo('Info account','Account creato correttamente!')
                elif response.text == "Email esistente":
                    messagebox.showinfo('Info account','Account creato correttamente!')


        btn_register = Button(rightframe,  text="Sign In", command=registration_function, font=("times new roman",19)).pack(side="right",anchor=CENTER,  pady = 5)
       




   



