from random import random
from tkinter import* 
import requests
from tkinter import messagebox
import app
import preventive
import mainpage
import ticket
import preventive
import invoices
import login
from fpdf import FPDF
from tkinter import ttk
#`id_preventivo`, `id_ticket`, `id_professionista`, `descrizione_intervento`, `materiali_o_ricambi_previsti`, `costo`, `dataora_intervento`
bill = {
        'id_ticket': ' ',
        'id_preventivo': ' ',
        'id_professionista': ' ',
        "stato" : ' ',
        "categoria" : ' ',
        "titolo": ' ',
        "descrizione" : ' ',
        'materiali_o_ricambi_previsti': ' ',
        'costo': ' ',
        'dataora_intervento': ' ',
        'email': ' '
        }

ticketId = -1

class Bill(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        buttonframe = Frame(self, highlightbackground="blue", highlightthickness=2, width=700, height=250)
        buttonframe.pack(side="top", fill="x")

        b1 = Button(buttonframe, text="Home", command=lambda: controller.show_frame(mainpage.MainPage))
        b2 = Button(buttonframe, text="Nuovi Ticket", command=lambda: controller.show_frame(ticket.Ticket))
        b3 = Button(buttonframe, text="Preventivi in Attesa", command=lambda: controller.show_frame(preventive.PreventiveAll))
        b4 = Button(buttonframe, text="Fatturazione", command=lambda: controller.show_frame(invoices.Invoices))
        b5 = Button(buttonframe, text="Logout", command= lambda:logout(controller))

        b1.grid(row = 0, column = 2, pady = 10, padx = 20)
        b2.grid(row = 0, column = 4, pady = 10, padx = 20)
        b3.grid(row = 0, column = 6, pady = 10, padx = 20)
        b4.grid(row = 0, column = 8, pady = 10, padx = 20)
        b5.grid(row = 0, column = 10, pady = 10, padx = 20)

        title = Label(self, text="Fattura", font=("times new roman", 20, "bold"), fg="Black")
        title.pack(side="top",anchor=CENTER)

        frameTable = Frame(self, highlightbackground="red", highlightthickness=2, width=900, height=30)
        frameTable.pack(expand=True,  anchor=CENTER)

        frameTable2 = Frame(self, highlightbackground="red", highlightthickness=2, width=900, height=30)
        frameTable2.pack(expand=True,  anchor=CENTER)

        title = Label(frameTable, text="Ticket", font=("times new roman", 12, "bold"), fg="Black")
        title.pack(side="top",anchor=CENTER)

        title = Label(frameTable2, text="Preventivo", font=("times new roman", 12, "bold"), fg="Black")
        title.pack(side="top",anchor=CENTER)

        infoframe = Frame(self, highlightbackground="red", highlightthickness=2, width=700, height=100)
        infoframe.pack(expand=True,  anchor=CENTER)

        contentframe = Frame(self, highlightbackground="red", highlightthickness=2, width=700, height=100)
        contentframe.pack(expand=True,  anchor=CENTER)

         # crea PDF fattura ------------------------------------------------------------------------------
            
        title = Label(infoframe, text="Crea e Invia la Fattura", font=("times new roman", 12, "bold"), fg="Black")
        title.pack(side="top",anchor=CENTER)
        b = Button(infoframe, text="Crea Fattura", command= lambda  : insertFatturaProfessionist())
        b.pack(side="top",anchor=CENTER)
        
# tabella ticket -------------------------------------------------------------------------------------------------------
        def printPreventivi(*args):
            jsn = getTicketProfessionistById()
            ticketId = -1

            total_rows = len(jsn)
            lst = ["Id", "Stato", "Categoria", "Titolo", "Descrizione"]

            tree = ttk.Treeview(frameTable,name = "tree", selectmode="browse", height=1)
            tree['columns'] = ('Id', 'Stato', 'Categoria', 'Titolo', 'Descrizione')

            tree.column("#0", width=0,  stretch=NO)
            tree.column("Id",anchor=CENTER, width=30)
            tree.column("Stato",anchor=CENTER,width=60)
            tree.column("Categoria",anchor=CENTER,width=150)
            tree.column("Titolo",anchor=CENTER,width=200)
            tree.column("Descrizione",anchor=CENTER,width=400)

            tree.heading("#0",text="",anchor=CENTER)
            tree.heading("Id",text="Id",anchor=CENTER)
            tree.heading("Stato",text="Stato",anchor=CENTER)
            tree.heading("Categoria",text="Categoria",anchor=CENTER)
            tree.heading("Titolo",text="Titolo",anchor=CENTER)
            tree.heading("Descrizione",text="Descrizione",anchor=CENTER)
            
            for i in range(total_rows):   #row
                bill['id_ticket'] = jsn[i][lst[0]]
                bill['stato'] = jsn[i][lst[1]]
                bill['categoria'] = jsn[i][lst[2]]
                bill['titolo'] = jsn[i][lst[3]]
                bill['descrizione'] = jsn[i][lst[4]]

                tree.insert(parent='',index='end',iid=i,text='', values=( jsn[i][lst[0]], jsn[i][lst[1]], jsn[i][lst[2]], jsn[i][lst[3]],  jsn[i][lst[4]]))
            
            tree.bind("<Button-1>", lambda *args: self._handle_button(*args,tree,controller)) #'<Alt-t>'

            tree.pack()

#tabella preventivo ____________________________________________________________________________________________________________________________________
            print("getPreventivoByIdTicket()")
            js = getPreventivoByIdTicket()
            preventiveId = -1

            total_rows = len(js)
            lst = ['Id', 'IdTicket', 'IdProfessionista', 'Descrizione', 'MaterialiRicambi', 'Costo', 'DataOra']

            treePreventivo = ttk.Treeview(frameTable2,name = "treePreventivo", selectmode="browse", height=1)
            treePreventivo['columns'] = ('Descrizione', 'Materiali/Ricambi', 'Costo', 'Data e Ora')

            treePreventivo.column("#0", width=0,  stretch=NO)
            treePreventivo.column("Descrizione",anchor=CENTER,width=400)
            treePreventivo.column("Materiali/Ricambi",anchor=CENTER,width=200)
            treePreventivo.column("Costo",anchor=CENTER,width=50)
            treePreventivo.column("Data e Ora",anchor=CENTER,width=200)

            treePreventivo.heading("#0",text="",anchor=CENTER)
            treePreventivo.heading("Descrizione",text="Descrizione",anchor=CENTER)
            treePreventivo.heading("Materiali/Ricambi",text="Materiali/Ricambi",anchor=CENTER)
            treePreventivo.heading("Costo",text="Costo",anchor=CENTER)
            treePreventivo.heading("Data e Ora",text="Data e Ora",anchor=CENTER)
  
            for i in range(total_rows):   #row
                bill['id_preventivo'] = js[i][lst[0]]
                bill['id_professionista'] = js[i][lst[2]]
                bill['descrizione'] = js[i][lst[3]]
                bill['materiali_o_ricambi_previsti'] = js[i][lst[4]]
                bill['costo'] = js[i][lst[5]]
                bill['dataora_intervento'] = js[i][lst[6]]
                treePreventivo.insert(parent='',index='end',iid=i,text='', values=( js[i][lst[3]], js[i][lst[4]], js[i][lst[5]], js[i][lst[6]]))
            
            #treePreventivo.bind("<Button-1>", lambda *args: self._handle_button(*args,treePreventivo,controller)) #'<Alt-t>'
            treePreventivo.pack()
 # FORM _________________________________________________________________________________________________________________________________________           

            title = Label(contentframe, text="Aggiorna Costo Intervento", font=("times new roman", 12, "bold"), fg="Black")
            title.grid(row= 1, column=1 )

            lst = ['Id', 'IdTicket', 'IdProfessionista', 'Descrizione', 'MaterialiRicambi', 'Costo', 'DataOra']

            self.e = Entry(contentframe, width=10, bg='LightBlue',fg='Black',font=('Arial', 10, 'bold'))
            list_entry = []
            self.e.grid(row=4, column=1)
            list_entry.append(self.e)
            self.e.insert(END, bill['costo'])
            self.e = Entry(contentframe, width=30, font=('Arial',10,'bold'))
            
            self.e = Button(contentframe, text=">>>", command= lambda  : updateCosto(list_entry))
            self.e.grid(row=5, column=3) # , width=4, height=2


        contentframe.bind('<Visibility>',lambda  *args: printPreventivi(*args) )
    

        

def getTicketProfessionistById():
            print("getTicketProfessionistById")
            url = 'http://localhost:8000/geticketsprofessionistbyid'
            #print("id ticket : " + str(ticketId))
            credentials = { 'email': app.session['email'], 'idTicket': ticketId }
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            response = requests.post(url, data=credentials, headers=headers)
            #print("Status code: ", response.status_code)
            #print("text: ", response.text)

            if response.text != None :
                return response.json() 
            else:
                return response.text  
        
def getPreventivoByIdTicket():
            print("getPreventivoProfessionistById")
            url = 'http://localhost:8000/getpreventivoprofessionistbyidticket'
            #print("id preventivo : " + str(ticketId))
            credentials = { 'email': app.session['email'], 'idTicket': ticketId }
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            response = requests.post(url, data=credentials, headers=headers)
            #print("Status code: ", response.status_code)
            #print("text: ", response.text)

            if response.text != None :
                return response.json() 
            else:
                return response.text  


def insertFatturaProfessionist():  
    print("/insertFatturaProfessionist")
# creazione PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    pdf.cell(200, 10, txt = "Fattura", ln = 1, align = 'C')
    pdf.cell( 100, 20, txt = "Id Ticket:  " + str(bill['id_ticket'])+ "                   Stato: " + str(bill['stato'])  , ln = 2, align = 'C')
    pdf.cell( 100, 20, txt = "Cateoria:  " + str(bill['categoria'])  + "              Titolo: " + str(bill['titolo']) , ln = 2, align = 'C')
    pdf.cell( 100, 20, txt = "Descrizione: " + str(bill['descrizione'])  ,ln = 2, align = 'C')
    pdf.cell( 100, 20, txt ="Materiali e Ricambi: " + str(bill['materiali_o_ricambi_previsti']),ln = 2, align = 'C')
    pdf.cell( 200, 20, txt =" Costo: " + str(bill['costo'])  + " euro",ln = 2, align = 'C')

    path = "./fatture/Fattura-Id" + str(bill['id_ticket']) +"-p"+ str(bill['id_preventivo'])+"-"+str(random()) + ".pdf"
    pdf.output(path)
#Upload 
    file ={'file': open(path, 'rb')} 
    print(file)
    url = 'http://localhost:8000/uploadfile'
    test_response = requests.post(url, files = file )

    if test_response.ok:
        print("Upload effettuato correttamente")
        print("\n")
        print(test_response)
        print("\n")
        print(test_response.text)
    else:
        print("upload non riuscito")

# insert db 
    url = 'http://localhost:8000/insertFatturaProfessionist'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    bill['email'] = app.session['email']
    credentials = { 'email': app.session['email'], 
                'id_ticket': bill['id_ticket'],
                'id_professionista': bill['id_professionista'],
                'id_preventivo': bill['id_preventivo'],
                'path': path
                 }
    response = requests.post(url, data=credentials, headers=headers)
    #print("Status code: ", response.status_code)
    #print("text: ", response.text)

    if response.text == 'Inserito correttamente':
        messagebox.showinfo('Risultato Inserimento','Fattura creata e inviata correttamente')
    else:
        messagebox.showinfo('Risultato Inserimento','inserimento negato')
    return response.text  


def updateCosto(list_entry):  # da cambiare ****__
    print("/updateCosto")
    url = 'http://localhost:8000/updatecostoProfessionist'

    for obj in list_entry:
        print(obj.get())
  
    payload = { 
                'email': app.session['email'], 
                'id_ticket': bill['id_ticket'],
                'id_professionista': bill['id_professionista'],
                'id_preventivo': bill['id_preventivo'],
                'costo': obj.get()
                 }

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, data=payload, headers=headers)
    print("Status code: ", response.status_code)
    print("text: ", response.text)

    if response.text == "inserito correttamente":
        messagebox.showinfo('Risultato Inserimento',response.text)
    else:
        messagebox.showinfo('Risultato Inserimento','inserimento negato')
    return response.text      




def getFatturaProfessionist(): #id_fattura	id_ticket	id_professionista	path_fattura
    print("getpreventiviprofessionist")
    url = 'http://localhost:8000/getpreventiviprofessionist'

    #print("email " + app.session['email'])
    credentials = { 'email': app.session['email']}
    #print("credentials " + credentials["email"])
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, data=credentials, headers=headers)
    #print("Status code: ", response.status_code)
    #print("text: ", response.text)

    if response.text != None :
        return response.json() 
    else:
        return response.text  
 

def logout(controller):
    app.session["email"] = ""
    app.session["login"] = 0
    controller.show_frame(login.LoginFrame) 

class billAll(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        buttonframe = Frame(self, highlightbackground="blue", highlightthickness=2, width=700, height=250)
        buttonframe.pack(side="top", fill="x")

        b1 = Button(buttonframe, text="Home", command=lambda: controller.show_frame(mainpage.MainPage))
        b2 = Button(buttonframe, text="Nuovi Ticket", command=lambda: controller.show_frame(ticket.Ticket))
        b3 = Button(buttonframe, text="Preventivi in Attesa", command=lambda: controller.show_frame(preventive.PreventiveAll))
        b4 = Button(buttonframe, text="Fatturazione", command=lambda: controller.show_frame(invoices.Invoices))
        b5 = Button(buttonframe, text="Logout", command= lambda:logout(controller))

        b1.grid(row = 0, column = 2, pady = 10, padx = 20)
        b2.grid(row = 0, column = 4, pady = 10, padx = 20)
        b3.grid(row = 0, column = 6, pady = 10, padx = 20)
        b4.grid(row = 0, column = 8, pady = 10, padx = 20)
        b5.grid(row = 0, column = 10, pady = 10, padx = 20)

        title = Label(self, text="Preventivi", font=("times new roman", 20, "bold"), fg="Black")
        title.pack(side="top",anchor=CENTER)

        frameTable = Frame(self, highlightbackground="red", highlightthickness=2, width=700, height=30)
        frameTable.pack(expand=True,  anchor=CENTER)

        lst = ['IdTicket', 'Descrizione', 'MaterialiRicambi', 'Costo', 'DataOra']

        tree = ttk.Treeview(frameTable,name = "tree", selectmode="browse", height=1)
        tree['columns'] = ('Id', 'Descrizione', 'Materiali', 'Costo', 'Data')

        tree.column("#0", width=0,  stretch=NO)
        tree.column("Id",anchor=CENTER, width=20)
        tree.column("Descrizione",anchor=CENTER,width=60)
        tree.column("Materiali",anchor=CENTER,width=150)
        tree.column("Costo",anchor=CENTER,width=150)
        tree.column("Data",anchor=CENTER,width=400)

        tree.heading("#0",text="",anchor=CENTER)
        tree.heading("Id",text="Id",anchor=CENTER)
        tree.heading("Descrizione",text="Descrizione",anchor=CENTER)
        tree.heading("Materiali",text="Materiali",anchor=CENTER)
        tree.heading("Costo",text="Costo",anchor=CENTER)
        tree.heading("Data",text="Data",anchor=CENTER)
     

        def printAllPreventivi(*args):
            print("printAllPreventivi")
            jsn = getPreventiviProfessionist()

            total_rows = len(jsn)
            print(total_rows)

            
            for i in range(total_rows):   #row `id_preventivo`, `id_ticket`, `id_professionista`, `descrizione_intervento`, `materiali_o_ricambi_previsti`, `costo`, `dataora_intervento`
                tree.insert(parent='',index='end',iid=i,text='', values=( jsn[i][lst[0]], jsn[i][lst[1]], jsn[i][lst[2]], jsn[i][lst[3]],  jsn[i][lst[4]]))

            
            #tree.bind("<Button-1>", lambda *args: self._handle_button(*args,tree,controller)) #'<Alt-t>'

            tree.pack()



        frameTable.bind('<Visibility>',lambda  *args: printAllPreventivi(*args) )