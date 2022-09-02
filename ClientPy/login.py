from tkinter import* 
import requests
import register
import app
import mainpage


class LoginFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        buttonframe = Frame(self, highlightbackground="blue", highlightthickness=2, width=700, height=250)
        buttonframe.pack(side="top", fill="x")

        b1 = Button(buttonframe, text="Login",  command=lambda: controller.show_frame(LoginFrame) )
        b2 = Button(buttonframe, text="Registrati",  command=lambda: controller.show_frame(register.Register) )

        b1.grid(row = 0, column = 2, pady = 10, padx = 20)
        b2.grid(row = 0, column = 4, pady = 10, padx = 20)

        frameLogin = Frame(self,name= "frameTable" , highlightbackground="red", highlightthickness=2, width=700, height=250)
        frameLogin.pack(expand=True,  anchor=CENTER, pady=5, padx=5)
       
        title = Label(frameLogin, text="Login", font=("times new roman", 20, "bold"),  fg="Black").pack(side="top",anchor=CENTER)
            
        f_email = Label(frameLogin, text="Email", font=("times new roman", 15, "bold"), fg="gray").pack(side="top",anchor=CENTER)
        self.email = Entry(frameLogin, font=("times new roman", 15), bg="lightgray")
        self.email.pack(side="top",anchor=CENTER)
       
        f_password = Label(frameLogin, text="Password", font=("times new roman", 15, "bold"), fg="gray").pack(side="top",anchor=CENTER)
        self.password = Entry(frameLogin, font=("times new roman", 15), bg="lightgray")
        self.password.pack(side="top",anchor=CENTER)
       
        def login_function():
         print("loginFunction")
         url = 'http://localhost:8000/login'

         credentials = { 'password': self.password.get(),
                        'email': self.email.get()}

         headers = {'Content-Type': 'application/x-www-form-urlencoded'}

         #print(credentials["email"])
         #print(credentials["password"])

         response = requests.post(url, data=credentials, headers=headers)

         #print("Status code: ", response.status_code)
         print("Status code: ", response.text)

         if response.text == "Credenziali corrette":
             app.session['email'] = self.email.get()
             app.session['logged'] = 1
             print(app.session['email'])
             print(app.session['logged'] )
             print ("logged in ")
             print(self.winfo_parent())
             controller.show_frame(mainpage.MainPage)


        btn_register = Button(frameLogin,  text="Sign In", command=login_function, font=("times new roman",19), bd=0, cursor="hand2").pack(side="top",anchor=CENTER)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = Button(
            self,
            text="Go to the Side Page",
            command=lambda: controller.show_frame(mainpage.MainPage),
        )
        switch_window_button.pack(side="bottom", fill=X)