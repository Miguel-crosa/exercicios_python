import math
j = 0

for i in range(5):

    k = int(input("\nQual o numero desejado? \n"))

    if k <= 0:
        print("\nErro, digite um numero inteiro positivo")
        break

    if k % 2 == 0:
        print(f"\nNumero par: -- {k} --\n")
        j += 1  # feito para mostrar o total de numeros pares no final
    else:
        print(f"\nNumero impar: -- {k} --\n")


print(f"\nO total de numeros pares é de: {j}")
