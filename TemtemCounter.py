import time
import pyautogui
from discordpresence import DiscordPresence
from Screenreader import CheckForEncounter
import webhook

_allNames = ["mosu"]
_isTemtemValid = False
_inCombat = True
_encounters = 0
_temToHunt = input("Enter the Temtem's name that you are hunting: ").lower()

#Check if Temtem is a valid Temtem
while _isTemtemValid == False:

    for name in _allNames:
        if _temToHunt == name:
            _isTemtemValid = True

    if _isTemtemValid == False:
        _temToHunt = input(_temToHunt + " is not a valid Temtem, please enter a valid one: ").lower()

#Ask for current streak
_input = input("Start fresh? (Y/N): ")
if _input.lower() == "n":
    _encounters = int(input("Enter your current encounters: "))

print("You are now hunting " + _temToHunt.title() + ". Good luck!")
print(" ")
#Set Discord Rich Presence to show that you're Luma Hunting
_startTime = time.time()
discPres = DiscordPresence()
discPres.update(_temToHunt, _encounters, _startTime)

#Check for encounters
while 1:
    _newEncounters = int(0)
    _newEncounters = CheckForEncounter(_temToHunt)
    if (_newEncounters > int(0)): #If more Tems are found, show total and update rich presence
        if _newEncounters == 1:
            print("A "+ _temToHunt.title() + " was found!") 
        if _newEncounters == 2:
            print("Two "+ _temToHunt.title() + " were found!")
        _encounters += _newEncounters
        
        #Report dry streaks (500 encounters)
        if _encounters % 500 == 0 and _encounters != 0:
            webhook.DryStreak(_encounters, _temToHunt)
        if _encounters % 500 == 1 and _encounters != 1:
            webhook.DryStreak((_encounters - 1), _temToHunt)
        print(str(_encounters%500) )   
        print("Total encounters: "+str(_encounters))
        discPres.update(_temToHunt, _encounters, _startTime)


        

