import json
import os

# Limpa o console
os.system('clear')

def deletarArquivo(arquivoFinal):
    # Verifica se o arquivo especificado existe no sistema de arquivos
    if os.path.isfile(arquivoFinal):
        # Se o arquivo existir, remove-o
        os.remove(arquivoFinal)
    else:
        # Se o arquivo não existir, imprime uma mensagem de erro
        print(f"Erro: arquivo não encontrado {arquivoFinal}")

def copiandoJSON(arquivoOriginal, arquivoFinal, qntCopias):
    # Chama a função deletarArquivo para remover o arquivoFinal se ele existir
    deletarArquivo(arquivoFinal)

    # Abre o arquivoOriginal no modo de leitura e carrega os dados JSON nele
    with open(arquivoOriginal, 'r') as arquivo:
        dadosOriginal = json.load(arquivo)

    # Cria uma nova lista que consiste em qntCopias do primeiro objeto no arquivoOriginal
    listaDadosFinal = [dadosOriginal[0] for _ in range(qntCopias)]

    # Abre o arquivoFinal no modo de gravação e grava os dados na listaDadosFinal nele
    with open(arquivoFinal, 'w') as arquivo:
        json.dump(listaDadosFinal, arquivo, indent=4)

def setupzin():
    nomeArquivoOriginal = input('Qual nome do arquivo que será copiado: ')
    # Adiciona a extensão .json ao nome do arquivo
    nomeArquivoOriginal = nomeArquivoOriginal + '.json'

    # Continua perguntando ao usuário o nome do arquivo a ser copiado até que um arquivo válido seja fornecido
    while os.path.isfile(nomeArquivoOriginal) is False:
        nomeArquivoOriginal = input('Arquivo não encontrado!\nQual nome do arquivo que será copiado: ')
        nomeArquivoOriginal = nomeArquivoOriginal + '.json'

    nomeArquivoFinal = input('Qual será o nome do arquivo a ser criado: ')
    # Adiciona a extensão .json ao nome do arquivo final
    nomeArquivoFinal = nomeArquivoFinal + '.json'

    # Solicita ao usuário a quantidade de cópias do objeto
    qnt = int(input('Qual será a quantidade de vezes que o objeto será copiado: '))

    if qnt <= 0:
        # Se a quantidade for 0 ou menor, termina o programa
        exit()
    else:
        # Caso contrário, chama a função copiandoJSON com os argumentos fornecidos e retorna o resultado
        a = copiandoJSON(nomeArquivoOriginal, nomeArquivoFinal, qnt)
        return a

# Chama a função setupzin
a = setupzin()