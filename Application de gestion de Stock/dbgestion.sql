-- Active: 1645709454977@@127.0.0.1@3306@dbgestion
/* SELECT produit.nom, categorie.nom, produit.quantite, produit.prix_unitaire
 FROM produit
JOIN categorie ON produit.categorie_id = categorie.id */




/* UPDATE produit SET quantite = quantite - vente_quantite WHERE id = id */

/* UPDATE `vente` SET `date` = '2023-06-26' WHERE `vente`.`id` = 3 */

/* SELECT * FROM client WHERE email="donatien@gmail.com" AND password=1234  */

 /* DELETE FROM `vente` WHERE `id`=3 */

/* SELECT id FROM produit  */

 

/* 
UPDATE produit
SET quantite_en_stock = quantite_en_stock - (SELECT quantite_vendue FROM vente WHERE id_produit = produit.id)
WHERE id = [ID DU PRODUIT VENDU]; */


/* my_cursor.execute("update produit set  nom= %s, categorie_id= %s,quantite= %s , prix_unitaire= %s where id= %s", ( self.var_nom.get(), self.var_prix_unitaire.get(), self.var_quantite.get(), self.var_categorie.get(),self.var_id.get())) */




 /* my_cursor.execute("update vente set quantite= quantite- %s where produit_id= %s", (self.var_quantite.get(),self.var_produit_id.get())) */


select produit.nom, categorie.nom, produit.quantite, produit.prix_unitaire from produit JOIN categorie ON produit.categorie_id = categorie.id