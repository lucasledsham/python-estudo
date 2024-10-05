import sys

cursos = ["Jave SE", "Spring", "Java OO Avançado"]
print("Os cursos disponíveis são: ")
print("[1] " + cursos[0])
print("[2] " + cursos[1])
print("[3] " + cursos[2])

cursoEscolhido = int(input("Digite o número do curso desejado: "))

curso_Escolhido_Verificacao = cursoEscolhido > 0 and cursoEscolhido <= len(cursos)

if not curso_Escolhido_Verificacao:
    print("Digite um número válido!")
    sys.exit(0)


print("\nPagamentos disponíveis: ")
pagamento = ["Cartão", "Boleto"]
print("[1] " + pagamento[0])
print("[2] " + pagamento[1])

pagamentoEscolhido = int(input("Digite o número do pagamento desejado: "))
pagamento_Escolhido_Verificacao = pagamentoEscolhido > 0 and pagamentoEscolhido <= len(cursos)

if not pagamento_Escolhido_Verificacao:
    print("Digite um número válido!")
    sys.exit(0)

print("=" * 40)
print(f"Curso escolhido: {cursos[cursoEscolhido - 1]}\nForma de Pagamento: {pagamento[pagamentoEscolhido - 1]}")