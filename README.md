# Propósito

Porque tenho preguiça.

## Scripts

Este projeto inclui os seguintes scripts:

- **Gerador_JSONS**: Este script gera arquivos JSON baseados na entrada do usuário.

- **Gerador_JSONS_v2**: Uma versão melhorada do Gerador_JSONS. Este script copia um objeto JSON especificado várias vezes em um novo arquivo. Ele primeiro solicita ao usuário o nome do arquivo JSON a ser copiado, o nome do novo arquivo a ser criado e a quantidade de vezes que o objeto deve ser copiado. Este script também inclui uma função para deletar o novo arquivo se ele já existir antes de criar a nova versão.

- **Conversor_Tempo**: Este script permite ao usuário converter unidades de tempo entre segundos, minutos, horas e dias.

- **pyproject.toml** e **poetry.lock**: Estes são arquivos de configuração para o Poetry, que é uma ferramenta para gerenciamento de dependências e empacotamento em Python.

Este projeto também inclui um arquivo JSON de teste que pode ser usado para testar o script Gerador_JSONS_v2.

## Executando os Scripts

Para executar qualquer um dos scripts, você pode usar o seguinte comando:

```bash
python <nome_do_script>.py
```

## Ambiente

Este script foi criado e testado em um ambiente WSL (Windows Subsystem for Linux).