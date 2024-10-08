# Dado uma sequência de números, calcule a soma e média dos números.
# ATENÇÃO: não vale usar a função sum() !

valores = [10, 30, 45, 33, 88, 100,12, 32,36,74, 44]
soma = 0

for valor in valores:
    soma += valor
media = soma / len(valores)
print(f"Soma dos Numeros = {soma}")
print(f"Media dos numeros = {media}")


# Dado uma sequência de números, calcule o maior valor da sequência.
# ATENÇÃO: não vale usar a função max() !

maiorValor = 0
valores = [10, 30, 45, 33, 88, 100,12, 32,36,74, 44, 29, 41, 20, 13]
for valor in valores:
    if valor > maiorValor:
        maiorValor = valor
print(f"Maior valor = {maiorValor}")

# Dado uma lista de palavras, printe todas as palavras
# com pelo menos 5 caracteres.

palavras = ["Arthur", "Joao", "Nina", "Ana", "Leonardo", "Moises", "Leo", "Carolina", "Isac", "Isaac", "Patricia", "Sol"]
for palavra in palavras:
    if len(palavra) >= 5:
        print(palavra)

print(len(palavras))