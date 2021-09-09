# Получаем список котировок со страницы:
# https://habr.com/ru/post/332700/
import requests
from bs4 import BeautifulSoup as bs
import json
import sys
sys.path.append("../../")
from db import db

"""
  Собирает список котировок с finam, обновляет изменение цены и стоимость акции
"""

# https://www.finam.ru/quotes/stocks/foreign/ -- зарубежные
# https://www.finam.ru/quotes/stocks/usa/ -- США
base_url='https://www.finam.ru/quotes/stocks/russia/' 
# $('#react_1').data('json')['table']['body'][0] -- первый элемент таблицы
def get_content(url,page):
  if page>1: url+=f'?pageNumber={page}'
  response = requests.get(url)
  soup = bs(response.text, 'lxml')
  
  if soup:
    div=soup.find("div", { "id" : "react_1" })
    
    if div and div.has_attr('data-json'):
      return json.loads(div.attrs['data-json'])
  
  return ''





page=1;
while 1:
  url=base_url
  content=get_content(base_url,page)
  parse_ok=0
  if 'table' in content and 'body' in content['table']:
    body=content['table']['body']
    
    for b in body:
      #print()
      data={
        'id': b['instrument']['id'],
        'header': b['instrument']['name'],
        'finam_code': b['instrument']['quoteUrl'].split('/')[-1],
        'url': b['instrument']['url'],
        'price': b['last'],
        'price_change': b['priceChange']['value'].replace('%',''),
        'currency':b['measureUnit'],
        'last_update':'func:now()'
      }
      exists=db.query(query='select id from finam_stock where id=%s',values=[data['id']],onevalue=1)
      if exists:
        db.save(
          table='finam_stock',
          update=1,
          where=f"id={data['id']}",
          debug=1,
          data=data
        )
        
      else:
        db.save(
          table='finam_stock',
          data=data
        )


    if not len(body): quit()

  else:
    quit()

  page+=1



 #<div id="react_1" data-json="