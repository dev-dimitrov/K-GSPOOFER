# VER 2.0 UPDATED ON 01/2025
# Made by Kaizen
# Do NOT sell this >:(
# Feel free to modify the code as u want

# SPECIAL THANKS TO: N0rmie and D <3

import secrets, os, time, winreg, ctypes, logging, datetime
# from pathlib import Path
# from datetime import timedelta


class bcolors:
    end = '\033[0m'        # end
    red = '\033[31m'      	# red
    green = '\033[32m'     # green
    blue ='\033[34m'      	# blue

run = 1
while run == 1:
    os.system("cls")

    if not ctypes.windll.shell32.IsUserAnAdmin():
        print(bcolors.red+"Oops... Need to run as Administrator!"+bcolors.end)
        time.sleep(2)
        print(bcolors.blue+"Closing..."+bcolors.end)
        time.sleep(1)

        run += 1
    elif ctypes.windll.shell32.IsUserAnAdmin():
        
        # This function makes problems with antivirures bc is copying an executable into the Windows Startup programs. 
        # It will be added later when I find a solution for this xdd.
        #  def setUpChecker():
        #   exeDir = os.getcwd()
        #   os.system('xcopy "'+exeDir+'\\checker.exe"  "C:\\Users\\%UserProfile%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')

        def checkFirstTime():
            if not os.path.isfile("C:\KAIZEN-SPOOFER-LOGS.txt"):
                return True

        def makeID(a,b): # True stays for GUID, false for HWID 
            id = "{"
            for i in range(0, len(a)):
                if i != len(a)-1:
                    id += a[i]+"-"
                else:
                    id += a[i]
    
            if not b:
                return id+'}'
            else:
                id = id.replace('{','')
            return id

        def makeLog(oldmachineguid,oldhwprofileguid,newmachine,newhwid):
            actualhour = datetime.datetime.now()
            hour = actualhour.strftime('[%Y-%m-%d %H:%M:%S]')

            logging.basicConfig(filename='C:\KAIZEN-SPOOFER-LOGS.txt', level=logging.DEBUG, format=hour+'~[KAIZEN]:%(message)s')
            logging.info("Old MachineGuid: "+oldmachineguid)
            logging.info("Old HwProfileGuid: "+oldhwprofileguid)
            logging.info("New MachineGuid: "+newmachine)
            logging.info("New HwProfileGuid: "+newhwid)
            logging.info("===========================================================")
        
        def modifyMachine(a):
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,"SOFTWARE\Microsoft\Cryptography", 0, winreg.KEY_WRITE)
            mguid = "MachineGuid"
            winreg.SetValueEx(key,mguid,0,winreg.REG_SZ,a) #Setting new MachineGuid value
            winreg.CloseKey(key)

        def modifyHwid(a):
            key2 = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\\0001",0, winreg.KEY_WRITE)
            hguid = "HwProfileGuid"
            winreg.SetValueEx(key2,hguid,0,winreg.REG_SZ,a) #Setting new HwProfileGuid value
            winreg.CloseKey(key2)

        def readValues(a):
            if a: # True stays for machine and False for hwid
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,"SOFTWARE\Microsoft\Cryptography", 0, winreg.KEY_READ)
                oldmachineguid, x = winreg.QueryValueEx(key, "MachineGuid") # 2 variables bc the fuction winreg outputs 2 types of values
                return oldmachineguid
            else:
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\\0001",0, winreg.KEY_READ)
                oldhwprofileguid, x = winreg.QueryValueEx(key, "HwprofileGuid")
                return oldhwprofileguid
        
        if checkFirstTime():
            print(bcolors.red+"It looks like you are using this program for the first time. The spoofer makes changes into the Windows Registry.\nDo you want to make a BACKUP of your original registry values?[Y/n]: "+bcolors.end,end="")
            print(bcolors.blue,end="")
            spoofmenu = input()
            bcolors.end
            if spoofmenu.lower() == 'y':
                os.system('REG EXPORT "HKLM\\SYSTEM\\CurrentControlSet\\Control\\IDConfigDB\\Hardware Profiles\\0001" "C:\\ORIGINAL-HwProfileGuid.reg"')
                os.system('REG EXPORT "HKLM\\SOFTWARE\\Microsoft\\Cryptography" "C:\\ORIGINAL-MachineGuid.reg"')
                print(bcolors.green+'\nReady! You can find your backup files in "C:\\" '+bcolors.end)
                time.sleep(5)
            os.system('cls')

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
    
        print(bcolors.red+"\nDo you want to spoof your Guid and Hwid system?[Y/n]: "+bcolors.end,end="")
        print(bcolors.blue,end="")
        spoofmenu = input()
        bcolors.end
        if spoofmenu.lower() == "y":
            time.sleep(0.3)
            
            #Generating HwProfileGuid array
            hwProfileGuid = [secrets.token_hex(4),secrets.token_hex(2),
                        secrets.token_hex(2),secrets.token_hex(2),secrets.token_hex(6)]

            #Generating MachineGuid strings
            MachineGuid = [secrets.token_hex(4),secrets.token_hex(2),
                         secrets.token_hex(2),secrets.token_hex(2),secrets.token_hex(6)]

            # False stays for makin HWID, True for GUID
            newmachine = makeID(MachineGuid,True)
            newhwid = makeID(hwProfileGuid,False)


            if MachineGuid == hwProfileGuid:
                print("A strange error happened here xD")
                print("Please re-open the program")
                time.sleep(1)
                exit()

            # reading old values
            oldmachineguid = readValues(True)
            print(bcolors.red+"\nOld MachineGuid: "+bcolors.end,end="")
            print(bcolors.blue+oldmachineguid+bcolors.end)

            # reading old values
            oldhwprofileguid = readValues(False)
            print(bcolors.red+"Old HwProfileGuid: "+bcolors.end,end="")
            print(bcolors.blue+oldhwprofileguid+bcolors.end)     

            time.sleep(1)

            # Logs config
            makeLog(oldmachineguid,oldhwprofileguid,newmachine,newhwid)

            # Modifying regedit values
            modifyMachine(newmachine) 
            modifyHwid(newhwid)

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

        # Next feature to add:
        # print(bcolors.red+"Open the program after 15 days to re-spoof the system?[Y/n]: "+bcolors.end,end="")
        # print(bcolors.blue,end="")
        # spoofmenu = input() 
        # if spoofmenu.lower() == 'y':
        #    setUpChecker()

        print(bcolors.red+"\nDo you want to close the Spoofer?[Y/n]: "+bcolors.end,end="")
        print(bcolors.blue,end="")
        menu1 = input()
        bcolors.end
        if menu1.lower() == "n":
            print(bcolors.blue+"Re-opening the program..."+bcolors.end)
            time.sleep(1)
        elif menu1.lower()== "y":
            print(bcolors.blue+"Thanks for chosing me <3")
            print("Closing..."+bcolors.end)
            time.sleep(0.6)
            os.system("cls")
            run += 1
