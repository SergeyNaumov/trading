from fastapi import FastAPI, APIRouter
from config import config
from db import db,db_read,db_write
#from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from parse.InvestingCom.rates_list import get_key_list




router = APIRouter()

# Список акций 
# SMARTLAB
# @router.get('/list')
# async def test_headers():
#   comp_list=db.get(table='company')
#   return {
#     'success':True,
#     'data':comp_list
#   }

# Список акций 
# INVESTING.COM
@router.get('/list')
async def test_headers():
  comp_list=db.get(table='investing_com_stock')
  return {
    'success':True,
    
    'data':{
      'comp_list':comp_list,
      'key_list':get_key_list()
    }
  }

# FROM SMARTLAB
@router.get('/fundamental/{sticker}')
async def get_fundamental(sticker: str):
  comp=db.getrow(table='company',where="sticker=%s",values=[sticker])
  fin_indicator_list=db.query(
    query=f"SELECT fin_indicator,year,value FROM company_year where company_id={comp['id']}  order by fin_indicator, year, value",
    
  )
  indicators={}
  for f in fin_indicator_list:
    if f['fin_indicator'] not in indicators:
      indicators[f['fin_indicator']]=[]

    indicators[f['fin_indicator']].append({'year':f['year'],'v':f['value']})

  indicator_list=db.query(query='select * from fin_indicator order by sort',)

  return {
    'success':True,
    'data':{
      'comp':comp,
      'indicators': indicators,
      'indicator_list':indicator_list
    }
  }