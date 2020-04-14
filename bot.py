# Doob
import discord
import json
import asyncio
import logging
import os

from discord.ext import commands

# Creates and loads the json file.
def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)

client.remove_command("help")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print(f'Loaded {extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print(f'Unloaded {extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

doob_logo = "http://i.mmatt.pw/bz0i1U0V"

client.run("token")
#hi mr jones lol
