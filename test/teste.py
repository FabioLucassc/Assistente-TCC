import os
import string
import urllib.request, json
import re

# with urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q=jundiai&units=metric&appid=7bad02a3959dce28b73e516b02972c73&lang=pt_br") as url:
#     data = json.loads(url.read().decode())
# print(data)
# print(data['main']['temp'])
# print(data['weather'])

lista = os.listdir('D:\\Users\\fabio\\Desktop')

# pattern=re.compile(r'Blitz')

str_match = [x for x in lista if re.search('blitz', x)]
print(str_match)

word1 = str(str_match)
word2 = '[]\''

for i in word2:
    word1 = word1.replace(i, '')

print(word1)

a = (map(lambda x: x.lower(), lista))
b = list(a)
print(b)

# os.startfile('D:\\Users\\fabio\\Desktop\\'+ word1)


# index = lista.index(1)

teste = lista.__getitem__(0)
print('The index of i:', str(teste))

for i in range(len(lista)):
    print(lista.__getitem__(i))