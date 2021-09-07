from fastapi import FastAPI, APIRouter
from config import config
from db import db,db_read,db_write
#from fastapi_mail import FastMail, MessageSchema,ConnectionConfig





router = APIRouter()

# Список акций
@router.get('/list')
async def test_headers():
  comp_list=db.get(table='company')
  return {
    'success':True,
    'data':comp_list
  }

