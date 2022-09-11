from tkinter import* 
import requests
import register
import app
from tkinter import messagebox
import mainpage
from PIL import Image, ImageTk

class LoginFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        buttonframe = Frame(self, highlightbackground="gray", bg="gray92", highlightthickness=2, width=700, height=250)
        buttonframe.pack(side="top", fill="x")

        imgframe = Frame(buttonframe, highlightthickness=2, width=200, height=200)
        imgframe.grid(row = 0, column = 1, pady = 10, padx = 10)

        load = Image.open("./img/instafix.png")
        render = ImageTk.PhotoImage(load)
        img = Label(imgframe, image=render)
        img.image = render
        img.pack(side="top",anchor=CENTER)

        b1 = Button(buttonframe, text="Login",  command=lambda: controller.show_frame(LoginFrame) )
        b2 = Button(buttonframe, text="Registrati",  command=lambda: controller.show_frame(register.Register) )

        b1.grid(row = 0, column = 4, pady = 10, padx = 20)
        b2.grid(row = 0, column = 8, pady = 10, padx = 20)

        frameLogin = Frame(self,name= "frameTable" , bg="gray92", highlightthickness=2, width=700, height=250)
        frameLogin.pack(expand=True,  anchor=CENTER, pady=5, padx=5)
       
        title = Label(frameLogin, text="Login",bg="gray92", font=("times new roman", 20, "bold"),  fg="gray37").pack(side="top",anchor=CENTER,  pady = 10, padx=10)
            
        f_email = Label(frameLogin, text="Email", font=("times new roman", 15, "bold"), bg="gray92" , fg="gray").pack(side="top",anchor=CENTER,  pady = 10, padx=10)
        self.email = Entry(frameLogin, font=("times new roman", 15), bg="lightgray")
        self.email.pack(side="top",anchor=CENTER,  pady = 5, padx=5)
       
        f_password = Label(frameLogin, text="Password", font=("times new roman", 15, "bold"), bg="gray92", fg="gray").pack(side="top",anchor=CENTER,  pady = 10, padx=10)
        self.password = Entry(frameLogin, font=("times new roman", 15), bg="lightgray")
        self.password.pack(side="top",anchor=CENTER,  pady = 5, padx=5)

        print(" ID: "+ app.session["id"])
       
        def login_function():
         print("loginFunction")
         url = 'http://localhost:8000/loginProfessionist'

         credentials = { 'password': self.password.get(),
                        'email': self.email.get()}

         headers = {'Content-Type': 'application/x-www-form-urlencoded'}
         response = requests.post(url, data=credentials, headers=headers)

         if response.text != "Credenziali errate":
             app.session['id'] = response.text
             app.session['logged'] = 1
             controller.show_frame(mainpage.MainPage)
         else:
            messagebox.showinfo('Risultato Login',response.text )

        btn_register = Button(frameLogin,  text="Sign In", command=login_function, font=("times new roman",19)).pack(side="top",anchor=CENTER,  pady = 10, padx=10)
