import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} çevrimiçi!")
    await bot.change_presence(activity=discord.Game(name="!yardım ile komutları öğren"))

# Çevre kirliliği türleri komutu
@bot.command()
async def kirlilik(ctx):
    mesaj = (
        "**Çevre Kirliliği Türleri:**\n"
        "- 🌫️ Hava kirliliği\n"
        "- 💧 Su kirliliği\n"
        "- 🌱 Toprak kirliliği\n"
        "- 🔊 Gürültü kirliliği\n"
        "- 💡 Işık kirliliği"
    )
    await ctx.send(mesaj)
@bot.command()
async def öneri(ctx):
    mesaj = (
        "**Çevreyi Koruma Önerileri:**\n"
        "- 🌿 Enerji tasarruflu ürünler kullanın.\n"
        "- ♻️ Geri dönüşüme önem verin.\n"
        "- 🚲 Daha fazla bisiklet kullanın veya yürüyün.\n"
        "- 🛍️ Tek kullanımlık plastiklerden kaçının.\n"
        "- 🌳 Ağaç dikin ve yeşil alanları koruyun."
    )
    await ctx.send(mesaj)
@bot.command()
async def yardım(ctx):
    mesaj = (
        "**Kullanılabilir Komutlar:**\n"
        "- `!kirlilik`: Çevre kirliliği türleri hakkında bilgi verir.\n"
        "- `!öneri`: Çevreyi koruma önerilerini paylaşır.\n"
        "- `!yardım`: Komut listesini gösterir."
    )
    await ctx.send(mesaj)

TOKEN = "BOT_TOKENİNİZİ_BURAYA_YAPIŞTIRIN"
bot.run(TOKEN)
