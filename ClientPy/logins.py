from tkinter import* 
import requests

import main

class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()


class Login(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = Label(self, text="This is page 1")
       label.pack(side="top", fill="both", expand=True)
       
       title = Label(self, text="Login", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=270, y=180)
            
       f_email = Label(self, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=260)
       self.email = Entry(self, font=("times new roman", 15), bg="lightgray")
       self.email.place(x=220, y=260, width=250)
       
       f_password = Label(self, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=300)
       self.password = Entry(self, font=("times new roman", 15), bg="lightgray")
       self.password.place(x=220, y=300, width=250)
       
       def login_function():
        print("loginFunction")
        url = 'http://localhost:8000/login'

        credentials = { 'password': self.password.get(),
                        'email': self.email.get()}

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        print(credentials["email"])
        print(credentials["password"])

        response = requests.post(url, data=credentials, headers=headers)

        print("Status code: ", response.status_code)
        print("Status code: ", response.text)

        if response.text == "Credenziali corrette":
            main.session['email'] = self.email.get()
            main.session['logged'] = 1
            print(main.session['email'])
            print(main.session['logged'] )

            print (" One of the accounts have successfully logged in ")
        
            main.root.after(2000, main.NewPage) 




    


    
       btn_register = Button(self,  text="Sign In", command=login_function, font=("times new roman",19), bd=0, cursor="hand2").place(x=365, y=480)

       
