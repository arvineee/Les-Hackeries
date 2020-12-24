import os
import subprocess
os.system("python -m pip install --upgrade pip")

commandinstall = "pip install "


listes = ["pynput","pyautogui","smtplib","email"]

for mod in listes:
	os.system(commandinstall + mod)
