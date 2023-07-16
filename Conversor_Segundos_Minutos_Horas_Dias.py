def converter_segundos(valor):
    # Converte segundos em minutos, horas e dias
    # Dividindo o valor por 60, obtemos o número total de minutos
    minutos = int(valor / 60)
    # O resto da divisão por 60 nos dá o número de segundos restantes
    segundos = int(valor % 60)
    # Dividindo os minutos por 60, obtemos o número total de horas
    horas = int(minutos / 60)
    # O resto da divisão por 60 nos dá o número de minutos restantes
    minutos = int(minutos % 60)
    # Dividindo as horas por 24, obtemos o número total de dias
    dias = int(horas / 24)
    # O resto da divisão por 24 nos dá o número de horas restantes
    horas = int(horas % 24)
    return dias, horas, minutos, segundos

def converter_minutos(valor):
    # Converte minutos em segundos, horas e dias
    # Multiplicando a parte fracionária do valor por 60, obtemos o número de segundos
    segundos = int((valor % 1) * 60)
    # Dividindo o valor por 60, obtemos o número total de horas
    horas = int(valor / 60)
    # O resto da divisão por 60 nos dá o número de minutos restantes
    minutos = int(valor % 60)
    # Dividindo as horas por 24, obtemos o número total de dias
    dias = int(horas / 24)
    # O resto da divisão por 24 nos dá o número de horas restantes
    horas = int(horas % 24)
    return dias, horas, minutos, segundos

def converter_horas(valor):
    # Converte horas em segundos, minutos e dias
    # Multiplicando a parte fracionária do valor por 60, obtemos o número de minutos
    minutos = int((valor % 1) * 60)
    # Multiplicando a parte fracionária dos minutos por 60, obtemos o número de segundos
    segundos = int((((valor % 1) * 60) % 1) * 60)
    # Dividindo o valor por 24, obtemos o número total de dias
    dias = int(valor / 24)
    # O resto da divisão por 24 nos dá o número de horas restantes
    horas = int(valor % 24)
    return dias, horas, minutos, segundos

def converter_dias(valor):
    # Converte dias em segundos, minutos e horas
    segundos = 0
    minutos = 0
    # Multiplicando a parte fracionária do valor por 24, obtemos o número de horas
    horas = int((valor % 1) * 24)
    dias = int(valor)
    return dias, horas, minutos, segundos

def exibir_tempo(dias, horas, minutos, segundos):
    # Exibe o resultado em um formato legível
    if dias >= 1:
        print(f"{dias} dia(s), {horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)")
    elif horas >= 1:
        print(f"{horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)")
    elif minutos >= 1:
        print(f"{minutos} minuto(s) e {segundos} segundo(s)")
    else:
        print(f"{segundos} segundo(s)")

def converter_tempo():
    # Pede ao usuário para escolher a opção desejada e digitar o valor
    opcao = input("Digite a opção desejada (segundos, minutos, horas ou dias): ")
    valor = input("Digite o valor: ")
    
    # Converte o valor digitado pelo usuário em um número inteiro ou de ponto flutuante
    try:
        valor = int(valor)
    except ValueError:
        valor = float(valor)

    # Chama a função apropriada com base na opção escolhida pelo usuário
    if opcao == "segundos":
        dias, horas, minutos, segundos = converter_segundos(valor)
    elif opcao == "minutos":
        dias, horas, minutos, segundos = converter_minutos(valor)
    elif opcao == "horas":
        dias, horas, minutos, segundos = converter_horas(valor)
    elif opcao == "dias":
        dias, horas, minutos, segundos = converter_dias(valor)

    # Exibe o resultado usando a função exibir_tempo()
    exibir_tempo(dias, horas, minutos, segundos)

# Executa a função principal
converter_tempo()