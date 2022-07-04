from .postgress import metadata

from sqlalchemy import Table, Column, String, SmallInteger, DateTime

t_BirthPlace = Table(
    "BirthPlace",
    metadata,
    Column('IdPersonMis', String), # Это UUID идентификатора Person
    Column('Country', String), #  Страна
    Column('Region' , String), #  Регион
    Column('City'   , String), #  Город
    )
