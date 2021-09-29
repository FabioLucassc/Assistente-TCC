import yaml

dados = yaml.safe_load(open('treinamento.yml', 'r', encoding='utf-8').read())

for comando in dados['comandos']:
    print(comando)