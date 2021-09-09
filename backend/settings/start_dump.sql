create table report(
  id int unsigned primary key auto_increment,
  header varchar(255) not null default ''
) engine=innodb default charset=utf8;
# Компании
alter table company add roa decimal(12,2);
create table company(
  id int unsigned primary key auto_increment,
  header varchar(255) not null default '',
  sticker varchar(30) not null default '',
  report_id int unsigned comment 'отчёт',
  market_cap int unsigned  default '0' comment 'Капитализация, млрд руб',
  ev bigint   default '0' comment 'EV, млрд руб',
  revenue bigint   default '0' comment 'Выручка, млрд руб',
  net_income bigint   default '0' comment 'Чистая прибыль',
  div_yield decimal(5,2)  default '0.0' comment 'Див. доходность, акции обычные %',
  div_yield_priv decimal(5,2)  default '0.0' comment 'Див. доходность, акции прив. %',
  div_payout_ratio decimal(12,2)  default '0.0' comment 'ДД/ЧП % ; коэффициент дивидендных выплат в процентах от прибыли',
  pe decimal(12,2)  default NULL comment 'P/E',
  ps decimal(12,2)  default NULL comment 'P/S',
  pb decimal(12,2)  default NULL comment 'P/B',
  roa decimal(12,2)  default NULL comment 'ROA',
  roe decimal(12,2)  default NULL comment 'ROA',
  ev_ebitda decimal(12,2)  default '0.0' comment 'EV/EBITDA',
  ebitda_margin decimal(12,2) default '0.0' comment 'Рентаб. EBITDA',
  debt_ebitda decimal(5,2) default '0.0' comment 'Долг/EBITDA',
  fundamental_link varchar(255) not null default '',

  unique key(sticker)
) engine=innodb default charset=utf8 comment 'компании и фундаментальные показатели';

create table company_year(
  company_id int unsigned not null,
  year int unsigned,
  fin_indicator varchar(20) not null comment 'финансовый показатель',
  value decimal(12,2),
  primary key(company_id,year,fin_indicator)
) engine=innodb default charset=utf8 comment 'Таблица с финансовыми показателями по годам';
drop table fin_indicator;
create table fin_indicator(
  indicator varchar(20) not null primary key,
  header varchar(255) not null default '',
  sort int unsigned not null default '0'
) engine=innodb default charset=utf8;

REPLACE INTO fin_indicator(indicator,header,sort) values
('market_cap','Капитализация, млрд руб',10),
('common_share','Цена акции',20),
('ev','EV, млрд руб',30),
('pe','P/E',40),
('ps','P/S',50),
('roe','ROE',60),
('roa','ROA',70),
('p_bv','P/BV',80),
('ev_ebitda','EV/EBITDA',90),


('capex','CAPEX, млрд руб',100),
('capex_revenue','CAPEX / выручка',110),
('opex','Операционные расходы, млрд руб',115),
('revenue','Выручка, млрд руб',120),
('net_income','Чистая прибыль, млрд руб',125),
('assets','Активы, млрд руб',130),
('net_assets','Чистые активы, млрд руб',132),
('capital','Капитал, млрд руб',134),

('cash','Наличность',140),
('dividend_payout','Дивидендная выплата, млрд руб',145),
('div_yield','Див. доход ао',150),
('div_yield_priv','Див. доход ап',155),


('debt','Долг, млрд руб',160),
('net_debt','Чистый долг',165),
('debt_ebitda','Долг/EBITDA',170),

('bv_share','BV/акцию, руб',175), 
('eps','EPS, руб',180);

-- fin_indicator:
--   pe: P/E
--   ps: P/S
--   p_bv: P/BV
--   ev_ebitda: EV/EBITDA
--   debt_ebitda: Долг/EBITDA
--   capex: CAPEX, млрд руб
--   opex: Операционные расходы, млрд руб
--   revenue: Выручка, млрд руб
--   assets: Активы, млрд руб
--   net_assets: Чистые активы, млрд руб
--   debt: долг, млрд руб
--   cash --  Наличность
--   net_debt -- чистый долг
--   common_share -- Цена акции 
--   cash --  Наличность
--   net_debt -- чистый долг
--   common_share -- Цена акции 
--   number_of_shares -- Число акций, млн



--   
alter table finam_stock add header varchar(255) not null default '';
create table finam_stock(
  id int unsigned primary key comment 'em на finam',
  sticker varchar(30) not null default '' comment 'code на finam',
  header varchar(255) not null default '',
  finam_code varchar(50) not null default '',
  currency varchar(10) not null default '',
  price_change decimal(6,2)  comment 'изменение цены, %',
  price decimal(15,6) unsigned,
  last_update timestamp,
  unique key(finam_code)
) engine=innodb default charset=utf8;


create table investing_com_stock(
  id int unsigned primary key comment 'pairId на investing.com',
  sticker varchar(30) not null default '' comment 'Стикер акции',
  header varchar(255) not null default '',
  code varchar(50) not null default '' comment 'code на investing.com'
) engine=innodb default charset=utf8;

create table investing_com_stock_values(
  stock_id int unsigned not null,
  name enum("pe","ps","p_cf","p_fcf","pb","ptbv","COGS","COGS_5ya","operating_margin","operating_margin_5ya","pentax_margin","pentax_margin_5ya","net_profit_margin","net_profit_margin_5ya","eps","basic_eps","deluded_eps","bvps","tbvps","cps","cfps","roe","roe_5ya","roa","roa_5ya","roi","roi_5ya","EPS_vs_QTR","EPS_vs_TTM","5y_eps_growth_5ya","sales_vs_qtr_1y_ago","sales_vs_ttm_1y_ago","sales_growth_5y","capital_spending_growth_5y","quick_ratio","current_ratio","ltde","de","asset_turnover","inventory_turnover","revenue_per_employee","nipe","receivable_turnover","dividend_yield","dividend_yield_5ya","dividend_growth_rate","dpr") not null,
  value decimal(15,6),
  constraint foreign key(stock_id) references investing_com_stock(id) on update cascade on delete cascade,
  primary key(stock_id,name)
) engine=innodb default charset=utf8;