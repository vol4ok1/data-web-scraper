from bs4 import BeautifulSoup
import requests

kilobaitas = requests.get('https://www.kilobaitas.lt/kompiuteriai_ir_komponentai/kompiuteriu_komponentai/vaizdo_plokstes_gpu/kategorija.aspx?groupfilterid=432&orderby=2&limit=200&cf=4086').text

kilobaitas = BeautifulSoup(kilobaitas, 'lxml')


def uzduotis1():
    palyginimas = kilobaitas.find('div', {'class', 'pricebox'})
    
print(palyginimas)


