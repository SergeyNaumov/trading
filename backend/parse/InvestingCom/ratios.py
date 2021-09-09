'''
Получаем фундаментальеык показатели со
Страницы вида:
  https://ru.investing.com/equities/{ code }-ratios
  
  https://ru.investing.com/equities/abrau-durso-oao-ratios

'''

import requests
from bs4 import BeautifulSoup as bs
import json
import sys
sys.path.append("../../")
from db import db
#from ratio import html as html_ratio
from lib.get_ratio_by_name import get_ratio_by_name

headers = {

'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#'accept-encoding: gzip, deflate, br
'accept-language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
'cache-control':'max-age=0',
#'cookie: logglytrackingsession=7b29197e-14a7-4c49-9f7b-caf741b45750; G_AUTHUSER_H=0; adBlockerNewUserDomains=1630910473; udid=33277d43912d54491794c8a2a10c51db; protectedMedia=2; top100_id=t1.-1.1293533140.1630910475253; _ym_uid=16309104776229278; _ym_d=1630910477; tmr_lvid=ff2f1d27847bfe82b590f420722dbf12; tmr_lvidTS=1630910476568; G_ENABLED_IDPS=google; PHPSESSID=73vmsmvke9ailub5grc3gtjbct; gtmFired=OK; StickySession=id.48344778765.901ru.investing.com; _gid=GA1.2.1476155835.1631167930; _ym_isad=1; adsFreeSalePopUp=3; smd=33277d43912d54491794c8a2a10c51db-1631193289; OB-USER-TOKEN=5a73b360-9e2f-4143-bd73-483b234cb09a; logglytrackingsession=8cb7a1ce-fd49-433e-9d56-bb79cfe71fd8; _ym_visorc=w; __gads=ID=3f0421fb3355b056:T=1631193357:S=ALNI_MaYsewmSuuM-xM41vTiioz5dohkew; _fbp=fb.1.1631193358240.1976478831; _ga=GA1.2.1201543066.1630910475; comment_notification_210483809=1; adsFreeSalePopUp0c50f84b1b4a6c1f482f21a2a1a12274=1; r_p_s_n=1; _ga_H1WYEJQ780=GS1.1.1631193302.2.1.1631193390.49; G_AUTHUSER_H=0; SideBlockUser=a%3A2%3A%7Bs%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A6%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bi%3A13684%3Bs%3A10%3A%22pair_title%22%3Bs%3A7%3A%22Gazprom%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A21%3A%22%2Fequities%2Fgazprom_rts%22%3B%7Di%3A1%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bi%3A13709%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A23%3A%22%2Fequities%2Fsg-mechel_rts%22%3B%7Di%3A2%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A5%3A%2221468%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A13%3A%22%2Fequities%2Ftmk%22%3B%7Di%3A3%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A5%3A%2213786%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A26%3A%22%2Fequities%2Fgazprom-neft_rts%22%3B%7Di%3A4%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A6%3A%22945998%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A25%3A%22%2Fequities%2Fabrau-durso-oao%22%3B%7Di%3A5%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A5%3A%2213678%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A25%3A%22%2Fequities%2Fafk-sistema_rts%22%3B%7D%7D%7Ds%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7D%7D; geoC=RU; __cflb=0H28uv9TXEXY1dxGsSwM21AWkmXN8C3KG2UdAbY4NUb; UserReactions=true; outbrain_cid_fetch=true; __cf_bm=VnosSF34_w47TmJWXYaCVPeYIBzb3R91PC04z.eaF58-1631197644-0-AVCgMNFwCqNlATKi0AK6m5OTxdv0lUWDhKtySP5SSDak50VxG4WOegwLCwLfWtVTybNWGTyX1BuO1EK/s0Sv3xJ0bRQ2sz+oWlF3o9eDZDUH94RzLea+sY9hSUfo4I3xLQ==; _gat_allSitesTracker=1; _gat=1; last_visit=1631187015308::1631197815308; t1_sid_-1=s1.944182795.1631193295394.1631197815320.4.20.24; ses_id=MX9lJG9gZm5hJT44Zjc0NzVkP2AxPjIzMzo1NjI8Y3U0IGJsNWIydDI9PnBmZWJ%2BZ2cyY2NkMWA2ZGA5ZDM3YzE2ZTZvOGY7YTU%2BZmZkND81ZD8yMTEyNDM6NTMyMmM4NGZiYjU2MmQybT5lZmliaWd1Mi5jJzEgNmRgMGQlN3AxPmUkbz9mO2E0PmNmNDRnNWM%2FYzFlMjMzYTU3MmFjezR%2F; nyxDorf=ODk%2Fam4mYT4wb2Bybz44OTRkMXQ0Mjc2YGk%3D; tmr_detect=0%7C1631197822450; tmr_reqNum=85
'sec-ch-ua':'"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Linux"',
'sec-fetch-dest':'document',
'sec-fetch-mode':'navigate',
'sec-fetch-site':'none',
'sec-fetch-user':'?1',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}




def report_table_process(table,set_attr):
  tr_list=table.find_all('tr')
  
  for tr in tr_list:
    ratio=get_ratio_by_name(tr.find_all('td'))
    if ratio:
      if not ratio['value']: ratio['value']='NULL'
      set_attr.append(f"{ratio['name']}={ratio['value']}")

  set_attr.append(f"registered=now()")



def get_ratios(c):
  #print(f'https://investing.com/equities/{c["code"]}-ratios')
  html = requests.get(f'https://investing.com/equities/{c["code"]}-ratios', headers=headers).text
  #html=html_ratio
  
  soup = bs(html, 'lxml')
  #return soup
  ratio_table=soup.find('table',class_='ratioTable')
  if not ratio_table: return
  tables=ratio_table.find_all('table',class_='reportTbl')
  #print(len(tables))
  #quit()
  # 8 таблиц
  j=1
  set_attr=[]
  for t in tables:
    #print(j,'=> ')
    report_table_process(t,set_attr)
    j+=1
  #print('set_attr:',set_attr)
  if len(set_attr):
    db.query(
      query=f"UPDATE investing_com_stock SET {', '.join(set_attr) } WHERE id={c['id']}",
    )
  



comp_list=db.query(query="SELECT * from investing_com_stock where id>13786 order by id")
for c in comp_list:
  print(c['id'],'=>',c['header'])

  get_ratios(c)
  
  #print(c['header'])