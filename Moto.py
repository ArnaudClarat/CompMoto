import string

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
	moto=""
	moto += input("\nMarque? ") + ";"
	moto += input("Modèle? ") + ";"
	moto += input("Prix? ") + ";"
	moto += input("Note personnelle? /100 ") + "\n"
	return moto
	
def marqueMoto(ligne):
	moto = {}
	moto["Marque"], moto["Modèle"], moto["Prix"], moto["Note personnelle"] = ligne.split(";")
	return moto

def selectMoto():
	menu = "a"
	i = 0
	print("\nListe Moto :")
	with open("motoDB.csv", "r") as dataBase :
		for moto in dataBase :
			dicoMoto = marqueMoto(moto)
			print(i, ":", dicoMoto["Marque"], dicoMoto["Modèle"])
			i += 1
		menu2 = input("Quelle moto voulez-vous choisir? ")
		try :
			test = int(menu2) or int(menu2) < 9
		except :
			menu2 = input("Veuillez saisir un numéro correct : ")
		print("\nListe Info :")
		dataBase.seek(0,int(menu2))
		selectMoto = ((dataBase.readline()[:-1]).split(";"))
		print(selectMoto)
		for i in selectMoto :
			print(i)
	return selectMoto

def modMoto():
	a = 0

def viewMoto():
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
		with open("motoDB.csv", "a") as dataBase :
			dataBase.write(newMoto())
	if menu == "2" :
		selectMoto()
		input("Appuyez sur entrée pour continuer")
	if menu == "3" :
		a = 3
	if menu == "4" :
		a = 4
	if menu == "5" :
		a = 5
