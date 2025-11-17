pessoa = input("Qual seu nome ")
nota1 = float(input("Qual Sua Primeira Nota "))
nota2 = float(input("Qual Sua Segunda Nota "))
nota3 = float(input("Qual Sua Terceira Nota "))
nota4 = float(input("Qual Sua Quarta Nota "))

conta = (nota1 + nota2 + nota3 + nota4) / 4


print(f"{pessoa}. A média das suas notas é de: {conta:.2F}")
