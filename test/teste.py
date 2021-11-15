import urllib.request, json

with urllib.request.urlopen("https://economia.awesomeapi.com.br/json/last/USD-BRL") as url:
    data = json.loads(url.read().decode())
valor = round(float(data['USDBRL']['ask']), 2)
print(valor)