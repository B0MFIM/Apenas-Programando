# ESTE ROBÔ FOI DELETADO!!

import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    # Respondendo comandos do usuário (?)
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        # (?regras)
        if message.content == "?regras":
            await message.channel.send(f"{message.author.name} as regras do servidor são: {os.linesep}1 - Não desrespeitar os membros!{os.linesep}# Ocasionalmente haverá BAN!")
        # (?nivel)
        elif message.content == "?nivel" or message.content == "?nível":
            await message.author.send("Nível 1")
        # (?help)
        elif message.content == "?help":
            await message.channel.send(f"{message.author.name} os comandos são: {os.linesep}- ?regras {os.linesep}- ?nivel")

    
    # Novo membro entrando do servidor
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            message = f"{member.mention} acabou de entrar no {guild.name}"
            await guild.system_channel.send(message)

intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('My Token Goes Here')

# ESTE ROBÔ FOI DELETADO!!