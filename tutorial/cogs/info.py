import discord, datetime, time
from discord.ext import commands, tasks
from itertools import cycle
import datetime as DT
from datetime import time
import requests

class Information(commands.Cog):


    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['latency', 'lag', 'Lag', 'Latency', 'Ping'])
    async def ping(self, ctx):
        embed = discord.Embed(colour=discord.Colour(1080748), description=f'This is the current ping to the bot: {round(self.client.latency * 1000)}ms')
        embed.set_author(name='Ping', icon_url='https://i.imgur.com/xrMGaT8.png')
        await ctx.send(embed=embed)

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
        embed = discord.Embed(colour=discord.Colour(1080748), description=f'Bot is currently on version: 0.0.4')
        embed.set_author(name='DLux Bot Version', icon_url='https://i.imgur.com/rYL13Is.png')
        await ctx.send(embed=embed)

    @commands.command(aliases=['Info'])
    async def userinfo(self, ctx, *, user: discord.Member = None):
        """
        Get information about you, or a specified user.

        `user`: The user who you want information about. Can be an ID, mention or name.
        """

        if user is None:
            user = ctx.author

        embed = discord.Embed(colour=discord.Colour(1080748), description='test')
        embed.set_author(name=f"{user.name}'s Stats and Information.")
        embed.set_footer(text=f"ID: {user.id}")
        embed.set_thumbnail(url=user.avatar_url_as(format="png"))
        embed.add_field(name="__**General information:**__", value=f"**Discord Name:** {user}\n"
                                                                   f"**Account created:** {user.created_at.__format__('%A %d %B %Y at %H:%M')}\n"
                                                                   f"**Status:** {utils.user_status(user)}\n"
                                                                   f"**Activity:** {utils.user_activity(user)}", inline=False)
        embed.add_field(name="__**Server-related information:**__", value=f"**Nickname:** {user.nick}\n"
                                                                          f"**Joined server:** {user.joined_at.__format__('%A %d %B %Y at %H:%M')}\n"
                                                                          f"**Roles:** {' '.join([r.mention for r in user.roles[1:]])}")
        await ctx.send(embed=embed)

    #@userinfo.error
    #async def userinfo_error(self, ctx, error):
    #    if isinstance(error, commands.MissingRequiredArgument):
    #        embed = discord.Embed(colour=discord.Colour(1080748), description=f'You must specify which member you want information on.')
    #        embed.set_author(name='Error', icon_url='https://i.imgur.com/ty7SEua.png')
    #        await ctx.send(embed=embed)

    @commands.command()
    async def pydoc(self, ctx):
        embed = discord.Embed(colour=discord.Colour(1080748), description=f'Here you go, here is the link to the discord.py documentation.\nhttps://discordpy.readthedocs.io/en/latest/index.html')
        embed.set_author(name='Discord.py documentation', icon_url='https://cdn.discordapp.com/emojis/596577034537402378.png?v=1')
        await ctx.send(embed=embed)

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

    @commands.command()
    async def time(self, ctx):
        time_date_now = DT.datetime.now().strftime('%H:%M:%S')
        embed = discord.Embed(colour=discord.Colour(1080748), description=f'The current time in GMT is: {time_date_now}')
        embed.set_author(name='Time', icon_url='https://i.imgur.com/CYPtUD3.png')
        await ctx.send(embed=embed)




def setup(client):
    client.add_cog(Information(client))
