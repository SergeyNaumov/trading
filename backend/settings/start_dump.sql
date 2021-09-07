create table report(
  id int unsigned primary key auto_increment,
  header varchar(255) not null default ''
) engine=innodb default charset=utf8;
# Компании
drop table company;
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

