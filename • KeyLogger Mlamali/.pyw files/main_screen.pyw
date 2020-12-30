import os
import datetime
import time

from shutil import copyfile

username = os.getlogin()
nomFichierActuelle = os.path.basename(__file__)

# **** AU DEMARRAGE t
#copyfile(nomFichierActuelle,f"C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/{nomFichierActuelle}")

# **** EMPLACEMENT SAUVEGARDE
nomEmplacementSauvegarde = "C:/data_key_screen"
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

# **** YEAH PHOTOS DE LECRAN YEAH
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
    

	  

