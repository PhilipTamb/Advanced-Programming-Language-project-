from tkinter import* 
import requests
import main


from PIL import Image,ImageTk

class MainPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        title = Label(self, text="Home", font=("times new roman", 20, "bold"), bg="white", fg="green")
        #title.place(in_=contentframe,x=270, y=180)
        title.pack(side="top",anchor=CENTER)

        contentframe = Frame(self, highlightbackground="red", highlightthickness=2, width=700, height=250)
        contentframe.pack(expand=True,  anchor=CENTER)

        content_table = Frame(self, highlightbackground="red", highlightthickness=2, width=700, height=250)
        content_table .pack(expand=True,  anchor=CENTER)

        jsn = getPreventiviProfessionist()
        print(jsn)

                # take the data
        lst = [(1,'Raj','Mumbai',19),
                (2,'Aaryan','Pune',18),
                (3,'Vaishnavi','Mumbai',20),
                (4,'Rachna','Mumbai',21),
                (5,'Shubham','Delhi',21)]
            
            # find total number of rows and
            # columns in list
        total_rows = len(lst)
        total_columns = len(lst[0])



            # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                if i == 0:
                    self.e = Entry(contentframe, width=20, bg='LightSteelBlue',fg='Black',font=('Arial', 16, 'bold'))
                    
                self.e = Entry(contentframe, width=20, fg='blue',font=('Arial',16,'bold'))
                        
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
        


def getPreventiviProfessionist():
    print("getnome")
    url = 'http://localhost:8000/getpreventiviprofessionist'

    print("email " + main.session['email'])

    credentials = { 'email': main.session['email']}

    print("credentials " + credentials["email"])

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, data=credentials, headers=headers)

    print("Status code: ", response.status_code)
    print("text: ", response.text)
    return response.text           
               





    
