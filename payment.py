from hashlib import new
from tkinter import *
import sqlite3
from click import confirm
from tkcalendar import Calendar
root = Tk()
root.title("Payment gateway")

# Creating a frame to place widgets in it
myframe = Frame(root)
root.configure(bg='#DFF6FF')
# myfame = configure(bgcolor="#DFF6FF")

#Creating a font tuple
fontTuple = ("Montserrat",10, 'bold') 

# nearest location
mylabel2 = Label(myframe, text="Enter the nearest theatre:", font=fontTuple)
mylabel2.grid(row=1, column=13, padx=25, pady=25)

# declaring the variable clicked
clicked = StringVar()

# Creating a list
theatre =[ 
    "Carnival Cinema", 
    "Maxus Cinema", 
    "INOX",
    "The Forum Vijaya Mall",
    "Satyam Cinemas",
    "Raj Mandir Cinema",
    "Luxe Cinema",
    "Palazzo",
    "Urvashi Cinema"
]
clicked.set(theatre[0])

# Creating Drop Down OptionMenu
drop = OptionMenu(myframe,clicked,*theatre)
drop.config(font=fontTuple)
drop.grid(row=1, column=14, padx=25, pady=25)

# asking the preferred language
mylabel3 = Label(myframe, text="Preferred Language:",font=fontTuple)
mylabel3.grid(row=2, column=13,padx=25, pady=25)

# creating a list of langauges 
langauges = [
    "Hindi",
    "English",
    "Tamil",
    "Marathi",
    "Kannada",
]

# declaring the variable clicked
clicked1 = StringVar()
#  setting a default value for the drop down list
clicked1.set(langauges[0])

# Creating Drop Down OptionMenu
drop = OptionMenu(myframe, clicked1, *langauges)
drop.config(font=fontTuple)
drop.grid(row=2, column=14, padx=25, pady=25)

# asking the date
mylabel4 = Label(myframe, text="Select Date:",padx=25, pady=25,font=fontTuple)
mylabel4.grid(row=3, column=13, padx=25, pady=25)

# Creating a calendar optionMenu
cal = Calendar(myframe, selectmode='day', year=2022,month=2, day=23)
cal.grid(row=3, column=14, padx=25, pady=25)

# creating Radio button
r = IntVar()
Radiobutton(myframe, text="Card", variable=r, value=1,font=fontTuple).grid(row=5, column=13, padx=25, pady=25)
Radiobutton(myframe, text="Goggle Pay", variable=r, value=2,font=fontTuple).grid(row=5, column=14, padx=25, pady=25)

# Creating a function for a selected payment mode 
def pay(value):
    if value==1:
        newwindow = Toplevel(myframe)
        newwindow.configure(bg='#DFF6FF')
        myframe2 = Frame(newwindow)
        mylabel5 = Label(myframe2, text="Card holder name:", font=fontTuple)
        mylabel5.grid(row=0,column=13,padx=25, pady=25)
        myentry = Entry(myframe2, font= fontTuple)
        myentry.grid(row = 0, column = 14,padx=25, pady=25)
        mylabel6 = Label(myframe2, text="Card Number:", font=fontTuple)
        mylabel6.grid(row=1, column=13, padx=25, pady=25)
        myentry2 = Entry(myframe2, font=fontTuple)
        myentry2.grid(row=1, column=14, padx=25, pady=25)
        mylabel6 = Label(myframe2, text="Expiry date:", font=fontTuple)
        mylabel6.grid(row=2,column=13,padx=25, pady=25)
        myentry3 = Entry(myframe2, font= fontTuple)
        myentry3.insert(0,"mm/yy")
        myentry3.grid(row = 2, column = 14,padx=25, pady=25)
        mylabel7 = Label(myframe2, text="Enter the CVV:", font=fontTuple)
        mylabel7.grid(row=3, column=13, padx=25, pady=25)
        myentry = Entry(myframe2, font=fontTuple, show="*")
        myentry.grid(row=3, column=14, padx=25, pady=25)
        def confirmation():
            fontTuple2 = ("Montserrat", 20, 'bold')
            newwindow2 = Toplevel(myframe2)
            myframe3 = Frame(newwindow2)
            mylabel8 = Label(myframe3,text="Thankyou! Payment Successful🤩", font=fontTuple2 )
            mylabel8.grid(row = 0, column=0, padx=25, pady=25)
            mylabel9 = Label(myframe3,text="Please close all the windows!", font= fontTuple)
            mylabel9.grid(row=1, column=0, padx=25,pady=25)
            myframe3.pack(padx=50, pady=50)
            newwindow2.pack()
        mybutton4 = Button(myframe2,text="Pay",font=fontTuple, command= confirmation)
        mybutton4.grid(row=4, column=13, padx=25, pady=25)
        mybutton5 = Button(myframe2,text="Back",font=fontTuple, command=newwindow.destroy )
        mybutton5.grid(row=4, column=14, padx=25, pady=25)
        myframe2.pack(padx=50, pady=50)
        newwindow.pack()
    elif value == 2:
        newwindow2 = Toplevel(myframe)
        newwindow2.configure(bg='#DFF6FF')
        myframe3 = Frame(newwindow2)
        mylabel10 = Label(myframe3,text="Enter your Mobile number: ", font=fontTuple)
        mylabel10.grid(row=0,column=13,padx=25, pady=25)
        myentry4 = Entry(myframe3, font=fontTuple)
        myentry4.grid(row=0, column=14, padx=25, pady=25)
        mylabel11 = Label(myframe3,text="Enter your UPI ID: ", font=fontTuple)
        mylabel11.grid(row=1,column=13,padx=25, pady=25)
        myentry5 = Entry(myframe3, font=fontTuple)
        myentry5.grid(row=1, column=14, padx=25,pady=25)
        def confirmPayment():
            openwindow = Toplevel(newwindow2)
            openwindow.config(bg="#DFF6FF")
            newframe = Frame(openwindow)
            fontTuple3 = ("Montserrat", 20, 'bold')
            newlabel = Label(newframe, text="Thankyou! Payment Successful🤩", font= fontTuple3)
            newlabel.grid(row=0,column=1,padx=25,pady=25)
            newlabel1 = Label(newframe, text="Please close all the windows!", font=fontTuple)
            newlabel1.grid(row=1,column=1,padx=25,pady=25)
            newframe.pack(padx=50,pady=50)
            openwindow.pack()

        buttonpay = Button(myframe3, text="Pay", command= confirmPayment, font=fontTuple)
        buttonpay.grid(row=2,column=13)
        buttonback = Button(myframe3,text="Back",font=fontTuple, command=newwindow2.destroy )
        buttonback.grid(row=2, column=14, padx=25, pady=25)
        myframe3.pack(padx=50,pady=50)
        newwindow2.pack()
# Creating a button Pay
mybutton1 = Button(myframe, text="Pay", command=lambda:pay(r.get()), font=fontTuple)
mybutton1.grid(row=7, column=13, padx=25, pady=25)
myframe.pack(padx=50,pady=50)
root.mainloop()