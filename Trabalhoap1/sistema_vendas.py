from os import system

# VARIAVEIS DECLARADAS:

contador = 0
total = 0

# LISTAS USADAS:

lista_produtos = [
    'Arroz', 'Macarrão', 'Feijão', 'Açucar', 'Maizena',
    'Café', 'Leite', 'Leite em pó', 'Óleo', 'Farinha de trigo',
    'Creme de Leite', 'Azeite', 'Tomate', 'Batata', 'Batata Doce',
    'Achocolatado', 'Molho de Tomate', 'Aveia em Flocos', 'Cereal', 'Sal',
    'Biscoito Recheado', 'Salgadinho', 'Barra de chocolate']

preço_produtos = [
    5.90, 4.30, 7.00, 3.00, 4.82,
    4.00, 2.25, 3.60, 3.75, 2.70,
    2.00, 9.00, 8.30, 5.10, 4.70,
    4.00, 3.50, 4.89, 5.00, 2.00,
    1.50, 2.00, 8.00]

Chaves_de_escolha = []

Carrinho_de_compras = []

preço_carrinho = []

pagamento_opção = ["Crédito", "Débito", "PIX", "Dinheiro Físico"]

desconto_forma_pagamento = [7.5, 5.0, 2.5, 2.0]

# MENU DE OPÇÃO:


while True:
    system("cls")
    print("=" * 50)
    print("BEM VINDO AO SUPERMERCADO!")
    print("1- ADICIONAR PRODUTOS AO CARRINHO")
    print("2- VERIFICAR CARRINHO DE COMPRA")
    print("3- REMOVER PRODUTOS DO CARRINHO")
    print("4- EFETUAR O PAGAMENTO")
    print("5- SAIR DO MERCADO")
    print("=" * 50)

    opt = int(input("Escolha a opção desejada:"))

    if opt == 1:
        system("cls")
        print("=" * 50)
        for produtos in lista_produtos:
            contador += 1
            print(f"{contador}°- {produtos}", end="\n")

        contador = 0
        while True:
            contador += 1
            produto_escolhido = int(input(f"Digite o produto N°{contador}:"))
            produto_escolhido -= 1
            Chaves_de_escolha.append(produto_escolhido)
            Carrinho_de_compras.append(lista_produtos[produto_escolhido])
            preço_carrinho.append(preço_produtos[produto_escolhido])
            continuar = input("Você deseja continuar a colocar produtos no carrinho? [S/N]")
            if (continuar == "S" or continuar == "s"):
                pass
            else:
                break

    if opt == 2:
        if len(Carrinho_de_compras) == 0:
            system("cls")
            print("A lista de compras está vazia!")
            print("APERTE ENTER PARA CONTINUAR")
            a = input('').split(" ")[0]
        else:
            system("cls")
            contador = 0
            total = 0
            print("=" * 50)
            print("Seus produtos escolhidos atualmente:")
            for chaves_produtos in Chaves_de_escolha:
                contador += 1
                print(
                    f"{contador}°- {lista_produtos[chaves_produtos]} - Preço: R${preço_produtos[chaves_produtos]:.2f}",
                    end="\n")

            for i in preço_carrinho:
                total += i

            print(f"Valor total das compras: R${total:.2f}")

            print("APERTE ENTER PARA CONTINUAR")
            a = input('').split(" ")[0]
            print(a)

    if opt == 3:
        system("cls")
        contador = 0
        if len(Carrinho_de_compras) == 0:
            print("A lista de compras está vazia!")
            print("APERTE ENTER PARA CONTINUAR")
            a = input('').split(" ")[0]
        else:
            print("=" * 50)
            print("Seus produtos escolhidos atualmente:")
            for chaves_produtos in Chaves_de_escolha:
                contador += 1
                print(
                    f"{contador}°- {lista_produtos[chaves_produtos]} - Preço: R${preço_produtos[chaves_produtos]:.2f}",
                    end="\n")

            while True:
                remover_do_carrinho = int(input("Digite o número do produto que você deseja remover do carrinho:"))

                if remover_do_carrinho > len(Carrinho_de_compras):
                    print("Código inválido, tente novamente!")

                elif remover_do_carrinho <= 0:
                    print("Código inválido, tente novamente!")

                else:
                    del Carrinho_de_compras[remover_do_carrinho - 1]
                    del Chaves_de_escolha[remover_do_carrinho - 1]
                    del preço_carrinho[remover_do_carrinho - 1]

                    if len(Carrinho_de_compras) == 0:
                        print("Carrinho está atualmente vazio!")
                        break
                    else:
                        escolha = input("Você deseja remover mais algum produto do seu carrinho? [S/N]")
                        if escolha == 'S' or escolha == 's':
                            pass
                        else:
                            break

    if opt == 4:
        total = 0
        for i in preço_carrinho:
            total += i

        if len(Carrinho_de_compras) == 0:
            system("cls")
            print("A lista de compras está vazia!")
            print("APERTE ENTER PARA CONTINUAR")
            a = input('').split(" ")[0]
        else:
            system("cls")
            contador = 0
            print("=" * 50)
            print("Digite a forma que irá efetuar o pagamento:")
            for formas_pagar in pagamento_opção:
                contador += 1
                print(f"{contador} - {formas_pagar}", end="\n")

            contador = 0
            escolha_forma = int(input("Forma que efetuará o pagamento:"))
            system("cls")

            escolha_forma -= 1

            valor_final = total - (total / 100) * desconto_forma_pagamento[escolha_forma]

            print("=" * 50)
            for chaves_produtos in Chaves_de_escolha:
                contador += 1
                print(
                    f"{contador}°- {lista_produtos[chaves_produtos]} - Preço: R${preço_produtos[chaves_produtos]:.2f}",
                    end="\n")

            print(f"Valor total das compras: R${total:.2f}")
            print(f"Valor final com o desconto da opção {pagamento_opção[escolha_forma]}: {valor_final:.2f}")

            print("OBRIGADO POR COMPRAR, SEJA SEMPRE BEM VINDO!")
            print("APERTE ENTER PARA CONTINUAR")
            a = input('').split(" ")[0]
            break

    if opt == 5:
        system("cls")
        print("VOLTE SEMPRE! OBRIGADO PELA PREFERÊNCIA!!")
        break