desconto = 3 / 100
desconto2 = 5 / 100
desconto3 = 7 / 100

camisetas = int(input("Quantas camisetas você deseja?"))
preco = 12.50

if camisetas <= 5:
    precoDesc = preco * desconto
    precoDescFinal = preco - precoDesc
    precoTotal = precoDescFinal * camisetas
    print(f"Você pagara {precoTotal:.2F}")
elif camisetas > 5 and camisetas <= 10:
    precoDesc = preco * desconto2
    precoDescFinal = preco - precoDesc
    precoTotal = precoDescFinal * camisetas
    print(f"Você pagara {precoTotal:.2F}")
else:
    precoDesc = preco * desconto3
    precoDescFinal = preco - precoDesc
    precoTotal = precoDescFinal * camisetas
    print(f"Você pagara {precoTotal:.2F}")
