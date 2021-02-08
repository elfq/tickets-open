  
import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel
from core import *
from bot import *


class ThreadsAmtPlugin(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
      
    @commands.command(name="ticketsop", aliases=["ticketsopen"])
    async def threadsamt_(self, ctx):
      await ctx.send(f"There is currently **{len(self.bot.threads)}** threads open!")
      overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(connect=False)}
      voice_channel = await ctx.guild.create_voice_channel(f'Tickets Open: {len(self.bot.threads)}', overwrites=overwrites)
      voice_channel = 808347876492705812
    
    @commands.Cog.listener()
    async def on_thread_create(self, thread):
      channel = self.bot.get_channel(voice_channel.id)
      await channel.edit(name=len(self.bot.threads))
    

        
        
    

def setup(bot):
    bot.add_cog(ThreadsAmtPlugin(bot))
