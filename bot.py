mport discord,asyncio,youtube_dl
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()




def get_prefix(bot, msg):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    prefixes = [';'] #Your bot prefix(s)

    return commands.when_mentioned_or(*prefixes)(bot, msg)

bot=commands.Bot(command_prefix=get_prefix,description='Team Inea')




exts=['music'] #Add your Cog extensions here


@bot.event
async def on_ready():
    song_name='TWICE - What is love?' 
    await client.change_presence(status=discord.Status.online)
    await client.change_presence(activity=discord.Game(name=";도움 | Team Inea"))
    print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)






for i in exts:
    bot.load_extension(i)


bot.run(os.environ['TOKEN'])
