import pyautogui
import time
import datetime
import os
import filecmp

from tkinter import *
from functools import partial
from tkinter import ttk

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
		
		
window = Tk()
window.title("SCREENEY")
window.geometry('300x150')

 #lbl = Label(window, text="Hello")
#lbl.grid(column=0, row=0)
labelChoix = Label(window, text = "Matières")
labelChoix.pack()
listeMatieres=["AlgoProc", "Proba","MesureIntegration","Optimisation"]
listeMatieres.sort()
listeCombo = ttk.Combobox(window,values=listeMatieres)
listeCombo.current(0)
listeCombo.pack()

c = 0
ancienphoto = ""
def clicked():
	global c,ancienphoto
	nomMatiere = listeCombo.get()
	nomEmplacementSauvegarde = "Screen Automatique - " + nomMatiere
	if not os.path.exists(nomEmplacementSauvegarde):
		os.makedirs(nomEmplacementSauvegarde)

	nomEmplacementSauvegarde += "/" + datetime.datetime.now().strftime('%Y-%m-%d')
	if not os.path.exists(nomEmplacementSauvegarde):
		os.makedirs(nomEmplacementSauvegarde)
	
	semblable = False
	
	
	myDatetime = datetime.datetime.now()
	nomFichier= myDatetime.strftime('%Y-%m-%d-' + nomMatiere + '-%H%M%S')
	photo = nomEmplacementSauvegarde + "/" + nomFichier + ".png"
	
	# prendre photo	
	pyautogui.screenshot(photo)
	print("#" + str(c) + "# " + photo)
	
	# pour les photo sauf la premiere
	if (c > 0):	
		# si photo semblable a lancienne photo alors suprr photo
		semblable = SemblableFichier(photo,ancienphoto)
		if semblable[0]:
			print(">>> PAREIL! "+str(semblable[1]) + " # " +photo+" VS "+ancienphoto)
			label.config(text="Image similaire ! Je cala pas")
			SupprimerFichier(photo)
		#sinon, si nouvelle photo
		else:
			label.config(text=photo.split('/')[-1])
			ancienphoto = photo
			c+= 1
	else:
		label.config(text=photo.split('/')[-1])
		ancienphoto = photo
		c+=1
	
	
	time.sleep(1)

btn = Button(window, text="Screen", command=clicked)
btn.pack()
label = Label(window, text = "")
label.pack()

window.mainloop()

