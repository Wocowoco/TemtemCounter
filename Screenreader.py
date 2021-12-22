import pyautogui
import time



def CheckForEncounter(_temToHunt):
    _encounters = int(0)
    #Check for encounter - screen fades black
    if pyautogui.pixel(0,0) == (0,0,0):
        #print("Blackscreen detected")
        time.sleep(2)
        #Check if entering or exiting combat
        if pyautogui.pixel(1770,30) != (60,232,234): #If minimap color can be seen, out of combat
            #print("Going in combat")
            time.sleep(6.8) #If entering combat, wait 10 seconds for names to show up and read names
            
            #Check for correct Temtem (left spot)
            if pyautogui.locateOnScreen("names/"+_temToHunt+".png", confidence=0.9, region=(1150,20,350,60)) != None:
                print("A "+ _temToHunt.title() + " was found!")
                _encounters += 1

            #Check for correct Temtem (right spot / single battle)
            if pyautogui.locateOnScreen("names/"+_temToHunt+".png", confidence=0.9, region=(1500,60,350,60)) != None:
                print("A "+ _temToHunt.title() + " was found!")
                _encounters += 1

            return int(_encounters) #Return the amount of valid encounters
        else:
            #print("Going out of combat")
            return int(0) #No encounters can be found going out of combat
        
    return int(0) #If no blackscreen is found, return 0 encounters
