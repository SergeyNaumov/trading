'''
получение кода финам по стикеру
  POST https://ru.investing.com/search/service/searchTopBar
  search_text: TRMK

'''
import sys
import json
import time
sys.path.append("../../")

import requests
from db import db


headers = {

  'accept':'application/json, text/javascript, */*; q=0.01',
  'accept-language':'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'content-length':'16',
  'content-type':'application/x-www-form-urlencoded',
  #'cookie':'adBlockerNewUserDomains=1630910473; udid=33277d43912d54491794c8a2a10c51db; protectedMedia=2; top100_id=t1.-1.1293533140.1630910475253; _ym_uid=16309104776229278; _ym_d=1630910477; tmr_lvid=ff2f1d27847bfe82b590f420722dbf12; tmr_lvidTS=1630910476568; G_ENABLED_IDPS=google; PHPSESSID=73vmsmvke9ailub5grc3gtjbct; geoC=RU; gtmFired=OK; StickySession=id.48344778765.901ru.investing.com; _gid=GA1.2.1476155835.1631167930; _ym_isad=1; adsFreeSalePopUp=3; smd=33277d43912d54491794c8a2a10c51db-1631193289; __cf_bm=wrDp1t7xf7gJJmrLnNGt11DAyXTIrSQ9uAEmM902J6w-1631193291-0-Actrs3vo/syQNwTwc5489ePp18ZLu/3ry8VGJ2oMTa6Zj8Lg3ptHmWj5Ot6tJh/r9aJQK8uj+PdKauC2jlZVRlTgVQ6ZUanJo9i46h3WPXqxxZTtgaYtI44HVDuTF9sw0A==; OB-USER-TOKEN=5a73b360-9e2f-4143-bd73-483b234cb09a; __cflb=0H28uv9TXEXY1dxGsSkwBDbonFi7JwudeCy14EHnXTR; logglytrackingsession=8cb7a1ce-fd49-433e-9d56-bb79cfe71fd8; _ym_visorc=w; __gads=ID=3f0421fb3355b056:T=1631193357:S=ALNI_MaYsewmSuuM-xM41vTiioz5dohkew; _fbp=fb.1.1631193358240.1976478831; _ga=GA1.2.1201543066.1630910475; comment_notification_210483809=1; adsFreeSalePopUp0c50f84b1b4a6c1f482f21a2a1a12274=1; r_p_s_n=1; _ga_H1WYEJQ780=GS1.1.1631193302.2.1.1631193390.49; UserReactions=true; SideBlockUser=a%3A2%3A%7Bs%3A6%3A%22stacks%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Ba%3A4%3A%7Bi%3A0%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bi%3A13684%3Bs%3A10%3A%22pair_title%22%3Bs%3A7%3A%22Gazprom%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A21%3A%22%2Fequities%2Fgazprom_rts%22%3B%7Di%3A1%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bi%3A13709%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A23%3A%22%2Fequities%2Fsg-mechel_rts%22%3B%7Di%3A2%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A5%3A%2221468%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A13%3A%22%2Fequities%2Ftmk%22%3B%7Di%3A3%3Ba%3A3%3A%7Bs%3A7%3A%22pair_ID%22%3Bs%3A5%3A%2213786%22%3Bs%3A10%3A%22pair_title%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22pair_link%22%3Bs%3A26%3A%22%2Fequities%2Fgazprom-neft_rts%22%3B%7D%7D%7Ds%3A10%3A%22stack_size%22%3Ba%3A1%3A%7Bs%3A11%3A%22last_quotes%22%3Bi%3A8%3B%7D%7D; last_visit=1631183213157::1631194013157; t1_sid_-1=s1.944182795.1631193295394.1631194013166.4.13.17; tmr_detect=0%7C1631194019497; nyxDorf=MTA1YGAoNWo2aWt5bz5hYDNjZSA%2FOTAxZ24%3D; ses_id=MX9lJDE%2BNz8zdzo8M2JlZjFgNGtlajc2YmthYjI8Y3UwJDU7ZDNhJzQ7aSdubTMvZ2A3NT89MmFnMjM4MGBubjFiZTYxZzc%2FM2E6MDNlZWExZjQ8ZWs3NGJhYWMyMGNhMD41NmRjYWw0ZWk3bmYzb2d1Nys%2FezIjZzUzYzBxbikxPmUkMWE3ajNmOmczYGUyMWY0PGVrNzJiYmE2MjNjezB7; tmr_reqNum=48',
  'origin':'https://ru.investing.com',
  'referer':'https://ru.investing.com/equities/',
  'sec-ch-ua':'"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
  'sec-ch-ua-mobile':'?0',
  'sec-ch-ua-platform':'"Linux"',
  'sec-fetch-dest':'empty',
  'sec-fetch-mode':'cors',
  'sec-fetch-site':'same-origin',
  'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
  'x-requested-with':'XMLHttpRequest'
}

def get_record_from_site(c):
  d=requests.post('https://ru.investing.com/search/service/searchTopBar',
    data={'search_text':c['sticker']},
    headers=headers
  )
  quotes=json.loads(d.text)['quotes']
  for q in quotes:
    if q['symbol']==c['sticker']: 
      return {
        'id': q['pairId'],
        'header': q['name'],
        'sticker': c['sticker'],
        'code': q['link'].split('/')[-1]
      }
  
  return False


comp_list=db.query(
  query='''
    SELECT
      c.id, c.sticker
    from
      company c
      LEFT JOIN investing_com_stock ics ON ics.sticker=c.sticker
    WHERE ics.id is null
  '''
)

for c in comp_list:
  

  data=get_record_from_site(c)
  time.sleep(1)
  if data:
    db.save(
      debug=1,
      table="investing_com_stock",
      data=data
    )
  time.sleep(1)
  
  

