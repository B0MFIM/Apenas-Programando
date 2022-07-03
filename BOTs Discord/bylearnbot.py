import discord
import requests
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
    -> Faz a execução de um evento
    PARÂMETROS:
        message -> Enviar uma mensagem para a função
    """
    if message.author == bot.user:
        return

    if "palavrão" in message.content:
        await message.channel.send(f"Por Favor! {message.author}, não ofenda os outros usuários.")
        await message.delete()

    await bot.process_commands(message) # Fazer o bot executar todos os comandos


# COMANDOS DO BOT
@bot.command(name="oi") # Add comando pro bot
async def send_hello(ctx):
    """
    -> Faz a execução de um comando
    PARÂMETROS:
        ctx -> Saber onde a mensagem foi enviada
    """
    name = ctx.author.name
    response = "Olá, " + name
    await ctx.send(response)

@bot.command(name="calcular") # Add comando pro bot
async def calculate_expression(ctx, *expression):
    """
    -> Faz a execução de um comando
    PARÂMETROS:
        ctx         -> Saber onde a mensagem foi enviada
        expression  -> Calcula a expressão inserida
    """
    expression = "".join(expression) #
    response = eval(expression)  # eval() - tomar cuidado com esta função, procurar não utiliza-la
    await ctx.send("Resposta: " +  str(response))

@bot.command()
async def binance(ctx, coin, base):
    """
    -> Faz a execução de um comando
    PARÂMETROS:
        ctx  -> Saber onde a mensagem foi enviada
        coin -> Moeda utilizada
        base -> Base de conversão
    """
    try:
        response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}")
        data = response.json()
        price = data.get("price")
        if price:
            await ctx.send(f"[{coin}-{base}]: {float(price):.2f}")
        else:
            await ctx.send(f"O par {coin}/{base} é inválido!")
    except Exception as error:
        await ctx.send("Ops... Deu algum erro!")
        print(error)

@bot.command(name="segredo")
async def secret(ctx):
    """
    -> Faz a execução de um comando
    PARÂMETROS:
        ctx  -> Saber onde a mensagem foi enviada
    """
    try:
        await ctx.author.send("Eu sou lindo!")
        await ctx.author.send("E bolo de maracuja é o melhor que existe!")
    except discord.errors.Forbidden:
        await ctx.send("Erro em enviar o segredo")


# TAREFAS DO BOT
@tasks.loop(hours=1) # Add tarefa pro bot
async def curret_time():
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y às %H:%M:%S")
    channel = bot.get_channel(993252657500258437)
    await channel.send("Data atual: " + now)


# EXECUTAR O BOT
bot.run("My Token Here")