import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix='/', intents=intents)

TOKEN = #Your TOKEN

@bot.event
async def on_ready():
    print("Bot is Online")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1295033059711783033)
    text = f"Welcome to the server, {member.mention}!"
    await channel.send(text)

    embed = discord.Embed(
            title='Welcome to the server!',
            description=f"{member.mention}, we're glad to have you here!",
            color=0x66FFFF
        )
    embed.add_field(name="Member Count", value=f"{member.guild.member_count}", inline=True)
    embed.set_thumbnail(url=member.avatar.url)
    embed.set_footer(text="Don't do anything bad and have fun!")
    await channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1295033059711783033)
    text = f"Goodbye, {member.name}. Hope to see you again! 😢"
    await channel.send(text)

@bot.event 
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content == 'Bot Creator contact':
        await message.channel.send("Hello, here is my Creator's contact.")
        
        embed = discord.Embed(
            title='Here is my contact',
            url="https://discordapp.com/users/600895386730758175",
            description="Feel free to reach out!",
            color=0x00ff00
        )
        await message.channel.send(embed=embed)

    await bot.process_commands(message)

bot.run(TOKEN)