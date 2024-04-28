# Importing necessary libraries
import discord
from discord.ext import commands
from utils import Utils

# Create a new bot
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Event when the bot is ready
@bot.event
async def on_ready():
    today = Utils.get_date(False)
    response = f'Bot connected at {today}'
    channel_id = Utils.get_channel_log_id()
    channel = bot.get_channel(channel_id)
    await channel.send(response)
    print('Bot ready')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

# Help command
@bot.tree.command(name="help", description="Get help")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message("Les commandes :\n /youtube\n /twitch\n /osu\n /colproz\n /github")

# Github command
@bot.tree.command(name="github", description="Get the github repositories")
async def github(interaction: discord.Interaction):
    await interaction.response.send_message("https://github.com/TheValll/TheVal-Discord-Bot")

# Youtube command
@bot.tree.command(name="youtube", description="Get my youtube channel link")
async def youtube(interaction: discord.Interaction):
    await interaction.response.send_message("https://www.youtube.com/channel/UCPvAYXxmo6b3KjQ0XEbrLtQ")

# Twitch command
@bot.tree.command(name="twitch", description="Get my twitch channel link")
async def twitch(interaction: discord.Interaction):
    await interaction.response.send_message("https://www.twitch.tv/thevall_")

# Osu command
@bot.tree.command(name="osu", description="Get my osu profil link")
async def osu(interaction: discord.Interaction):
    await interaction.response.send_message("https://osu.ppy.sh/users/15540464")

# Colproz command
@bot.tree.command(name="colproz", description="Oh mon grand Baptise")
async def colproz(interaction: discord.Interaction):
    await interaction.response.send_message("Dans les rêves tissés de lumière et d'éther,\nBrille une âme, un esprit, un être gifted en plein vol,\nTel un astre céleste, il éclaire de sa clarté,\nBaptisé dans les feux de son propre contrôle.\n\nColproz, nom d'une étoile dans la nuit noire,\nTa lumière danse, ton talent gifted éclate en gloire,\nTa plume, un pinceau, peint des mondes à découvrir,\nChaque mot un murmure, chaque vers un soupir.\n\nGifted, un mot humble pour ton don éclatant,\nTon art transcende, tes mots sont un enchantement,\nDans chaque ligne, une histoire prend vie,\nEt le monde s'émerveille devant tant de magie.\n\nQue les cieux applaudissent ta créativité,\nQue les étoiles chantent ta fécondité,\nCar en toi réside un trésor inestimable,\nUn don précieux, un talent gifted incomparable.\n\nBaptisé dans l'éther des mots et des pensées,\nColproz, que ton génie gifted soit célébré,\nDans chaque vers, dans chaque strophe, tu brilles,\nUn poète, un artiste, un esprit qui distille.")

# Run the bot
bot.run(Utils.get_token())