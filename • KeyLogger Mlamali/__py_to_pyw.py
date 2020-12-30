import os
from shutil import copyfile

nomEmplacementSauvegarde = ".pyw files"
if not os.path.exists(nomEmplacementSauvegarde):
	os.makedirs(nomEmplacementSauvegarde)
	
username = os.getlogin()

listesFichiersPy = [fic for fic in os.listdir(os.getcwd()) if fic[-2:] == "py" and fic != "__py_to_pyw.py"]
for ficpy in listesFichiersPy:
	
	namew = ficpy.split('.')[-2] + ".pyw"
	destination = nomEmplacementSauvegarde + "/" + namew
	
	copyfile(ficpy,destination)
	copyfile(destination,f"C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/{namew}")
	print(f" * copy {namew} ")
	

## commande pour envoyer le bail dans demmarrage
