import json 
import psutil
from aiohttp import BodyPartReader
from lcu_driver import Connector
from time import sleep
connector = Connector()
@connector.ready

async def connect(connection):
    nick = []
    counter = 1
    print("\nNick Sniper its ready!")
    print("Any doubt, discord: @agonised and twitter: @agxnia!")
    print("Nick to snipe: ")
    nick = input()
    k = 0
    while True:
                sleep(4)
                changename = await connection.request('get', "/lol-summoner/v1/check-name-availability/" + nick)
                changename = await changename.json()
                print("Try", counter , nick,  changename, "(Ctrl+C to stop)")
                counter += 1
                #if the name is found, you can change your name with this code:
                if changename == True:
                    # Check for Essences and RP
                    essences_response = await connection.request('get', '/lol-inventory/v1/wallet/purchase-credits')                        
                    essences_data = await essences_response.json()
                    blue_essences = essences_data.get('lol_blue_essence')
                    riot_points = essences_data.get('RP')
                    if(blue_essences>=13900):     
                        print("Nick found and conditions met (RP or BE sufficients) ! Attempting to change the nick to:", nick)
                        response = await connection.request('put', '/lol-summoner/v1/current-summoner/name', data=json.dumps({"name": nick}))
                        print("Nick changed successfully! 13900 BE Spent")
                        print("\n")
                        input("Press Enter to end the program...")
                        exit(0)
                    elif(riot_points>=1300):
                        print("Nick found and conditions met (RP or BE sufficients) ! Attempting to change the nick to:", nick)
                        response = await connection.request('put', '/lol-summoner/v1/current-summoner/name', data=json.dumps({"name": nick}))
                        print("Nick changed successfully! 1300 RP Spent")
                        print("\n")
                        input("Press Enter to end the program...")
                        exit(0)
                    else:      
                        print("Conditions not met to change the name. Missing BE, make sure you have 13900 BE to change the nick.")
                        print("Change your account and try again.")
                        print("\n")
                        input("Press Enter to end the program...")
                        exit(0)
connector.start()
