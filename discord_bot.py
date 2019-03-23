# Discord bot gui
"""DISCONTINUED UNTIL FURTHER USE FOUND

Bot progress stopped because apparently shufflebot
can't take commands from another bot.
"""
from tkinter import *
from tkinter.ttk import *
import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content == "Testing":
        await client.send_message(message.channel, "Mic is on. Testing 1, 2, 3!")
    elif message.content == "Try shufflebot":
        await client.send_message(message.channel, "$help")

token = "NTU4OTU0NzU4OTIxMjU2OTYw.D3euNQ.elG13zgPdAulpr_gVW7qLhcA3gY"
client.run(token)