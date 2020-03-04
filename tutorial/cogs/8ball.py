import discord
import random
from discord.ext import commands

class _8ball(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball', '8', '8b', 'Eightball', '8B'])
    async def eightball(self, ctx, *, question):
        responses =['It is certain.',
                    'It is decidedly so.',
                    'Without a doubt.',
                    'Yes - definitely',
                    'You may rely on it.',
                    'As I see it, yes.',
                    'Most likely.',
                    'Outlook good',
                    'Yes.',
                    'Signs point to yes.',
                    'Reply hazy, try again.',
                    'Ask again later.',
                    'Better not tell you now.',
                    'Cannot predict now.',
                    'Concentrate and ask again',
                    "Don't count on it",
                    'My reply is no.',
                    'No.',
                    'My sources say no.',
                    'Outlook not so good',
                    'Very doubtful',
                    "I see something written in the stars....It's a yes!"]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

def setup(client):
    client.add_cog(_8ball(client))
