import os
import json

# Limpa a tela do console
os.system('clear')

# Verifica se o arquivo 'dados.json' existe antes de tentar removê-lo
if os.path.isfile('dados.json'):
    # Remove o arquivo se ele existir
    os.remove('dados.json')
else:
    # Exibe um erro se o arquivo não existir
    print("Erro: %s arquivo não encontrado" % 'dados.txt')

# Função para solicitar ao usuário a quantidade de chaves para o objeto JSON
def quantidadesDeChaves():
    # Solicita a quantidade de chaves ao usuário
    qnt = input('Digite a quantidade de chaves que você deseja criar no JSON: ')
    # Entra em um loop infinito
    while True:
        # Verifica se a variável contém apenas números
        if not qnt.isnumeric():
            qnt = input('Quantidade inválida!\nDigite novamente a quantidade de chaves que deseja criar no JSON: ')  # Solicita ao usuário que digite novamente
        else:
            # Se tiver, tranforma em inteiro
            qnt = int(qnt)
            # Se a quantidade for 0
            if qnt <= 0:
                # Solicita ao usuário que digite novamente
                qnt = input('Quantidade inválida!\nDigite novamente a quantidade de chaves que deseja criar no JSON: ')
            else:
                # Sai do loop se a quantidade for um número positivo
                break
    # Retorna a quantidade
    return qnt

# Função para determinar o tipo do valor a ser inserido: número inteiro, número flutuante ou string
def tipoDoValor(chave, tipoDigitado):
    # Se o valor for um número
    if tipoDigitado == 'n':
        # Solicita ao usuário que insira o valor da chave
        valor = input(f"Digite o valor da chave {chave}: ")
        # Se o valor contiver um ponto
        if '.' in valor:
            # Converte o valor para um número flutuante
            valor = float(valor)
        else:
            # Converte o valor para um número inteiro
            valor = int(valor)
        # Retorna o valor
        return valor
    # Se o valor for uma string
    else:
        # Solicita ao usuário que insira o valor da chave
        valor = input(f"Digite o valor da chave {chave}: ")
        # Retorna o valor
        return valor

# Função para criar o objeto JSON com base nas informações inseridas pelo usuário
def conteudoDasChaves(quantidade):
    # Inicializa um objeto JSON vazio
    objetoJSON = {}

    # Para cada chave que o usuário deseja criar
    for _ in range(quantidade):
        # Solicita o nome da chave ao usuário
        chave = input(f'Digite o nome da chave {_ + 1}: ')
        # Solicita o tipo de valor ao usuário
        valorTipo = input('O tipo do valor será: "S"tring ou "N"úmero: ').lower()

        # Se o tipo de valor não for uma string ou um número, solicita ao usuário que digite novamente
        while valorTipo != 's' and valorTipo != 'n':
            valorTipo = input('Valor inválido\nDigite novamente se o valor será: "S"tring ou "N"úmero: ').lower()
        
        # Obtém o valor da chave com o tipo correto
        a = tipoDoValor(chave, valorTipo)

        # Adiciona a chave e o valor ao objeto JSON
        objetoJSON[chave] = a

    # Converte o objeto JSON para uma string JSON formatada
    dadosJSON = json.dumps(objetoJSON, indent=4)
    return dadosJSON  # Retorna a string JSON

def copiandoJSON(json_str):
    # Solicita ao usuário quantas vezes ele deseja replicar o objeto JSON
    repeticao = int(input('Quantas vezes você quer que esse objeto se repita no arquivo: '))

    # Se a quantidade for um número negativo
    while repeticao < 0:
        # Solicita ao usuário que digite novamente
        repeticao = int(input('Valor inválido\nDigite novamente quantas vezes você quer que esse objeto se repita no arquivo: '))

    # Converte a string JSON para um objeto JSON
    objeto = json.loads(json_str)

    # Se a quantidade for zero
    if repeticao == 0:
        # Cria uma lista com o objeto JSON sozinho
        lista_de_objetos = [objeto]
    else:
        # Cria uma lista com o objeto JSON replicado
        lista_de_objetos = [objeto] * repeticao
    # Retorna a lista de objetos JSON
    return lista_de_objetos

def criandoArquivoJSON(lista_de_objetos):
    # Abre o arquivo 'dados.json' em modo de escrita
    with open('dados.json', 'w') as arquivo:
        # Grava a lista de objetos JSON no arquivo com uma indentação de 4 espaços
        json.dump(lista_de_objetos, arquivo, indent=4)

# Solicita ao usuário a quantidade de chaves para o objeto JSON
a = quantidadesDeChaves()
print(a)

# Cria o objeto JSON com base nas informações do usuário
b = conteudoDasChaves(a)
print(b)

# Cria uma lista com o objeto JSON replicado
c = copiandoJSON(b)

# Grava a lista de objetos JSON no arquivo
d = criandoArquivoJSON(c)