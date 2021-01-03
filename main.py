import discord
import os

#this is the prefix for the bot
PREFIX = '-'
client = discord.Client() #client is the connection to discord

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('b') or message.content.lower().startswith('p'):
        await message.channel.send(bify(message.content.lower()))

    #this is where the commands will be stored
    if message.content.lower().startswith(PREFIX):
        cmd = message.content.lower()[1:]

        if cmd.startswith('help'):
            help()

        if cmd.startswith('b'):
            await message.channel.send(bify(cmd[1:]))


#Takes message and changes the first letter of every word (if its a b or p) and changes them to :b:
def bify(message):
    if len(message) == 0:
        return "Please enter a message :b:!"
    newMessage = message.replace("b", ":b:")
    newMessage = newMessage.replace("p", ":b:")

    if ":b:" not in newMessage:
        newMessage += " :b:"
    return  newMessage

#explane the roles
def help():
    msg = " "


client.run(os.getenv('TOKEN'))