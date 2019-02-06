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

def calculNoteTotale(moto):
	notePuissance = (int(moto[3]) - 20) #Coté sur 15 (Meilleur = 35/Pire = 20)
	noteConso = (float(moto[4]) - 2) * 5 #Coté sur 20 (Meilleur = 2/Pire = 6)
	noteReserv = (float(moto[5]) - 5) * 1.5 #Coté sur 30 (Meilleur = 25/Pire = 5)
	noteAutonomie = (float(moto[6]) - 200) / 20 #Coté sur 20 (Meilleur = 600/Pire = 200)
	notePrix = (float(moto[7]) - 1000) / 160 #Coté sur 25 (Meilleur = 1000/Pire = 5000)
	noteNPerso = (int(moto[8]) * 0.9) #Coté sur 90 (Meilleur = 100/Pire = 0)
	noteTotale = (notePuissance + noteConso + noteReserv + noteAutonomie + notePrix + noteNPerso) / 2
	return noteTotale

def newMoto():
	marque = input("\nMarque? ")
	modele = input("Modèle? ")
	puissance = input("Puissance? kW ")
	conso = input("Consommation? L/100km ")
	reserv = input("Taille résérvoir? L ")
	autonomie = input("Autonomie? km ")
	prix = input("Prix? ")
	notePerso = input("Note personnelle? /100 ")
	moto = marque, modele, puissance, conso, reserv, autonomie, prix, notePerso
	noteTotale = calculNoteTotale(moto)
	print("Note totale = ", noteTotale)
	return marque, modele, puissance, conso, reserv, autonomie, prix, notePerso, noteTotale

def remplissage():
		# Opération sur la DB
		cur.execute("CREATE TABLE IF NOT EXISTS motos (id INTEGER PRIMARY KEY, marque TEXT, modele TEXT, puissance INTEGER, conso REAL, reserv REAL, autonomie REAL, prix INTEGER, notePerso INTEGER, noteTotale REAL)")
		cur.execute("INSERT INTO motos (marque, modele, puissance, conso, reserv, autonomie, prix, notePerso, noteTotale) VALUES(?,?,?,?,?,?,?,?,?)",(newMoto()))

def modDonneeMoto(moto):
	return menu, change

def modMoto(cur, menu1) :
	noteTotale = 0
	nomDonnee = input("Quelle donnée voulez-vous modifier? ")
	newDonnee = input("Veuillez rentrer la nouvelle donnée : ")
	cmd = "UPDATE motos SET " + nomDonnee + " = " + newDonnee + " WHERE id = " + menu1
	cur.execute(cmd)
	cur.execute("SELECT * FROM motos WHERE id = " + menu1)
	test = cur.fetchall()
	print(test)
	noteTotale = calculNoteTotale(test)
	cmd2 = "UPDATE motos SET noteTotale = " + str(noteTotale) + " WHERE id = " + menu1
	cur.execute(cmd2)

def choiceMoto(cur) :
	print("\nListe des motos :\n")
	cur.execute("SELECT id, marque, modele FROM motos")
	for moto in cur :
		print(moto[0], ":", moto[1], moto[2])
	menu1 = input("Quelle moto voulez-vous choisir? ")
	try :
		test = int(menu1) or int(menu1) < 9
	except :
		menu1 = input("Veuillez saisir un numéro correct : ")
	cur.execute("SELECT * FROM motos WHERE id = ?",(menu1))
	for donnee in cur :
		print(
		"\nListe info : \nNom :", donnee[1], donnee[2],
		"\npuissance :", donnee[3],
		"\nconso : " + str(donnee[4]) + "l/100km\nreserv : " + str(donnee[5]) + "l\
		\nautonomie : " + str(donnee[6]) + "km\nprix : " + str(donnee[7]) + "€\nnotePerso :", str(donnee[8]),
		"\nnoteTotale : " + str(donnee[9])
		)
	menu2 = input("\nVoulez-vous la modifier? ")
	if menu2 == "oui" :
		modMoto(cur, menu1)

def delMoto(cur):
	menu1 = choiceMoto(cur)
	menu2 = input("Voulez-vous VRAIMENT la supprimer? ")
	if menu2 == "oui" :
		cmd = "DELETE FROM Motos WHERE id = " + menu1
		cur.execute(cmd)
		print("Moto supprimée")

def bestMoto(cur):
    cur.execute("SELECT marque, modele FROM motos WHERE noteTotale = (SELECT MAX(noteTotale) FROM motos)")
    print(cur.fetchall())

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
		choiceMoto(cur)
		db.commit()
	if choix == "3" :
		delMoto(cur)
		db.commit()
	if choix == "4" :
		bestMoto(cur)

db.commit()
db.close()