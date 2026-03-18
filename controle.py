import csv

arquivo = "C:/temp/gastos.csv"

print("INICIOU")

while True:
    print("\n1 - Adicionar gasto")
    print("2 - Ver gastos")
    print("3 - Remover gasto")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")

        while True:
            valor_input = input("Valor: ")

            if valor_input.strip() == "":
                print("Digite um valor!")
                continue

            valor_input = valor_input.replace(",", ".")

            try:
                valor = float(valor_input)
                break
            except:
                print("Valor inválido! Ex: 50 ou 50.90")

        try:
            with open(arquivo, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([nome, valor])
            print("Gasto salvo com sucesso!")
        except Exception as e:
            print("Erro ao salvar:", e)

    elif opcao == "2":
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                print("\n--- GASTOS ---")

                total = 0
                vistos = set()

                for linha in reader:
                    chave = (linha[0], linha[1])

                    if chave not in vistos:
                        valor = float(linha[1])
                        print(f"{linha[0]} - R${valor:.2f}")
                        total += valor
                        vistos.add(chave)

                print(f"\nTOTAL: R${total:.2f}")

        except:
            print("Nenhum gasto encontrado.")

    elif opcao == "3":
        gastos = []

        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for linha in reader:
                    gastos.append(linha)

            if not gastos:
                print("Nenhum gasto para remover.")
                continue

            print("\n--- ESCOLHA O GASTO PARA REMOVER ---")
            for i, gasto in enumerate(gastos, start=1):
                print(f"{i} - {gasto[0]} - R${float(gasto[1]):.2f}")

            escolha = int(input("Digite o número: "))
            indice = escolha - 1

            del gastos[indice]

            # 🔥 AQUI SALVA DE VERDADE (CRUD COMPLETO)
            with open(arquivo, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(gastos)

            print("Gasto removido com sucesso!")

        except:
            print("Erro ao remover.")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida")

input("Pressione ENTER para sair...")