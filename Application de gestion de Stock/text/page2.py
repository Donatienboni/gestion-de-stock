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
        self.root.title("Gestion de stock de magasin")

        #   VARIABLE
        self.var_id = StringVar()
        self.var_nom = StringVar()
        self.var_categorie = StringVar()
        self.var_quantite = StringVar()
        self.var_prix_unitaire = StringVar()

        # Créer les widgets ici
        titre_label = Label(root, text="GESTION DE STOCK",
                            font=("times new roman", 20, "bold"), bg="darkblue", fg="white")
        titre_label.place(x=0, y=0, width=1200, height=45)

        main_frame = Frame(root, bd=2, bg="yellow")
        main_frame.place(x=10, y=50, width=1180, height=540)

        Frame_1 = LabelFrame(main_frame, bd=1, bg="white", relief="solid", text="Données",
                             font=("times new roman", 12, "bold"))
        Frame_1.place(x=10, y=10, width=1000, height=150)

        # 2eme Frame
        Frame_2 = LabelFrame(main_frame, bd=5, bg="yellow", relief=RIDGE,text="Liste de personnes enregistrées", font=("times new roman", 12, "bold"))
        Frame_2.place(x=10, y=165, width=1240, height=450)
        
        # id
        
        etudiant_ID_Label = Label(Frame_1, text="Id", font=("times new roman", 13, "bold"))
        etudiant_ID_Label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        etudiant_ID = ttk.Entry(Frame_1, textvariable=self.var_id, width=5, font=("times new roman", 13, "bold"))
        etudiant_ID.grid(row=1, column=3, padx=10, pady=10, sticky=W)           
        
        # prix
        etudiant_ID_Label = Label(
            Frame_1, text="Prix Unitaire", font=("times new roman", 13, "bold"))
        etudiant_ID_Label.grid(row=0, column=4, padx=10, pady=10, sticky=W)

        etudiant_ID = ttk.Entry(Frame_1, textvariable=self.var_prix_unitaire, width=20, font=("times new roman", 13, "bold"))
        etudiant_ID.grid(row=0, column=5, padx=10, pady=10, sticky=W)

        # Nom
        etudiant_Nom_Label = Label(
            Frame_1, text="Nom du produit", font=("times new roman", 13, "bold"))
        etudiant_Nom_Label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        etudiant_Nom_Entry = ttk.Entry(Frame_1, textvariable=self.var_nom, width=20, font=("times new roman", 13, "bold"))
        etudiant_Nom_Entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Quantite
        etudiant_Tel_Label = Label(Frame_1, text="Quantité", font=("times new roman", 13, "bold"))
        etudiant_Tel_Label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        etudiant_Tel_Entry = ttk.Entry(Frame_1, textvariable=self.var_quantite, width=20, font=("times new roman", 13, "bold"))
        etudiant_Tel_Entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Categorie
        etudiant_Tel_Label = Label(Frame_1, text="Categorie", font=("times new roman", 13, "bold"))
        etudiant_Tel_Label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        Categorie = ["Alimantation", "Electrique", "Vetement"]
        etudiant_Tel_Entry = ttk.Combobox(Frame_1, textvariable=self.var_categorie, width=20, font=("times new roman", 13, "bold"), values=Categorie)
        etudiant_Tel_Entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        # etudiant_Tel_Entry=

# =============Button
        btn_frame = Frame(Frame_1, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=10, y=90, width=715, height=35)

        btn_enregistrer = Button(btn_frame, text="Enregistrer", command=self.insertion_donnee, width=17, font=(
            "times new roman", 13, "bold"), bg="green")
        btn_enregistrer.grid(row=0, column=0)
        
        btn_modifier = Button(btn_frame, text="Produit et Categorie",command=self.produit_categorie,  width=17, font=("times new roman", 13, "bold"), bg="darkblue")
        btn_modifier.grid(row=0, column=1)
        
        btn_actualiser = Button(btn_frame, text="Quantite de stock", command=self.quantiteDeStock ,width=17, font=("times new roman", 13, "bold"), bg="yellow")
        btn_actualiser.grid(row=0, column=2)

        btn_supprimer = Button(btn_frame, text="supprimer",  width=17, font=("times new roman", 13, "bold"), bg="red")
        btn_supprimer.grid(row=0, column=3)

        # =========================================Table form=============================================================
        table_frame = Frame(Frame_2, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=2, width=1218, height=365)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.table_etudiant = ttk.Treeview(table_frame, columns=(
            "nom", "nom de categorie", "Quantité", "prix"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.table_etudiant.xview)
        scroll_y.config(command=self.table_etudiant.yview)

        
        self.table_etudiant.heading("nom", text="Nom du produit")
        self.table_etudiant.heading("nom de categorie", text="nom de categorie")
        self.table_etudiant.heading("Quantité", text="Quantité")
        self.table_etudiant.heading("prix", text="Prix")
        self.table_etudiant["show"] = "headings"

 
        self.table_etudiant.column("nom", width=150)
        self.table_etudiant.column("nom de categorie", width=10)
        self.table_etudiant.column("Quantité", width=10)
        self.table_etudiant.column("prix", width=50)

        self.table_etudiant.pack(fill=BOTH, expand=1)
        self.table_etudiant.bind("<ButtonRelease>", self.get_cursor)
        self.afficher_donnee()

        # ===============================================déclaration des fonctions=================================

    # def insertion_donnee(self):
    #     if self.var_nom.get() == "" or self.var_prix_unitaire.get() == "" or self.var_quantite.get() == "" or self.var_categorie.get() == "":
    #         messagebox.showerror("Erreur", "Tous les champs sont obligatoire!!!", parent=self.root)
    #     else:
    #         try:
    #             conn = mysql.connector.connect(host="localhost", username="root", password="", database="dbgestion")
    #             my_cursor = conn.cursor()
    #             my_cursor.execute("insert into produit values(%s,%s,%s,%s,%s)", (self.var_id.get(),self.var_nom.get(), self.var_prix_unitaire.get(), self.var_quantite.get(), self.var_categorie.get()))

    #             conn.commit()
    #             self.afficher_donnee()
    #             conn.close()
    #             messagebox.showinfo(
    #                 "Succes", "enregistrées effectuer avec succès!", parent=self.root)
    #         except Exception as es:
    #             messagebox.showerror(
    #                 "Erreur", f"Due à: {str(es)}", parent=self.root)

# ===========================================================ici pour recuperer produit et quantiter==========================================================================

    def insertion_donnee(self):
      if self.var_nom.get()=="" or self.var_prix_unitaire.get()=="" or self.var_quantite.get()==""or self.var_categorie.get()=="":
        messagebox.showerror("Erreur" , "Tous les champs sont obligatoire!!!" , parent=self.root)
      else:
        try:
          conn=mysql.connector.connect(host="localhost" , username="root" , password="", database="dbgestion")
          my_cursor=conn.cursor()
          my_cursor.execute("select produit.nom, categorie.nom, produit.quantite, produit.prix_unitaire from produit JOIN categorie ON produit.categorie_id = categorie.id" )

          conn.commit()
          self.afficher_donnee()
          conn.close()
          messagebox.showinfo("Succes","enregistrées effectuer avec succès!", parent=self.root)
        except Exception as es:
          messagebox.showerror("Erreur", f"Due à: {str(es)}" , parent=self.root)

                # ==================================================fetch data=========================================

    def afficher_donnee(self):
        try:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="", database="dbgestion")
            my_cursor = conn.cursor()
            my_cursor.execute("select produit.nom, categorie.nom, produit.quantite, produit.prix_unitaire from produit JOIN categorie ON produit.categorie_id = categorie.id")
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

        # self.var_id.set(data[0]),
        self.var_nom.set(data[0]),
        self.var_categorie.set(data[1]),
        self.var_quantite.set(data[2]),
        self.var_prix_unitaire.set(data[3]),


# rediriger vers une nouvelle page  
    def quantiteDeStock(self):
        if self.quantiteDeStock == self.quantiteDeStock: 
            root.destroy()
            import page3

    def produit_categorie(self):
        if self.produit_categorie == self.produit_categorie:
            root.destroy()
            import page2
    

root = Tk()
obj = gestion(root)
root.mainloop()

