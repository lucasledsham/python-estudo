# JOGO ACERTE O NÚMERO - 3 CHANCES

numero = 23
descobriu = False

print("\nVocê é bom em adivinhar? Vamo fazer o teste!")
print("Você tem 3 chances para adivinhar o número que estou pensando.\nO número está entre 1 e 30. Boa sorte!")

print("=" * 50)

for _ in range(3):
    if not descobriu:
        chute = int(input("Escolha um número entre 1 e 30: "))
        if chute < numero:
            print("Número incorreto. Dica: escolha um número mais alto.")
        elif chute > numero:
            print("Número incorreto. Dica: escolha um número mais baixo")
        else:
            print("Você acertou o número!")
            descobriu = True

if descobriu:
    print("\nParabéns, você venceu o jogo!")
else:
    print(f"\nVocê não conseguiu acertar o número :( O número era: {numero}")