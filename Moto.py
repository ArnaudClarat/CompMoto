import sqlite3
from sqlite3 import Error

def menu():
	print("""
	Menu :
		1 = Ajouter une moto
		2 = Afficher une moto
		3 = Supprimer une moto
		4 = Afficher la meilleure moto
		Q = Quitter le programme""")

def newMoto():
	marque = input("\nMarque? ")
	modele = input("Modèle? ")
	conso = input("Consommation? L/100km ")
	puissance = input("Puissance? CV ")
	reserv = input("Taille résérvoir? L")
	autonomie = input("Autonomie? km")
	prix = input("Prix? ")
	notePerso= input("Note personnelle? /100 ")
	return marque, modele, conso, puissance, reserv, autonomie, prix, notePerso

def remplissage():
		# Opération sur la DB
		cur.execute("CREATE TABLE IF NOT EXISTS motos (id INTEGER PRIMARY KEY, marque TEXT, modele TEXT, conso REAL, puissance INTEGER, reserv REAL, autonomie REAL, prix INTEGER, notePerso INTEGER)")
		cur.execute("INSERT INTO motos (marque, modele, conso, puissance, reserv, autonomie, prix, notePerso) VALUES(?,?,?,?,?,?,?,?)",(newMoto()))

def modDonneeMoto(moto):
	i = 0
	print("")
	print("marque : " + str(moto[1]))
	print("modele : " + str(moto[2]))
	print("prix : " + str(moto[3]))
	print("notePerso : " + str(moto[4]))
	menu = input("Quelle donnée voulez-vous modifier? ")
	change = input("Veuillez rentrer la nouvelle donnée : ")
	return menu, change

def choiceMoto(cur) :
	print("\nListe des motos :\n")
	cur.execute("SELECT id, marque, modele FROM motos")
	for moto in cur :
		print(moto)
	menu1 = input("Quelle moto voulez-vous choisir? ")
	try :
		test = int(menu1) or int(menu1) < 9
	except :
		menu1 = input("Veuillez saisir un numéro correct : ")
	print("\nListe info :")
	cur.execute("SELECT * FROM motos WHERE id = ?",(menu1))
	for donnee in cur :
		print(donnee)
	return menu1

def modMoto(cur) :
	menu1 = choiceMoto(cur)
	menu2 = input("Voulez-vous la modifier? ")
	if menu2 == "oui" :
		nomDonnee, newDonnee = modDonneeMoto(donnee)
		cmd = "UPDATE motos SET " + nomDonnee + " = " + newDonnee + " WHERE id = " + menu1
		cur.execute(cmd)

def delMoto(cur):
	menu1 = choiceMoto(cur)
	menu2 = input("Voulez-vous VRAIMENT la supprimer? ")
	if menu2 == "oui" :
		cmd = "DELETE FROM Motos WHERE id = " + menu1
		cur.execute(cmd)
		print("Moto supprimée")

def bestMoto():
	a = 0

#Définition Variable Globale
moto=""
msg= "	Que voulez-vous faire? "
choix = "x"

#Programme
print("\nBienvenue dans ce comparateur de moto!")
try:
    db = sqlite3.connect('data/moto.db')
    cur = db.cursor()
except Error as e:
    print(e)

while choix != "Q" :
	menu()
	choix = input(msg).upper()

	if choix == "1" : 
		remplissage()
		db.commit()
	if choix == "2" :
		modMoto(cur)
		db.commit()
	if choix == "3" :
		delMoto(cur)
		db.commit()
	if choix == "4" :
		a = 4
	if choix == "Q" :
		a = 0

db.commit()
db.close()