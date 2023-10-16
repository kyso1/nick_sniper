import json
import platform
import os
import requests
from lcu_driver import Connector
from time import sleep
from bs4 import BeautifulSoup
import webbrowser
import pygame

pygame.init()
notification_sound = pygame.mixer.Sound('notification_sound.mp3')
def notify():
    pygame.mixer.Sound.play(notification_sound)

def clean():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clean()

with open('config.json', 'r') as file:
    config = json.load(file)    
credentials = config['account']['credentials']

connector = Connector()
@connector.ready

async def connect(connection):
    counter = 1
    print("=============================================================")
    print("\nNick Sniper its ready!")
    print("Any doubt, discord: @agonised!")
    print("\n=============================================================")
    print("\nRegion to Snipe(lowercase ex.: euw,na,etc.): ")
    region = input()
    print("\nNick to snipe: ")
    nick = input()
    r = requests.get('https://lols.gg/en/name/checker/'+region+'/'+nick+'/')
    if(r.status_code==200):
       soup = BeautifulSoup(r.content, 'html.parser')
       elements = soup.find_all("h4",class_='text-center')
       for element in elements:
              print('\n',element.text)
    else:
       print(r.status_code)
    
    while True:
        sleep(4.5)
        changename = await connection.request('get', "/lol-summoner/v1/check-name-availability/" + nick)
        changename = await changename.json()
        print("Try", counter , nick,  changename, "(Ctrl+C to stop)")
        counter += 1
        if changename == True:
            notify()
            print("Nick live after ",counter," tries! Attempting to change the nick to: ",nick)
            print("Redirecting you to payment...")
            notify()
            url = 'https://v1.giftsender.lol/?tipo=NICK&smode=nick'
            webbrowser.open_new_tab(url)
            r = requests.post(url)
            exit(0)
connector.start()
