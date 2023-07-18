import requests
from bs4 import BeautifulSoup as BS
import lxml

url = "https://tables.finance.ua/ua/currency/cash/-/ua/eur/0#3:0"

r = requests.get(url)
soup = BS(r.text, "lxml")
curs = soup.select("tr.selected")  # или soup.find_all("tr", class_="selected")

data = {}  # Ассоциативный массив (словарь) для хранения результатов

for tr in curs:
    key = tr.text.strip()  # Содержимое строки <tr> будет ключом
    value = tr.text.strip()  # Текст строки будет значением
    data[key] = value

# Удаление ненужных строк
keys_to_delete = ["ненужный ключ1", "ненужный ключ2"]
for key in keys_to_delete:
    if key in data:
        del data[key]

for item in data:# Вывод результатов в столбик
    print(item)


# data = {
#     "ключ1": "значение1",
#     "ключ2": "значение2",
#     "ключ3": "значение3"
# }
#
# # Удаление ненужных строк
# keys_to_delete = ["ключ2", "ключ3"]
# for key in keys_to_delete:
#     if key in data:
#         del data[key]
#
# print(data)