from tkinter import* 
import requests
import app
import ticket
import preventive
import invoices
import login
from tkinter import ttk
from PIL import Image, ImageTk

nome = None

class MainPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        print("MainPage")
        print(app.session["id"])

        title = Label(self, text="HOME",  font=("times new roman", 20, "bold"), fg="Gray")
        title.pack(side="top",anchor=CENTER)

        buttonframe = Frame(self,highlightbackground="gray", bg="gray92", highlightthickness=2, width=700, height=250)
        buttonframe.pack(side="left")

        imgframe = Frame(buttonframe,bg="gray92", highlightthickness=2, width=200, height=200)
        imgframe.grid(row = 1, column = 0, pady = 10, padx = 10)

        load = Image.open("./img/instafix.png")
        render = ImageTk.PhotoImage(load)
        img = Label(imgframe, image=render)
        img.image = render
        img.pack(side="top",anchor=CENTER)

        frameTable = Frame(self,name= "frameTable", highlightthickness=2, width=700, height=800)
        frameTable.pack(side="right",  anchor=CENTER, pady=5, padx=5)

        b1 = Button(buttonframe, text="Home", command=lambda: controller.show_frame(MainPage))
        b2 = Button(buttonframe, text="Nuovi Ticket", command=lambda: controller.show_frame(ticket.Ticket))
        b3 = Button(buttonframe, text="Preventivi in Attesa", command=lambda: controller.show_frame(preventive.PreventiveAll))
        b4 = Button(buttonframe, text="Fatturazione", command=lambda: controller.show_frame(invoices.Invoices))
        b5 = Button(buttonframe, text="Logout", command= lambda:logout(controller))

        b1.grid(row = 6, column = 0, pady = 10, padx = 10)
        b2.grid(row = 8, column = 0, pady = 10, padx = 10)
        b3.grid(row = 10, column = 0, pady = 10, padx = 10)
        b4.grid(row = 12, column = 0, pady = 10, padx = 10)
        b5.grid(row = 14, column = 0, pady = 10, padx = 10)

        lst = ["Id", "Stato", "Categoria", "Titolo", "Descrizione"]

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
        tree.column("Stato",anchor=CENTER,width=70)
        tree.column("Categoria",anchor=CENTER,width=150)
        tree.column("Titolo",anchor=CENTER,width=150)
        tree.column("Descrizione",anchor=CENTER,width=400)

        tree.heading("#0",text="",anchor=CENTER)
        tree.heading("Id",text="Id",anchor=CENTER)
        tree.heading("Stato",text="Stato",anchor=CENTER)
        tree.heading("Categoria",text="Categoria",anchor=CENTER)
        tree.heading("Titolo",text="Titolo",anchor=CENTER)
        tree.heading("Descrizione",text="Descrizione",anchor=CENTER)

        print(" ID: "+ app.session["id"])

        frameTable.bind('<Expose>',lambda  *args: MainPage.printTicket(tree,buttonframe,*args) )

    def printTicket(tree,buttonframe,*args):
        nome = MainPage.getnome()
        l1 = Label(buttonframe, text="Benvenuto " + nome, bg="gray92", font=("times new roman", 15, "bold"), fg="Gray")
        l1.grid(row = 3, column = 0, pady = 0, padx = 0)

        recensione = MainPage.getRecensione()
        l2 = Label(buttonframe, text="La tua recensione\n media è: " + recensione, bg="gray92", font=("times new roman", 15, "bold"), fg="Gray")
        l2.grid(row = 4, column = 0, pady = 0, padx = 0)



        jsn = MainPage.getTicketProfessionist()

        if(len(tree.get_children())!= 0 ):
            for i in tree.get_children():
                tree.delete(i)

        if(jsn != None):
            total_rows = len(jsn)
            lst = ["Id", "Stato", "Categoria", "Titolo", "Descrizione"]

            for i in range(total_rows):   
                if jsn[i][lst[1]] == 'creato' or jsn[i][lst[1]] == 'in attesa' or jsn[i][lst[1]] == 'in corso':
                    tree.insert(parent='',index='end',iid=i,text='', values=( jsn[i][lst[0]], jsn[i][lst[1]], jsn[i][lst[2]], jsn[i][lst[3]],  jsn[i][lst[4]]))

        tree.pack()

    def _handle_button(self,event,tree,controller, *args):
            children_widgets = tree.winfo_children()
         #   for child_widget in children_widgets:
         #       print(child_widget)

            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                print("preventive id: " + record[0])
                preventive.preventiveId = record[0]
                if preventive.preventiveId  != -1:
                  controller.show_frame(preventive.PreventiveId)
    
    def getnome():
        print("getnome")
        url = 'http://localhost:8000/getnomeprofessionist'
        credentials = { 'id_professionista': app.session['id']}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(url, data=credentials, headers=headers)
        return response.text

    def getRecensione():
        print("getRecensione")
        url = 'http://localhost:8000/getrecensioneprofessionist'
        credentials = { 'id_professionista': app.session['id']}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(url, data=credentials, headers=headers)
        print("recensione " + response.text )
        return response.text
    
    def getTicketProfessionist():
        print("getTicketProfessionist")
        url = 'http://localhost:8000/geticketsprofessionist'
        credentials = { 'id_professionista': app.session['id']}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(url, data=credentials, headers=headers)

        if response.text != None :
            return response.json() 
        else:
            return response.text

def logout(controller):
    app.session["id"] = " "
    app.session["login"] = 0
    controller.show_frame(login.LoginFrame)







    
