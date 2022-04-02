# ****  RajaSekhar Thimmarayappagari ****

from tkinter import *
import random

class BillingSystem:
    tea = IntVar()
    coffee = IntVar()
    lemon_tea = IntVar()
    black_coffee = IntVar()
    milk = IntVar()
    pani_puri = IntVar()
    gobi = IntVar()
    poha = IntVar()
    pakoda = IntVar()
    lassi = IntVar()
    pepsi = IntVar()
    coke = IntVar()
    sprite = IntVar()
    thumsup = IntVar()
    bindu_zeera = IntVar()
    total_mc = StringVar()
    total_chat = StringVar()
    total_softd = StringVar()
    tax_mc = StringVar()
    tax_chat = StringVar()
    tax_softd = StringVar()

    def __init__(self, roo):
        self.total_softd_prices = None
        self.total_chat_prices = None
        self.total_mc_prices = None
        self.root = roo
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width=900, height=650)
        self.root.minsize(width=1300, height=700)
        self.root.title("Raja Bill project")

        # ====================Variables========================#
        self.cus_name = StringVar()
        self.c_phone = StringVar()

        # For Generating Random Bill Numbers
        x = random.randint(1000, 9999)
        self.c_bill_no = StringVar()

        # Setting Value to variable
        self.c_bill_no.set(str(x))

        # ===================================
        bg_color = "white"
        fg_color = "black"
        lbl_color = 'blue'

        # Title of Application
        Label(self.root, text="Raja's Billing ", fg=fg_color, bg=bg_color,
              font=("Cambria", 25, "bold"), pady=1).pack(fill=X)

        # ****  Customer's details  ****
        f1 = LabelFrame(text="Customer Details", font=("time new roman", 16, "bold"), fg="brown", bg=bg_color)
        f1.place(x=0, y=80, relwidth=1)

        # ****  Customer Name Design  ****

        Label(f1, text="Customer Name", bg=bg_color, fg=fg_color,
              font=("Monaco", 20, "bold")).grid(row=0, column=0, padx=10, pady=5)
        cname_en = Entry(f1, textvariable=self.cus_name)
        cname_en.grid(row=0, column=1, ipady=4, ipadx=35, pady=5)

        # ****  Customer Phone number design  ****
        Label(f1, text="Phone No:", bg=bg_color, fg=fg_color, font=("Monaco", 20, "bold")).grid(
            row=0, column=2, padx=20)
        cphone_en = Entry(f1, textvariable=self.c_phone)
        cphone_en.grid(row=0, column=3, ipady=4, ipadx=30, pady=5)

        # ****  Main Course Frame Design  ****
        f2 = LabelFrame(self.root, text='Main Course', bg=bg_color, fg="gold",
                        font=("Arial", 13, "bold"))
        f2.place(x=5, y=180, width=325, height=380)

        # ****  Frame for Tea  ****
        bath_lbl = Label(f2, font=("Arial", 15, "bold"), fg=lbl_color, bg=bg_color, text="Tea")
        bath_lbl.grid(row=0, column=0, padx=10, pady=20)
        bath_en = Entry(f2, textvariable=self.tea)
        bath_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # ****  Coffee  ****
        face_lbl = Label(f2, font=("Arial", 15, "bold"), fg=lbl_color, bg=bg_color, text="Coffee")
        face_lbl.grid(row=1, column=0, padx=10, pady=20)
        face_en = Entry(f2, textvariable=self.coffee)
        face_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # ****  LemonTea  ****
        wash_lbl = Label(f2, font=("Arial", 15, "bold"), fg=lbl_color, bg=bg_color, text="LemonTea")
        wash_lbl.grid(row=2, column=0, padx=10, pady=20)
        wash_en = Entry(f2, textvariable=self.lemon_tea)
        wash_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # ****  Black Coffee ****
        hair_lbl = Label(f2, font=("Arial", 15, "bold"), fg=lbl_color, bg=bg_color, text="Black Coffee")
        hair_lbl.grid(row=3, column=0, padx=10, pady=20)
        hair_en = Entry(f2, textvariable=self.black_coffee)
        hair_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # **** Milk ****
        lot_lbl = Label(f2, font=("Arial", 15, "bold"), fg=lbl_color, bg=bg_color, text="Milk")
        lot_lbl.grid(row=4, column=0, padx=10, pady=20)
        lot_en = Entry(f2, textvariable=self.milk)
        lot_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # **** chat Frame ****
        f2 = LabelFrame(self.root, text='Chats', bg=bg_color, fg="gold",
                        font=("Arial", 13, "bold"))
        f2.place(x=330, y=180, width=325, height=380)

        # ****  Frame Content ****
        pani_puri_lbl = Label(f2, font=("Arial", 15, "bold"), fg=lbl_color, bg=bg_color, text="Pani Puri")
        pani_puri_lbl.grid(row=0, column=0, padx=10, pady=20)
        pani_puri_en = Entry(f2, textvariable=self.pani_puri)
        pani_puri_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # ****  Poha ****
        oil_lbl = Label(f2, font=("Arial", 15, "bold"), fg=lbl_color, bg=bg_color, text="Poha")
        oil_lbl.grid(row=1, column=0, padx=10, pady=20)
        oil_en = Entry(f2, textvariable=self.poha)
        oil_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # **** Gobi ****
        gobi_lbl = Label(f2, font=("Arial", 15, "bold"), fg=lbl_color, bg=bg_color, text="Gobi")
        gobi_lbl.grid(row=2, column=0, padx=10, pady=20)
        gobi_en = Entry(f2, textvariable=self.gobi)
        gobi_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # ****  Pakoda  ****
        pakoda_lbl = Label(f2, font=("Arial", 15, "bold"), fg=lbl_color, bg=bg_color, text="Pakoda")
        pakoda_lbl.grid(row=3, column=0, padx=10, pady=20)
        pakoda_en = Entry(f2, textvariable=self.pakoda)
        pakoda_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # ****  Lassi  ****
        lassi_lbl = Label(f2, font=("Arial", 15, "bold"), fg=lbl_color, bg=bg_color, text="Lassi")
        lassi_lbl.grid(row=4, column=0, padx=10, pady=20)
        lassi_en = Entry(f2, textvariable=self.lassi)
        lassi_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # ****  Soft Drinks  ****

        f2 = LabelFrame(self.root, text='Soft Drinks', bg=bg_color, fg="gold",
                        font=("Arial", 13, "bold"))
        f2.place(x=655, y=180, width=325, height=380)

        # ****  pepsi****
        pepsi_lbl = Label(f2, font=("Arial", 15, "bold"), fg=lbl_color, bg=bg_color, text="Pepsi")
        pepsi_lbl.grid(row=0, column=0, padx=10, pady=20)
        pepsi_en = Entry(f2, textvariable=self.pepsi)
        pepsi_en.grid(row=0, column=1, ipady=5, ipadx=5)

        # **** Coke ****
        coke_lbl = Label(f2, font=("Arial", 15, "bold"), fg=lbl_color, bg=bg_color, text="Coke")
        coke_lbl.grid(row=1, column=0, padx=10, pady=20)
        coke_en = Entry(f2, textvariable=self.coke)
        coke_en.grid(row=1, column=1, ipady=5, ipadx=5)

        # ****  Sprite  ****
        sprite_lbl = Label(f2, font=("Arial", 15, "bold"), fg=lbl_color, bg=bg_color, text="Sprite")
        sprite_lbl.grid(row=2, column=0, padx=10, pady=20)
        sprite_en = Entry(f2, textvariable=self.sprite)
        sprite_en.grid(row=2, column=1, ipady=5, ipadx=5)

        # ****  Thumsup ****
        cold_lbl = Label(f2, font=("Arial", 15, "bold"), fg=lbl_color, bg=bg_color, text="Thumsup")
        cold_lbl.grid(row=3, column=0, padx=10, pady=20)
        cold_en = Entry(f2, textvariable=self.thumsup)
        cold_en.grid(row=3, column=1, ipady=5, ipadx=5)

        # ****  Bindu Zeera  ****
        bis_lbl = Label(f2, font=("Arial", 15, "bold"), fg=lbl_color, bg=bg_color, text="Bindu Zeera")
        bis_lbl.grid(row=4, column=0, padx=10, pady=20)
        bis_en = Entry(f2, textvariable=self.bindu_zeera)
        bis_en.grid(row=4, column=1, ipady=5, ipadx=5)

        # *********   Bill Area   ********
        f3 = Label(self.root)
        f3.place(x=960, y=180, width=325, height=380)
        # ===========
        bill_title = Label(f3, text="Raja Billing System", font=("Blockletter", 20, "bold"))
        bill_title.pack(fill=X)

        # ============
        scroll_y = Scrollbar(f3, orient=VERTICAL)
        self.txt = Text(f3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txt.yview)
        self.txt.pack(fill=BOTH, expand=1)

        # ****  Buttons Frame Area  ****
        f4 = LabelFrame(self.root, text='Bill Summary', bg=bg_color, fg="gold",
                        font=("times new roman", 13, "bold"))
        f4.place(x=0, y=560, relwidth=2, height=150)

        # **** Total of Main Course  ****
        cosm_lbl = Label(f4, font=("calibri", 15, "bold"),
                         fg=lbl_color, bg=bg_color, text="Total Main Course")
        cosm_lbl.grid(row=0, column=0, padx=10, pady=0)
        cosm_en = Entry(f4, textvariable=self.total_mc)
        cosm_en.grid(row=0, column=1, ipady=2, ipadx=5)

        # ****  Total Chats  ****
        chat_lbl = Label(f4, font=("calibri", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Chats")
        chat_lbl.grid(row=1, column=0, padx=10, pady=5)
        chat_en = Entry(f4, textvariable=self.total_chat)
        chat_en.grid(row=1, column=1, ipady=2, ipadx=5)

        # ****  Drinks Total  ****
        oth_lbl = Label(f4, font=("calibri", 15, "bold"),
                        fg=lbl_color, bg=bg_color, text="Total Drinks")
        oth_lbl.grid(row=2, column=0, padx=10, pady=5)
        oth_en = Entry(f4, textvariable=self.total_softd)
        oth_en.grid(row=2, column=1, ipady=2, ipadx=5)

        # ******* Tax Area  *******

        # ****  Main Course Tax  ****
        mainc_lbl = Label(f4, font=("calibri", 15, "bold"),
                          fg=lbl_color, bg=bg_color, text="Main Course Tax")
        mainc_lbl.grid(row=0, column=2, padx=30, pady=0)
        mainc_en = Entry(f4, textvariable=self.tax_mc)
        mainc_en.grid(row=0, column=3, ipady=2, ipadx=5)

        # ****  chat Tax  ****
        chatt_lbl = Label(f4, font=("calibri", 15, "bold"),
                          fg=lbl_color, bg=bg_color, text="Chats Tax")
        chatt_lbl.grid(row=1, column=2, padx=30, pady=5)
        chatt_en = Entry(f4, textvariable=self.tax_chat)
        chatt_en.grid(row=1, column=3, ipady=2, ipadx=5)

        # ****  Soft Drinks Tax  ****
        softd_lbl = Label(f4, font=("calibri", 15, "bold"),
                          fg=lbl_color, bg=bg_color, text="Drinks Tax")
        softd_lbl.grid(row=2, column=2, padx=10, pady=5)
        softd_en = Entry(f4, textvariable=self.tax_softd)
        softd_en.grid(row=2, column=3, ipady=2, ipadx=5)

        # ****   Total   ****
        total_btn = Button(f4, text="Total",
                           bg="red", fg=fg_color, font=("lucida", 12, "bold"), command=self.total)
        total_btn.grid(row=1, column=4, ipadx=20, padx=30)

        # ****  Print Bill  ****
        generate_bill_btn = Button(f4, text="Print Bill", bg="green", fg=fg_color, font=("lucida", 12, "bold"),
                                   command=self.bill_area)
        generate_bill_btn.grid(row=1, column=5, ipadx=20)

        # ****  Delete  ****
        delete_btn = Button(f4, text="Delete", bg="indigo", fg=fg_color, font=("lucida", 12, "bold"),
                            command=self.delete)
        delete_btn.grid(row=1, column=6, ipadx=20, padx=30)

        # ****  Exit  ****
        exit_btn = Button(f4, text="Exit", bg="brown",
                          fg=fg_color, font=("lucida", 12, "bold"), command=self.exit)
        exit_btn.grid(row=1, column=7, ipadx=20)

    # ****  Function to define get total prices & Tax ****

    def total(self):
        # ****  Total Main Course Prices  ****

        self.total_mc_prices = (
                (self.tea.get() * 20) +
                (self.coffee.get() * 20) +
                (self.lemon_tea.get() * 30) +
                (self.black_coffee.get() * 50) +
                (self.milk.get() * 20))

        self.total_mc.set("Rs. " + str(self.total_mc_prices))
        self.tax_mc.set("Rs. " + str(round(self.total_mc_prices * 0.01)))

        # ====================Total chat Prices
        self.total_chat_prices = (
                (self.pakoda.get() * 50) +
                (self.poha.get() * 40) +
                (self.gobi.get() * 80) +
                (self.pani_puri.get() * 50) +
                (self.lassi.get() * 40)

        )
        self.total_chat.set("Rs. " + str(self.total_chat_prices))
        self.tax_chat.set("Rs. " + str(round(self.total_chat_prices * 0.01)))
        # ****  Total chat Prices  ****
        self.total_softd_prices = (
                (self.pepsi.get() * 30) +
                (self.sprite.get() * 40) +
                (self.coke.get() * 40) +
                (self.thumsup.get() * 40) +
                (self.bindu_zeera.get() * 30))
        self.total_softd.set("Rs. " + str(self.total_softd_prices))
        self.tax_softd.set("Rs. " + str(round(self.total_softd_prices * 0.018)))

    # ****   Function For Text Area  ****
    def welcome(self):
        self.txt.delete('1.0', END)
        self.txt.insert(END, "  Welcome To Raja Tea Stall\n")
        self.txt.insert(END, f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END, f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END, f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END, "\nProduct          Qty         Prices")

    # ****  Function to clear the bill area  ****
    def delete(self):
        self.txt.delete('1.0', END)

    # ****  Add Product name , qty and Prices to bill area  ****
    def bill_area(self):
        self.welcome()
        if self.tea.get() != 0:
            self.txt.insert(END, f"\nTea  "
                                 f"       {self.tea.get()}           {self.tea.get() * 20}")
        if self.coffee.get() != 0:
            self.txt.insert(END, f"\nCoffee "
                                 f"       {self.coffee.get()}           {self.coffee.get() * 20}")
        if self.lemon_tea.get() != 0:
            self.txt.insert(END, f"\nLemonTea   "
                                 f"      {self.lemon_tea.get()}           {self.lemon_tea.get() * 30}")
        if self.black_coffee.get() != 0:
            self.txt.insert(END,
                            f"\nBlack Coffee  "
                            f"      {self.black_coffee.get()}           {self.black_coffee.get() * 50}")
        if self.milk.get() != 0:
            self.txt.insert(END, f"\nMilk       {self.milk.get()}           {self.milk.get() * 20}")
        if self.pakoda.get() != 0:
            self.txt.insert(END, f"\nPakoda  "
                                 f"           {self.pakoda.get()}           {self.pakoda.get() * 50}")
        if self.poha.get() != 0:
            self.txt.insert(END, f"\nPoha "
                                 f"         {self.poha.get()}           {self.poha.get() * 40}")
        if self.gobi.get() != 0:
            self.txt.insert(END, f"\nGobi              {self.gobi.get()}           {self.gobi.get() * 80}")
        if self.pani_puri.get() != 0:
            self.txt.insert(END,
                            f"\nPani_puri              {self.pani_puri.get()}           {self.pani_puri.get() * 50}")
        if self.lassi.get() != 0:
            self.txt.insert(END, f"\nLassi  "
                                 f"           {self.lassi.get()}           {self.lassi.get() * 50}")
        if self.pepsi.get() != 0:
            self.txt.insert(END, f"\nPepsi "
                                 f"            {self.pepsi.get()}           {self.pepsi.get() * 30}")
        if self.sprite.get() != 0:
            self.txt.insert(END, f"\nSprite  "
                                 f"          {self.sprite.get()}           {self.sprite.get() * 40}")
        if self.coke.get() != 0:
            self.txt.insert(END, f"\nCoke       "
                                 f"       {self.coke.get()}           {self.coke.get() * 40}")
        if self.thumsup.get() != 0:
            self.txt.insert(END, f"\nThumsup             {self.thumsup.get()}  "
                                 f"         {self.thumsup.get() * 40}")
        if self.bindu_zeera.get() != 0:
            self.txt.insert(END,
                            f"\nBindu_zeera          {self.bindu_zeera.get()}           {self.bindu_zeera.get() * 30}")
        self.txt.insert(END, "\n===================================")
        self.txt.insert(END,
                        f"\n  Total :"
                        f" {self.total_mc_prices + self.total_chat_prices + self.total_softd_prices + self.total_mc_prices * 0.01 + self.total_chat_prices * 0.01 + self.total_softd_prices * 0.018}")

    # Function to exit
    def exit(self):
        self.root.destroy()

    # Function To Clear All Fields


root = Tk()
obj = BillingSystem(root)
root.mainloop()
