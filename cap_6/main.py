from inserir_dados import inserir_producao
from consultar_dados import listar_producoes
from atualizar_dados import atualizar_producao_real

def menu():
    while True:
        print("\n=== SISTEMA AGRO ===")
        print("1 - Inserir produção")
        print("2 - Listar produções")
        print("3 - Atualizar produção real")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cultura = input("Cultura: ")
            area_hectares = float(input("Área em hectares: "))
            producao_esperada = float(input("Produção esperada: "))
            producao_real = float(input("Produção real: "))
            perdas_percentual = round(((producao_esperada - producao_real) / producao_esperada) * 100, 2)
            tipo_colheita = input("Tipo de colheita: ")
            data_colheita = input("Data da colheita (YYYY-MM-DD): ")
            regiao = input("Região: ")

            inserir_producao(
                cultura, area_hectares, producao_esperada, producao_real,
                perdas_percentual, tipo_colheita, data_colheita, regiao
            )

        elif opcao == "2":
            listar_producoes()

        elif opcao == "3":
            id_registro = int(input("ID do registro: "))
            nova_producao_real = float(input("Nova produção real: "))
            atualizar_producao_real(id_registro, nova_producao_real)

        elif opcao == "4":
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida.")

menu()