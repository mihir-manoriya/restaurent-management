import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from sqlite3 import Error

class B():


    def __init__(self):
        self.con=sqlite3.connect("rest-db.db")
        print("Connection established")

        
    def RawMaterial_fetch(self):
            
        self.cur=self.con.cursor()
        self.cur.execute("SELECT * from Raw_material")
        self.RawMaterial_res = self.cur.fetchall()

    def Menu_fetch(self):
            
        self.cur=self.con.cursor()
        self.cur.execute("SELECT * from Menu")
        self.Menu_res = self.cur.fetchall()

        

    def screen(self):
        self.root=Tk()
        self.root.title("My App")
        self.root.resizable(height=False, width=False)

        self.canvas=Canvas(self.root,width=1200,height=500)
        self.img=ImageTk.PhotoImage(Image.open("rest-bg.jpg"))
        self.canvas.create_image(0,0,anchor=NW,image=self.img)
        self.canvas.pack()

        

    def controls(self):

        #Buttons For Home Screen

        self.lb1=Label(self.root,text="Restaurant Management System", font=('calibri',30))
        self.canvas.create_window(600,150,window=self.lb1)

        self.btn1=Button(text='Billing System',width=30,height=3,command=self.Billing)
        self.canvas.create_window(350,400,window=self.btn1)

        self.btn2=Button(text='Current Inventory',width=30,height=3,command=self.raw_management)
        self.canvas.create_window(650,400,window=self.btn2)

        self.btn2=Button(text='List Updatation',width=30,height=3,command=self.listupdate)
        self.canvas.create_window(950,400,window=self.btn2)

    def Billing(self):
            self.Bill_screen=Tk()
            self.Bill_screen.title("Billing")
            self.Bill_screen.resizable(height=False, width=False)

            self.canvas=Canvas(self.Bill_screen,width=800,height=400)
            self.canvas.pack()

            # Table 1
            
            self.Table1=Button(self.Bill_screen,text='Table 1',width=30,height=3,command=self.Invoice)
            self.canvas.create_window(180,100,window=self.Table1)

            # Table 2
            
            self.Table2=Button(self.Bill_screen,text='Table 2',width=30,height=3,command=self.Invoice)
            self.canvas.create_window(420,100,window=self.Table2)

            # Table 3
            
            self.Table3=Button(self.Bill_screen,text='Table 3',width=30,height=3,command=self.Invoice)
            self.canvas.create_window(650,100,window=self.Table3)

            # Table 4
            
            self.Table4=Button(self.Bill_screen,text='Table 4',width=30,height=3,command=self.Invoice)
            self.canvas.create_window(180,200,window=self.Table4)

            # Table 5
            
            self.Table5=Button(self.Bill_screen,text='Table 5',width=30,height=3,command=self.Invoice)
            self.canvas.create_window(420,200,window=self.Table5)

            # Table 6
            
            self.Table6=Button(self.Bill_screen,text='Table 6',width=30,height=3,command=self.Invoice)
            self.canvas.create_window(650,200,window=self.Table6)

    def Invoice(self):
        self.menulist=[]
        self.menuprice=[]

        self.cur=self.con.cursor()
        self.cur.execute("SELECT * from Menu")
        self.Menu_res = self.cur.fetchall()
        self.Menu_len=len(self.Menu_res)

        for self.i in self.Menu_res:
            self.menulist.append(self.i[1])
            self.menuprice.append(self.i[2])

        print(self.menulist)

        self.FinalInvoice_screen=Tk()
        self.FinalInvoice_screen.title("Invoice")
        self.FinalInvoice_screen.resizable(height=False, width=False)

        self.canvas=Canvas(self.FinalInvoice_screen,width=600,height=500)
        self.canvas.pack()

                    # Heading 
        self.lb=Label(self.FinalInvoice_screen,text="Invoice", font=('calibri',30))
        self.canvas.create_window(300,50,window=self.lb)

                    #Customer Name
        self.name=Label(self.FinalInvoice_screen,text="Customer Name", font=('calibri',12))
        self.canvas.create_window(110,110,window=self.name)
        
        self.customer=Entry(self.FinalInvoice_screen,width=20)
        self.canvas.create_window(250,110,window=self.customer)

                    #Menu Headhig
        self.menu_name=Label(self.FinalInvoice_screen,text="Food Items", font=('calibri',15))
        self.canvas.create_window(100,150,window=self.menu_name)

                    #Menu

        self.lb1=Label(self.FinalInvoice_screen,text=self.menulist[0], font=('calibri',10))
        self.canvas.create_window(133,200,window=self.lb1)

        self.lb2=Label(self.FinalInvoice_screen,text=self.menulist[1], font=('calibri',10))
        self.canvas.create_window(90,250,window=self.lb2)

        self.lb3=Label(self.FinalInvoice_screen,text=self.menulist[2], font=('calibri',10))
        self.canvas.create_window(90,300,window=self.lb3)

        self.lb4=Label(self.FinalInvoice_screen,text=self.menulist[3], font=('calibri',10))
        self.canvas.create_window(102,350,window=self.lb4)

        self.lb5=Label(self.FinalInvoice_screen,text=self.menulist[4], font=('calibri',10))
        self.canvas.create_window(98,400,window=self.lb5)

                        #Menu-Price

        self.lb11=Label(self.FinalInvoice_screen,text=self.menuprice[0], font=('calibri',10))
        self.canvas.create_window(250,200,window=self.lb11)

        self.lb12=Label(self.FinalInvoice_screen,text=self.menuprice[1], font=('calibri',10))
        self.canvas.create_window(250,250,window=self.lb12)

        self.lb13=Label(self.FinalInvoice_screen,text=self.menuprice[2], font=('calibri',10))
        self.canvas.create_window(250,300,window=self.lb13)

        self.lb14=Label(self.FinalInvoice_screen,text=self.menuprice[3], font=('calibri',10))
        self.canvas.create_window(250,350,window=self.lb14)

        self.lb15=Label(self.FinalInvoice_screen,text=self.menuprice[4], font=('calibri',10))
        self.canvas.create_window(250,400,window=self.lb15)

                    #For "*"

        self.lb6=Label(self.FinalInvoice_screen,text="*", font=('calibri',10))
        self.canvas.create_window(320,200,window=self.lb6)

        self.lb7=Label(self.FinalInvoice_screen,text="*", font=('calibri',10))
        self.canvas.create_window(320,250,window=self.lb7)

        self.lb8=Label(self.FinalInvoice_screen,text="*", font=('calibri',10))
        self.canvas.create_window(320,300,window=self.lb8)

        self.lb9=Label(self.FinalInvoice_screen,text="*", font=('calibri',10))
        self.canvas.create_window(320,350,window=self.lb9)

        self.lb10=Label(self.FinalInvoice_screen,text="*", font=('calibri',10))
        self.canvas.create_window(320,400,window=self.lb10)


                    #Menu Headhig
        self.menu_Quantity=Label(self.FinalInvoice_screen,text="Quantity", font=('calibri',15))
        self.canvas.create_window(400,150,window=self.menu_Quantity)

                # Textbox for Qnt#

        self.item1=Entry(self.FinalInvoice_screen,width=5)
        self.canvas.create_window(400,200,window=self.item1)

        self.item2=Entry(self.FinalInvoice_screen,width=5)
        self.canvas.create_window(400,250,window=self.item2)

        self.item3=Entry(self.FinalInvoice_screen,width=5)
        self.canvas.create_window(400,300,window=self.item3)

        self.item4=Entry(self.FinalInvoice_screen,width=5)
        self.canvas.create_window(400,350,window=self.item4)

        self.item5=Entry(self.FinalInvoice_screen,width=5)
        self.canvas.create_window(400,400,window=self.item5)

            # ID Button
        self.Amt_button=Button(self.FinalInvoice_screen,text='Total Amount',width=10,height=1,command=self.Amount)
        self.canvas.create_window(100,450,window=self.Amt_button)


    def Amount(self):

            self.val1=int(self.item1.get())
            self.val2=int(self.item2.get())
            self.val3=int(self.item3.get())
            self.val4=int(self.item4.get())
            self.val5=int(self.item5.get())

            self.price1=int(self.menuprice[0])
            self.price2=int(self.menuprice[1])
            self.price3=int(self.menuprice[2])
            self.price4=int(self.menuprice[3])
            self.price5=int(self.menuprice[4])

            

            self.finalitem1= self.price1 * self.val1
            self.finalitem2=self.price2*self.val2
            self.finalitem3=self.price3*self.val3
            self.finalitem4=self.price4*self.val4
            self.finalitem5=self.price5*self.val5
            self.TotalAmount=self.finalitem1+self.finalitem2+self.finalitem3+self.finalitem4+self.finalitem5

                        #Price after qunatity

            self.lb16=Label(self.FinalInvoice_screen,text=self.finalitem1, font=('calibri',10))
            self.canvas.create_window(450,200,window=self.lb16)

            self.lb17=Label(self.FinalInvoice_screen,text=self.finalitem2, font=('calibri',10))
            self.canvas.create_window(450,250,window=self.lb17)

            self.lb18=Label(self.FinalInvoice_screen,text=self.finalitem3, font=('calibri',10))
            self.canvas.create_window(450,300,window=self.lb18)

            self.lb19=Label(self.FinalInvoice_screen,text=self.finalitem4, font=('calibri',10))
            self.canvas.create_window(450,350,window=self.lb19)

            self.lb20=Label(self.FinalInvoice_screen,text=self.finalitem5, font=('calibri',10))
            self.canvas.create_window(450,400,window=self.lb20)

            
        

                        #Total Amount
            self.Total=Label(self.FinalInvoice_screen,text=self.TotalAmount, font=('calibri',15))
            print(self.TotalAmount)
            self.canvas.create_window(450,450,window=self.Total)


             # Pay Button
            self.Pay_button=Button(self.FinalInvoice_screen,text='Pay',width=10,height=1,command=self.Record)
            self.canvas.create_window(200,450,window=self.Pay_button)


    def Record(self):

        self.CName=self.customer.get()
        print(self.CName)

        self.Thankyou_screen=Tk()
        self.Thankyou_screen.title("Thank You")
        self.Thankyou_screen.resizable(height=False, width=False)

        self.canvas=Canvas(self.Thankyou_screen,width=500,height=400)
        self.canvas.pack()

        self.lb=Label(self.Thankyou_screen,text=self.CName+" thank you for paying Rs. "+ str(self.TotalAmount), font=('calibri',20))
        self.canvas.create_window(250,200,window=self.lb)

        self.lb1=Label(self.Thankyou_screen,text=" Visit Us Again ", font=('calibri',20),bg='Grey')
        self.canvas.create_window(250,300,window=self.lb1)

        
         

    def raw_management(self):

            self.inventory_screen=Tk()
            self.inventory_screen.title("Inventory")
            self.inventory_screen.resizable(height=False, width=False)

            self.canvas=Canvas(self.inventory_screen,width=800,height=400)
            self.canvas.pack()
            
            
             #Treeview
            self.tree=ttk.Treeview(self.inventory_screen,height=15)
            
            self.vsb = ttk.Scrollbar(self.inventory_screen)
            #self.tree.configure(yscrollcommand=self.vsb.set)
            
            self.canvas.create_window(400,200,window=self.tree)
            
            self.tree["columns"]=("one","two","three","four")
            self.tree.column("#0", width=100, minwidth=50)
            self.tree.column("one", width=100, minwidth=50)
            self.tree.column("two", width=100, minwidth=50)
            self.tree.column("three",width=100, minwidth=50)
            self.tree.column("four", width=100, minwidth=50)
            
            self.tree.heading("#0",text="Item Id",anchor=S)
            self.tree.heading("one", text="Item Name",anchor=S)
            self.tree.heading("two", text="Item Price",anchor=S)
            self.tree.heading("three", text="Item Quantity",anchor=S)
            self.tree.heading("four", text="Unit Type",anchor=S)

            

            for self.row in self.RawMaterial_res:
               self.tree.insert('', 'end', text=self.row[0],values=(self.row[1],self.row[2],self.row[3],self.row[4]))


    def listupdate(self):
        
            self.Menu_screen=Tk()
            self.Menu_screen.title("Menu")
            self.Menu_screen.resizable(height=False, width=False)

            self.canvas=Canvas(self.Menu_screen,width=800,height=400)
            self.canvas.pack()

            

             #Treeview
            self.tree=ttk.Treeview(self.Menu_screen,height=15)
            
            self.vsb = ttk.Scrollbar(self.Menu_screen)
            #self.tree.configure(yscrollcommand=self.vsb.set)
            
            self.canvas.create_window(400,200,window=self.tree)
            
            self.tree["columns"]=("one","two")
            self.tree.column("#0", width=100, minwidth=50)
            self.tree.column("one", width=200, minwidth=50)
            self.tree.column("two", width=100, minwidth=50)
            
            
            self.tree.heading("#0",text="Menu Id",anchor=S)
            self.tree.heading("one", text="Menu Name",anchor=S)
            self.tree.heading("two", text="Menu Price",anchor=S)

            for self.row in self.Menu_res:
               self.tree.insert('', 'end', text=self.row[0],values=(self.row[1],self.row[2]))

            

             #ID for show

            self.lb7=Label(self.Menu_screen,text="Enter Menu Id", font=('calibri',10),bg='light grey')
            self.canvas.create_window(100,100,window=self.lb7)

            #TextBox For Id
            self.text_id=Entry(self.Menu_screen,width=15)
            self.canvas.create_window(100,130,window=self.text_id)

            
            #To change price

            self.lb8=Label(self.Menu_screen,text="Enter Price", font=('calibri',10),bg='light grey')
            self.canvas.create_window(100,170,window=self.lb8)

            #TextBox For Price
            self.text_price=Entry(self.Menu_screen,width=15)
            self.canvas.create_window(100,200,window=self.text_price)

            

            # ID Button
            self.ID_button=Button(self.Menu_screen,text='Get Data',width=5,height=1,command=self.getMenuId)
            self.canvas.create_window(175,130,window=self.ID_button)

            

            # Update Button
            
            self.update_button=Button(self.Menu_screen,text='Update Data',width=15,height=1,command=self.Updatevalue)
            self.canvas.create_window(100,300,window=self.update_button)

            

    def Updatevalue(self):
        
        self.newprice=self.text_price.get()
        print(self.newprice)
        self.cur=self.con.cursor()
        self.cur.execute("UPDATE Menu SET menu_Price="+self.newprice+" WHERE menu_Id="+self.data)
        self.con.commit()
        print("Success")
           
    

    def getMenuId(self):
        self.data=self.text_id.get()
        self.cur=self.con.cursor()
        self.cur.execute("SELECT menu_Price from Menu where menu_Id="+self.data)
        self.res=self.cur.fetchone()
        print(self.res)

        #TextBox For Price
        self.text_price.insert(0,self.res)

        return self.data



ob=B()
ob.screen()
ob.controls()
ob.RawMaterial_fetch()
ob.Menu_fetch()




