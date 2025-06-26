import os
import discord
from discord.ext import commands, tasks
from discord import app_commands
from dotenv import load_dotenv
import datetime

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

DAYS = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")
    try:
        synced = await bot.tree.sync(guild=discord.Object(id=GUILD_ID))
        print(f"Commandes slash synchronisées : {len(synced)}")
    except Exception as e:
        print(f"Erreur de sync : {e}")
    post_poll.start()

# Fonction utilitaire pour envoyer le sondage
async def send_poll():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        jours = ["Ce soir", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
        emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣"]

        poll_text = "**📅 Jour de la semaine pour le Ciné Guedin**\nVotez en réagissant !\n"
        for emoji, day in zip(emojis, jours):
            poll_text += f"{emoji} {day}\n"

        msg = await channel.send(poll_text)
        for emoji in emojis:
            await msg.add_reaction(emoji)

# Commande slash pour lancer le sondage manuellement
@bot.tree.command(name="cine", description="Lancer le sondage Ciné Guedin", guild=discord.Object(id=GUILD_ID))
async def cine(interaction: discord.Interaction):
    await send_poll()
    await interaction.response.send_message("Sondage lancé !", ephemeral=True)

# Tâche programmée chaque dimanche à 11h
@tasks.loop(minutes=1)
async def post_poll():
    now = datetime.datetime.now()
    if now.weekday() == 6 and now.hour == 11 and now.minute == 0:  # 6 = Dimanche
        await send_poll()

bot.run(TOKEN)
