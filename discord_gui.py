# Discord shufflebot controller gui
from tkinter import *
from tkinter.ttk import *
import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import datetime

# client = discord.Client()

# email = input('email: ')
# password = input('password: ')

# @client.event
# async def on_ready():
#     for i in client.servers:
#         print(i.name)

class DiscordClient(discord.Client):
    def __init__(self, *args, **kwargs):
        discord.Client.__init__(self, **kwargs)

    @asyncio.coroutine
    def on_ready(self):
        servers = list(self.servers)
        for server in servers:
            if server.name == "Loegrath's Realm":
                break

        for channel in server.channels:
            if channel.name == 'music-bot-channel':
                break

        now = datetime.datetime.now()
        yield from self.send_message(channel, 'Api Success! at ' + str(now))
        yield from self.send_message(channel, "$help")
        print('Success!')
        yield from self.close()

if __name__ == '__main__':
    dc = DiscordClient()
    email = input('email : ')
    password = input('password : ')
    dc.run(email, password)

# client.run(email, password)