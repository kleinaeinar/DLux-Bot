import discord, datetime, time
from discord.ext import commands, tasks
from itertools import cycle
import datetime as DT
from datetime import time



class Information(commands.Cog):


    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['latency', 'lag', 'Lag', 'Latency', 'Ping'])
    async def ping(self, ctx):
        await ctx.send(f'This is the current ping to the bot: {round(self.client.latency * 1000)}ms')

    @commands.command()
    async def creator(self, ctx):
        embed = discord.Embed(colour=discord.Colour(1080748), description="I was created by OrionAF#6982 while he was self learning to make a discord bot with Python.  He started by following the guides from Lucas on Youtube.\nIf you would like to learn yourself, do ``*learn``")

        embed.set_author(name="How I was created", icon_url="https://i.imgur.com/R2G5wEZ.jpg")
        await ctx.send(embed=embed)

    @commands.command()
    async def learn(self, ctx):
        embed = discord.Embed(colour=discord.Colour(1080748), description="If you would like to learn how to make a discord bot, Lucas made a\n fantastic guide on Youtube.  Click the [link](https://www.youtube.com/channel/UCR-zOCvDCayyYy1flR5qaAg) to learn more")

        embed.set_author(name="Lucas's Youtube channel", icon_url="https://yt3.ggpht.com/a/AATXAJwiAcGLmb5c3NJNp-MfBusQlPB54IQ_n4rOcw=s288-c-k-c0xffffffff-no-rj-mo")
        await ctx.send(embed=embed)

    @commands.command(aliases=['v', 'V'])
    async def version(self, ctx):
        await ctx.send(f'``Bot is currently on version: 0.0.3``')

    @commands.command(aliases=['Info'])
    async def info(self, ctx, *, member: discord.Member):
        fmt = '{0} joined on {0.joined_at} and has {1} roles.'
        await ctx.send(fmt.format(member, len(member.roles)))

    @info.error
    async def infor_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You must specify which member you want information on.')

    @commands.command()
    async def pydoc(self, ctx):
        await ctx.send(f'Here you go, here is the link to the discord.py documentation.\nhttps://discordpy.readthedocs.io/en/latest/index.html')

    @commands.command(pass_context=True)
    async def help(self, ctx):
        author = ctx.message.author

        embed = discord.Embed(colour=discord.Colour(0x30a30f), description="Use this help section to learn more about the commands I have to offer.")

        embed.set_author(name='Your server prefix is: *', icon_url="https://i.imgur.com/9ptY0hp.png")
        embed.set_footer()

        embed.add_field(name="**Ping**", value="Tells you the bot's latency.\nAliases= ***ping***, ***Lag***, ***lag***, ***Latency*** and ***latency***")
        embed.add_field(name="**Creator**", value="Tells you some information about my creator")
        embed.add_field(name="**Learn**", value="Incase you want to learn how to make a discord bot yourself, this is where my\nmaster started.")
        embed.add_field(name="**Version**", value="Shows the current version of the bot\nAliases= ***v*** and ***V***")
        embed.add_field(name="**Info**", value="Shows some very small information about the mentioned user.\nAliases= ***Info***")
        embed.add_field(name="**8ball**", value="Very basic.  Just a magic 8ball.\nAliases= ***eightball***, ***8***, ***8b***, ***Eightball*** and ***8B***")
        embed.add_field(name="**Clear**", value="Clears any messages in a channel.  Must specify how many messages to delete.\nAliases= ***clear***, ***purge***, ***Purge***, ***nuke***, ***Nuke***, ***clean***, and ***Clean***")
        embed.add_field(name="**Kick**", value="Kicks the mentioned user from the server.\nAliases= ***kick***, ***boot*** and ***Boot***")
        embed.add_field(name="**Ban**", value="Bans the mentioned user from the server.\nAliases= ***ban***, ***remove*** and ***Remove***")
        embed.add_field(name="**Unban**", value="Unbans the user from the server. You can not @mention the user, you must type\nin the name, then the discriminator:'*'unban OrionAF#6982\nAliases= ***unban***")
        embed.set_footer(text=time_date_now)

        await author.send(embed=embed)

def setup(client):
    client.add_cog(Information(client))
