from turtle import title
import discord
import requests
import datetime
from discord.ext import commands, tasks


# PREFIXO P/ COMANDOS
bot = commands.Bot("!")


# EVENTOS DO BOT
@bot.event # Add evento pro bot
async def on_ready(): # Para saber se o bot está conectado
    print(f"I'm ready! I'm logged in as {bot.user}")
    curret_time.start() # Iniciar task 'curret_time'

@bot.event 
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

@bot.event
async def on_reaction_add(reaction, user): # Para o bot add cargo à um usuário (a partir de uma reação)
    if reaction.emoji == "👍":
        role = user.guild.get_role(993299588792451152)
        await user.add_roles(role)
    elif reaction.emoji == "💩":
        role = user.guild.get_role(993299987242942576)
        await user.add_roles(role)


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

@bot.command(name="calcular")
async def calculate_expression(ctx, *expression): # Calcular uma expressão qualquer
    """
    -> Faz a execução de um comando
    PARÂMETROS:
        ctx         -> Saber onde a mensagem foi enviada
        expression  -> Calcula a expressão inserida
    """
    expression = "".join(expression)
    response = eval(expression)  # eval() - tomar cuidado com esta função, procurar não utiliza-la
    await ctx.send("Resposta: " +  str(response))

@bot.command()
async def binance(ctx, coin, base): # Ver cotações
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
async def secret(ctx): # Enviar uma mensagem privada pra um user
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

@bot.command(name="foto")
async def get_random_image(ctx):
    """
    -> Faz a execução de um comando
    PARÂMETROS:
        ctx  -> Saber onde a mensagem foi enviada
    """
    url_image = "https://picsum.photos/1920/1080"
    embed = discord.Embed(
        title = "Resultado da busca",
        description = "PS: A imagem é aleatória",
        color = 0x0000FF
    )
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_footer(text="Feito por " + bot.user.name, icon_url=bot.user.avatar_url)
    embed.add_field(name="API", value="Usamos a API do picsum.photos")
    embed.add_field(name="Parâmetros", value="{largura}/{altura}")
    embed.add_field(name="Exemplo", value=url_image,  inline=False)
    embed.set_image(url=url_image)
    await ctx.send(embed=embed)


# TAREFAS DO BOT
@tasks.loop(hours=1) # Add tarefa pro bot (exibir data e hora)
async def curret_time():
    now = datetime.datetime.now()
    now = now.strftime("%d/%m/%Y às %H:%M:%S")
    channel = bot.get_channel(993252657500258437)
    await channel.send("Data atual: " + now)
  

# EXECUTAR O BOT
bot.run("My Token Here")