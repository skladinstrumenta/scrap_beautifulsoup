import requests
from bs4 import BeautifulSoup

url = 'https://book24.ua/ua/catalog/ukrainskaya_literatura/'
r = requests.get(url)


soup = BeautifulSoup(r.text, "lxml")
# Если делать в писочнице, то сначала нужно сделать 'import lxml'

# Можно и так, но парсит медленнее
# soup = BeautifulSoup(r.text, 'html.parser')


data =[]
list_books = soup.findAll('div', class_='item_info')

for book in list_books:
    title = book.find('div', class_='item-title').find('span').text.upper()
    author = book.find('div', class_='catalog-item-info-bottom-manufacturer').find('a').text
    price = book.find('span', class_='price_value').text + 'грн'
    link = 'https://book24.ua' + book.find('a', class_='dark_link option-font-bold font_sm').get('href')
    data.append([title, author, price, link])
# print(data)
for item in data:
    print(item)

