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
                    essences_response = await connection.request('get', '/lol-store/v1/wallet/purchase-credits')
                    essences_data = await essences_response.json()
                    blue_essences = essences_data.get('balance')
                    rp_response = await connection.request('get', '/lol-store/v1/wallet/rp')
                    rp_data = await rp_response.json()
                    rp_balance = rp_data.get('rp')
                    try: 
                        print("Nick found and conditions met (RP or BE sufficients) ! Attempting to change the nick to:", nick)
                        response = await connection.request('post', '/lol-summoner/v1/current-summoner/name', data=json.dumps({"name": nick}), headers=headers)
                        print("Nick changed successfully!")
                        print("\n")
                        input("Press Enter to end the program...")
                        exit(0)
                    except:
                        print("Conditions not met to change the name. RP or BE missing.")
                        print("Change your account and try again.")
                        print("\n")
                        input("Press Enter to end the program...")
                        exit(0)
connector.start()