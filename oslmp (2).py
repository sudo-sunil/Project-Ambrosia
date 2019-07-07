from tkinter import *
import sqlite3
import time
import random
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image

root=Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management System")

f=Frame(root,width=1600,height=200,bg='White',relief=SUNKEN)
f.pack(side=TOP,fill=BOTH,expand=True)

f1=Frame(root,width=1600,height=600,bg='White',relief=SUNKEN)
f1.pack(side=BOTTOM,fill=BOTH,expand=True)

#===========================================================================================Info============================================================================================
photo=PhotoImage(file="ambrosia.png")
lblimg=Label(f, image=photo)
lblimg.pack()
lblInfo=Label(f,font=('Helvetica',20,'bold'),text="(Pure Veg. Restaurant)",bg='White',bd=5,anchor='center')
lblInfo.pack()

#===========================================================================================Time============================================================================================
localtime=time.strftime("%a %b %e %H:%M %G", time.localtime(time.time()))
lblInfo=Label(f,font=('arial',20,'bold'),text=localtime,bd=5,bg='White',anchor='center')
lblInfo.pack()

#=====================================================================================Button Function=======================================================================================
def Clear():
    rand.set(random.randint(1,10001))
    tkvar1.set('Item 1')
    tkvar2.set('Item 2')
    tkvar3.set('Item 3')
    tkvar4.set('Item 4')
    tkvar5.set('Item 5')
    txtquant1.delete(0,'end')
    txtquant2.delete(0,'end')
    txtquant3.delete(0,'end')
    txtquant4.delete(0,'end')
    txtquant5.delete(0,'end')
    txtrate1.delete(0,'end')
    txtrate2.delete(0,'end')
    txtrate3.delete(0,'end')
    txtrate4.delete(0,'end')
    txtrate5.delete(0,'end')
    txttotal1.delete(0,'end')
    txttotal2.delete(0,'end')
    txttotal3.delete(0,'end')
    txttotal4.delete(0,'end')
    txttotal5.delete(0,'end')
    txtNTotal.delete(0,'end')
    txtGST.delete(0,'end')
    txtGTotal.delete(0,'end')
    v.set(4)

def ButtonClick():
    i1=tkvar1.get()
    i2=tkvar2.get()
    i3=tkvar3.get()
    i4=tkvar4.get()
    i5=tkvar5.get()
    '''print(i1)
    print(i2)
    print(i3)
    print(i4)
    print(i5)'''
    
    insertdb(i1,i2,i3,i4,i5)

def PayClick():
    val=v.get()
    if val==1:
        print("You Selected Card Payment Mode")
    if val==2:
        print("You Selected Cash Payment Mode")
    if val==3:
        print("You Selected E-Wallet Payment Mode")

def BillClick():
    #print("Nothing")
    c = canvas.Canvas(rand.get()+'.pdf',pagesize=landscape(letter))
    resimg="ambrosia.png"
    c.drawImage(resimg,250,450,width=None,height=None)

    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(675,450,"(Pure Veg. Restaurant)")
    
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(300,425,"Ref.No.")
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(400,425,rand.get())

    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(300,400,"Date")
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(400,400,time.strftime("%D", time.localtime(time.time())))

    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(300,350,"ITEMS")
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(450,350,"QUANTITY")
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(600,350,"PRICE")
    
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(300,300,tkvar1.get())
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(450,300,txtquant1.get())
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(600,300,total1.get())
    
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(300,275,tkvar2.get())
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(450,275,txtquant2.get())
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(600,275,total2.get())
    
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(300,250,tkvar3.get())
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(450,250,txtquant3.get())
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(600,250,total3.get())
    
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(300,225,tkvar4.get())
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(450,225,txtquant4.get())
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(600,225,total4.get())
    
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(300,200,tkvar5.get())
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(450,200,txtquant5.get())
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(600,200,total5.get())
    
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(450,150,"NET TOTAL")
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(600,150,ntotal.get())

    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(450,125,"GST")
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(600,125,gst.get())

    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(450,100,"GROSS TOTAL")
    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(600,100,gtotal.get())

    c.setFont('Helvetica',20,leading=None)
    c.drawCentredString(600,50,"Signature")

    c.showPage()
    c.save()

#=======================================================================================Calculations========================================================================================
def CalcTotal(r1,r2,r3,r4,r5):
    q1=txtquant1.get()
    q2=txtquant2.get()
    q3=txtquant3.get()
    q4=txtquant4.get()
    q5=txtquant5.get()
    rate1.set(str(r1))
    rate2.set(str(r2))
    rate3.set(str(r3))
    rate4.set(str(r4))
    rate5.set(str(r5))
    t1=float(int(q1)*int(r1))
    t2=float(int(q2)*int(r2))
    t3=float(int(q3)*int(r3))
    t4=float(int(q4)*int(r4))
    t5=float(int(q5)*int(r5))
    nt=(t1+t2+t3+t4+t5)
    perc=nt*5/100
    gt=(nt+perc)
    total1.set(str(t1))
    total2.set(str(t2))
    total3.set(str(t3))
    total4.set(str(t4))
    total5.set(str(t5))
    ntotal.set(str(nt))
    gst.set(str(perc))
    gtotal.set(str(gt))           

#=======================================================================================Declarations========================================================================================
rand=StringVar()

rate1=StringVar()
rate2=StringVar()
rate3=StringVar()
rate4=StringVar()
rate5=StringVar()

total1=StringVar()
total2=StringVar()
total3=StringVar()
total4=StringVar()
total5=StringVar()

ntotal=StringVar()
gst=StringVar()
gtotal=StringVar()
v=IntVar()

tkvar1=StringVar()
tkvar2=StringVar()
tkvar3=StringVar()
tkvar4=StringVar()
tkvar5=StringVar()
rand.set(random.randint(1,10001))

#=======================================================================================Reference No========================================================================================
lblReference= Label(f1,font=('arial',16,'bold'),text="Reference",bd=5,bg='White',anchor='w')
lblReference.grid(row=0,column=0)
txtReference=Entry(f1,font=('arial',16,'bold'),textvariable=rand,bd=5,bg="#E5E7E9", justify='right')
txtReference.grid(row=0,column=1)

#=====================================================================================Dropdown Options======================================================================================
values1={'Veg. Clear Soup','Tomato Soup','Veg Manchow Soup','Veg. Hot & Sour Soup','Sweet Corn Soup','Mushroom Soup'}
values2={'Plain Rice','Jeera Rice','Veg Pulav','Veg Biryani','Peas Pulav','Paneer Pulav','Lemon Rice','Phulka (Tawa Roti)','Puri','Butter Phulka','Paneer Paratha','Stuff Paratha','Butter Tanduri Roti','Garlic Naan','Lachha Paratha','Masala Kulcha','Makke Ki Roti'}
values3={'Plain Dal','Dal Fry','Dal Tadka','Dal Maharani','Dal Makhani','Mix Veg','Veg Kadhai','Veg Handi','Veg Kofta','Chana Masala','Aalu Jeera','Dum Aalu','Aalu Gobhi Masala','Paneer Butter Masala','Paneer Kofta','Paneer Bhurji','Palak Paneer','Mutter Paneer','Shahi Paneer','Sarso Ka Saag'}
values4={'Bundi Raita','Mix Veg. Raita','Onion Salad','Green Salad'}
values5={'Banana Milkshake','Chocolate Milkshake','Kiwi Milkshake','Strawberry Milkshake','Blackcurrant Milkshake','Mix Fruit Milkshake','Mango Milkshake','Blue Lagoon','Ginger & Mint','Fruit Punch','Lemon & Blackcurrant','Double Scoop(Choco,Vanilla)','Choco Blast Icecream','Kasata','Malai Kulfi(Pista)','Gulab Jamoon','Rasagulla'}
#initial display on optionmenu widget
tkvar1.set('Item 1')
tkvar2.set('Item 2')
tkvar3.set('Item 3')
tkvar4.set('Item 4')
tkvar5.set('Item 5')
#======================================================================================Column Headings======================================================================================
lblfitem=Label(f1,font=('arial',16,'bold'),text="Food Item",bd=5,bg='White',anchor='w')
lblfitem.grid(row=1,column=1)

lbq1=Label(f1,font=('arial',16,'bold'),text="Quantity",bd=5,bg='White',anchor='w')
lbq1.grid(row=1,column=2)

lbq1=Label(f1,font=('arial',16,'bold'),text="Price",bd=5,bg='White',anchor='w')
lbq1.grid(row=1,column=3)

lbq1=Label(f1,font=('arial',16,'bold'),text="Total",bd=5,bg='White',anchor='w')
lbq1.grid(row=1,column=4)

lblpm=Label(f1,font=('arial',16,'bold'),text="Mode Of Payment",bd=5,bg='White',anchor='w')
lblpm.grid(row=1,column=5)

#=======================================================================================Row Headings========================================================================================
lblItem1=Label(f1,font=('arial',16,'bold'),text="Starters",bd=5,bg='White',anchor='w')
lblItem1.grid(row=2,column=0)

lblItem2=Label(f1,font=('arial',16,'bold'),text="Main Course",bd=5,bg='White',anchor='w',)
lblItem2.grid(row=3,column=0)

lblItem3=Label(f1,font=('arial',16,'bold'),text="Side Dish",bd=5,bg='White',anchor='w')
lblItem3.grid(row=4,column=0)

lblItem4=Label(f1,font=('arial',16,'bold'),text="Raita/Salads",bd=5,bg='White',anchor='w')
lblItem4.grid(row=5)

lblItem5=Label(f1,font=('arial',16,'bold'),text="Dessert/Milk Shakes",bd=5,bg='White',anchor='w')
lblItem5.grid(row=6,column=0)

lblNTotal=Label(f1,font=('arial',16,'bold'),text="Net Total",bd=5,bg='White',anchor='w')
lblNTotal.grid(row=7,column=3)

lblGST=Label(f1,font=('arial',16,'bold'),text="GST",bd=5,bg='White',anchor='w')
lblGST.grid(row=8,column=3)

lblGTotal=Label(f1,font=('arial',16,'bold'),text="Gross Total",bd=5,bg='White',anchor='w')
lblGTotal.grid(row=9,column=3)

#================================================================================Food item option selection=================================================================================
opItem1=OptionMenu(f1,tkvar1,*values1)
opItem1.config(font=('arial',16,'bold'),bd=5,bg="#E5E7E9",justify='right')
opItem1["menu"].config(font=('arial',16,'bold'),bd=5,bg="#E5E7E9")
opItem1.grid(row=2,column=1,sticky="ew")

opItem2=OptionMenu(f1,tkvar2,*values2)
opItem2.config(font=('arial',16,'bold'),bd=5,bg="#E5E7E9",justify='right')
opItem2["menu"].config(font=('arial',16,'bold'),bd=5,bg="#E5E7E9")
opItem2.grid(row=3,column=1,sticky="ew")

opItem3=OptionMenu(f1,tkvar3,*values3)
opItem3.config(font=('arial',16,'bold'),bd=5,bg="#E5E7E9",justify='right')
opItem3["menu"].config(font=('arial',16,'bold'),bd=5,bg="#E5E7E9")
opItem3.grid(row=4,column=1,sticky="ew")

opItem4=OptionMenu(f1,tkvar4,*values4)
opItem4.config(font=('arial',16,'bold'),bd=5,bg="#E5E7E9",justify='right')
opItem4["menu"].config(font=('arial',16,'bold'),bd=5,bg="#E5E7E9")
opItem4.grid(row=5,column=1,sticky="ew")

opItem5=OptionMenu(f1,tkvar5,*values5)
opItem5.config(font=('arial',16,'bold'),bd=5,bg="#E5E7E9",justify='right')
opItem5["menu"].config(font=('arial',16,'bold'),bd=5,bg="#E5E7E9")
opItem5.grid(row=6,column=1,sticky="ew")

#======================================================================================Quantity Input=======================================================================================
txtquant1=Entry(f1,font=('arial',16,'bold'),bd=5,bg="#E5E7E9", justify='right')
txtquant1.grid(row=2,column=2,sticky=W)

txtquant2=Entry(f1,font=('arial',16,'bold'),bd=5,bg="#E5E7E9", justify='right')
txtquant2.grid(row=3,column=2,sticky=W)

txtquant3=Entry(f1,font=('arial',16,'bold'),bd=5,bg="#E5E7E9", justify='right')
txtquant3.grid(row=4,column=2,sticky=W)

txtquant4=Entry(f1,font=('arial',16,'bold'),bd=5,bg="#E5E7E9", justify='right')
txtquant4.grid(row=5,column=2,sticky=W)

txtquant5=Entry(f1,font=('arial',16,'bold'),bd=5,bg="#E5E7E9", justify='right')
txtquant5.grid(row=6,column=2,sticky=W)

#=======================================================================================Rate Outputs========================================================================================
txtrate1=Entry(f1,font=('arial',16,'bold'),textvariable=rate1,bd=5,bg="#E5E7E9", justify='right')
txtrate1.grid(row=2,column=3,sticky=W)

txtrate2=Entry(f1,font=('arial',16,'bold'),textvariable=rate2,bd=5,bg="#E5E7E9", justify='right')
txtrate2.grid(row=3,column=3,sticky=W)

txtrate3=Entry(f1,font=('arial',16,'bold'),textvariable=rate3,bd=5,bg="#E5E7E9", justify='right')
txtrate3.grid(row=4,column=3,sticky=W)

txtrate4=Entry(f1,font=('arial',16,'bold'),textvariable=rate4,bd=5,bg="#E5E7E9", justify='right')
txtrate4.grid(row=5,column=3,sticky=W)

txtrate5=Entry(f1,font=('arial',16,'bold'),textvariable=rate5,bd=5,bg="#E5E7E9", justify='right')
txtrate5.grid(row=6,column=3,sticky=W)

#========================================================================================Row Totals=========================================================================================
txttotal1=Entry(f1,font=('arial',16,'bold'),textvariable=total1,bd=5,bg="#E5E7E9", justify='right')
txttotal1.grid(row=2,column=4,sticky=W)

txttotal2=Entry(f1,font=('arial',16,'bold'),textvariable=total2,bd=5,bg="#E5E7E9", justify='right')
txttotal2.grid(row=3,column=4,sticky=W)

txttotal3=Entry(f1,font=('arial',16,'bold'),textvariable=total3,bd=5,bg="#E5E7E9", justify='right')
txttotal3.grid(row=4,column=4,sticky=W)

txttotal4=Entry(f1,font=('arial',16,'bold'),textvariable=total4,bd=5,bg="#E5E7E9", justify='right')
txttotal4.grid(row=5,column=4,sticky=W)

txttotal5=Entry(f1,font=('arial',16,'bold'),textvariable=total5,bd=5,bg="#E5E7E9", justify='right')
txttotal5.grid(row=6,column=4,sticky=W)

#=======================================================================================Final Totals========================================================================================
txtNTotal=Entry(f1,font=('arial',16,'bold'),textvariable=ntotal,bd=5,bg="#E5E7E9", justify='right')
txtNTotal.grid(row=7,column=4,sticky=W)

txtGST=Entry(f1,font=('arial',16,'bold'),textvariable=gst,bd=5,bg="#E5E7E9", justify='right')
txtGST.grid(row=8,column=4,sticky=W)

txtGTotal=Entry(f1,font=('arial',16,'bold'),textvariable=gtotal,bd=5,bg="#E5E7E9", justify='right')
txtGTotal.grid(row=9,column=4,sticky=W)

#=======================================================================================Payment Modes=======================================================================================
rb1=Radiobutton(f1,text="Card",variable=v,value=1,font=('arial',16,'bold'),bd=5,bg='White',justify='right')
rb1.grid(row=2,column=5)

rb2=Radiobutton(f1,text="Cash",variable=v,value=2,font=('arial',16,'bold'),bd=5,bg='White',justify='right')
rb2.grid(row=3,column=5)

rb3=Radiobutton(f1,text="E-Wallet",variable=v,value=3,font=('arial',16,'bold'),bd=5,bg='White',justify='right')
rb3.grid(row=4,column=5)

#==========================================================================================Buttons==========================================================================================
btn1=Button(f1,bd=5,fg="black",font=('arial',16,'bold'),text="Submit",bg="#E5E7E9", justify='right',command=ButtonClick).grid(row=10,column=0)

btn2=Button(f1,bd=5,fg="black",font=('arial',16,'bold'),text="Proceed To Payment",bg="#E5E7E9", justify='right',command=PayClick).grid(row=10,column=1)

btn3=Button(f1,bd=5,fg="black",font=('arial',16,'bold'),text="Print",bg="#E5E7E9", justify='right',command=BillClick).grid(row=10,column=2)

btn4=Button(f1,bd=5,fg="black",font=('arial',16,'bold'),text="New Bill",bg="#E5E7E9", justify='right',command=Clear).grid(row=10,column=3)

#=========================================================================================Database====================================================================================================
def insertdb(A,B,C,D,E):
    conn=sqlite3.connect("Restaurant.db")
    c=conn.cursor()
    c.execute("drop table Menu")
    c.execute("create table Menu(Item varchar(20), Cost varchar(5))")
    c.execute("insert into Menu values('%s','%s')" %('Veg. Clear Soup','40'))
    c.execute("insert into Menu values('%s','%s')" %('Tomato Soup','50'))
    c.execute("insert into Menu values('%s','%s')" %('Veg Manchow Soup','60'))
    c.execute("insert into Menu values('%s','%s')" %('Veg. Hot & Sour Soup','60'))
    c.execute("insert into Menu values('%s','%s')" %('Sweet Corn Soup','60'))
    c.execute("insert into Menu values('%s','%s')" %('Mushroom Soup','65'))
    c.execute("insert into Menu values('%s','%s')" %('Plain Rice','50'))
    c.execute("insert into Menu values('%s','%s')" %('Jeera Rice','60'))
    c.execute("insert into Menu values('%s','%s')" %('Veg Pulav','75'))
    c.execute("insert into Menu values('%s','%s')" %('Veg Biryani','80'))
    c.execute("insert into Menu values('%s','%s')" %('Peas Pulav','75'))
    c.execute("insert into Menu values('%s','%s')" %('Paneer Pulav','90'))
    c.execute("insert into Menu values('%s','%s')" %('Lemon Rice','65'))
    c.execute("insert into Menu values('%s','%s')" %('Plain Dal','50'))
    c.execute("insert into Menu values('%s','%s')" %('Dal Fry','65'))
    c.execute("insert into Menu values('%s','%s')" %('Dal Tadka','75'))
    c.execute("insert into Menu values('%s','%s')" %('Dal Maharani','85'))
    c.execute("insert into Menu values('%s','%s')" %('Dal Makhani','85'))
    c.execute("insert into Menu values('%s','%s')" %('Phulka (Tawa Roti)','06'))
    c.execute("insert into Menu values('%s','%s')" %('Puri','06'))
    c.execute("insert into Menu values('%s','%s')" %('Butter Phulka','09'))
    c.execute("insert into Menu values('%s','%s')" %('Paneer Paratha','50'))
    c.execute("insert into Menu values('%s','%s')" %('Stuff Paratha','40'))
    c.execute("insert into Menu values('%s','%s')" %('Butter Tanduri Roti','15'))
    c.execute("insert into Menu values('%s','%s')" %('Garlic Naan','30'))
    c.execute("insert into Menu values('%s','%s')" %('Lachha Paratha','20'))
    c.execute("insert into Menu values('%s','%s')" %('Masala Kulcha','25'))
    c.execute("insert into Menu values('%s','%s')" %('Makke Ki Roti','25'))
    c.execute("insert into Menu values('%s','%s')" %('Mix Veg','75'))
    c.execute("insert into Menu values('%s','%s')" %('Veg Kadhai','85'))
    c.execute("insert into Menu values('%s','%s')" %('Veg Handi','85'))
    c.execute("insert into Menu values('%s','%s')" %('Veg Kofta','90'))
    c.execute("insert into Menu values('%s','%s')" %('Chana Masala','80'))
    c.execute("insert into Menu values('%s','%s')" %('Aalu Jeera','65'))
    c.execute("insert into Menu values('%s','%s')" %('Dum Aalu','70'))
    c.execute("insert into Menu values('%s','%s')" %('Aalu Gobhi Masala','85'))
    c.execute("insert into Menu values('%s','%s')" %('Paneer Butter Masala','115'))
    c.execute("insert into Menu values('%s','%s')" %('Paneer Kofta','120'))
    c.execute("insert into Menu values('%s','%s')" %('Paneer Bhurji','110'))
    c.execute("insert into Menu values('%s','%s')" %('Palak Paneer','115'))
    c.execute("insert into Menu values('%s','%s')" %('Mutter Paneer','110'))
    c.execute("insert into Menu values('%s','%s')" %('Shahi Paneer','115'))
    c.execute("insert into Menu values('%s','%s')" %('Sarso Ka Saag','95'))
    c.execute("insert into Menu values('%s','%s')" %('Bundi Raita','50'))
    c.execute("insert into Menu values('%s','%s')" %('Mix Veg. Raita','60'))
    c.execute("insert into Menu values('%s','%s')" %('Onion Salad','25'))
    c.execute("insert into Menu values('%s','%s')" %('Green Salad','35'))
    c.execute("insert into Menu values('%s','%s')" %('Banana Milkshake','60'))
    c.execute("insert into Menu values('%s','%s')" %('Chocolate Milkshake','70'))
    c.execute("insert into Menu values('%s','%s')" %('Kiwi Milkshake','80'))
    c.execute("insert into Menu values('%s','%s')" %('Strawberry Milkshake','70'))
    c.execute("insert into Menu values('%s','%s')" %('Blackcurrant Milkshake','70'))
    c.execute("insert into Menu values('%s','%s')" %('Mix Fruit Milkshake','70'))
    c.execute("insert into Menu values('%s','%s')" %('Mango Milkshake','70'))
    c.execute("insert into Menu values('%s','%s')" %('Blue Lagoon','80'))
    c.execute("insert into Menu values('%s','%s')" %('Ginger & Mint','90'))
    c.execute("insert into Menu values('%s','%s')" %('Fruit Punch','90'))
    c.execute("insert into Menu values('%s','%s')" %('Lemon & Blackcurrant','80'))
    c.execute("insert into Menu values('%s','%s')" %('Double Scoop(Choco,Vanilla)','65'))
    c.execute("insert into Menu values('%s','%s')" %('Choco Blast Icecream','80'))
    c.execute("insert into Menu values('%s','%s')" %('Kasata','70'))
    c.execute("insert into Menu values('%s','%s')" %('Malai Kulfi(Pista)','40'))
    c.execute("insert into Menu values('%s','%s')" %('Gulab Jamoon','40'))
    c.execute("insert into Menu values('%s','%s')" %('Rasagulla','40'))
    conn.commit()
    
    c1=c.execute("select * from Menu where Item=?",(A,))   
    for row in c1:
        r1=row[1] 

    c2=c.execute("select * from Menu where Item=?",(B,))
    for row in c2:
        r2=row[1]

    c3=c.execute("select * from Menu where Item=?",(C,))    
    for row in c3:
        r3=row[1]    

    c4=c.execute("select * from Menu where Item=?",(D,))    
    for row in c1:
        r4=row[1]    

    c5=c.execute("select * from Menu where Item=?",(E,))    
    for row in c1:
        r5=row[1]
    
        
    #Calculation Function call
    CalcTotal(r1,r2,r3,r4,r5)

root.mainloop()
