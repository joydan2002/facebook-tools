import requests
import re
import random
import os
from os import system as automation
from datetime import datetime

banner = """ _____ _           _   ___ ____    _____ ____
|  ___(_)_ __   __| | |_ _|  _ \  |  ___| __ )
| |_  | | '_ \ / _` |  | || | | | | |_  |  _ \

|  _| | | | | | (_| |  | || |_| | |  _| | |_) |
|_|   |_|_| |_|\__,_| |___|____/  |_|   |____/\n"""

def clear():
    automation('clear' if 'linux' in __import__('sys').platform.lower() else 'cls')
    
def exit_code():
    __import__('sys').exit()

def success_dump(limit):
    print(f"Berhasil dump {limit} ID")

def process_dump():
    print("Sedang dump ID, Tunggu sesaat karena cukup lama")

def menu():
    print(banner)
    print("1. Find ID/username Facebook")
    print("2. Dump ID Facebook")
    pilihan = input("Pilih menu : ")
    
    if pilihan == "1":
        user = input("Input Username or ID : ")
        find(user)
        exit_code()
    elif pilihan == "2":
        dump()
    else:
        print("Pilihan tidak valid")

def dump():
    data = []
    limit = int(input("Masukan limit dump: "))
    while len(data) < limit:
        user = "1000"
        user += str(random.randint(11111111111, 99999999999))
        try:
            getData = requests.get("https://www.facebook.com/"+user)
            name = re.search('<title>(.*?)</title>', str(getData.text)).group(1)
            id = re.search('fb://profile/(.*?)"', str(getData.text)).group(1)
            clear()
            process_dump()
            print("\r• {} {} ".format(len(data), id), end = "", flush = True)
            data.append("{}|{}".format(id, name))
        except AttributeError:
            pass
        except requests.exceptions.ConnectionError:
        	print("• Koneksi Jaringan Bermasalah")
        exit_code()
    print("\n")
    print("Ressult ID :\n%s\n" % data)
    success_dump(limit)
    save_to_file(data)
        
import os

def save_to_file(data):
    now = datetime.now()
    timestamp = now.strftime("%d-%m-%Y")
    file_name = f"Result/Dump_{timestamp}.txt"
    
    # Membuat direktori "Result" jika belum ada
    if not os.path.exists("Result"):
        os.makedirs("Result")
    
    with open(file_name, "w") as f:
        for item in data:
            f.write("%s\n" % item)
    
    print(f"Hasil dump telah disimpan di file:\n• {file_name}")
    exit_code()


def find(user):
    try:
        getData = requests.get("https://www.facebook.com/"+user)
        name = re.search('<title>(.*?)</title>', str(getData.text)).group(1)
        id = re.search('fb://profile/(.*?)"', str(getData.text)).group(1)

        print("• Nama: " + name)
        print("• ID: " + id)

    except requests.exceptions.ConnectionError:
        print("• Koneksi Jaringan Bermasalah")

    except AttributeError as e:
        print("• ", str(e))

clear()
while True:
    menu()
