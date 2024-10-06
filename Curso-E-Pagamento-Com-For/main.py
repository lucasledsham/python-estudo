import sys

print("=" * 50)

print("Conheca os cursos disponiveis: ")
cursos = ["Java SE", "Spring", "Java OO Avancado"]
for index, curso in enumerate(cursos):
    print(f"[{index + 1}] {curso}")

cursoEscolhido = int(input("Escolha o numero do curso: "))

cursoEscolhidoValidacao = 1 <= cursoEscolhido <= len(cursos)
if not cursoEscolhidoValidacao:
    print("Digite um numero valido!")
    sys.exit(0)

print("=" * 50)

print("Formas de pagamentos disponiveis: ")

pagamentos = ["Cartao", "Boleto"]
for index, pagamento in enumerate(pagamentos):
    print(f"[{index + 1}] {pagamento}")

pagamentoEscolhido = int(input("Escolha o numero do pagamento: "))

pagamentoEscolhidoValidacao = 1 <= pagamentoEscolhido <= len(pagamentos)
if not pagamentoEscolhidoValidacao:
    print("Digite um numero valido!")
    sys.exit(0)

print("=" * 50)

print(f"Curso: {cursos[cursoEscolhido - 1]}\nPagamento: {pagamentos[pagamentoEscolhido - 1]}")