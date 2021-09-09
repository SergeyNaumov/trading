import re
report_hash={}
def get_report_id(db,value):
  value=value.strip()

  if value in report_hash:
    return report_hash[value]
  
  report_id=db.query(
    query='SELECT id from report where header=%s',
    values=[value],
    onevalue=1
  )
  if report_id:
    report_hash[value]=report_id
    return report_id
  
  report_id=db.save(
    table='report',
    data={
      'header':value
    }
  )

  return report_id

def save_company(db,data):
  debug=0

  
  if not('sticker' in data) or not data['sticker'] or re.search(r'[^a-zA-Zа-яА-Я]',data['sticker'] ):
    return 

  exists=db.get(
    table='company',
    where="sticker=%s",
    values=[data['sticker']],
    onerow=1
  )

  if exists:
    db.save(
      table='company',
      debug=debug,
      update=1,
      where=f'''id="{exists['id']}"''',
      data=data,
    )
  else:
    db.save(
      table='company',
      debug=debug,
      data=data,
    )