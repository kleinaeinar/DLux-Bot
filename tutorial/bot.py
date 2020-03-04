import discord, datetime, time
import json
import os
from discord.ext import commands, tasks
from itertools import cycle
import asyncio
import datetime as DT
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('BOT_TOKEN')
start_time = time.time()
time_date_now = DT.datetime.now().strftime('Date: %d-%m-%Y\nTime: %H:%M:%S')

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

"""
Link to youtube tutorials; https://www.youtube.com/channel/UCR-zOCvDCayyYy1flR5qaAg
Link to discord.py doc; https://discordpy.readthedocs.io/en/latest/index.html
Link to discord dev portal; https://discordapp.com/developers/applications
Link to learn more python; https://realpython.com/
"""

"""
Default prefix is '*'
"""
client = commands.Bot(command_prefix = get_prefix)
client.remove_command('help')
version = '0.0.4'

@client.event
async def on_ready():
    change_status.start()
    print('/-/-/-/-/-/-/-/-/-/-/-/-/-/')
    print(time_date_now)
    print('Created by #OrionAF#6983')
    print(f'Running on version: {version}')
    print('Bot is ready to RUMBLE!')
    print('---------------------------')

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '*'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(activity=discord.Game(f'Ping: {round(client.latency * 1000)}ms'))
    print(time_date_now)
    print(f'Ping: {round(client.latency * 1000)}ms\n---------------------------')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'The extension ``{extension}`` has been loaded successfully.')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'The extension ``{extension}`` has been unloaded successfully.')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'The extension ``{extension}`` has been reloaded successfully.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


def owner(ctx):
    return ctx.author.id == 221070014252449792

@client.command()
@commands.check(owner)
async def shutdown(ctx):
    print('Bot has been shutdown successfully.')
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    embed = discord.Embed(colour=discord.Colour(1080748), description=f'{ctx.author.mention} told me to go to sleep.  **Apparently** bots need to sleep as well.\n Oh well, nap time.')
    embed.add_field(name="Uptime before shutdown: ", value=text)
    try:
        await ctx.send(embed=embed)
    except discord.HTTPException:
        await ctx.send("Uptime before shutdown: ")
    await ctx.bot.close()

@client.command(aliases=['prefix'])
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send(f'My prefix has been changed to: ``{prefix}``')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'That is an invalid command.')

client.run(token)
