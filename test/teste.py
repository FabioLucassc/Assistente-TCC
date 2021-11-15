import string
import urllib.request, json
import re

with urllib.request.urlopen("https://economia.awesomeapi.com.br/json/last/USD-BRL") as url:
    data = json.loads(url.read().decode())
valor = round(float(data['USDBRL']['ask']), 2)
# print(valor)


with urllib.request.urlopen("https://viacep.com.br/ws/13221251/json/") as url:
    data = json.loads(url.read().decode())
print(data)
print(data['logradouro'])

temp_string = "buscar cep 13221-251"

out = temp_string.translate(str.maketrans('', '', string.punctuation))
numbers = [int(temp)for temp in out.split() if temp.isdigit()]
cep_limpo = ''.join(char for char in str(numbers) if char.isalnum())

print(cep_limpo)