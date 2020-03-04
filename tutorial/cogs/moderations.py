import discord
from discord.ext import commands

class Moderations(commands.Cog):

    def __init__(self, client):
        self.client = client

    """
    Clears any messages in the channel.  By default, clears the command and
    last 5 messages.  Can also specify how many messages to clear with a value, which
    will also clear the command.

    Usage = .clear [amount of messages deleted]
    """
    @commands.command(aliases=['Purge', 'purge', 'Clear', 'nuke', 'Nuke', 'clean', 'Clean'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'I cleared {amount} messages.  Yay me!', delete_after=5)


    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(colour=discord.Colour(13632027), description='You must specify how many messages you want to clear.')
            embed.set_author(name="Error", icon_url="https://i.imgur.com/ty7SEua.png")
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(colour=discord.Colour(13632027), description='You must have the ``Manage Messages`` permission enabled to use this command.\nIf you believe this is an error, please contact <@221070014252449792>')
            embed.set_author(name="Error", icon_url="https://i.imgur.com/ty7SEua.png")
            await ctx.send(embed=embed)

    """
    Kicks the user from the server.  User is able to join back in with an invite link.

    Usage= *kick {@member} [reason]
    """
    @commands.command(aliases=['boot', 'Boot', 'Kick'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(colour=discord.Colour(13632027), description=f'{ctx.author.mention} kicked {member.mention}.  Reason= {reason}.')
        embed.set_author(name="Member got kicked", icon_url="https://i.imgur.com/ymUbrYR.png")
        await ctx.send(embed=embed)

    """
    Mentions the author and asks if he typed something wrong if an error pops up while trying to kick someone
    """
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(colour=discord.Colour(13632027), description=f"{ctx.author.mention} what are you trying to do?  That user isn't on this server.  Did you make a typo?")
            embed.set_author(name="Error", icon_url="https://i.imgur.com/ty7SEua.png")
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(colour=discord.Colour(13632027), description='You must specify which member to kick by mentioning them')
            embed.set_author(name="Error", icon_url="https://i.imgur.com/ty7SEua.png")
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(colour=discord.Colour(13632027), description='You must have the ``Kick Members`` permission enabled to use this command.\nIf you believe this is an error, please contact <@221070014252449792>')
            embed.set_author(name="Error", icon_url="https://i.imgur.com/ty7SEua.png")
            await ctx.send(embed=embed)

    """
    Bans the user from joining the server again.  Will have to manually unban the user to allow him back in.

    Usage = *ban {@name} [reason]
    """
    @commands.command(aliases=['Ban', 'remove', 'Remove'])
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.channel.purge(limit=1)
        embed = discord.Embed(colour=discord.Colour(13632027), description=f'{ctx.author.mention} banned {member.mention}.  Reason= {reason}.')
        embed.set_author(name="Member got banned", icon_url="https://i.imgur.com/6m30yLY.png")
        await ctx.send(embed=embed)

    """
    Mentions the author and asks if he typed something wrong if an error pops up while trying to ban someone
    """
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(colour=discord.Colour(13632027), description=f"{ctx.author.mention} what are you trying to do?  That user isn't on this server.  Did you make a typo?")
            embed.set_author(name="Error", icon_url="https://i.imgur.com/ty7SEua.png")
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(colour=discord.Colour(13632027), description='You must specify which member to ban by mentioning them')
            embed.set_author(name="Error", icon_url="https://i.imgur.com/ty7SEua.png")
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(colour=discord.Colour(13632027), description='You must have the ``Ban Members`` permission enabled to use this command.\nIf you believe this is an error, please contact <@221070014252449792>')
            embed.set_author(name="Error", icon_url="https://i.imgur.com/ty7SEua.png")
            await ctx.send(embed=embed)

    """
    Unbans the user, allowing the user to join back into the server.

    Usage = *unban {name#discriminator} NOTE! You can NOT @ the user, you have to type his name, followed with # then theyr discriminator.  Example: .unban OrionAF#6982
    """
    @commands.command(aliases=['Unban'])
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.channel.purge(limit=1)
                embed = discord.Embed(colour=discord.Colour(1080748), description=f'{ctx.author.mention} unbanned {user.mention}')
                embed.set_author(name="Member got unbanned", icon_url="https://i.imgur.com/MVB7WEU.png")
                await ctx.send(embed=embed)
                return

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(colour=discord.Colour(13632027), description='You must have the ``Ban Members`` permission enabled to use this command.\nIf you believe this is an error, please contact <@221070014252449792>')
            embed.set_author(name="Error", icon_url="https://i.imgur.com/ty7SEua.png")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Moderations(client))
