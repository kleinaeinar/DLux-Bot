import discord
from discord.ext import commands

class Test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Test'])
    async def test(self, ctx):
        await ctx.send('Test')

def setup(client):
    client.add_cog(Test(client))
