import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Ola Mundo!")

@client.event
async def on_message(message):
    """
    Comandos de anti-divulgação
    """
    if message.author == client.user:
        return
    
    if message.content.startswith("discord.gg/"):
        await message.delete()
        embed = discord.Embed(title="Divulgação", color=0x00ff00)
        embed.add_field(name=f"O Usuario {message.author} esta tentando divulgar.", value="anti-divulgação", inline=False) 
        await message.channel.send(embed=embed)

    if message.content.startswith("https://discord.gg/"):
        await message.delete()
        embed = discord.Embed(title="Divulgação", color=0x00ff00)
        embed.add_field(name=f"O Usuario {message.author} esta tentando divulgar.", value="anti-divulgação", inline=False) 
        await message.channel.send(embed=embed)

@client.event
async def on_member_join(member):
    embed = discord.Embed(title="WELCOME", color=0x00ff00)
    embed.add_field(name="Welcome", value=f"{member} Seja bem vindo(a).", inline=False) 
    await client.get_channel(691716926329847940).send(embed=embed)
