"""
    Собираем стикеры для акций с финама
"""
import requests
from bs4 import BeautifulSoup as bs
import json
import sys
sys.path.append("../../")
import re
from db import db

def get_content(url):
  print(url)
  response = requests.get(url)
  return response.text


list_stock=db.query(
  query="SELECT id, finam_code from finam_stock where sticker='' and finam_code<>''"
)

for b in list_stock:
  url=f'https://www.finam.ru/profile/moex-akcii/{b["finam_code"]}/export/'
  html=get_content(url)
  
  finder = re.findall(r'Finam.IssuerProfile.Main.issue\s*=\s*(.*);', html)
  
  if finder:

    ob=json.loads(finder[0].replace(',}','}').replace(', }','}'))
    sticker=ob['company']['code']
    if not sticker:
      sticker=ob['quote']['code']

    if sticker:
      db.save(
        table="finam_stock",
        where=f"id={b['id']}",
        data={
          'sticker':sticker
        },
        update=1,
        debug=1
      )  

