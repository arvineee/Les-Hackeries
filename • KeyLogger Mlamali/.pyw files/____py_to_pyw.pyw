import os,errno
from shutil import copyfile

nomEmplacementSauvegarde = ".pyw files"
if not os.path.exists(nomEmplacementSauvegarde):
	os.makedirs(nomEmplacementSauvegarde)

listesFichiersPy = [fic for fic in os.listdir(os.getcwd()) if fic[-2:] == "py" and fic != "____py_to_pyw.pyw"]
for ficpy in listesFichiersPy:
	print(ficpy)
	namee = ficpy.split('.')[-2]
	destination = nomEmplacementSauvegarde + "/" + namee + ".pyw"
	print(destination)
	copyfile(ficpy,destination)
