import requests  # biblioteca para fazer requisições HTTP

cep = input("Digite o cep (somente numeros): ")
cep = cep.replace("-", "")  # Tirar - se o usuario digitar

if len(cep) != 8 or not cep.isdigit():
    print("CEP INVALIDO, DIGITE ATÉ 8 NUMEROS")
else:
    # Utilizar o site viacep.com.br
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    dados = resposta.json()

if "erro" in dados:
    print("CEP NÃO ENCONTRADO")
else:
    logradouro = dados.get("logradouro", "")
    complemento = dados.get("complemento", "")
    bairro = dados.get("bairro", "")
    cidade = dados.get("localidade", "")
    estado = dados.get("uf", "")

    print(f"\n --- Endereço Encontrado ---")
    print(f"\n Logradouro: {logradouro}")
    print(f"\n Complemento: {complemento}")
    print(f"\n Bairro: {bairro}")
    print(f"\n Cidade: {cidade}")
    print(f"\n Estado: {estado}")
    print(f"\n --- Endereço Encontrado ---")
