create table report(
  id int unsigned primary key auto_increment,
  header varchar(255) not null default ''
) engine=innodb default charset=utf8;
# Компании

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
  pe decimal(12,2)  default '0.0' comment 'P/E',
  ps decimal(12,2)  default '0.0' comment 'P/S',
  pb decimal(12,2)  default '0.0' comment 'P/B',
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

create table fin_indicator(
  indicator varchar(20) not null primary key,
  header varchar(255) not null default ''
) engine=innodb default charset=utf8;

INSERT INTO fin_indicator values
('pe','P/E'),
('ps','P/S'),
('p_bv','P/BV'),
('ev_ebitda','EV/EBITDA'),
('debt_ebitda','Долг/EBITDA'),
('capex','CAPEX, млрд руб'),
('opex','Операционные расходы, млрд руб'),
('revenue','Выручка, млрд руб'),
('assets','Активы, млрд руб'),
('net_assets','Чистые активы, млрд руб'),
('debt','долг, млрд руб'),
('net_debt','чистый долг'),
('common_share','Цена акции'), 
('cash','Наличность');
fin_indicator:
  pe: P/E
  ps: P/S
  p_bv: P/BV
  ev_ebitda: EV/EBITDA
  debt_ebitda: Долг/EBITDA
  capex: CAPEX, млрд руб
  opex: Операционные расходы, млрд руб
  revenue: Выручка, млрд руб
  assets: Активы, млрд руб
  net_assets: Чистые активы, млрд руб
  debt: долг, млрд руб
  cash --  Наличность
  net_debt -- чистый долг
  common_share -- Цена акции 
  cash --  Наличность
  net_debt -- чистый долг
  common_share -- Цена акции 
  number_of_shares -- Число акций, млн