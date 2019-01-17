import string
import sqlite3
from sqlite3 import Error

def strToList(string): 
	li = []
	for letter in string :
		li.append(letter)
	return li 

def isAlphabet(lettre):
	retour = []
	alpha = strToList(string.ascii_letters)
	craps = set(alpha)
	if lettre in craps:
		retour.append(lettre)
	return retour

def numOnly (string) :
	retour = ""
	for i in string :	
		if i.isdecimal() :
			retour += i
	return retour

def newMoto():
	marque = input("\nMarque? ")
	modele = input("Modèle? ")
	prix = input("Prix? ")
	notePerso= input("Note personnelle? /100 ")
	return marque, modele, prix, notePerso

def remplissage():
		# Opération sur la DB
		cur.execute("CREATE TABLE IF NOT EXISTS motos (id INTEGER PRIMARY KEY, marque TEXT, modele TEXT, prix INTEGER, notePerso INTEGER)")
		cur.execute("INSERT INTO motos (marque, modele, prix, notePerso) VALUES(?,?,?,?)",(newMoto()))
		db.commit()
	
def marqueMoto(ligne):
	moto = {}
	moto["Marque"], moto["Modèle"], moto["Prix"], moto["Note personnelle"] = ligne.split(";")
	return moto

def modMoto():
	a = 0

def viewMoto(cur) :
	print("Liste des motos :\n")
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
	menu2 = input("Voulez-vous la modifier? ")
	if menu2 == "oui" :
		a = 0

def delMoto():
	a = 0
def bestMoto():
	a = 0
#Définition Variable Globale

moto=""
menu = "x"

#Programme
print("\nBienvenue dans ce comparateur de moto!")
try:
    db = sqlite3.connect('data/moto.db')
    cur = db.cursor()
except Error as e:
    print(e)

while menu != "Q" :
	print("\nMenu :")
	print("1 = Ajouter une moto")
	print("2 = Afficher une moto")
	print("3 = Modifier une moto")
	print("4 = Supprimer une moto")
	print("5 = Afficher la meilleur moto")
	print("Q = Quitter le programme")
	menu = input("Que souhaitez-vous faire? ")


	if menu == "1" : 
		remplissage()
	if menu == "2" :
		viewMoto(cur)
	if menu == "3" :
		a = 3
	if menu == "4" :
		a = 4
	if menu == "5" :
		a = 5

db.commit()
db.close()