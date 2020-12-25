import os
from shutil import copyfile

nomEmplacementSauvegarde = ".pyw files"
if not os.path.exists(nomEmplacementSauvegarde):
	os.makedirs(nomEmplacementSauvegarde)
	
username = os.getlogin()

listesFichiersPy = [fic for fic in os.listdir(os.getcwd()) if fic[-2:] == "py" and fic != "__py_to_pyw.py"]
for ficpy in listesFichiersPy:
	
	namee = ficpy.split('.')[-2]
	destination = nomEmplacementSauvegarde + "/" + namee + ".pyw"
	
	copyfile(ficpy,destination)
	copyfile(ficpy,f"C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/{ficpy}")
	print(f" * copy {ficpy} ")
	

## commande pour envoyer le bail dans demmarrage
