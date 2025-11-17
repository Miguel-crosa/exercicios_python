horas = float(input("Quantas Horas Você assiste streamings por semana? "))
mensal = float(input("Valor mensal da assinatura "))
horas_mensais = horas * 4

preco = mensal / horas_mensais

print(f"Valor Total: {preco:.2F}")
