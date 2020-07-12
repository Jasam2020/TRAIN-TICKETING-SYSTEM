from tkinter import *
from tkinter import Tk, StringVar, ttk, messagebox
import random
import time;
import datetime

root = Tk()
root.geometry("1350x750+0+0")
root.title("Train Ticket")
root.configure(background="black")

Tops = Frame(root, width=3550, height=100, bd=14, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=650, bd=8, relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root, width=440, height=650, bd=8, relief="raise")
f2.pack(side=RIGHT)

frametopRight = Frame(f2, width=440, height=650, bd=12, relief="raise")
frametopRight.pack(side=TOP)
frameBottomRight = Frame(f2, width=440, height=50, bd=16, relief="raise")
frameBottomRight.pack(side=BOTTOM)

f1a = Frame(f1, width=900, height=330, bd=8, relief="raise")
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=320, bd=8, relief="raise")
f2a.pack(side=BOTTOM)

topLeft1 = Frame(f1a, width=300, height=200, bd=16, relief="raise")
topLeft1.pack(side=LEFT)
topLeft2 = Frame(f1a, width=300, height=200, bd=16, relief="raise")
topLeft2.pack(side=RIGHT)
topLeft3 = Frame(f1a, width=300, height=200, bd=16, relief="raise")
topLeft3.pack(side=RIGHT)

# -------------------------------------------------------------------------------------

bottomLeft1 = Frame(f2a, width='450', height='450', bd='14', relief="raise")
bottomLeft1.pack(side=LEFT)

bottomLeft2 = Frame(f2a, width='450', height='450', bd='14', relief="raise")
bottomLeft2.pack(side=RIGHT)

# --------------------------------------------------------------------------------------

Tops.configure(background="black")
f1.configure(background="black")
f2.configure(background="black")
lblTitle = Label(Tops, font=('arial', 40, 'bold'), text="Train Ticketing Systems", bd=10, width=41, justify='center')
lblTitle.grid(row=0, column=0)

Date1 = StringVar()
time1 = StringVar()
Ticketclass = StringVar()
TicketPrice = StringVar()
Child_Ticket = StringVar()
Adult_Ticket = StringVar()
From_Destination = StringVar()
To_Destination = StringVar()
Fee_Price = StringVar()
Route = StringVar()
Receipt_Ref = StringVar()

Ticketclass.set("")
TicketPrice.set("")
Child_Ticket.set("")
Adult_Ticket.set("")
From_Destination.set("")
To_Destination.set("")
Fee_Price.set("")
Route.set("")
Receipt_Ref.set("")

# -------------------------------------------Receipt----------------------------------------

lblReceipt = Label(frametopRight, font=('arial', 18, 'bold'), text="Ticketing", bd=10, width=25,
                   justify='center')
lblReceipt.grid(row=0, column=0)

lblClass1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text="Class", width=8, relief='sunken',
                  justify='center')
lblClass1.grid(row=0, column=0)

lblClass2 = Label(frameBottomRight, font=('arial', 14, 'bold'), width=8, relief='sunken', textvariable=Ticketclass,
                  justify='center')
lblClass2.grid(row=1, column=0)

lblTicket1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text="Ticket", width=8, relief='sunken',
                   justify='center')
lblTicket1.grid(row=0, column=1)

lblTicket2 = Label(frameBottomRight, font=('arial', 14, 'bold'), width=8, relief='sunken', textvariable=TicketPrice,
                   justify='center')
lblTicket2.grid(row=1, column=1)

lblAdult1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text="Adult", width=8, relief='sunken',
                  justify='center')
lblAdult1.grid(row=0, column=2)

lblAdult2 = Label(frameBottomRight, font=('arial', 14, 'bold'), width=8, relief='sunken', textvariable=Adult_Ticket,
                  justify='center')
lblAdult2.grid(row=1, column=2)

lblChild1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text="Child", width=8, relief='sunken',
                  justify='center')
lblChild1.grid(row=0, column=3)

lblChild2 = Label(frameBottomRight, font=('arial', 14, 'bold'), width=8, relief='sunken', textvariable=Child_Ticket,
                  justify='center')
lblChild2.grid(row=1, column=3)
# ---------------------------------------SPACE-------------
lblsp = Label(frameBottomRight, font=('arial', 14, 'bold'), width=34, height=2, relief='sunken',
              justify='center')
lblsp.grid(row=2, column=0, columnspan=4)

# ---------------------------------------------------
lblFrom1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text="From", width=8, relief='sunken',
                 justify='center')
lblFrom1.grid(row=3, column=1)
lblFrom2 = Label(frameBottomRight, font=('arial', 14, 'bold'), width=8, relief='sunken', textvariable=From_Destination,
                 justify='center')
lblFrom2.grid(row=3, column=2)
# ---------------------------------------------------
lblTo1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text="To", width=8, relief='sunken',
               justify='center')
lblTo1.grid(row=4, column=1)
lblTo2 = Label(frameBottomRight, font=('arial', 14, 'bold'), width=8, relief='sunken', textvariable=To_Destination,
               justify='center')
lblTo2.grid(row=4, column=2)
# ------------------------------------------------------------------
lblPrice1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text="Price", width=8, relief='sunken',
                  justify='center')
lblPrice1.grid(row=5, column=1)
lblPrice2 = Label(frameBottomRight, font=('arial', 14, 'bold'), width=8, relief='sunken', textvariable=Fee_Price,
                  justify='center')
lblPrice2.grid(row=5, column=2)
# -----------------------------------SPACE-------------------------------
lblsp = Label(frameBottomRight, font=('arial', 4, 'bold'), width=34, height=2, relief='sunken',
              justify='center')
lblsp.grid(row=6, column=0, columnspan=4)
# ------------------------------------------------------------------
lblRefNo1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text="Ref No", width=8, relief='sunken',
                  justify='center')
lblRefNo1.grid(row=7, column=0)

lblRefNo2 = Label(frameBottomRight, font=('arial', 14, 'bold'), width=8, relief='sunken', textvariable=Receipt_Ref,
                  justify='center')
lblRefNo2.grid(row=8, column=0)
# ---------------------------------------------------------------
lblTime1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text="Time", width=8, relief='sunken',
                 justify='center')
lblTime1.grid(row=7, column=1)

lblTime2 = Label(frameBottomRight, font=('arial', 14, 'bold'), width=8, relief='sunken', textvariable=time1,
                 justify='center')
lblTime2.grid(row=8, column=1)

lblDate1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text="Date", width=8, relief='sunken',
                 justify='center')
lblDate1.grid(row=7, column=2)

lblDate2 = Label(frameBottomRight, font=('arial', 14, 'bold'), width=8, relief='sunken', textvariable=Date1,
                 justify='center')
lblDate2.grid(row=8, column=2)

lblRoute1 = Label(frameBottomRight, font=('arial', 14, 'bold'), text="Route", width=8, relief='sunken',
                  justify='center')
lblRoute1.grid(row=7, column=3)

lblRoute2 = Label(frameBottomRight, font=('arial', 14, 'bold'), width=8, relief='sunken', textvariable=Route,
                  justify='center')
lblRoute2.grid(row=8, column=3)


# --------------------------------------Function---------------------------------------------

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


def iExit():
    qExit = messagebox.askyesno("Quit System", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return


def Travel_Cost():
    if (var9.get() == "Kampi" and var1.get() == 1 and var4.get() == 1):
        Tcost: float = float(30.8)
        Single = float(var12.get())
        Adult_Tax = "€", str('%.2f' % ((Tcost * Single) * 0.03))
        Adult_Fees = "€", str('%.2f' % (Tcost * Single))
        TotalCost = "€", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.03)))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        Ticketclass.set("Standard")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Espoo")
        To_Destination.set("Kampi")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109, 5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL" + randomRef)

    elif (var9.get() == "Kampi" and var1.get() == 1 and var5.get() == 1):
        Tcost = float(23.8)
        Single = float(var12.get())
        Child_Tax = "€", str('%.2f' % (Tcost * 0))
        Child_Fees = "€", str('%.2f' % (Tcost * Single))
        TotalCost = "€", str('%.2f' % ((Tcost * Single) + (Tcost * 0)))
        Tax.set(Child_Tax)
        SubTotal.set(Child_Fees)
        Ticketclass.set("Standard")
        TicketPrice.set(Child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("Espoo")
        To_Destination.set("Kampi")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        x = random.randint(109, 5876)
        randomRef = str(x)
        Receipt_Ref.set("TFL" + randomRef)


def chkbutton_value():
    if (var10.get() == 1):
        var12.set("")
        entSingle.configure(state=NORMAL)
    elif var10.get() == 0:
        entSingle.configure(state=DISABLED)
        var12.set("0")
    if (var11.get() == 1):
        var6.set("")
        entReturn.configure(state=NORMAL)
    elif var11.get == 0:
        entReturn.configure(state=DISABLED)
        var6.set("0")


def Reset():
    Tax.set("0")
    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    SubTotal.set("0")
    Total.set("0")
    TicketClass.set("")
    TicketPrice.set("")
    Child_Ticket.set("")
    Adult_Ticket.set("")
    From_Destination.set("")
    To_Destination.set("")
    Fee_Price.set("")


# -------------------------------------Variables---------------------------------------------
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = StringVar()
var7 = StringVar()
var8 = StringVar()
var9 = StringVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
Tax = StringVar()

var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0")
var7.set("0")
var8.set("0")
var9.set("0")
var10.set("0")
var11.set("0")
var12.set("0")

SubTotal = StringVar()
Total = StringVar()
text_Input = StringVar()
operator = ""
# ----------------------------WIDGET TOPLEFT1--------------------------------------------
Date1.set(time.strftime("%d/%m/%Y"))
time1.set(time.strftime('%H:%M:%S'))

# ----------------------------WIDGET TOPLEFT1--------------------------------------------
lblClass = Label(topLeft1, font=('arial', 22, 'bold'), text='Class', bd=8)
lblClass.grid(row=0, column=0, sticky=W)
chkStandard = Checkbutton(topLeft1, font=('arial', 20, 'bold'), text='Standard', variable=var1, onvalue=1, offvalue=0)
chkStandard.grid(row=1, column=0, sticky=W)
chkEconomy = Checkbutton(topLeft1, font=('arial', 20, 'bold'), text='Economy', variable=var2, onvalue=1, offvalue=0)
chkEconomy.grid(row=2, column=0, sticky=W)
chkFirstClass = Checkbutton(topLeft1, font=('arial', 20, 'bold'), text='First Class', variable=var3, onvalue=1,
                            offvalue=0)
chkFirstClass.grid(row=3, column=0, sticky=W)
# ----------------------------WIDGET TOPLEFT2--------------------------------------------
lblSelect = Label(topLeft3, font=('arial', 22, 'bold'), text='Select Destination', bd=8)
lblSelect.grid(row=0, column=0, sticky=W, columnspan=2)
lblDestination = Label(topLeft3, font=('arial', 20, 'bold'), text='Destination', bd=2)
lblDestination.grid(row=1, column=0, sticky=W)

cboDestination = ttk.Combobox(topLeft3, textvariable=var9, state='readonly', font=('arial', 20, 'bold'), width=8)
cboDestination['value'] = ('', 'Kampi', 'Tampere', 'Espoo', 'kirkinomi', 'Vantaa')
cboDestination.current(0)
cboDestination.grid(row=1, column=1)

chkAdult = Checkbutton(topLeft3, font=('arial', 20, 'bold'), text='Adult', variable=var4, onvalue=1, offvalue=0)
chkAdult.grid(row=2, column=0, sticky=W)
chkChild = Checkbutton(topLeft3, font=('arial', 20, 'bold'), text='Child', variable=var5, onvalue=1, offvalue=0)
chkChild.grid(row=3, column=0, sticky=W)

# --------------------------------------Ticket--------------------------------------------------

lblClass = Label(topLeft2, font=('arial', 22, 'bold'), text='Ticket Type', bd=8)
lblClass.grid(row=0, column=0, sticky=W)
chkSingle = Checkbutton(topLeft2, font=('arial', 20, 'bold'), text='Single', variable=var10,
                        onvalue=1, offvalue=0, command=chkbutton_value)
chkSingle.grid(row=1, column=0, sticky=W)
entSingle = Entry(topLeft2, font=('arial', 20, 'bold'), textvariable=var12, bd=2, width=8, state=DISABLED)
entSingle.grid(row=1, column=1, sticky=W)
chkReturn = Checkbutton(topLeft2, font=('arial', 20, 'bold'), text='Return', variable=var11,
                        onvalue=1, offvalue=0, command=chkbutton_value)
chkReturn.grid(row=2, column=0, sticky=W)
entReturn = Entry(topLeft2, font=('arial', 20, 'bold'), textvariable=var6, bd=2, width=8, state=DISABLED)
entReturn.grid(row=2, column=1, sticky=W)

lblComment = Label(topLeft2, font=('arial', 22, 'bold'), text='Comment', bd=8)
lblComment.grid(row=3, column=0, sticky=W)
entComment = Entry(topLeft2, font=('arial', 20, 'bold'), textvariable=var7, bd=2, width=8)
entComment.grid(row=3, column=1, sticky=W)

# -----------------------------------Calculator-----------------------------------------------------

text_Input = StringVar()
txtDisplay = Entry(bottomLeft2, font=('arial', 10, 'bold'), textvariable=text_Input, bd=16,
                   justify='right', width=36)
txtDisplay.grid(columnspan=4)

btn7 = Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'),
              text="7", command=lambda: btnClick(7), width=4).grid(row=2, column=0)

# noinspection PyUnresolvedReferences
btn8 = Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'),
              text="8", command=lambda: btnClick(8), width=4).grid(row=2, column=1)

# noinspection PyUnresolvedReferences
btn9 = Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'),
              text="9", command=lambda: btnClick(9), width=4).grid(row=2, column=2)

# noinspection PyUnresolvedReferences
Addition = Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'),
                  text="+", command=lambda: btnClick("+"), width=4).grid(row=2, column=3)

# ----------------------------------------------------------------------------------------------------------
# noinspection PyUnresolvedReferences
btn4 = Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'),
              text="4", command=lambda: btnClick(4), width=4).grid(row=3, column=0)

# noinspection PyUnresolvedReferences
btn5 = Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'),
              text="5", command=lambda: btnClick(5), width=4).grid(row=3, column=1)

# noinspection PyUnresolvedReferences
btn6 = Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'),
              text="6", command=lambda: btnClick(6), width=4).grid(row=3, column=2)

# noinspection PyUnresolvedReferences
Subtraction = Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'),
                     text="-", command=lambda: btnClick("-"), width=4).grid(row=3, column=3)

# ----------------------------------------------------------------------------------------------------------
# noinspection PyUnresolvedReferences
btn1 = Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'),
              text="1", command=lambda: btnClick(1), width=4).grid(row=4, column=0)

# noinspection PyUnresolvedReferences
btn2 = Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'),
              text="2", command=lambda: btnClick(2), width=4).grid(row=4, column=1)

# noinspection PyUnresolvedReferences
btn3 = Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'),
              text="3", command=lambda: btnClick(3), width=4).grid(row=4, column=2)

# noinspection PyUnresolvedReferences
Multiply = Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'),
                  text="*", command=lambda: btnClick("*"), width=4).grid(row=4, column=3)
# ----------------------------------------------------------------------------------------------------------
# noinspection PyUnresolvedReferences
btn0 = Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'),
              text="0", command=lambda: btnClick(0), width=4).grid(row=5, column=0)

# noinspection PyUnresolvedReferences
btnClear = Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'),
                  text="C", width=4, command=btnClearDisplay).grid(row=5, column=1)

# noinspection PyUnresolvedReferences
btnEquals = Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'),
                   text="=", width=4, command=btnEqualsInput).grid(row=5, column=2)

# noinspection PyUnresolvedReferences
Division = Button(bottomLeft2, padx=8, pady=8, bd=8, fg="black", font=('arial', 10, 'bold'),
                  text="/", command=lambda: btnClick("/"), width=4).grid(row=5, column=3)

# ----------------------------------------Tax----------------------------------------------------
lblStateTax = Label(bottomLeft1, font=('arial', 24, 'bold'), text="State Tax", bd=16, anchor='w')
lblStateTax.grid(row=3, column=2)

txtStateTax = Entry(bottomLeft1, font=('arial', 16, 'bold'), textvariable=Tax, bd=10, width=28,
                    bg='#ffffff', justify='right')
txtStateTax.grid(row=3, column=3)

lblSubTotal = Label(bottomLeft1, font=('arial', 24, 'bold'), text="Sub Total", bd=16, anchor='w')
lblSubTotal.grid(row=4, column=2)
txtSubTotal = Entry(bottomLeft1, font=('arial', 16, 'bold'), textvariable=SubTotal, bd=10, width=28,
                    bg='#ffffff', justify='right')
txtSubTotal.grid(row=4, column=3)

lblTotalCost = Label(bottomLeft1, font=('arial', 24, 'bold'), text='Total Cost', bd=16, anchor='w')
lblTotalCost.grid(row=5, column=2)
txtTotalCost = Entry(bottomLeft1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, width=28,
                     bg='#ffffff', justify='right')
txtTotalCost.grid(row=5, column=3)

# ------------------------------------------------------------------------------------------------------------
lblsp = Label(bottomLeft1, font=('arial', 4, 'bold'), width=44, height=2, relief='sunken',
              justify='center')
lblsp.grid(row=6, column=0, columnspan=4)
# -----------------------------------------------
lblSpace = Label(bottomLeft1, font=('arial', 24, 'bold'), text="      \n      ", bd=16, anchor='w')
lblSpace.grid(row=6, column=2)
# ------------------------------------------------------------------------------------------------------------
lblSpace = Label(bottomLeft2, font=('arial', 24, 'bold'), text="      \n      ", bd=16, anchor='w')
lblSpace.grid(row=6, columnspan=4)

# --------------------------------SPACE-------------------------
lblsp = Label(frameBottomRight, font=('arial', 14, 'bold'), width=34, height=1, relief='sunken',
              justify='center')
lblsp.grid(row=9, column=0, columnspan=4)

# ------------------------------------------------------------------------------------------------------------

btnTotal = Button(frameBottomRight, text='Total', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 12, 'bold'), width=6, height=1, command=Travel_Cost).grid(row=10, column=0)

btnClear = Button(frameBottomRight, text='Clear', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 12, 'bold'), width=6, height=1, command=Reset).grid(row=10, column=1)

btnReset = Button(frameBottomRight, text='Reset', padx=2, pady=2, bd=2, fg="black",
                  font=('arial', 12, 'bold'), width=6, height=1, command=Reset).grid(row=10, column=2)

btnExit = Button(frameBottomRight, text='Exit', padx=2, pady=2, bd=2, fg="black",
                 font=('arial', 12, 'bold'), width=6, height=1, command=iExit).grid(row=10, column=3)
# ------------------------------------------------------------------------------------------
lblsp = Label(frameBottomRight, font=('arial', 14, 'bold'), width=14, height=2, relief='sunken',
              justify='center')
lblsp.grid(row=11, column=0, columnspan=4)

mainloop()
