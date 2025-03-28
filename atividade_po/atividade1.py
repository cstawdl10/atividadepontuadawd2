import os 
os.system("clear")

preco_total = 0
pratos_solicitados = ""
valor = 0

while True:
    print("""
    ================= MENU =================
    Códigos     Pratos       \t\tValor 
    1 \t        Picanha \t\tR$ 25,00
    2 \t        Lasanha \t\tR$ 20,00
    3 \t        Strogonoff \t\tR$ 18,00
    4 \t        Bife acebolado \t\tR$ 15,00
    5 \t        Pão com ovo \t\tR$ 5,00
    6 \t        Cachorro Quente\t\tR$ 4,00
    7 \t        Pizza Grande\t\tR$ 40,00
        Digite (0) pra finalizar o seu pedido.
          """)
   
    opcao = int(input("Digite o número da opção desejada: "))
    if opcao == 0:
        break
    match opcao:
        case 1:
            prato = "Picanha"
            preco = 25
        case 2:
            prato = "Lasanha"
            preco = 20
        case 3:
            prato = "Strogonoff"
            preco = 18
        case 4:
            prato = "Bife acebolado"
            preco = 15
        case 5:
            prato = "Pão com ovo"
            preco = 5
        case 6:
            prato = "Cachorro Quente"
            preco = 4
        case 7:
            prato = "Pizza Grande"
            preco = 40
        case _ :
            prato = 0
            print("Informação Inválida \nTente Novamente")
            exit()
    preco_total += preco
    pratos_solicitados += ", " + prato if pratos_solicitados else prato
    mais_pedidos = input("Deseja fazer um novo pedido?\nUse 'S' para adicionar mais pratos: ").lower()
    total_pagar = preco_total
    if mais_pedidos == "0":
        break
print("""
=========== MENU ==========
Código   \tForma de Pagamento        
1                Debito 
2                Crédito      
""")

pagamento = int(input("Debito ou Crédito?: "))

match pagamento:
 
        case 1:
            codigo = 1
            resultado = "Debito"
            desconto = (preco_total * 0.1)
            total_pagar = preco_total - desconto
            os.system("clr || clear")
            print("""
    ================= MENU =================
    1 \t Picanha \t\tR$ 25,00
    2 \t Lasanha \t\tR$ 20,00
    3 \t Strogonoff \t\tR$ 18,00
    4 \t Bife acebolado \tR$ 15,00
    5 \t Pão com ovo \t\tR$ 5,00
    6 \t Cachorro Quente\tR$ 4,00
    7 \t Pizza Grande\t\tR$ 40,00
        
          """)
            print(f"Pratos solicitados: {pratos_solicitados}")
            print (f"Valor sem o desconto: {preco_total}")
            print(f"Forma de pagamento:{resultado}")
            print (f"Valor do desconto : {desconto}")
            print (f"Valor total com o desconto: {total_pagar}")
            print("=========Obrigado pela preferência==========")

        case 2:
            resultado = "Crédito"
            desconto = (preco_total * 0.10)
            total_pagar = preco_total + desconto
            os.system("clr || clear")
            print("""
    ================= MENU =================
    1 \t Picanha \t\tR$ 25,00
    2 \t Lasanha \t\tR$ 20,00
    3 \t Strogonoff \t\tR$ 18,00
    4 \t Bife acebolado \tR$ 15,00
    5 \t Pão com ovo \t\tR$ 5,00
    6 \t Cachorro Quente\tR$ 4,00
    7 \t Pizza Grande\t\tR$ 40,00
        
          """)
            print(f"Pratos solicitados: {pratos_solicitados}")
            print (f"Valor sem o acréscimo: {preco_total}")
            print(f"Forma de pagamento: {resultado}")
            print (f"Valor do acrescimo: {desconto}")
            print (f"Valor total com o acréscimo: {total_pagar}")
            print("=========Obrigado pela preferência==========")
            

        case _:
            resultado = "Invalido!"

   
               