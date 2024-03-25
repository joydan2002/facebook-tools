import requests, re, sys
from os import system as automation

baner = """ _____ _           _   ___ ____    _____ ____
|  ___(_)_ __   __| | |_ _|  _ \  |  ___| __ )
| |_  | | '_ \ / _` |  | || | | | | |_  |  _ \

|  _| | | | | | (_| |  | || |_| | |  _| | |_) |
|_|   |_|_| |_|\__,_| |___|____/  |_|   |____/\n"""

def clear():
	automation('clear' if 'linux' in sys.platform.lower() else 'cls')

def find(user):
    try:
        getData = requests.get("https://www.facebook.com/"+user)
        name = re.search('<title>(.*?)</title>', str(getData.text)).group(1)
        id = re.search('fb://profile/(.*?)"', str(getData.text)).group(1)

        print("• Nama: " + name)
        print("• ID: " + id)
        exit()

    except requests.exceptions.ConnectionError:
        exit("• Koneksi Jaringan Bermasalah")

    except AttributeError as e:
        exit("• ", str(e))

clear()
print(baner)
while True:
    user = input("• Input Username or ID : ")
    find(user)