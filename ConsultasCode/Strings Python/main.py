v1 = 54     # inteiro
v2 = 54.0   # flutuante
vs = "Olá"  # texto string
print(type(v1))
print(type(v2))
print(type(vs))

nome = " daniel marinho"
print(nome*3)
print(nome)
nome_duplicado = nome*2
print(nome_duplicado)
# alterar letra inicial do texto
nome_maiuscula = nome.strip().capitalize()
print(nome_maiuscula)
# alterar letras para maiusculas
nome_tudo_maiuscula = nome.strip().upper()
print(nome_tudo_maiuscula)
# alterar letras para minusculas
nome_minuscula = nome_maiuscula.casefold()
print(nome_minuscula)
# alterar letra específica
novo_nome = nome.replace("a", "e", 1)
print(novo_nome)
# mesclando nomes
nome = "daniel"
sobrenome = "bomfim"
nome_completo = nome.capitalize() + " " + sobrenome.capitalize()
print(nome_completo)

# verificando tipo
cpf = "11122233300"
print(cpf.isnumeric())
print(cpf.isalpha())
print(cpf.isalnum())
print(cpf.isascii()) # cpf = "111.222.333-00"
nome = "PEDRO"
print(nome.isupper())
print(nome.islower())

# procurar um texto
nome = "Pedro Bomfim"
print(nome.find("B"))
print(nome.find("a"))
# fatiamento
print(nome[:6])
print(nome[6:])
print(nome[3:9])
print(nome[0::2])
# exibindo letras do nome
for letra in nome:
    print(letra)
# Dividindo o nome em uma lista
palavras = nome.split()
print(palavras) 

# Acessando um arquivo de texto
import io
with io.open("C:\\Users\\bomfi\\OneDrive\\Documentos\\MeusProjetos\\Apenas-Programando\\emails.txt", "r") as t:
    texto = t.read()
print(texto)
# Acessando um arquivo de texto e separando as linhas
with io.open("C:\\Users\\bomfi\\OneDrive\\Documentos\\MeusProjetos\\Apenas-Programando\\emails.txt", "r") as l:
    linhas = l.readlines()
print(linhas)
# removendo marcador \n
emails = texto.split("\n")
print(emails)
# fatiamento
print(emails[2])
posição = emails[0].find("@")
print(posição)
print(emails[0][:5])

# .format
n1 = 4
n2 = 10
media = (n1 + n2)/2
print("A 1° nota é: {} A 2° nota é: {} A média é: {}".format(n1, n2, media))
print(f"A nota do Bomfim é de {media}")