from .postgress import metadata

from sqlalchemy import Table, Column, String, SmallInteger, DateTime

t_ContactDto = Table(
    "ContactDto",
    metadata,
    Column('IdPersonMis', String), # Это UUID идентификатора 
    Column('IdContactType', String), #  типа контакта 
                                     #(Справочник OID:1.2.643.2.69.1.1.1.27)
    Column('ContactValue' , String), #  Содержание
    )

"""
Справочник OID:1.2.643.2.69.1.1.1.27

| 1  | Мобильный телефон
| 2  | Стационарный телефон
| 3  | Адрес электронной почты
| 4  | Факс	

"""


