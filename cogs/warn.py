import discord
from discord.ext import commands
doob_logo = "http://i.mmatt.pw/bz0i1U0V"

class warn(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Warns a user specified.
    @commands.command(aliases=['w'])
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, user: discord.Member, *, reason=None):
        embed = discord.Embed(title=f"<@{ctx.message.author.id}> has warned {user.name}", description=f"{user.name} has been warned.", colour=discord.Color.blue())

        embed.add_field(name="User Wanred:", value=f"@{user.name}#{user.discriminator}")
        embed.add_field(name="Reason", value=f"{reason}")

        embed.set_thumbnail(url=doob_logo)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(warn(client))