from tkinter import* 
from tkinter import ttk
import requests
import app
import preventive
import mainpage
import preventive
import invoices
import login
from PIL import Image, ImageTk


class Ticket(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        print("Ticket")

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
        b2 = Button(buttonframe, text="Nuovi Ticket", command=lambda: controller.show_frame(Ticket))
        b3 = Button(buttonframe, text="Preventivi in Attesa", command=lambda: controller.show_frame(preventive.PreventiveAll))
        b4 = Button(buttonframe, text="Fatturazione", command=lambda: controller.show_frame(invoices.Invoices))
        b5 = Button(buttonframe, text="Logout", command= lambda:logout(controller))

        b1.grid(row = 0, column = 4, pady = 10, padx = 20)
        b2.grid(row = 0, column = 6, pady = 10, padx = 20)
        b3.grid(row = 0, column = 8, pady = 10, padx = 20)
        b4.grid(row = 0, column = 10, pady = 10, padx = 20)
        b5.grid(row = 0, column = 12, pady = 10, padx = 20)

        title = Label(self, text="TICKET", font=("times new roman", 20, "bold"),fg="Gray")
        title.pack(side="top",anchor=CENTER)

        frameTable = Frame(self,name= "frameTable" ,  highlightthickness=2, width=700, height=250)
        frameTable.pack(expand=True,  anchor=CENTER, pady=5, padx=5)

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


        def printTicket(*args):
            jsn = getTicketProfessionist()
            total_rows = len(jsn)
            
            for i in tree.get_children():
              tree.delete(i)

            for i in range(total_rows):   
              if jsn[i][lst[1]] == 'creato' :
                tree.insert(parent='',index='end',iid=i,text='', values=( jsn[i][lst[0]], jsn[i][lst[1]], jsn[i][lst[2]], jsn[i][lst[3]],  jsn[i][lst[4]]))
            
            tree.bind("<Button-1>", lambda *args: self._handle_button(*args,tree,controller)) #'<Alt-t>'
            tree.pack()
        

        frameTable.bind('<Visibility>',lambda  *args: printTicket(*args) )


 
    def _handle_button(self,event,tree,controller, *args):
            print(self)
            print(tree)
            print(type(self))

            children_widgets = tree.winfo_children()
            for child_widget in children_widgets:
                print(child_widget)

            #print(args)
            print(event.num)
            print(event.x)
            print(event.y)
            #tree = self.focus_get()
            print(tree.focus_get())

            for selected_item in tree.selection():
                item = tree.item(selected_item)
                print(item)
                record = item['values']
                print(record)
                print(record[0])
                preventive.preventiveId = record[0]
                if preventive.preventiveId  != -1:
                  controller.show_frame(preventive.PreventiveId)


def logout(controller):
    app.session["id"] = ""
    app.session["login"] = 0
    controller.show_frame(login.LoginFrame)

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




               





    
