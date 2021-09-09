import sys
sys.path.append("../../")
from db import db
import requests
from bs4 import BeautifulSoup as bs
from lib.routines import get_report_id, save_company

'''
    Парсинг фундаментальных показателей с https://smart-lab.ru/q/shares_fundamental/order_by_p_e/asc/
'''
url='https://smart-lab.ru/q/shares_fundamental/'
response = requests.get(url)
#print('response:',response.text)
bs_content = bs(response.text, 'lxml')
table_list=bs_content.find_all('table', class_='trades-table')

fields=[
{
  1: 'header', # название
  3: 'fundamental_link',
  4: 'market_cap', # капитализация
  5: 'ev', 
  6: 'revenue',
  7: 'net_income',
  8: 'div_yield',
  9: 'div_yield_priv',
  10: 'div_payout_ratio',
  11: 'pe',
  12: 'ps',
  13: 'pb',
  14: 'ev_ebitda',
  15: 'ebitda_margin',
  16: 'debt_ebitda',
  17: 'report_name'
},
{
  1: 'header', # название
  3: 'fundamental_link',
  4: 'market_cap', # капитализация
  # 5: '' -- чистый операционный доход
  #5: 'ev', 
  #6: 'revenue',
  #: 'net_income',
  7: 'div_yield',
  8: 'div_yield_priv',
  9: 'div_payout_ratio',
  10: 'pe',
  11: 'pb',
  # 12: '',ЧПМ, %
  13: 'roe',
  14: 'roa',
  #16: 'debt_ebitda',
  15: 'report_name'
},
]

table_idx=0
for table in table_list:
  # заголовки таблицы
  th_list=table.find_all('th')



  #i=0
  # для проверки th
  # for th in th_list:
  #   if i in fields:
  #     field_name=fields[i]
  #     print(f'''{i}, ({field_name}) => {th}''')
  #   i+=1

  tr_list=table.find_all('tr')
  tr_num=0
  for tr in tr_list:
    data={
      'ev': None,'revenue': None,
      'ps': None, 'net_income': None,
      'debt_ebitda': None,'report_name':''
    }
    td_list=tr.find_all('td')

    tr_num+=1
    if tr_num==1: continue
    
    i=0


    for td in td_list:
      field_name=''
      value=td.string

      if i in fields[table_idx]:
        field_name=fields[table_idx][i]
        
        if field_name=='report_name':
          data['report_id']=get_report_id(db,value)
        elif field_name=='fundamental_link':
          
          data['fundamental_link']=td.find('a')['href']
          data['sticker']=data['fundamental_link'].split('/')[2]
          
        elif value:
          if not (field_name in ('header')):
            value=value.replace(' ', '')
            value=value.replace('%', '')
          data[field_name]=value
        
        #if table_idx==1:
        #  print(i,'=>',td,' ',field_name)
        #  print(data)
      
      i+=1
        
        

      #print(f''' {i}, ({field_name}) => {td} / {value}''')

    #print(data)
    #quit()
  
    if table_idx==1:
  
      
      save_company(db,data)
  
  table_idx+=1
    


