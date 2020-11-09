import pyautogui
import time
import datetime
import os
import filecmp

nomMatiere = "AlgoProc"
nomEmplacementSauvegarde = "Screen Automatique - " + nomMatiere
delaiSec = 60*5
delaiSec = int(delaiSec)
if not os.path.exists(nomEmplacementSauvegarde):
	os.makedirs(nomEmplacementSauvegarde)

nomEmplacementSauvegarde += "/" + datetime.datetime.now().strftime('%Y-%m-%d')
if not os.path.exists(nomEmplacementSauvegarde):
	os.makedirs(nomEmplacementSauvegarde)	

#############################################################
def SemblableFichier(fic,fic2):
	a = os.path.getsize(fic)
	b = os.path.getsize(fic2)
	diff = abs(a - b)
	if (diff > 3000):
		return (False,diff)
	else:
		return (True,diff)
	
def SupprimerFichier(path):
	if os.path.exists(path):
		os.remove(path)
	else:
		print("Impossible de supprimer le fichier " + path +" car il n'existe pas")
#############################################################

semblable = False
c = 0
while c < 100:
	myDatetime = datetime.datetime.now()
	nomFichier= myDatetime.strftime('%Y-%m-%d-' + nomMatiere + '-%H%M%S-' + str(delaiSec))
	photo = nomEmplacementSauvegarde + "/" + nomFichier + ".png"
	
	if (c == 0):
		time.sleep(3)
		
	# prendre photo	
	pyautogui.screenshot(photo)
	print("#" + str(c) + "# " + photo)
	
	# pour les photo sauf la premiere
	if (c > 0):	
		# si photo semblable a lancienne photo alors suprr photo
		semblable = SemblableFichier(photo,ancienphoto)
		if semblable[0]:
			print(">>> PAREIL! "+str(semblable[1]) + " # " +photo+" VS "+ancienphoto)
			SupprimerFichier(photo)
		#sinon, si nouvelle photo
		else:
			ancienphoto = photo
			c+= 1
	else:
		ancienphoto = photo
		c+= 1
	
	time.sleep(delaiSec)
