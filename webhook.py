import requests
import json
import config

def LumaFound(_encounters, _temToHunt):
    data = {"content": "A Luma Temtem has been found by Woco!",
      "tts": "false",
      "embeds": [
        {
          "type": "rich",
          "title": "Luma "+ str(_temToHunt),
          "description": "",
          "color": 0x00FFFF,
          "fields": [
            {
              "name": "Encounters",
              "value": str(_encounters),
              "inline": "true"
            },
            {
              "name": "Luma Rate",
              "value": "1/3333 (3x)",
              "inline": "true"
            }
          ],
          "thumbnail": {"url": "https://static.wikia.nocookie.net/temtem_gamepedia_en/images/2/27/LumaMosu.png/revision/latest/scale-to-width-down/250?cb=20211216210530","height": 0,"width": 0
          }
        }]}
    request = requests.post(config.WEBHOOK, data=json.dumps(data), headers={'Content-Type':'application/json'})

def DryStreak(_encounters, _temToHunt):
    data = {"content": "Woco is on a dry streak...",
      "tts": "false",
      "embeds": [
        {
          "type": "rich",
          "title": "Trying for a Luma "+ str(_temToHunt),
          "description": "",
          "color": 0xFF6600,
          "fields": [
            {
              "name": "Encounters",
              "value": str(_encounters),
              "inline": "true"
            },
            {
              "name": "Luma Rate",
              "value": "1/3333 (3x)",
              "inline": "true"
            }
          ],
          "thumbnail": {"url": "https://static.wikia.nocookie.net/temtem_gamepedia_en/images/9/9e/Mosu.png/revision/latest/scale-to-width-down/250?cb=20211216202105","height": 0,"width": 0
          }
        }]}
    request = requests.post(config.WEBHOOK, data=json.dumps(data), headers={'Content-Type':'application/json'})
