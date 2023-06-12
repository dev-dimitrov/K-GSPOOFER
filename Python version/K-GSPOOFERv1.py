# Made by Kaizen
# Do NOT sell this >:(
# Feel free to modify the code as u want
# I am a newbie in python so the code is not entirely "opmitized". It works and that's enough xD
# SPECIAL THANKS TO: N0rmie and M <3

import secrets
import os
import time
import winreg
import ctypes
import logging
import colorama
import datetime

class bcolors:
    end = '\033[0m'        # end
    red = '\033[31m'      	# red
    green = '\033[32m'     # green
    blue ='\033[34m'      	# blue


run = 1
while run == 1:
    colorama.init()
    os.system("cls")
    guion = "-"

    if not ctypes.windll.shell32.IsUserAnAdmin():
        print(bcolors.red+"Oops... Need to run as Administrator!"+bcolors.end)
        time.sleep(2)
        print(bcolors.blue+"Closing..."+bcolors.end)
        time.sleep(1)

        run += 1
    elif ctypes.windll.shell32.IsUserAnAdmin():

        
        
        print(bcolors.red+'''
                                                                                                
                                                                                                
                                  .g8"""bgd `7MMF'   `7MF'`7MMF'`7MM"""Yb.                      
                                .dP'     `M   MM       M    MM    MM    `Yb.                    
                                dM'       `   MM       M    MM    MM     `Mb                    
                                MM            MM       M    MM    MM      MM                    
                                MM.    `7MMF' MM       M    MM    MM     ,MP                    
                                `Mb.     MM   YM.     ,M    MM    MM    ,dP'                    
                                  `"bmmmdPY    `bmmmmd"'  .JMML..JMMmmmdP'                      
                                
                 .M"""bgd `7MM"""Mq.   .g8""8q.     .g8""8q. `7MM"""YMM `7MM"""YMM  `7MM"""Mq.  
                ,MI    "Y   MM   `MM..dP'    `YM. .dP'    `YM. MM    `7   MM    `7    MM   `MM. 
                `MMb.       MM   ,M9 dM'      `MM dM'      `MM MM   d     MM   d      MM   ,M9  
                  `YMMNq.   MMmmdM9  MM        MM MM        MM MM""MM     MMmmMM      MMmmdM9   
                .     `MM   MM       MM.      ,MP MM.      ,MP MM   Y     MM   Y  ,   MM  YM.   
                Mb     dM   MM       `Mb.    ,dP' `Mb.    ,dP' MM         MM     ,M   MM   `Mb. 
                P"Ybmmd"  .JMML.       `"bmmd"'     `"bmmd"' .JMML.     .JMMmmmmMMM .JMML. .JMM.'''+bcolors.end)
        print(bcolors.blue+"                                                                                      By Kaizen"+bcolors.end)

        print(bcolors.blue+"                                 Reactivate your free trials of many programs.")
        print("                              Use this ONLY for educatonial and ethical purposes!!"+bcolors.end)
        time.sleep(1.1)
        

        #Generating HwProfileGuid strings
        #String1:
        hex1 = secrets.token_hex(4)

        #String2:
        hex2 = secrets.token_hex(2)
            
        #String3:
        hex3 = secrets.token_hex(2)

        #String4:
        hex4 = secrets.token_hex(2)

        #String5:
        hex5 = secrets.token_hex(6)

        #Generating MachineGuid strings
        #String1:
        hex6 = secrets.token_hex(4)

        #String2:
        hex7 = secrets.token_hex(2)
            
        #String3:
        hex8 = secrets.token_hex(2)

        #String4:
        hex9 = secrets.token_hex(2)

        #String5:
        hex10 = secrets.token_hex(6)

        strings = hex1,hex2,hex3,hex4,hex5
        hwid = guion.join(strings)
        newhwid = "{"+hwid+"}" # New HwProfileGuid
        
        strings2 = hex6,hex7,hex8,hex9,hex10
        newmachine = guion.join(strings2) # New MachineGuid

        if strings == strings2:
            print("A strange error happened here xD")
            print("Please re-open the program")
            time.sleep(1)
            run +=1
            exit()

        print(bcolors.red+"\nDo you want to spoof your Guid and Hwid system?[Y/n]: "+bcolors.end,end="")
        print(bcolors.blue,end="")
        spoofmenu = input()
        bcolors.end
        if spoofmenu.lower() == "y":
            time.sleep(0.3)

            #Reading reg old values
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,"SOFTWARE\Microsoft\Cryptography", 0, winreg.KEY_READ)
            oldmachineguid, x = winreg.QueryValueEx(key, "MachineGuid") # 2 variables bc the fuction winreg outputs 2 types of values
            print(bcolors.red+"\nOld MachineGuid: "+bcolors.end,end="")
            print(bcolors.blue+oldmachineguid+bcolors.end)

            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\\0001",0, winreg.KEY_READ)
            oldhwprofileguid, x = winreg.QueryValueEx(key, "HwprofileGuid")

            print(bcolors.red+"Old HwProfileGuid: "+bcolors.end,end="")
            print(bcolors.blue+oldhwprofileguid+bcolors.end)
            time.sleep(1)
            print(bcolors.blue+"\nSpoofing, wait a sec",end="",flush=True)   
            time.sleep(0.8)
            print(".",end="",flush=True)
            time.sleep(0.8)
            print(".",end="",flush=True)
            time.sleep(0.8)
            print("."+bcolors.end,flush=True)                

            # Logs config
            actualhour = datetime.datetime.now()
            hour = actualhour.strftime('[%Y-%m-%d %H:%M:%S]')

            logging.basicConfig(filename='C:\KAIZEN-SPOOFER-LOGS.txt', level=logging.DEBUG, format=hour+'~[KAIZEN]:%(message)s')
            logging.info("Old MachineGuid: "+oldmachineguid)
            logging.info("Old HwProfileGuid: "+oldhwprofileguid)
            logging.info("New MachineGuid: "+newmachine)
            logging.info("New HwProfileGuid: "+newhwid)
            logging.info("===========================================================")

            # Modifying regedit values
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,"SOFTWARE\Microsoft\Cryptography", 0, winreg.KEY_WRITE)

            mguid = "MachineGuid"
            winreg.SetValueEx(key,mguid,0,winreg.REG_SZ,newmachine) #Setting new MachineGuid value
            winreg.CloseKey(key)

            key2 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\\0001",0, winreg.KEY_WRITE)
            hguid = "HwProfileGuid"
            winreg.SetValueEx(key2,hguid,0,winreg.REG_SZ,newhwid) #Setting new HwProfileGuid value
            winreg.CloseKey(key2)

            print(bcolors.green+"\nSpoof completed!"+bcolors.end)
            print(bcolors.red+"You can see the changed values in: "+bcolors.end+bcolors.blue+"C:\\KAIZEN-SPOOFER-LOGS.txt"+bcolors.end)
            print(bcolors.red+"New MachineGuid: "+bcolors.end,end="")
            print(bcolors.blue+newmachine+bcolors.end)
            print(bcolors.red+"New HwprofileGuid: "+bcolors.end,end="")
            print(bcolors.blue+newhwid+bcolors.end)
        
        elif spoofmenu.lower() == "n":
            print(bcolors.blue+"Closing..."+bcolors.end)
            time.sleep(1)
            run +=1
            os.system("cls")
            exit()

        print(bcolors.red+"\nDo you want to close the Spoofer?[Y/n]: "+bcolors.end,end="")
        print(bcolors.blue,end="")
        menu1 = input()
        bcolors.end
        if menu1.lower() == "n":
            print(bcolors.blue+"Re-opening the program..."+bcolors.end)
            time.sleep(1)
            run = 1
        elif menu1.lower()== "y":
            print(bcolors.blue+"\nThanks for chosing me <3")
            time.sleep(1)
            print("Closing..."+bcolors.end)
            time.sleep(0.6)
            os.system("cls")
            run += 1
 
    




























