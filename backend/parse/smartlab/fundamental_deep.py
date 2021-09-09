import sys
sys.path.append("../../")
from db import db
import requests

from lib.routines import get_report_id, save_company
from lib.parse_fundamental_deep import parse_fundamental_deep
'''
    Глубокий сбор фундаментальной информации
'''
url='https://smart-lab.ru/'
comp_list=db.get(
  table='company',
  select_fields='id,fundamental_link,header',
  #where='id=186'

)
for c in comp_list:
  parse_fundamental_deep(db,c)
  if not c['fundamental_link']: continue
  print(c)


#response = requests.get(url)
#print('response:',response.text)
#bs_content = bs(response.text, 'lxml')
#table=bs_content.find('table', class_='trades-table')

# заголовки таблицы
