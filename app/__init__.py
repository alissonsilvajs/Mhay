# coding=utf-8
import discord
from discord.utils import get
import random

client = discord.Client()

COR =0x690FC3
msg_id = None
msg_user = None

@client.event
async def on_ready():
    print(-==-=-=-=-=-=-=
    print("Bot habi")

@client.event
async def on_message(message):
    """
    Comandos de anti-divulgação
    """
    if message.author == client.user:
        return

    if message.content.startswith("https://discord.gg/") or message.content.startswith("discord.gg/"):
        await message.delete()
        embed = discord.Embed(title="Divulgação", color=0x00ff00)
        embed.add_field(name=f"O Usuário {message.author} esta tentando divulgar! Eae irmão quer bagunçar é fela da puta??", value="anti-divulgação",
                        inline=False)
        await message.channel.send(embed=embed)

    if message.content.lower().startswith(">verificar"):

        embed1 = discord.Embed(
            title="Leia antes de aceitar!",
            color=COR,
            description="**Seja bem-vindo!** \n"
            "\n"
            "**Coffee Labs** é uma comunidade Pernambucana de programação que foi fundada em 21/03/2020 com intuito de reunir o máximo de pessoas com a mesmo vontade de ajudar e ser ajudado. \n"
            "\n"
            "Para você ter acesso aos canais, você precisa confirmar que aceita todas as regras da nossa comunidade **Clicando na reação :white_check_mark:  no fim desta mensagem** \n"
            "\n"
            ":warning:  Membros\n"
            "\n"
            "Respeite as **Diretrizes do Discord** => https://discordapp.com/guidelines \n"            
            "\n"
            "1 - Proibido qualquer compartilhamente de conteúdo sexual. \n"
            "\n"
            "2 - Proibido discursos de ódeio tendo por base características como raça, gênero, etnia, nacionalidade, religião, orientação sexual ou outro aspecto passível de discriminação \n"
            "\n"
            "4 - Mantenha o respeito com todos da comunidade. \n"
            "\n"
            "5 - Não faça flood/spam em qualquer canal do servidor. \n"
            "\n"
            "6 - Fale dentro do tópico.\n"
            "\n"
            "- Sim, eu aceito  =  ✅ ",
        )

        botmsg = await message.channel.send(embed=embed1)

        await botmsg.add_reaction("✅")

        global msg_id
        msg_id = botmsg.id

        global msg_user
        msg_user = message.author

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "✅" and msg.id == msg_id: #and user == msg_user:
        this_role = get(msg.guild.roles, id=int(697127171931635752))
        await user.add_roles(this_role)

        this_role = get(msg.guild.roles, id=int(697127350684352552))
        await user.remove_roles(this_role)

        print("Usuário verificado: ", user)

@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == "✅" and msg.id == msg_id: #and user == msg_user:
        this_role = get(msg.guild.roles, id=int(697127171931635752))
        await user.remove_roles(this_role)

        this_role = get(msg.guild.roles, id=int(697127350684352552))
        await user.add_roles(this_role)

        print("Usuário des-verificado: ", user)

@client.event
async def on_member_join(member):
    embed = discord.Embed(title="CoffeeBot - Mensagem de Boas-vindas", color=0x00ff00)
    embed.add_field(name="Seja bem-vindo(a)", value=f"{member} obrigado por entrar! Mas antes de mais nada, você é um usuário não verificado e deverá verificar no `verificar-conta` \n Atenciosamente,\n CoffeeLabs.", inline=False)
    await client.get_channel(696799654993592363).send(embed=embed)
