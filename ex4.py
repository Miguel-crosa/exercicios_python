dinheiro = float(input("Insira o seu dinheiro em reais "))
dolarPreco = 5.32
euroPreco = 6.16

dolarTotal = dinheiro / dolarPreco
euroTotal = dinheiro / euroPreco

print(f"\nValores:\n----\nDolar: {dolarTotal:.2F}\nEuro: {euroTotal:.2F}\n----")
