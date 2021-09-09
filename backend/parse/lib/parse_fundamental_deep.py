from bs4 import BeautifulSoup as bs
import requests
import re

base_url='https://smart-lab.ru'

def parse_fundamental_deep(db,comp):
  print(comp['header'])
  if not comp['fundamental_link']:
    return
  print(base_url+comp['fundamental_link'])
  response = requests.get(base_url+comp['fundamental_link'])
  #print('response:',response.text)
  bs_content = bs(response.text, 'lxml')
  table=bs_content.find('table', class_='financials')
  
  i=0
  
  years_hash=get_years_hash(table)
  
  get_indicator(db,comp,years_hash,table,'p_e','pe')
  get_indicator(db,comp,years_hash,table,'p_s','ps')
  get_indicator(db,comp,years_hash,table,'capex','capex')
  get_indicator(db,comp,years_hash,table,'opex','opex')
  get_indicator(db,comp,years_hash,table,'assets','assets')
  get_indicator(db,comp,years_hash,table,'net_assets','net_assets')
  get_indicator(db,comp,years_hash,table,'debt','debt')
  get_indicator(db,comp,years_hash,table,'cash','cash')
  get_indicator(db,comp,years_hash,table,'net_debt','net_debt')
  get_indicator(db,comp,years_hash,table,'common_share','common_share')
  get_indicator(db,comp,years_hash,table,'number_of_shares','number_of_shares')
  get_indicator(db,comp,years_hash,table,'revenue','revenue')
  get_indicator(db,comp,years_hash,table,'net_income','net_income')
  get_indicator(db,comp,years_hash,table,'dividend_payout','dividend_payout')
  get_indicator(db,comp,years_hash,table,'div_yield','div_yield')
  get_indicator(db,comp,years_hash,table,'div_yield_priv','div_yield_priv')
  get_indicator(db,comp,years_hash,table,'market_cap','market_cap')
  get_indicator(db,comp,years_hash,table,'ev','ev')
  get_indicator(db,comp,years_hash,table,'bv_share','bv_share')
  get_indicator(db,comp,years_hash,table,'eps','eps')
  get_indicator(db,comp,years_hash,table,'capital','capital')
  
  '''

  '''
  get_indicator(db,comp,years_hash,table,'roe','roe')
  get_indicator(db,comp,years_hash,table,'roa','roa')
  
  get_indicator(db,comp,years_hash,table,'p_bv','p_bv')
  get_indicator(db,comp,years_hash,table,'ev_ebitda','ev_ebitda')
  get_indicator(db,comp,years_hash,table,'debt_ebitda','debt_ebitda')
  


  #quit()
  
  
  

def get_indicator(db,comp,years_hash,table,field_attr,indicator_name):
  tr=table.find('tr',{"field":field_attr})
  if not tr:
    return 
  j=0
  td_list=tr.find_all('td')
  if not td_list or not len(td_list):
    return 
  for td in tr.find_all('td'):

    if j in years_hash:
      value=td.string

      
      value=re.sub("[^0-9\.]", "", value)
      if value:
        db_save(db,{
          'company_id':comp['id'],'year': years_hash[j],'value': value,'fin_indicator': indicator_name,
        })

    j+=1

def db_save(db,data):
  db.save(
    debug=0,
    table='company_year',
    data=data,
    replace=1
  )
def get_years_hash(table):
  tr=table.find('tr',class_='header_row')
  td_list=tr.find_all('td')
  years_hash={}
  j=0 # порядковый номер ячейки
  for td in td_list:
    value=td.string
    if value and value.isdigit():

      years_hash[j]=value
    j+=1
  return years_hash