from array import array
from tkinter import* 
from tkinter import ttk
from turtle import width
import requests
import bill
import app
import preventive
import mainpage
import ticket
import preventive
import invoices
import login

payload = {
        'descrizione_intervento': ' ',
        'materiali_o_ricambi_previsti': ' ',
        'costo': ' ',
        'dataora_intervento': ' ',
        'id_ticket': ' ',
        'email': ' ',
        }

ticket = -1



class Invoices(Frame):
 def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        print("Ticket")

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

        lst = ["Id", "Stato", "Categoria", "Titolo", "Descrizione"]

        title = Label(self, text="Fatture in corso", font=("times new roman", 20, "bold"), fg="Black")
        title.pack(side="top",anchor=CENTER)

        title2 = Label(self, text="selezionare la fattura da mandare al cliente", font=("times new roman", 15, "bold"), fg="Black")
        title2.pack(side="top",anchor=CENTER)

        frameTable = Frame(self,name= "frameTable" , highlightbackground="red", highlightthickness=2, width=700, height=250)
        frameTable.pack(expand=True,  anchor=CENTER, pady=5, padx=5)

        updateButton = Frame(self,name= "updateButton" , highlightbackground="red", highlightthickness=2, width=700, height=250)
        updateButton.pack(expand=True,  anchor=SE, pady=5, padx=5)

        b = Button(updateButton, text="Aggiorna", command= lambda *args: printTicket(*args))
        b.pack(side="right",anchor=CENTER)

        table_scroll = Scrollbar(frameTable)
        table_scroll.pack(side=RIGHT, fill=Y)

        table_scroll = Scrollbar(frameTable,orient='horizontal')
        table_scroll.pack(side= BOTTOM,fill=X)

        tree = ttk.Treeview(frameTable,name = "tree",yscrollcommand=table_scroll.set, xscrollcommand =table_scroll.set, selectmode="browse")

        table_scroll.config(command=tree.yview)
        table_scroll.config(command=tree.xview)

        tree['columns'] = ('Id', 'Stato', 'Categoria', 'Titolo', 'Descrizione')    
        
        tree.column("#0", width=0,  stretch=NO)
        tree.column("Id",anchor=CENTER, width=30)
        tree.column("Stato",anchor=CENTER,width=150)
        tree.column("Categoria",anchor=CENTER,width=150)
        tree.column("Titolo",anchor=CENTER,width=150)
        tree.column("Descrizione",anchor=CENTER,width=400)

        tree.heading("#0",text="",anchor=CENTER)
        tree.heading("Id",text="Id",anchor=CENTER)
        tree.heading("Stato",text="Stato",anchor=CENTER)
        tree.heading("Categoria",text="Categoria",anchor=CENTER)
        tree.heading("Titolo",text="Titolo",anchor=CENTER)
        tree.heading("Descrizione",text="Descrizione",anchor=CENTER)
                
        def printTicket(*args):
            jsn = getTicketProfessionist()
            
            total_rows = len(jsn)
            print(jsn)
            print(type(jsn))
            
            for i in range(total_rows):   #row
             if jsn[i][lst[1]] == 'in corso' :
                  tree.insert(parent='',index='end',iid=i,text='', values=( jsn[i][lst[0]], jsn[i][lst[1]], jsn[i][lst[2]], jsn[i][lst[3]],  jsn[i][lst[4]]))
            
            tree.bind("<Button-1>", lambda *args: self._handle_button(*args,tree,controller)) #'<Alt-t>'
            tree.pack()
        
        frameTable.bind('<Visibility>',lambda  *args: printTicket(*args) )


 def _handle_button(self,event,tree,controller, *args):

            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                bill.ticketId = record[0]
                if bill.ticketId   != -1:
                  controller.show_frame(bill.Bill )

def logout(controller):
    app.session["email"] = ""
    app.session["login"] = 0
    controller.show_frame(login.LoginFrame) 

def getTicketProfessionist():
    print("getTicketProfessionist")
    url = 'http://localhost:8000/geticketsprofessionist'

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




               





    

               

    
