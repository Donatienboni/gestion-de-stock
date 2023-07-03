from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import mysql.connector
import tkinter as tk


class gestion:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x650")
        self.root.title("Quantité de stock")

        #   VARIABLE
        self.var_id = StringVar()
        self.var_produit_id = StringVar()
        self.var_quantite = StringVar()
        self.var_date = StringVar()

        # Créer les widgets ici
        titre_label = Label(root, text="VENTE",
                            font=("times new roman", 20, "bold"), bg="darkblue", fg="white")
        titre_label.place(x=0, y=0, width=1200, height=45)

        main_frame = Frame(root, bd=2, bg="yellow")
        main_frame.place(x=10, y=50, width=1180, height=540)

        Frame_1 = LabelFrame(main_frame, bd=1, bg="white", relief="solid", text="Données",
                             font=("times new roman", 12, "bold"))
        Frame_1.place(x=10, y=10, width=1000, height=150)

        # 2eme Frame
        Frame_2 = LabelFrame(main_frame, bd=5, bg="yellow", relief=RIDGE,
                             text="Liste de personnes enregistrées", font=("times new roman", 12, "bold"))
        Frame_2.place(x=10, y=165, width=1240, height=450)

        # id

        etudiant_ID_Label = Label(
            Frame_1, text="ID_vente", font=("times new roman", 13, "bold"))
        etudiant_ID_Label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        etudiant_ID = ttk.Entry(Frame_1, textvariable=self.var_id, width=5, font=(
            "times new roman", 13, "bold"))
        etudiant_ID.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        # ID_produit
        etudiant_ID_Label = Label(
            Frame_1, text="id_produit", font=("times new roman", 13, "bold"))
        etudiant_ID_Label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        etudiant_ID = ttk.Entry(Frame_1, textvariable=self.var_produit_id, width=5, font=(
            "times new roman", 13, "bold"))
        etudiant_ID.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        # Quantite
        etudiant_Nom_Label = Label(
            Frame_1, text="Quantite", font=("times new roman", 13, "bold"))
        etudiant_Nom_Label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        etudiant_Nom_Entry = ttk.Entry(
            Frame_1, textvariable=self.var_quantite, width=20, font=("times new roman", 13, "bold"))
        etudiant_Nom_Entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # date
        etudiant_Tel_Label = Label(
            Frame_1, text="Date", font=("times new roman", 13, "bold"))
        etudiant_Tel_Label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        etudiant_Tel_Entry = ttk.Entry(
            Frame_1, textvariable=self.var_date, width=20, font=("times new roman", 13, "bold"))
        etudiant_Tel_Entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Categorie
        etudiant_Tel_Label = Label(
            Frame_1, text=" quantité du stock restant", font=("times new roman", 13, "bold"))
        etudiant_Tel_Label.grid(row=1, column=4, padx=10, pady=5, sticky=W)

        etudiant_Tel_Entry = ttk.Entry(
            Frame_1, width=15, font=("times new roman", 13, "bold"))
        etudiant_Tel_Entry.grid(row=1, column=5, padx=10, pady=5, sticky=W)

# ===================================== partie Button
        btn_frame = Frame(Frame_1, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=10, y=90, width=183, height=35)

        btn_frame1 = Frame(Frame_1, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=200, y=90, width=183, height=35)

        btn_frame2 = Frame(Frame_1, bd=2, relief=RIDGE, bg="white")
        btn_frame2.place(x=390, y=90, width=183, height=35)

        btn_frame3 = Frame(Frame_1, bd=2, relief=RIDGE, bg="white")
        btn_frame3.place(x=580, y=90, width=183, height=35)

        btn_frame4 = Frame(Frame_1, bd=2, relief=RIDGE, bg="white")
        btn_frame4.place(x=780, y=2, width=100, height=35)

        btn_enregistrer = Button(btn_frame, text="Enregistrer vente", command=self.insertion_donnee, width=17, font=(
            "times new roman", 13, "bold"), bg="green", fg="white")
        btn_enregistrer.grid(row=0, column=0)

        btn_modifier = Button(btn_frame1, text="Modidifier vente", command=self.ModidifierVente, width=17, font=(
            "times new roman", 13, "bold"), bg="darkblue", fg="white")
        btn_modifier.grid(row=0, column=1)

        btn_supprimer = Button(btn_frame2, text="Supprimer", command=self.SupprimerVente, width=17, font=(
            "times new roman", 13, "bold"), bg="red", fg="white")
        btn_supprimer.grid(row=0, column=1)

        btn_vente = Button(btn_frame3, text="Validé Vente", command=self.ValiderVente, width=17, font=(
            "times new roman", 13, "bold"), bg="red", fg="white")
        btn_vente.grid(row=0, column=1)

        btn_retour = Button(btn_frame4, text="Retour", command=self.retour, width=17, font=(
            "times new roman", 13, "bold"), bg="yellow", fg="black")
        btn_retour.grid(row=0, column=1)

        # =========================================Table form=============================================================
        table_frame = Frame(Frame_2, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=2, width=1218, height=365)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.table_etudiant = ttk.Treeview(table_frame, columns=(
            "id", "ID_produit", "quantite", "Date"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.table_etudiant.xview)
        scroll_y.config(command=self.table_etudiant.yview)

        self.table_etudiant.heading("id", text="ID_vente")
        self.table_etudiant.heading("ID_produit", text="id produit")
        self.table_etudiant.heading("quantite", text="Quantité")
        self.table_etudiant.heading("Date", text="Date")
        self.table_etudiant["show"] = "headings"

        self.table_etudiant.column("id", width=10,)
        self.table_etudiant.column("ID_produit", width=10)
        self.table_etudiant.column("quantite", width=10)
        self.table_etudiant.column("Date", width=10)

        self.table_etudiant.pack(fill=BOTH, expand=1)
        self.table_etudiant.bind("<ButtonRelease>", self.get_cursor)
        self.afficher_donnee()

        # ===============================================déclaration des fonctions=================================
# =================================inserer
    def insertion_donnee(self):
        if self.var_produit_id.get() == "" or self.var_quantite.get() == "":
            messagebox.showerror(
                "Erreur", "Tous les champs sont obligatoire!!!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="dbgestion")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into vente values(%s,%s,%s,%s)", (self.var_id.get(
                ), self.var_produit_id.get(), self.var_quantite.get(), self.var_date.get()))

                conn.commit()
                self.afficher_donnee()
                conn.close()
                messagebox.showinfo(
                    "Succes", "enregistrées effectuer avec succès!", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Erreur", f"Due à: {str(es)}", parent=self.root)

# ================================== modifier
    def ModidifierVente(self):
        if self.var_produit_id.get() == "" or self.var_quantite.get() == "":
            messagebox.showerror(
                "Erreur", "Tous les champs sont obligatoire!!!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="dbgestion")
                my_cursor = conn.cursor()
                my_cursor.execute("update vente set  produit_id= %s, quantite= %s , date= %s where id= %s", (
                    self.var_produit_id.get(), self.var_quantite.get(), self.var_date.get(), self.var_id.get()))
                # my_cursor.execute("update vente set quantite= quantite- %s where produit_id= %s", (self.var_quantite.get(),self.var_produit_id.get()))

                conn.commit()
                self.afficher_donnee()
                conn.close()
                messagebox.showinfo(
                    "Succes", "modification effectuer avec succès!", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Erreur", f"Due à: {str(es)}", parent=self.root)

# ====================================== supprimer
    def SupprimerVente(self):
        if self.var_id.get() == "":
            messagebox.showerror(
                "Erreur", "Tous les champs sont obligatoire!!!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="dbgestion")
                my_cursor = conn.cursor()
                # my_cursor.execute("delete from vente where id= %s ", (self.var_id.get()))
                my_cursor.execute(
                    "delete from vente where id= %s ", (self.var_id.get()))

                conn.commit()
                self.afficher_donnee()
                conn.close()
                messagebox.showinfo(
                    "Succes", "suppression effectuer avec succès!", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Erreur", f"Due à: {str(es)}", parent=self.root)
# ====================================== vendre

    def ValiderVente(self):
        if self.var_id.get() == "":
            messagebox.showerror(
                "Erreur", "Tous les champs sont obligatoire!!!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="", database="dbgestion")
                my_cursor = conn.cursor()
                my_cursor.execute("update vente set quantite= quantite- %s where produit_id= %s",
                                  (self.var_quantite.get(), self.var_produit_id.get()))

                conn.commit()
                self.afficher_donnee()
                conn.close()
                messagebox.showinfo(
                    "Succes", "suppression effectuer avec succès!", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Erreur", f"Due à: {str(es)}", parent=self.root)

# ===========================================================ici pour recuperer produit et quantiter==========================================================================

                # ==================================================fetch data=========================================

    def afficher_donnee(self):
        try:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="", database="dbgestion")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from vente ")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.table_etudiant.delete(*self.table_etudiant.get_children())
                for i in data:
                    self.table_etudiant.insert("", END, values=i)
                    conn.commit()
        except Exception as es:
            messagebox.showerror(
                "Erreur", f"Due à : {str(es)}", parent=self.root)
            # ==================================================Recuperer la ligne sélectionner=========================================

    def get_cursor(self, event=""):
        cursor_focus = self.table_etudiant.focus()
        content = self.table_etudiant.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_produit_id.set(data[1]),
        self.var_quantite.set(data[2]),
        self.var_date.set(data[3]),


# rediriger vers une nouvelle page

    def retour(self):
        if self.retour == self.retour:
            root.destroy()
            import page1

    # def produit_categorie(self):
    #     if self.produit_categorie == self.produit_categorie:
    #         root.destroy()
    #         import page2


root = Tk()
obj = gestion(root)
root.mainloop()
