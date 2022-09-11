from tkinter import* 
import requests
from tkinter import messagebox
from tkinter import ttk
import app
import preventive
import mainpage
import ticket
import preventive
import invoices
import login
from PIL import Image, ImageTk

payload = {
        'descrizione_intervento': ' ',
        'materiali_o_ricambi_previsti': ' ',
        'costo': ' ',
        'dataora_intervento': ' ',
        'id_ticket': ' ',
        'email': ' ',
        }

preventiveId = -1

class PreventiveId(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        buttonframe = Frame(self,highlightbackground="gray", bg="gray92",highlightthickness=2, width=700, height=250)
        buttonframe.pack(side="top", fill="x")

        imgframe = Frame(buttonframe,  bg="gray92",highlightthickness=2, width=200, height=200)
        imgframe.grid(row = 0, column = 1, pady = 10, padx = 10)

        load = Image.open("./img/instafix.png")
        render = ImageTk.PhotoImage(load)
        img = Label(imgframe, image=render)
        img.image = render
        img.pack(side="top",anchor=CENTER)

        b1 = Button(buttonframe, text="Home", command=lambda: controller.show_frame(mainpage.MainPage))
        b2 = Button(buttonframe, text="Nuovi Ticket", command=lambda: controller.show_frame(ticket.Ticket))
        b3 = Button(buttonframe, text="Preventivi in Attesa", command=lambda: controller.show_frame(preventive.PreventiveAll))
        b4 = Button(buttonframe, text="Fatturazione", command=lambda: controller.show_frame(invoices.Invoices))
        b5 = Button(buttonframe, text="Logout", command= lambda:logout(controller))

        b1.grid(row = 0, column = 4, pady = 10, padx = 20)
        b2.grid(row = 0, column = 6, pady = 10, padx = 20)
        b3.grid(row = 0, column = 8, pady = 10, padx = 20)
        b4.grid(row = 0, column = 10, pady = 10, padx = 20)
        b5.grid(row = 0, column = 12, pady = 10, padx = 20)

        title = Label(self, text="Completa il preventivo", font=("times new roman", 20, "bold"), fg="Gray")
        title.pack(side="top",anchor=CENTER)

        frameTable = Frame(self, highlightthickness=2, width=700, height=30)
        frameTable.pack(expand=True,  anchor=CENTER, pady=5, padx=5)

        infoframe = Frame(self,  highlightthickness=2, width=700, height=100)
        infoframe.pack(expand=True,  anchor=CENTER)

        title = Label(infoframe, text="Compila il Preventivo", font=("times new roman", 12, "bold"), fg="Gray")
        title.pack(side="top",anchor=CENTER)

        contentframe = Frame(self, highlightthickness=2, width=700, height=100)
        contentframe.pack(expand=True,  anchor=CENTER)

        lst = ["Id", "Stato", "Categoria", "Titolo", "Descrizione"]

        tree = ttk.Treeview(frameTable,name = "tree", selectmode="browse", height=1)
        tree['columns'] = ('Id', 'Stato', 'Categoria', 'Titolo', 'Descrizione')

        tree.column("#0", width=0,  stretch=NO)
        tree.column("Id",anchor=CENTER, width=30)
        tree.column("Stato",anchor=CENTER,width=60)
        tree.column("Categoria",anchor=CENTER,width=150)
        tree.column("Titolo",anchor=CENTER,width=100)
        tree.column("Descrizione",anchor=CENTER,width=400)

        tree.heading("#0",text="",anchor=CENTER)
        tree.heading("Id",text="Id",anchor=CENTER)
        tree.heading("Stato",text="Stato",anchor=CENTER)
        tree.heading("Categoria",text="Categoria",anchor=CENTER)
        tree.heading("Titolo",text="Titolo",anchor=CENTER)
        tree.heading("Descrizione",text="Descrizione",anchor=CENTER)

        buttonDenyframe = Frame(self, highlightthickness=2, width=200, height=200)
        buttonDenyframe.pack(side="top", fill="x")

        title = Label(buttonDenyframe, text="Rifiuta il Ticket",  font=("times new roman", 12, "bold"), fg="Gray")  
        title.pack(side="top",anchor=CENTER,  pady = 10, padx=10)

        btn_deny = Button(buttonDenyframe,  text="Rifiuta", command= lambda  :denyticket(controller), font=("times new roman",12)).pack(side="top",anchor=CENTER,  pady = 10, padx=10)

            
        def printPreventivi(*args):
            jsn = getTicketProfessionistById()
            preventiveId = -1
            lst = ["Id", "Stato", "Categoria", "Titolo", "Descrizione"]

            if(len(tree.get_children())!= 0 ):
                for i in tree.get_children():
                    tree.delete(i)

            if(jsn != None):
                total_rows = len(jsn)

                for i in range(total_rows):   #row
                    if jsn[i][lst[1]] == 'creato':
                        payload['id_ticket'] = jsn[i][lst[0]]
                        tree.insert(parent='',index='end',iid=i,text='', values=( jsn[i][lst[0]], jsn[i][lst[1]], jsn[i][lst[2]], jsn[i][lst[3]],  jsn[i][lst[4]]))

            tree.pack()

            total_rows = len(jsn)

            lst = ["Descrizione Intervento", "Materiali e Ricambi", "Costo", "Data e ora Intervento"] #"Id Ticket"

                # code for creating table
            for z in range(len(lst)):
                if  lst[z] == 'Id Ticket':
                    self.e = Entry(contentframe, width=10, bg='LightBlue',fg='Gray',font=('Arial', 10, 'bold'))
                elif lst[z] == 'Descrizione Intervento':
                    self.e = Entry(contentframe, width=40, bg='LightBlue',fg='Gray',font=('Arial', 10, 'bold'))
                elif lst[z] == 'Materiali e Ricambi':
                    self.e = Entry(contentframe, width=40, bg='LightBlue',fg='Gray',font=('Arial', 10, 'bold'))
                elif lst[z] == 'Costo':
                    self.e = Entry(contentframe, width=10, bg='LightBlue',fg='Gray',font=('Arial', 10, 'bold'))
                else:
                    self.e = Entry(contentframe, width=15, bg='LightBlue',fg='Gray',font=('Arial', 10, 'bold'))

                self.e.grid(row= 0, column=z)
                self.e.insert(END, lst[z])  
                self.e.configure(state='disabled')
            list_entry = []
            for i in range(total_rows):   #row
                for j in range(len(lst)): #column
                        if lst[j] == 'Id Ticket':
                            self.e = Entry(contentframe, width=10, fg='Black',font=('Arial',10,'bold'))
                        elif lst[j] == 'Descrizione Intervento':
                            self.e = Entry(contentframe, width=40, fg='Black',font=('Arial',10,'bold'))
                        elif lst[j] == 'Materiali e Ricambi':
                            self.e = Entry(contentframe, width=40, fg='Black',font=('Arial',10,'bold'))
                        elif lst[j] == 'Costo':
                            self.e = Entry(contentframe, width=10, fg='Black',font=('Arial',10,'bold'))
                        else:
                         self.e = Entry(contentframe, width=15, fg='Black',font=('Arial', 10, 'bold'))
                    
                        self.e.grid(row=i+1, column=j)
                        list_entry.append(self.e)

                self.e = Entry(contentframe, width=30, fg='blue',font=('Arial',10,'bold'))
                self.e = Button(contentframe, text=">>>", command= lambda  : insertPreventivoProfessionista(list_entry,controller))
                self.e.grid(row=i+1, column=len(lst)+1 ) # , width=4, height=2

        contentframe.bind('<Expose>',lambda  *args: printPreventivi(*args) )

def getTicketProfessionistById():
            print("getTicketProfessionistById")
            url = 'http://localhost:8000/geticketsprofessionistbyid'
            credentials = { 'id_professionista': app.session['id'], 'id_ticket': preventiveId }
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            response = requests.post(url, data=credentials, headers=headers)

            if response.text != None :
                return response.json() 
            else:
                return response.text

def logout(controller):
    app.session["id"] = ""
    app.session["login"] = 0
    controller.show_frame(login.LoginFrame)     

def insertPreventivoProfessionista(list_entry,controller):
    print("/insertpreventivoprofessionist")
    url = 'http://localhost:8000/insertpreventivoprofessionist'

    for obj in list_entry:
        print(obj.get())

    lst = ['descrizione_intervento', 'materiali_o_ricambi_previsti', 'costo', 'dataora_intervento']

    for i in range(len(list_entry)):
     payload[lst[i]] = list_entry[i].get()
 
    payload['id_professionista'] = app.session['id']
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, data=payload, headers=headers)

    if response.text == 'Inserito correttamente':
        messagebox.showinfo('Risultato Inserimento',response.text)
        controller.show_frame(mainpage.MainPage)
    else:
        messagebox.showinfo('Risultato Inserimento','inserimento negato')
    return response.text      

def denyticket(controller):
    print("/denyticket")
    url = 'http://localhost:8000/denyticket'
    payload = { 'id_ticket': preventiveId }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, data=payload, headers=headers)

    if response.text == 'Preventivo rifiutato':
        messagebox.showinfo('Risultato Inserimento','Ticket rifiutato')
        controller.show_frame(mainpage.MainPage)
    else:
        messagebox.showinfo('Risultato Inserimento','Non siamo riusciti a rifiutare il ticket')
    return response.text      


    
class PreventiveAll(Frame):
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

        b1 = Button(buttonframe, text="Home", command=lambda: controller.show_frame(mainpage.MainPage))
        b2 = Button(buttonframe, text="Nuovi Ticket", command=lambda: controller.show_frame(ticket.Ticket))
        b3 = Button(buttonframe, text="Preventivi in Attesa", command=lambda: controller.show_frame(preventive.PreventiveAll))
        b4 = Button(buttonframe, text="Fatturazione", command=lambda: controller.show_frame(invoices.Invoices))
        b5 = Button(buttonframe, text="Logout", command= lambda:logout(controller))

        b1.grid(row = 0, column = 4, pady = 10, padx = 20)
        b2.grid(row = 0, column = 6, pady = 10, padx = 20)
        b3.grid(row = 0, column = 8, pady = 10, padx = 20)
        b4.grid(row = 0, column = 10, pady = 10, padx = 20)
        b5.grid(row = 0, column = 12, pady = 10, padx = 20)

        title = Label(self, text="Preventivi in Attesa di Accettazione dai clienti", font=("times new roman", 20, "bold"), fg="Gray")
        title.pack(side="top",anchor=CENTER)

        lst = ['IdTicket', 'Descrizione', 'MaterialiRicambi', 'Costo', 'DataOra']

        frameTable = Frame(self, highlightthickness=2, width=700, height=30)
        frameTable.pack(expand=True,  anchor=CENTER, pady=5, padx=5)

        table_scroll = Scrollbar(frameTable)
        table_scroll.pack(side=RIGHT, fill=Y)

        table_scroll = Scrollbar(frameTable,orient='horizontal')
        table_scroll.pack(side= BOTTOM,fill=X)

        tree1 = ttk.Treeview(frameTable,name = "tree1",yscrollcommand=table_scroll.set, xscrollcommand =table_scroll.set, selectmode="browse")

        table_scroll.config(command=tree1.yview)
        table_scroll.config(command=tree1.xview)

        tree1['columns'] = ('Id', 'Descrizione', 'Materiali', 'Costo', 'Data')

        tree1.column("#0", width=0,  stretch=NO)
        tree1.column("Id",anchor=CENTER, width=30)
        tree1.column("Descrizione",anchor=CENTER,width=150)
        tree1.column("Materiali",anchor=CENTER,width=150)
        tree1.column("Costo",anchor=CENTER,width=150)
        tree1.column("Data",anchor=CENTER,width=400)

        tree1.heading("#0",text="",anchor=CENTER)
        tree1.heading("Id",text="Id",anchor=CENTER)
        tree1.heading("Descrizione",text="Descrizione",anchor=CENTER)
        tree1.heading("Materiali",text="Materiali",anchor=CENTER)
        tree1.heading("Costo",text="Costo",anchor=CENTER)
        tree1.heading("Data",text="Data",anchor=CENTER)

        tree1.pack()

        def printAllPreventivi(*args):
            jsn = getPreventiviInAttesaProfessionist()
            
            if(len(tree1.get_children())!= 0 ):
                for i in tree1.get_children():
                    tree1.delete(i)

            if(jsn != None):
                total_rows = len(jsn)

                for i in range(total_rows):   
                    tree1.insert(parent='',index='end',iid=i,text='', values=( jsn[i][lst[0]], jsn[i][lst[1]], jsn[i][lst[2]], jsn[i][lst[3]],  jsn[i][lst[4]]))
        
            tree1.pack()

        frameTable.bind('<Expose>',lambda  *args: printAllPreventivi(*args) )

def getPreventiviInAttesaProfessionist():
    print("getpreventiviprofessionist")
    url = 'http://localhost:8000/getpreventiviinattesaprofessionist'

    credentials = { 'id_professionista': app.session['id']}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, data=credentials, headers=headers)

    if response.text != None :
        return response.json() 
    else:
        return response.text