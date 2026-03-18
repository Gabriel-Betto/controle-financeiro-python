import csv

arquivo = "C:/temp/gastos.csv"

total = 0
maior_valor = 0
maior_nome = ""
quantidade = 0

try:
    with open(arquivo, "r", encoding="utf-8") as f:
        reader = csv.reader(f)

        for linha in reader:
            nome = linha[0]
            valor = float(linha[1])

            total += valor
            quantidade += 1

            if valor > maior_valor:
                maior_valor = valor
                maior_nome = nome

    print("\n--- ANÁLISE DOS GASTOS ---")
    print(f"Total gasto: R${total:.2f}")
    print(f"Maior gasto: {maior_nome} - R${maior_valor:.2f}")
    print(f"Quantidade de gastos: {quantidade}")

except:
    print("Erro ao ler o arquivo ou arquivo não encontrado.")

input("\nPressione ENTER para sair...")