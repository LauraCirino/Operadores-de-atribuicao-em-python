total = 0

print("Simludor de Caixa de mercado")
print("1 - adicionar produto ao carrinho (especifique o valor)")
print("2 - aplicar desconto (10% do total)")
print("3 - Remover um valor do total")
print("4 - Finalizar compra")

while True:
    opcao = int(input("escolha uma açâo"))
    if opcao == 1:
        valor =  float(input("digite o valor do produto : R$ "))
        total += valor
    elif opcao == 2:
        total *= 0.9 
    elif opcao == 3:
        valor = float(input("digite o valor a ser removido : R$"))
    elif opcao == 4:
        print(f"compra finalizada. total: R$ {total:.2f}")
    else:
        print("opcao incalida!")

    print(f"total atual: R$ {total:.2f}")

