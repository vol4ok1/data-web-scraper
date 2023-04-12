import requests
from bs4 import BeautifulSoup

url = 'https://www.kilobaitas.lt/kompiuteriai_ir_komponentai/kompiuteriu_komponentai/vaizdo_plokstes_gpu/kategorija.aspx?groupfilterid=432&orderby=2&limit=200&cf=4086'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for item in soup.select('.product-item'):
    name = item.select_one('.product-item-title').text.strip()
    price = item.select_one('.price').text.strip()
    print(name, price)
