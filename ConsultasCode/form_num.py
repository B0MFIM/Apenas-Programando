# Praticando Formatação Numérica:
faturamento = 1500
custo = 500
lucro = faturamento - custo
print(f"O lucro foi de R${lucro:,.2f}")

margem = lucro / faturamento
print(f"A margem foi de {margem:.1%}")

# Formatando em forma BR
t_l = f"R${lucro:_.2f}" 
t_l = t_l.replace(".", ",").replace("_", ".")
print(f"O lucro foi de R${t_l}")
