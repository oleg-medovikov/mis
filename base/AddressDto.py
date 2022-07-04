from .postgress import metadata

from sqlalchemy import Table, Column, String, Integer, SmallInteger

t_AddressDto = Table(
    "AddressDto",
    metadata,
    Column('IdPersonMis', String), # Это UUID идентификатора Person
    Column('Appartment', String),  # Номер квартиры
    Column('Building' , String),   # Номер дома
    Column('City'   , String),     # Код города КЛАДР
    Column('GeoData' , String),    # Геокоординаты объекта
    Column('IdAddressType' , SmallInteger), # типа адреса 
                                   #(Справочник OID:1.2.643.2.69.1.1.1.28)
    Column('PostalCode', Integer),   # Индекс
    Column('Street' , ),             # Код улицы. Значение КЛАДР
    Column('StringAddress', String), # Адрес строкой
    )

"""
Справочник OID:1.2.643.2.69.1.1.1.28

| 1 | адрес регистрации |
| 2 | адрес фактического проживания |
| 3 | адрес места рождения |
| 4 | Служебный адрес |
| 5 | Прямой почтовый или телекоммуникационный адрес рабочего места |
| 6 | Общий почтовый или телекоммуникационный адрес рабочего места |
| 7 | Неправильный адрес |
| 8 | Временный адрес |
| 9 | Адрес для писем |

"""
