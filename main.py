from tkinter import *
from tkinter import messagebox
import random, os,tempfile,smtplib


#functionality part

def clear():
    bathsoapEntry.delete(0, END)
    facecreamEntry.delete(0, END)
    hairgelEntry.delete(0, END)
    hairsprayEntry.delete(0, END)
    bodylotionEntry.delete(0, END)
    facewashEntry.delete(0, END)

    daalEntry.delete(0, END)
    wheatEntry.delete(0, END)
    riceEntry.delete(0, END)
    oilEntry.delete(0, END)
    sugarEntry.delete(0, END)
    teaEntry.delete(0, END)

    pepsiEntry.delete(0, END)
    cocacolaEntry.delete(0, END)
    maazaEntry.delete(0, END)
    bovontoEntry.delete(0, END)
    spriteEntry.delete(0, END)
    frootiEntry.delete(0, END)

    bathsoapEntry.insert(0,0)
    facecreamEntry.insert(0,0)
    hairgelEntry.insert(0,0)
    hairsprayEntry.insert(0,0)
    bodylotionEntry.insert(0,0)
    facewashEntry.insert(0,0)

    daalEntry.insert(0,0)
    wheatEntry.insert(0,0)
    riceEntry.insert(0,0)
    oilEntry.insert(0,0)
    sugarEntry.insert(0,0)
    teaEntry.insert(0,0)

    pepsiEntry.insert(0,0)
    cocacolaEntry.insert(0,0)
    maazaEntry.insert(0,0)
    bovontoEntry.insert(0,0)
    spriteEntry.insert(0,0)
    frootiEntry.insert(0,0)

    cosmetictaxEntry.delete(0,END)
    grocerytaxEntry.delete(0,END)
    DrinkstaxEntry.delete(0,END)

    cosmeticpriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    DrinkspriceEntry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)

    textarea.delete(1.0,END)

def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderEntry.get(),passwordEntry.get())
            message=email_textarea.get(1.0,END)
            ob.sendmail(senderEntry.get(),recieverEntry.get(),message)
            ob.quit()
            messagebox.showinfo('success','bill is successfully sent',parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('error','something  went  wrong,please try again',parent=root1)
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('error','bill is empty')
    else:
        root1=Tk()
        root1.grab_set()    #its help not to perform the main window just close the window then only you can perform that
        root1.title('send gmail')
        root1.config(bg='gray20')
        root1.resizable(False,False)

        senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),
                               bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        senderLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bg='gray20',fg='white')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)

        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        passwordLabel = Label(senderFrame, text="password", font=('arial', 14, 'bold'), bg='gray20', fg='white')
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry = Entry(senderFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE,show='*')
        passwordEntry.grid(row=1, column=1, padx=10, pady=8)

        recipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'),
                                 bd=6, bg='gray20', fg='white')
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        recieverLabel = Label(recipientFrame, text="Email Address", font=('arial', 14, 'bold'), bg='gray20', fg='white')
        recieverLabel.grid(row=0, column=0, padx=10, pady=8)

        recieverEntry = Entry(recipientFrame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        recieverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(recipientFrame, text="Message", font=('arial', 14, 'bold'), bg='gray20', fg='white')
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea=Text(recipientFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,
                            width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','')
                              .replace('-','').replace('\t\t\t','\t\t'))

        sendButton=Button(root1,text='SEND',font=('arial',16,'bold'),width=15,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=20)

        root1.mainloop()

def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('error','bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')
def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billnumberEntry.get():
            f = open(f'bills/{i}', 'r')
            textarea.delete(1.0, END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
        else:
            messagebox.showerror('error', 'invalid bill number')


if not os.path.exists('bills'):
    os.mkdir('bills')


def save_bill():
    global billnumber
    result = messagebox.askyesno('confirm', 'do you want to save the bill?')
    if result:
        bill_content = textarea.get(1.0, END)
        file = open(f'bills/{billnumber}.txt', 'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('success', '{billnumber} is saved successfully')
        billnumber = random.randint(500, 1000)


billnumber = random.randint(500, 1000)


def bill_area():
    if nameEntry.get() == '' or phoneEntry.get() == '':
        messagebox.showerror("error", 'customer details are Required')
    elif cosmeticpriceEntry.get() == '' and grocerypriceEntry.get() == '' and DrinkspriceEntry.get() == '':
        messagebox.showerror('error', 'no products are selected')
    elif cosmeticpriceEntry.get() == '0 Rs' and grocerypriceEntry.get() == '0 Rs' and DrinkspriceEntry.get() == '0 Rs':
        messagebox.showerror('error', 'no products are selected')
    else:
        textarea.delete(1.0, END)

        textarea.insert(END, '\t\t**welcome**\n\n')
        textarea.insert(END, f'Bill Number: {billnumber}\n')
        textarea.insert(END, f'Customer Name: {nameEntry.get()}\n')
        textarea.insert(END, f'Customer Phone Number: {phoneEntry.get()}')
        textarea.insert(END, '\n=======================================================')
        textarea.insert(END, '\nProduct\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END, '\n=======================================================')

        if bathsoapEntry.get() != '0':
            textarea.insert(END, f'\nBath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs')
        if facecreamEntry.get() != '0':
            textarea.insert(END, f'\nFace Cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs')
        if facewashEntry.get() != '0':
            textarea.insert(END, f'\nFace Wash\t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs')
        if hairsprayEntry.get() != '0':
            textarea.insert(END, f'\nHair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs')
        if hairgelEntry.get() != '0':
            textarea.insert(END, f'\nHair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs')
        if bodylotionEntry.get() != '0':
            textarea.insert(END, f'\nBody Lotion\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Rs')

        if riceEntry.get() != '0':
            textarea.insert(END, f'\nRice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs')
        if oilEntry.get() != '0':
            textarea.insert(END, f'\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs')
        if daalEntry.get() != '0':
            textarea.insert(END, f'\nDaal\t\t\t{daalEntry.get()}\t\t\t{daalprice} Rs')
        if wheatEntry.get() != '0':
            textarea.insert(END, f'\nWheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rs')
        if sugarEntry.get() != '0':
            textarea.insert(END, f'\nSugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Rs')
        if teaEntry.get() != '0':
            textarea.insert(END, f'\nTea\t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs')

        if maazaEntry.get() != '0':
            textarea.insert(END, f'\nMaaza\t\t\t{maazaEntry.get()}\t\t\t{maazaprice} Rs')
        if pepsiEntry.get() != '0':
            textarea.insert(END, f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Rs')
        if spriteEntry.get() != '0':
            textarea.insert(END, f'\nSprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice} Rs')
        if bovontoEntry.get() != '0':
            textarea.insert(END, f'\nBovonto\t\t\t{bovontoEntry.get()}\t\t\t{bovontoprice} Rs')
        if frootiEntry.get() != '0':
            textarea.insert(END, f'\nFrooti\t\t\t{frootiEntry.get()}\t\t\t{frootiprice} Rs')
        if cocacolaEntry.get() != '0':
            textarea.insert(END, f'\nCoca Cola\t\t\t{cocacolaEntry.get()}\t\t\t{cocacolaprice} Rs')

        textarea.insert(END, '\n=======================================================')

        if cosmetictaxEntry.get() != '0.0 Rs':
            textarea.insert(END, f'\nCosmetic Tax\t\t{cosmetictaxEntry.get()}')
        if grocerytaxEntry.get() != '0.0 Rs':
            textarea.insert(END, f'\nGrocery Tax\t\t{grocerytaxEntry.get()}')
        if DrinkstaxEntry.get() != '0.0 Rs':
            textarea.insert(END, f'\nDrinks Tax\t\t{DrinkstaxEntry.get()}')

        textarea.insert(END, f'\n\n\t\tTotal Bill \t\t {totalbill}')

        textarea.insert(END, '\n=======================================================')

        save_bill()


def total():
    global soapprice, facecreamprice, facewashprice, hairgelprice, hairsprayprice, bodylotionprice
    global riceprice, daalprice, wheatprice, oilprice, sugarprice, teaprice
    global maazaprice, pepsiprice, spriteprice, bovontoprice, frootiprice, cocacolaprice
    global totalbill
    #cosmetics price calculation
    soapprice = int(bathsoapEntry.get()) * 20
    facecreamprice = int(facecreamEntry.get()) * 50
    facewashprice = int(facewashEntry.get()) * 100
    hairsprayprice = int(hairsprayEntry.get()) * 150
    hairgelprice = int(hairgelEntry.get()) * 80
    bodylotionprice = int(bodylotionEntry.get()) * 60

    totalcosmeticprice = soapprice + facewashprice + facecreamprice + hairsprayprice + hairgelprice + bodylotionprice
    cosmeticpriceEntry.delete(0, END)
    cosmeticpriceEntry.insert(0, str(totalcosmeticprice) + ' Rs')

    #cosmetic tax
    cosmetictax = totalcosmeticprice * 0.12
    cosmetictaxEntry.delete(0, END)
    cosmetictaxEntry.insert(0, str(cosmetictax) + ' Rs')

    #grocery price calculation
    riceprice = int(riceEntry.get()) * 30
    daalprice = int(daalEntry.get()) * 100
    oilprice = int(oilEntry.get()) * 120
    sugarprice = int(sugarEntry.get()) * 50
    teaprice = int(teaEntry.get()) * 140
    wheatprice = int(wheatEntry.get()) * 80

    totalgroceryprice = riceprice + daalprice + oilprice + sugarprice + teaprice + wheatprice
    grocerypriceEntry.delete(0, END)
    grocerypriceEntry.insert(0, str(totalgroceryprice) + ' Rs')

    # grocery tax
    grocerytax = totalgroceryprice * 0.05
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, str(grocerytax) + ' Rs')

    #colddrinks price calculation
    maazaprice = int(maazaEntry.get()) * 50
    pepsiprice = int(pepsiEntry.get()) * 20
    spriteprice = int(spriteEntry.get()) * 30
    bovontoprice = int(bovontoEntry.get()) * 20
    frootiprice = int(frootiEntry.get()) * 90
    cocacolaprice = int(cocacolaEntry.get()) * 45

    totaldrinksprice = maazaprice + pepsiprice + spriteprice + bovontoprice + frootiprice + cocacolaprice
    DrinkspriceEntry.delete(0, END)
    DrinkspriceEntry.insert(0, str(totaldrinksprice) + ' Rs')

    # colddrinks tax
    Drinkstax = totaldrinksprice * 0.08
    DrinkstaxEntry.delete(0, END)
    DrinkstaxEntry.insert(0, str(Drinkstax) + ' Rs')

    totalbill = totalcosmeticprice + totalgroceryprice + totaldrinksprice + cosmetictax + grocerytax + Drinkstax


#GUI part

root = Tk()
root.title("retail billing system created by sowmiya")
root.geometry("1270x685")
root.iconbitmap('icon.ico')

headinglabel = Label(root, text='Retail Billing System', font=('times new roman', 30, 'bold'),
                     bg='gray20', fg='gold', bd=12, relief="groove")
headinglabel.pack(fill=X)

#customer details
customer_details_frame = LabelFrame(root, text='Customer Details', font=('times new roman', 15, 'bold')
                                    , fg='gold', bd=8, relief="groove", bg='gray20')
customer_details_frame.pack(fill=X)

#name label
nameLabel = Label(customer_details_frame, text='Name', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='white')
nameLabel.grid(row=0, column=0, padx=20, pady=2)
#name entry

nameEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
nameEntry.grid(row=0, column=1, padx=8)

#phone label
phoneLabel = Label(customer_details_frame, text='Phone Number', font=('times new roman', 15, 'bold'), bg='gray20',
                   fg='white')
phoneLabel.grid(row=0, column=2, padx=20, pady=2)

#phoneentry
phoneEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
phoneEntry.grid(row=0, column=3, padx=8)

#bill label
billnumberLabel = Label(customer_details_frame, text='BillNumber', font=('times new roman', 15, 'bold'), bg='gray20',
                        fg='white')
billnumberLabel.grid(row=0, column=4, padx=20, pady=2)

#bill entry
billnumberEntry = Entry(customer_details_frame, font=('arial', 15), bd=7, width=18)
billnumberEntry.grid(row=0, column=5, padx=8)

#search button
searchButton = Button(customer_details_frame, text='SEARCH',
                      font=('arial', 12, 'bold'), bd=7, width=10, command=search_bill)
searchButton.grid(row=0, column=6, padx=20, pady=8)

#product details
productsFrame = Frame(root)
productsFrame.pack(fill=X)

#cosmetic frame
cosmeticsFrame = LabelFrame(productsFrame, text='Cosmetics', font=('times new roman', 15, 'bold')
                            , fg='gold', bd=8, relief="groove", bg='gray20')
cosmeticsFrame.grid(row=0, column=0)

#bathsoap
bathsoapLabel = Label(cosmeticsFrame, text='Bath Soap', font=('times new roman', 15, 'bold'), bg='gray20',
                      fg='white')
bathsoapLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

bathsoapEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
bathsoapEntry.grid(row=0, column=1, pady=9, padx=10)
bathsoapEntry.insert(0, 0)

#face cream
facecreamLabel = Label(cosmeticsFrame, text='Face Cream', font=('times new roman', 15, 'bold'), bg='gray20',
                       fg='white')
facecreamLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

facecreamEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
facecreamEntry.grid(row=1, column=1, pady=9, padx=10)
facecreamEntry.insert(0, 0)

#face wash
facewashLabel = Label(cosmeticsFrame, text='Face Wash', font=('times new roman', 15, 'bold'), bg='gray20',
                      fg='white')
facewashLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

facewashEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
facewashEntry.grid(row=2, column=1, pady=9, padx=10)
facewashEntry.insert(0, 0)

#hair spray
hairsprayLabel = Label(cosmeticsFrame, text='Hair Spray', font=('times new roman', 15, 'bold'), bg='gray20',
                       fg='white')
hairsprayLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

hairsprayEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
hairsprayEntry.grid(row=3, column=1, pady=10)
hairsprayEntry.insert(0, 0)

#hair gel
hairgelLabel = Label(cosmeticsFrame, text='Hair Gel', font=('times new roman', 15, 'bold'), bg='gray20',
                     fg='white')
hairgelLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

hairgelEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
hairgelEntry.grid(row=4, column=1, pady=9, padx=10)
hairgelEntry.insert(0, 0)

#body lotion
bodylotionLabel = Label(cosmeticsFrame, text='Body Lotion', font=('times new roman', 15, 'bold'), bg='gray20',
                        fg='white')
bodylotionLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

bodylotionEntry = Entry(cosmeticsFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
bodylotionEntry.grid(row=5, column=1, pady=9, padx=10)
bodylotionEntry.insert(0, 0)

#Grocery frame
groceryFrame = LabelFrame(productsFrame, text='Grocery', font=('times new roman', 15, 'bold')
                          , fg='gold', bd=8, relief="groove", bg='gray20')
groceryFrame.grid(row=0, column=1)

#rice
riceLabel = Label(groceryFrame, text='Rice', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='white')
riceLabel.grid(row=0, column=0, pady=9, padx=10, sticky='w')

riceEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
riceEntry.grid(row=0, column=1, pady=9, padx=10)
riceEntry.insert(0, 0)

#oil
oilLabel = Label(groceryFrame, text='Oil', font=('times new roman', 15, 'bold'), bg='gray20',
                 fg='white')
oilLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

oilEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
oilEntry.grid(row=1, column=1, pady=9, padx=10)
oilEntry.insert(0, 0)

#daal
daalLabel = Label(groceryFrame, text='Daal', font=('times new roman', 15, 'bold'), bg='gray20',
                  fg='white')
daalLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

daalEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
daalEntry.grid(row=2, column=1, pady=9, padx=10)
daalEntry.insert(0, 0)

#wheat
wheatLabel = Label(groceryFrame, text='Wheat', font=('times new roman', 15, 'bold'), bg='gray20',
                   fg='white')
wheatLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

wheatEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
wheatEntry.grid(row=3, column=1, pady=9, padx=10)
wheatEntry.insert(0, 0)

#sugar
sugarLabel = Label(groceryFrame, text='Sugar', font=('times new roman', 15, 'bold'), bg='gray20',
                   fg='white')
sugarLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

sugarEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
sugarEntry.grid(row=4, column=1, pady=9, padx=10)
sugarEntry.insert(0, 0)

#tea
teaLabel = Label(groceryFrame, text='Tea', font=('times new roman', 15, 'bold'), bg='gray20',
                 fg='white')
teaLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

teaEntry = Entry(groceryFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
teaEntry.grid(row=5, column=1, pady=9, padx=10)
teaEntry.insert(0, 0)

#drinks frame
drinksFrame = LabelFrame(productsFrame, text='Cold Drinks', font=('times new roman', 15, 'bold')
                         , fg='gold', bd=8, relief="groove", bg='gray20')
drinksFrame.grid(row=0, column=2)

#maaza
maazaLabel = Label(drinksFrame, text='Maaza', font=('times new roman', 15, 'bold'), bg='gray20',
                   fg='white')
maazaLabel.grid(row=1, column=0, pady=9, padx=10, sticky='w')

maazaEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
maazaEntry.grid(row=1, column=1, pady=9, padx=10)
maazaEntry.insert(0, 0)

#pepsi
pepsiLabel = Label(drinksFrame, text='Pepsi', font=('times new roman', 15, 'bold'), bg='gray20',
                   fg='white')
pepsiLabel.grid(row=2, column=0, pady=9, padx=10, sticky='w')

pepsiEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
pepsiEntry.grid(row=2, column=1, pady=9, padx=10)
pepsiEntry.insert(0, 0)

#sprite
spriteLabel = Label(drinksFrame, text='sprite', font=('times new roman', 15, 'bold'), bg='gray20',
                    fg='white')
spriteLabel.grid(row=3, column=0, pady=9, padx=10, sticky='w')

spriteEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
spriteEntry.grid(row=3, column=1, pady=9, padx=10)
spriteEntry.insert(0, 0)

#bovonto
bovontoLabel = Label(drinksFrame, text='Bovonto', font=('times new roman', 15, 'bold'), bg='gray20',
                     fg='white')
bovontoLabel.grid(row=4, column=0, pady=9, padx=10, sticky='w')

bovontoEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
bovontoEntry.grid(row=4, column=1, pady=9, padx=10)
bovontoEntry.insert(0, 0)

#frooti
frootiLabel = Label(drinksFrame, text='Frooti', font=('times new roman', 15, 'bold'), bg='gray20',
                    fg='white')
frootiLabel.grid(row=5, column=0, pady=9, padx=10, sticky='w')

frootiEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
frootiEntry.grid(row=5, column=1, pady=9, padx=10)
frootiEntry.insert(0, 0)

#cocacola
cocacolaLabel = Label(drinksFrame, text='CocaCola', font=('times new roman', 15, 'bold'), bg='gray20',
                      fg='white')
cocacolaLabel.grid(row=6, column=0, pady=9, padx=10, sticky='w')

cocacolaEntry = Entry(drinksFrame, font=('times new roman', 15, 'bold'), width=10, bd=5)
cocacolaEntry.grid(row=6, column=1, pady=9, padx=10)
cocacolaEntry.insert(0, 0)

#bill frame
billframe = Frame(productsFrame, bd=7, relief="groove")
billframe.grid(row=0, column=3, padx=10)

#bill area
billareaLabel = Label(billframe, text="Bill Area", font=('times new roman', 15, 'bold'), bd=7, relief="groove")
billareaLabel.pack(fill=X)

scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

textarea = Text(billframe, height=18, width=55, yscrollcommand=scrollbar.set)
textarea.pack()

scrollbar.config(command=textarea.yview)  #for viewing the upper scroll

#billmenu frame
billmenuFrame = LabelFrame(root, text='Bill Menu', font=('times new roman', 15, 'bold')
                           , fg='gold', bd=8, relief="groove", bg='gray20')
billmenuFrame.pack()

#Cosmetic price
cosmeticpriceLabel = Label(billmenuFrame, text='Cosmetic price', font=('times new roman', 14, 'bold'), bg='gray20',
                           fg='white')
cosmeticpriceLabel.grid(row=0, column=0, pady=6, padx=10, sticky='w')

cosmeticpriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
cosmeticpriceEntry.grid(row=0, column=1, pady=6, padx=10)

#grocery price
grocerypriceLabel = Label(billmenuFrame, text='Grocery price', font=('times new roman', 14, 'bold'), bg='gray20',
                          fg='white')
grocerypriceLabel.grid(row=1, column=0, pady=6, padx=10, sticky='w')

grocerypriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
grocerypriceEntry.grid(row=1, column=1, pady=6, padx=10)

#cold drink price
DrinkspriceLabel = Label(billmenuFrame, text='ColdDrink price', font=('times new roman', 14, 'bold'), bg='gray20',
                         fg='white')
DrinkspriceLabel.grid(row=2, column=0, pady=6, padx=10, sticky='w')

DrinkspriceEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
DrinkspriceEntry.grid(row=2, column=1, pady=6, padx=10)

#Cosmetic tax
cosmetictaxLabel = Label(billmenuFrame, text='Cosmetic tax', font=('times new roman', 14, 'bold'), bg='gray20',
                         fg='white')
cosmetictaxLabel.grid(row=0, column=2, pady=6, padx=10, sticky='w')

cosmetictaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
cosmetictaxEntry.grid(row=0, column=3, pady=6, padx=10)

#grocery tax
grocerytaxLabel = Label(billmenuFrame, text='Grocery Tax', font=('times new roman', 14, 'bold'), bg='gray20',
                        fg='white')
grocerytaxLabel.grid(row=1, column=2, pady=6, padx=10, sticky='w')

grocerytaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
grocerytaxEntry.grid(row=1, column=3, pady=6, padx=10)

#cold drink tax
DrinkstaxLabel = Label(billmenuFrame, text='ColdDrink tax', font=('times new roman', 14, 'bold'), bg='gray20',
                       fg='white')
DrinkstaxLabel.grid(row=2, column=2, pady=6, padx=10, sticky='w')

DrinkstaxEntry = Entry(billmenuFrame, font=('times new roman', 14, 'bold'), width=10, bd=5)
DrinkstaxEntry.grid(row=2, column=3, pady=6, padx=10)

#button frame
buttonFrame = Frame(billmenuFrame, bd=8, relief="groove")
buttonFrame.grid(row=0, column=4, rowspan=3)

totalButton = Button(buttonFrame, text='total', font=('arial', 16, 'bold'), bg='gray20', fg='white',
                     bd=5, width=8, pady=10, command=total)
totalButton.grid(row=0, column=0, pady=20, padx=5)

billButton = Button(buttonFrame, text='Bill', font=('arial', 16, 'bold'), bg='gray20', fg='white',
                    bd=5, width=8, pady=10, command=bill_area)
billButton.grid(row=0, column=1, pady=20, padx=5)

emailButton = Button(buttonFrame, text='Email', font=('arial', 16, 'bold'), bg='gray20', fg='white',
                     bd=5, width=8, pady=10,command=send_email)
emailButton.grid(row=0, column=2, pady=20, padx=5)

printButton = Button(buttonFrame, text='Print', font=('arial', 16, 'bold'), bg='gray20', fg='white',
                     bd=5, width=8, pady=10,command=print_bill)
printButton.grid(row=0, column=3, pady=20, padx=5)

clearButton = Button(buttonFrame, text='Clear', font=('arial', 16, 'bold'), bg='gray20', fg='white',
                     bd=5, width=8, pady=10,command=clear)
clearButton.grid(row=0, column=4, pady=20, padx=5)

root.mainloop()
