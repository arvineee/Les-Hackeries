import os
import subprocess
#os.system("python -m pip install --upgrade pip")

commandinstall = f"ln -s {os.path.abspath(__file__)} ~/Bureau/"


os.system(commandinstall)


