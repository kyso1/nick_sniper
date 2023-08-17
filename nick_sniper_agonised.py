import json 
from aiohttp import BodyPartReader
from lcu_driver import Connector
from time import sleep
connector = Connector()
@connector.ready

async def connect(connection):
    headers = {"Content-Type": "application/json"}
    nick = []
    counter = 1
    print("=============================================================")
    print("\nNick Sniper its ready!")
    print("Any doubt, discord: @agonised and twitter: @agxnia!")
    print("=============================================================")
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
                    if(blue_essences>=13900 or riot_points>=1300):     
                        print("Nick found and conditions met (RP or BE sufficients) ! Attempting to change the nick to:", nick)
                        print("Blue Essences:",blue_essences)
                        print("RP:",riot_points)
                        print("Input 1 to spent BE or 2 to spent RP")
                        op = input()
                        if(op=='1'):
                            response = await connection.request('post','/lol-summoner/v1/current-summoner/name', data=json.dumps({"name": nick}), headers = headers)
                            if(response.status==200):   
                                print("Total amount of BE:",blue_essences,".")
                                print("Nick changed successfully! 13900 BE Spent")
                                print("Blue essences after trade:",blue_essences-13900)
                            else:
                                print("[",response.status,"] Error code.")
                                print("Internal server error, please change the nick manually.")
                            print("\n")
                            input("Press Enter to end the program...")
                            exit(0)
                        elif(op=='2'):
                            response = await connection.request('post', '/lol-summoner/v1/current-summoner/name', data=json.dumps({"name": nick}),headers = headers)
                            if(response.status==200):   
                                print("Total amount of RP:",riot_points,".") 
                                print("Nick changed successfully! 1300 RP Spent")
                                print("Riot Points after trade:",riot_points-1300)
                            else:
                                print("[",response.status,"] Error code.")
                                print("Internal server error, please change the nick manually.")
                            print("\n")
                            input("Press Enter to end the program...")
                            exit(0)
                        else:
                            print("Unvalid option.")
                            exit(0)
                    else:      
                        print("Conditions not met to change the name. Missing BE, make sure you have 13900 BE to change the nick.")
                        print("Change your account and try again.")
                        print("\n")
                        input("Press Enter to end the program...")
                        exit(0)
connector.start()
