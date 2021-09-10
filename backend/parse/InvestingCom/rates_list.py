name='name'
label='label'
description='description'
small_desc='small_desc'
on='on'
percent='percent'
body='body'
LIST=[
  {
    name:'pe',description: 'P/E',
    body:'коэффициент цена / прибыль',
    label: 'P/E Ratio TTM',
    on: True
  },
  {
    name:'ps',description: 'P/S',
    label: 'Price to Sales TTM',
    on: True
  },
  {
    name: 'p_cf',
    description:'Price/Cash Flow Ratio',
    'body':'''
      Отношение «Цена/Денежный Поток» (Price/Cash Flow Ratio, P/CF) –
      финансовый коэффициент, с помощью которого можно сравнить рыночную капитализацию компании (рыночную цену акции) с величиной 
      ее денежного потока от операций, что позволяет сделать выводы о способности
    ''',
    label:'Price to Cash Flow MRQ',
    on: False
  },
  {
    label:'Price to Free Cash Flow TTM',name:'p_fcf',
    description:'Р/FCF (Price/Free Cash Flow, FCF, Цена/Свободный денежный поток)',
    on: False
  },
  {
    label:'Price to Book MRQ',name:'pb',
    description:'P/B',
    on: True
  },
  {
    label:'Price to Tangible Book MRQ',name:'ptbv',
    description:'PTBV',
    on: False
  },
  {
    label:'Gross margin TTM',name:'COGS',
    small_desc: 'COGS',
    description:'Валовая прибыль',
    body:'<b>Gross margin</b> - это выручка компании за вычетом себестоимости реализованных товаров (COGS)',
    on: False,
    percent: 1
  },
  {
    label:'Gross Margin 5YA',name:'COGS_5ya',
    description:'Валовая прибыль за 5 лет',
    on: False,
    percent: 1
  },
  {
    label:'Operating margin TTM',name:'operating_margin',
    description:'Операционная рентабельность',
    on: True,
    percent: 1
  },
  {
    label:'Operating margin 5YA',name:'operating_margin_5ya',
    description:'Операционная рентабельность за 5 лет',
    on: False,
    percent: 1
  },
  {
    label:'Pretax margin TTM',name:'pentax_margin',
    description:'Рентабельность до налогообложения',
    on: False,
    percent: 1
  },
  {
    label:'Pretax margin 5YA',name:'pentax_margin_5ya',
    description:'Рентабельность до налогообложения 5Y',
    on: False,
    percent: 1
  },
  {
    label:'Net Profit margin TTM', name:'net_profit_margin',
    description:'Чистая рентабельность',
    on: True,
    percent: 1
  },
  {
    label:'Net Profit margin 5YA',name:'net_profit_margin_5ya',
    description:'',
    on: False,
    percent: 1
  },
  {
    label:'Revenue/Share TTM',name:'eps',
    description:'Earnings per share, EPS',
    on: False
  },
  {
    label:'Basic EPS ANN',name:'basic_eps',
    description:'BASIC_EPS',
    on: False
  },
  {
    label:'Diluted EPS ANN',name:'deluded_eps',
    description:'Diluted EPS, разводнённая прибыль на акцию',
    on: False
  },

  {
    label:'Book Value/Share MRQ',name:'bvps',
    description:'BVPS',
    on: False
  },
  {
    label:'Tangible Book Value/Share MRQ',name:'tbvps',
    description:'TBVPS',
    on: False
  },
  {
    label:'Cash/Share MRQ',name:'cps',
    description:'SPS Cash/Share Денежная стоимость акции (Cash per Share)',
    on: False
  },
  {

    label:'Cash Flow/Share TTM',name:'cfps',
    description:'CFPS',
    on: False
  },
  {

    label:'Return on Equity TTM',name:'roe',
    description:'ROE',
    on: True,
    percent: 1
  },
  {
    label:'Return on Equity 5YA',name:'roe_5ya',
    description:'ROE 5Y',
    on: False,
    percent: 1
  },
  {
    label:'Return on Assets TTM',name:'roa',
    description:'ROA',
    on: True,
    percent: 1
  },
  { 
    label:'Return on Assets 5YA',name:'roa_5ya',
    description:'ROA 5Y',
    on: False,
    percent: 1
  },
  { 
    label:'Return on Investment TTM',name:'roi',
    description:'ROI',
    on: True,
    percent: 1
  },
  { 
    label:'Return on Investment 5YA',name:'roi_5ya',
    description:'ROI 5Y',
    on: False,
    percent: 1
  },
  { 
    label:'EPS(MRQ) vs Qtr. 1 Yr. Ago MRQ',name:'EPS_vs_QTR',
    description:'Прибыль на акцию за последний квартал к квартальной год назад ',
    on: False,
    percent: 1
  },
  { 
    label:'EPS(TTM) vs TTM 1 Yr. Ago TTM',name:'EPS_vs_TTM',
    description:'Прибыль на акцию за последние 12 месяцев к аналогичному периоду год назад TTM',
    on: False,
    percent: 1
  },
  { 
    label:'5 Year EPS Growth 5YA',name:'5y_eps_growth_5ya',
    description:'Рост прибыли на акцию за 5 лет',
    on: False,
    percent: 1
  },
  { 
    label:'Sales (MRQ) vs Qtr. 1 Yr. Ago MRQ',name:'sales_vs_qtr_1y_ago',
    description:'Продажи за последний квартал к квартальным год назад',
    on: False,
    percent: 1
  },
  { 
    label:'Sales (TTM) vs TTM 1 Yr. Ago TTM',name:'sales_vs_ttm_1y_ago',
    description:'Продажи за последние 12 месяцев к аналогичному периоду год назад',
    on: False,
    percent: 1
  },
  { 
    label:'5 Year Sales Growth 5YA',name:'sales_growth_5y',
    description:'Рост продаж за последние 5 лет',
    on: False,
    percent: 1
  },
  { 
    label:'5 Year Capital Spending Growth 5YA',name:'capital_spending_growth_5y',
    description:'Рост капитальных расходов за последние 5 лет',
    on: False,
    percent: 1
  },
  { 
    label:'Quick Ratio MRQ',name:'quick_ratio',
    description:'коэффициент быстрой ликвидности',
    on: False
  },
  { 
    label:'Current Ratio MRQ',name:'current_ratio',
    description:'текущая ликвидность',
    on: False
  },
  { 
    label:'LT Debt to Equity MRQ',name:'ltde',
    description:'коэффициент долгосрочных обязательств по отношению к собственному или акционерному капиталу',
    on: False,
    percent: 1
  },
  { 
    label:'Total Debt to Equity MRQ',name:'de',
    description:'D/E',
    on: False,
    percent: 1
  },
  { 
    label:'Asset Turnover TTM',name:'asset_turnover',
    description:'оборачиваемость активов',
    on: False
  },
  { 
    label:'Inventory Turnover TTM',name:'inventory_turnover',
    description:'оборачиваемость запасов',
    on: False
  },
  { 
    label:'Revenue/Employee TTM',name:'revenue_per_employee',
    description:'доход на сотрудника',
    on: False
  },
  { 
    label:'Net Income/Employee TTM',name:'nipe',
    description:'NIPE',
    on: False
  },
  { 
    label:'Receivable Turnover TTM',name:'receivable_turnover',
    description:'Оборачиваемость дебиторсокой задолженности',
    on: False
  },
  { 
    label:'Dividend Yield ANN',name:'dividend_yield',
    description:'Див. доходность (год)',
    percent:True,
    on: False
  },
  { 
    label:'Dividend Yield 5 Year Avg. 5YA',name:'dividend_yield_5ya',
    description:'Див. доходность, средняя за 5 лет',
    percent:True,
    on: False
  },
  { 
    label:'Dividend Growth Rate ANN',name:'dividend_growth_rate',
    description:'Скорость дивидендного роста',
    percent:True,
    on: False
  },
  { 
    label:'Payout Ratio TTM',name:'dpr',
    description:'DPR',
    percent:True,
    on: False
  }
]



def get_rates_dict():
  D={}
  for l in LIST:
    D[l['label']]=l['name']
  
  return D




def get_key_list(): # Возвращяет список параметров в виде ключей
  out_dict={
    'header':{
      'header':'Наименование',
      'on':True
    }
  }

  for l in LIST:
    per=False
    if percent in l and l[percent]:
      per=True
    b=''
    if body in l:
      b=l[body]

    out_dict[l['name']]={
      'header':l['description'],
      'percent':per,
      'body':b,
      'on':l['on']
    }
    
  return out_dict