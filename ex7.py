soma = 0

n = int(input("Digite um numero inteiro positivo \n"))


for i in range(n):
    m = int(input("Digite um numero inteiro positivo para a média aritmetica\n"))
    soma += m


print(soma / n)
