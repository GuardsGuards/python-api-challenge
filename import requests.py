import requests
from bs4 import BeautifulSoup
import json
from pandas import DatFrame as df

page = requests.get(XYZ)
soup = BeautifulSoup(page.text, 'html.parser')

bolded = soup.find_all(class_ = 'itemlist')
bolded_link = []

for i in bolded:
    cont = i.content
    attr = cont.attrs
    hrefs = attr['href']
    bolded_link.append(href)

    