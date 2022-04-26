import discord
from discord.ext import commands
import os

#import all of the cogs

from music_cog import music_cog

bot = commands.Bot(command_prefix='/')


bot.remove_command('help')



bot.add_cog(music_cog(bot))

bot.run(os.getenv("OTY4MjkwMjQ5OTkyMTkyMDEx.YmcskQ.rj6ltXz9XxiLTHU0ndiIU3ykMTY"))