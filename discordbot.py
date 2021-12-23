import discord
import config
import zmq
import asyncio

client = discord.Client()
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    await SendMessage("Bot online")
    #Find the ID of the channel and server (guild) to post in
    #servers = client.guilds
    #for server in servers:
        #print(server.channels)
    
    ##Personal Temtem bot channel= 923317714481729646
    
async def SendMessage(message):
    channel = client.get_channel(923317714481729646)
    print("Message sent: " + str(message))
    await channel.send(str(message))


client.run(config.TOKEN)




