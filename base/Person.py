from .postgress import metadata

from sqlalchemy import Table, Column, String, SmallInteger, DateTime

t_Person = Table(
    "Person",
    metadata,
    Column('IdPersonMis', String), # Это UUID строки
    Column('HumanName', String),   # Это UUID HumanName
    Column('Sex', SmallInteger),   # Код пола (Справочник OID 1.2.643.5.1.13.2.1.1.156)
    Column('Birthdate', DateTime), # Дата рождения
    )
