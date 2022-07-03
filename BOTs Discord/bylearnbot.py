import discord
import datetime
from discord.ext import commands, tasks


# PREFIXO P/ COMANDOS
bot = commands.Bot("!")


# EVENTOS DO BOT
@bot.event # Add eventos pro bot
async def on_ready(): # Para saber se o bot está conectado
    print(f"I'm ready! I'm logged in as {bot.user}")
    curret_time.start() # Iniciar task 'curret_time'

@bot.event  # Add eventos pro bot
async def on_message(message): # Para o bot enviar uma mensagem
    """
    -> Faz a execução de uma mensagem
    PARÂMETROS:
        message -> Enviar uma mensagem para a função
    """
    if message.author == bot.user:
        return

    if "palavrão" in message.content:
        await message.channel.send(f"Please, {message.author}, do not offend other users.")
        await message.delete()

    await bot.process_commands(message) # Fazer o bot executar todos os comandos


# COMANDOS DO BOT
@bot.command(name="oi") # Add comando pro bot
async def send_hello(ctx):
    """
    -> Faz a execução de uma mensagem
    PARÂMETROS:
        ctx -> Onde a mensagem foi enviada
    """
    name = ctx.author.name
    response = "Hello, " + name
    await ctx.send(response)


# TAREFAS DO BOT
@tasks.loop(hours=1) # Add tarefa pro bot
async def curret_time():
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y às %H:%M:%S")
    channel = bot.get_channel(993252657500258437)
    await channel.send("Data atual: " + now)


# EXECUTAR O BOT
bot.run("OTkzMjUwNjE0NDAwMjc0NTA0.Gxl1UD.VYbxtMe7BIY4euG7lZWPAmVuObp4TBQqwwDWHQ")