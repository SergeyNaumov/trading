from rates_list import get_rates_dict
import re 
dict_detect=get_rates_dict()



def get_ratio_by_name(td_list):
  # получаем название ratio по содержимому ячейки
  #print(td_list)
  if len(td_list)==3:
    label=td_list[0].text

    value=td_list[1].string
    
    
    ratio_name=''
    if label in dict_detect:
      ratio_name=dict_detect[label]

    if ratio_name:
      value=value.replace('%','').replace(',','')
      if value=='-': value=''
      
      if re.search(r'M$', value):
        value=float(value.replace('M',''))
        value*=1000000
      
      elif re.search(r'K$', value):
        value=float(value.replace('K',''))
        value*=1000
    
      return {'name':ratio_name, 'value':value}
    
  #print('NONE:',td_list)
  return None