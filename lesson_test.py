import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = 'https://rabota.by/vacancies/programmist_python/bez_opyta_raboty'
FILE_NAME = 'vacancy.csv'

r = requests.get(URL_TEMPLATE, headers={'User-Agent': 'Custom'})
text = r.text
soup = bs(text, 'html.parser')
page = soup.find('h3', class_='bloko-header-section-3')
print(r.status_code)
print(page)
