import discord
from discord.ext import commands
bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
    print('Logged in as : ' + bot.user.name)
    print('---------------------------------------------------------------')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="aider des gens !"))

@bot.command()
async def salut(ctx):
    await ctx.send("Salut !")
    print('commande ".salut" utilisée')
    print('---------------------------------------------------------------')


@bot.command()
async def aide(ctx):
    await ctx.send("voici la liste de mes commandes :")
    await ctx.send(".salut")
    await ctx.send(".aide")
    await ctx.send(".invitation")
    await ctx.send(".créateur")
    await ctx.send(".jeu   (en cours de développement donc indisponible)")
    await ctx.send(".présentation")
    await ctx.send(".nouvellevidéo [nom yt] [liens de la vidéo]")
    await ctx.send(".dire [ce que le bot va dire]")
    print('commande ".aide" utilisée')
    print('---------------------------------------------------------------')

@bot.command()
async def dankbroom(ctx):
    await ctx.send("Envoi ce message à @DankBroomy#1156 pour tenter de gagner une nitro : 'j'ai mangé une nitro au lieu de ma banane' (oui le dev c'est bien amusé)")
    print('commande ".dankbroom" utilisée')
    print('---------------------------------------------------------------')

@bot.command()
async def invitation(ctx):
    await ctx.send("https://discord.gg/PpqUYPUbKs")
    print('commande ".invitation" utilisée')
    print('---------------------------------------------------------------')

@bot.command()
async def créateur(ctx):
    await ctx.send("J'ai été créé par @DankBroomy#1156")
    await ctx.send("Son serveur discord : https://discord.gg/2HUjpM8Axk")
    print('commande ".créateur" utilisée')
    print('---------------------------------------------------------------')

@bot.command()
async def jeu(ctx):
    await ctx.send("en développement...")
    print('commande ".jeu" utilisée')
    print('---------------------------------------------------------------')

@bot.command()
async def présentation(ctx):
    await ctx.send("coucou je suis un bot créé par DankBroomy#1156 (il faut bien qu'il face sa pub) pour Theomaestro#6901.")
    await ctx.send("Je suis en cours de développement donc venez ici pour proposer des commandes : https://discord.gg/32EVq7DEmA")
    await ctx.send("Aussi je contient 1 easter egg ! trouvez le et vous gagnerez peut-être un discord nitro !")
    print('commande ".présentation" utilisée')
    print('---------------------------------------------------------------')

@bot.command()
async def mainte(ctx):
    await ctx.send("```maintenance en cours vous ne pourrez plus m'utiliser```")
    print('commande ".mainte" utilisée')
    print('---------------------------------------------------------------')

@bot.command()
async def nouvellevidéo(ctx, link1, link2):
    await ctx.send("Regardez ça ! " + link1 + " viens de mettre en ligne une vidéo ! Allez vite la voir : " + link2)
    print('commande ".nouvellevidéo" utilisée avec les arguments ' + link1 + ' et ' + link2)
    print('---------------------------------------------------------------')

@bot.command()
async def dire(ctx, *link):
    await ctx.send(" ".join(link))
    print('commande ".dire" utilisée')
    print('le BOT à dit : ' + " ".join(link))
    print('---------------------------------------------------------------')
    
bot.run('ODM3NTg3OTMwMjg5MTQzODA4.YIuujA.7kAab2ZeBe3VMJWw-FcTgVBZJZM')
