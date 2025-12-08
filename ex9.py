# Importando
import os
import random
import time

# Variaveis
senha = 123456
saldo = random.uniform(1.0, 500)
escolha = 0
i = 3
seuNome = input("Qual seu nome?\n--> ")

# Loop principal
while True:
    # Se escolher encerrar dentro do sistema bancário, encerrar a aplicação
    if escolha == 4:
        break

    n = int(input("Digite sua senha\n--> "))
    if n == senha:
        print(f"\nOlá, {seuNome}. Seja bem-vindo ao nosso banco!\n")
        while True:
            # Loop sistema bancario
            print("-- Ver saldo --")
            print("-- Depositar --")
            print("-- Sacar --")
            print("-- Sair --")
            escolha = int(input("\nDigite o que deseja\n-->"))

            # Switch case para escolhas
            match escolha:
                case 1:  # Ver saldo
                    os.system('cls')  # Usado para limpar o CMD (windows)
                    print(f"\nSeu saldo é de: R${saldo:.2F}\n")
                case 2:  # Depósito
                    os.system('cls')  # Usado para limpar o CMD (windows)
                    deposito = int(
                        input(f"\nQuanto você deseja depositar?\nSaldo na conta: R${saldo:.2F}\n-->"))
                    saldo += deposito
                case 3:  # Sacar
                    os.system('cls')  # Usado para limpar o CMD (windows)
                    sacar = int(
                        input(f"\nQuanto Você deseja Sacar?\nSaldo na conta: R${saldo:.2F}\n-->"))
                    if saldo < sacar:
                        print("\nErro, você não possui essa quantia\n")
                    else:
                        saldo -= sacar
                case 4:  # Sair
                    os.system('cls')  # Usado para limpar o CMD (windows)
                    print("\nVolte sempre.\n")
                    time.sleep(1)
                    # Usado para limpar o CMD (windows) após 1 segundo
                    os.system('cls')
                    break

    else:
        i -= 1
        if i == 0:
            os.system('cls')  # Usado para limpar o CMD (windows)
            print(
                "\nSua senha foi bloqueada, por favor dirija-se a um de nossos caixas.")
            break
        else:
            os.system('cls')  # Usado para limpar o CMD (windows)
            print(f"\nSenha incorreta, voce ainda tem {i} tentativa(s)\n")
